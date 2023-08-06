import asyncio as aio
import json
from typing import Literal, Union

from .base import ClientBase
from .utils import edict

Direction = Union[
    Literal["left"],
    Literal["right"],
    Literal["up"],
    Literal["down"],
]


StateQuery = Union[
    Literal["focused-monitor-index"],
    Literal["focused-workspace-index"],
    Literal["focused-container-index"],
    Literal["focused-window-index"],
]


class Komorebic(ClientBase):
    def __init__(self, exe: str = "komorebic.exe", pipe_name: str = "komorebic_pipe"):
        super().__init__(exe)

    async def start(
        self, port: int = 0, await_configuration: bool = True, ffm: bool = False
    ):
        cmd = []
        if port:
            cmd += ["-t", port]
        if await_configuration:
            cmd.append("-a")
        if ffm:
            cmd.append("-f")

        return await self.run(cmd)

    async def state(self) -> edict:
        return edict(json.loads(await self.run("state")))

    async def focused_monitor_index(self) -> int:
        return await self.query("focused-monitor-index")

    async def focused_workspace_index(self) -> int:
        return await self.query("focused-monitor-index")

    async def focused_container_index(self) -> int:
        return await self.query("focused-container-index")

    async def focused_window_index(self) -> int:
        return await self.query("focused-window-index")

    async def query(self, state: StateQuery) -> int:
        return int(await self.run("query", state))

    async def focus(self, direction: Direction) -> None:
        await self.run("focus", direction)

    async def focused_monitor(self):
        state, idx = await aio.gather(self.state(), self.focused_monitor_index())

        return state["monitors"]["elements"][idx]

    async def focused_workspace(self):
        focused_monitor, idx = await aio.gather(
            self.focused_monitor(), self.focused_workspace_index()
        )

        return focused_monitor["workspace"]["elements"][idx]

    async def focused_container(self):
        focused_workspace, idx = await aio.gather(
            self.focused_workspace(), self.focused_container_index()
        )

        return focused_workspace["containers"][idx]

    async def focused_window(self):
        focused_container, idx = await aio.gather(
            self.focused_container(), self.focused_window_index()
        )

        return focused_container["windows"][idx]

    async def subscribe(self, pipe: str):
        return await self.run("subscribe", pipe)
