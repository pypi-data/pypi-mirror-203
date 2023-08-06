import asyncio as aio
from pathlib import Path

from loguru import logger

from .client import Komorebic


class ActiveMonitors:
    def __init__(self, path):
        self.path = Path(path)
        self.read()

    def read(self):
        lines = [
            line.strip() for line in self.path.read_text().split("\n") if line.strip()
        ]
        self.primary, self.secondary, self.tertiary = [
            int(line.split(" ")[-1]) for line in lines
        ]

    def write(self, primary, secondary, tertiary):
        self.primary = primary
        self.secondary = secondary
        self.tertiary = tertiary

        text = f"$PRIMARY = {self.primary}\n"
        text += f"$SECONDARY = {self.secondary}\n"
        text += f"$TERTIARY = {self.tertiary}"
        self.path.write_text(text)


NOTEBOOK_SIZE = 1920
HOME_SIZE = 7040
WORK_SIZE = 1000


# komorebic ensure-named-workspaces $PRIMARY P1 P2 P3
# komorebic ensure-named-workspaces $SECONDARY S1 S2 S3 M1 M2 C1 C2
# komorebic ensure-named-workspaces $TERTIARY N1 N2 N3


async def main():
    komorebic = Komorebic()
    active_monitors_path = "C:\\Users\\sesa715731\\active_monitors.ps1"
    am = ActiveMonitors(active_monitors_path)

    while True:
        state = await komorebic.state()
        if state is None:
            await aio.sleep(1)
            continue

        monitors = state.monitors.elements
        size = sum(
            [max(abs(moni.size.left), abs(moni.size.right)) for moni in monitors]
        )
        logger.info(size)

        # NOTEBOOK
        if size == NOTEBOOK_SIZE and (
            am.primary != 0 or am.secondary != 0 or am.tertiary != 0
        ):
            await komorebic.kill()
            am.write(0, 0, 0)
            await komorebic.start(await_configuration=True)
        # IS HOME
        elif size == HOME_SIZE and (
            am.primary != 2 or am.secondary != 0 or am.tertiary != 1
        ):
            await komorebic.kill()
            am.write(2, 0, 1)
            await komorebic.start(await_configuration=True)
        # IS WORK
        elif size == WORK_SIZE and (
            am.primary != 1 or am.secondary != 2 or am.tertiary != 0
        ):
            await komorebic.kill()
            am.write(1, 2, 0)
            await komorebic.start(await_configuration=True)

        await aio.sleep(5)


if __name__ == "__main__":
    aio.run(main())
