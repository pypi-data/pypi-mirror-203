import asyncio as aio

from loguru import logger


class ClientBase:
    def __init__(self, exe: str):
        self.exe = exe

    async def run(self, *cmd):
        cmd = [str(param) for param in cmd]
        logger.debug(cmd)

        return await self._run(self.exe, *cmd)

    async def _run(self, exe, *cmd):
        proc = await aio.create_subprocess_exec(
            exe, *cmd, stdout=aio.subprocess.PIPE, stderr=aio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        stdout, stderr = stdout.decode(), stderr.decode()
        if stderr:
            logger.error(stderr)

        return stdout
