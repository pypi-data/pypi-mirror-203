import asyncio as aio
from typing import Any, Awaitable, Callable, Optional, Union

import ujson
from loguru import logger

from .events import KomorebicEvent
from .utils import NamedPipe, PipeClosedError, edict

KomorebicEventCallbackParam = Union[dict, edict]
KomorebicEventCallbackT = Callable[
    [KomorebicEventCallbackParam, KomorebicEventCallbackParam], Awaitable[None]
]
KomorebicEventT = Union[KomorebicEvent, str]


class KomorebicEventManager:
    def __init__(
        self, komorebic, pipe_name: str, before_dispatch: Callable[[dict], Any] = None
    ):
        self.komorebic = komorebic
        self.pipe_name = pipe_name

        self.before_dispatch = before_dispatch

        self._dispatcher_task: aio.Task = None
        self._subscriptions = {}

    async def subscribe(self, event: KomorebicEventT, handler: KomorebicEventCallbackT):
        # on first call subscribe to komorebic events and start the dispatcher task
        if self._dispatcher_task is None:
            self._dispatcher_task = aio.create_task(self._dispatcher_loop())

        if isinstance(event, KomorebicEvent):
            event = event.value

        if event not in self._subscriptions:
            self._subscriptions[event] = []

        self._subscriptions[event].append(handler)

    async def unsubscribe(
        self, event: KomorebicEventT, handler: KomorebicEventCallbackT
    ):
        if isinstance(event, KomorebicEvent):
            event = event.value

        if event not in self._subscriptions:
            return

        cbs = self._subscriptions[event]
        cb = next((cb for cb in cbs if id(cb) == id(handler)), None)
        if not cbs or not cb:
            return

        cbs.remove(handler)

        if not self.has_subscriptions:
            self._dispatcher_task.cancel()

    @property
    def has_subscriptions(self):
        return any((bool(cbs) for cbs in self._subscriptions.values()))

    async def _dispatcher_loop(self):
        """
        Handles errors with the pipe, receives data from the pipe and dispatches
        the data based on the event to the respective callback.
        Callbacks are executed async, TODO maybe change this?
        """
        # retry on error loop
        while True:
            try:
                async with NamedPipe(self.pipe_name) as pipe:
                    await self.komorebic._subscribe(self.pipe_name)
                    # read loop
                    while True:
                        data = await pipe.read()
                        # TODO maybe here allow the user to decide whether he wants a dict
                        # or an edict, or replac edict with something
                        data = ujson.loads(data)
                        if self.before_dispatch is not None:
                            data = self.before_dispatch(data)

                        # dispatch all event callbacks async
                        cbs = self._subscriptions.get(data["event"]["type"], [])
                        for cb in cbs:
                            aio.create_task(cb(data["event"], data["state"]))

            except PipeClosedError:
                logger.error("PipeClosed, reconnecting...")
                await aio.sleep(1)
            except Exception as e:
                logger.error("UNKNOWN EXCEPTION")
                logger.exception(e)
