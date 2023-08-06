import asyncio as aio

from loguru import logger


class ClientBase:
    def __init__(self, exe: str):
        self.exe = exe

    async def run(self, *cmd) -> str:
        cmd = [str(param) for param in cmd]
        logger.debug(cmd)

        return await self._run(self.exe, *cmd)

    async def _run(self, exe, *cmd) -> str:
        proc = await aio.create_subprocess_exec(
            exe, *cmd, stdout=aio.subprocess.PIPE, stderr=aio.subprocess.PIPE
        )
        # sometime when komorebi somehow becomes unresponsive, raises TimeoutError
        stdout, stderr = await aio.wait_for(proc.communicate(), timeout=2)

        stdout, stderr = stdout.decode(), stderr.decode()
        if stderr:
            logger.error(stderr)

        return stdout
