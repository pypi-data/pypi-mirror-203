import asyncio as aio
from dataclasses import dataclass
from typing import Optional

import pywintypes
import win32file
import win32pipe
from easydict import EasyDict as edict  # noqa
from loguru import logger


async def make_async(f, *args, **kwargs):
    loop = aio.get_event_loop()
    return await loop.run_in_executor(None, f, *args, **kwargs)


class PipeClosedError(Exception):
    pass


@dataclass
class NamedPipe:
    name: str = "unnamed"
    open_mode: int = win32pipe.PIPE_ACCESS_DUPLEX
    pipe_mode: int = (
        win32pipe.PIPE_TYPE_MESSAGE
        | win32pipe.PIPE_READMODE_MESSAGE
        | win32pipe.PIPE_WAIT
    )
    max_instances: int = 1
    buffer_size_in: int = 64 * 1024
    buffer_size_out: int = 64 * 1024
    default_timeout_ms: int = 0
    security_attributes = None

    polling_interval: float = 0.01

    async def __aenter__(self):
        await self.open()
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def open(self):
        self.handle = await make_async(
            win32pipe.CreateNamedPipe,
            f"\\\\.\\pipe\\{self.name}",
            self.open_mode,
            self.pipe_mode,
            self.max_instances,
            self.buffer_size_in,
            self.buffer_size_out,
            self.default_timeout_ms,
            self.security_attributes,
        )

    async def read(self) -> str:
        while True:
            s = await self.try_read()
            if s is None:
                await aio.sleep(self.polling_interval)
                continue

            return s

    async def try_read(self) -> Optional[str]:
        try:
            _, bytes_to_read, _ = await make_async(
                win32pipe.PeekNamedPipe, self.handle, 1
            )
            if not bytes_to_read:
                return None

            _, data = await make_async(
                win32file.ReadFile, self.handle, bytes_to_read, None
            )
            if not data.strip():
                return None
        except pywintypes.error as e:
            if e.winerror in (109, 230):
                raise PipeClosedError()

            logger.error(f"[UNKNOWN] {e.winerror} {e.strerror}")
            raise e

        return data

    async def close(self):
        await make_async(win32file.CloseHandle, self.handle)
