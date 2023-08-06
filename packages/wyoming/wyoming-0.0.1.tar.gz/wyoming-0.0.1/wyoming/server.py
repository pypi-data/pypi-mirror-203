import asyncio
from abc import ABC, abstractmethod
from functools import partial
from pathlib import Path
from typing import Callable, Set, Union

from .event import Event, async_read_event, async_write_event


class AsyncEventHandler(ABC):
    """Base class for async Wyoming event handler."""

    def __init__(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        self.reader = reader
        self.writer = writer

    @abstractmethod
    async def handle_event(self, event: Event) -> bool:
        return True

    async def write_event(self, event: Event) -> None:
        await async_write_event(event, self.writer)

    async def run(self) -> None:
        while True:
            event = await async_read_event(self.reader)
            if event is None:
                break

            if not (await self.handle_event(event)):
                break


HandlerFactory = Callable[
    [asyncio.StreamReader, asyncio.StreamWriter], AsyncEventHandler
]


class AsyncServer(ABC):
    """Base class for async Wyoming server."""

    def __init__(self) -> None:
        self._tasks: Set[asyncio.Task] = set()

    @abstractmethod
    async def run(self, handler_factory: HandlerFactory) -> None:
        pass

    @staticmethod
    def from_uri(uri: str) -> "AsyncServer":
        if uri.startswith("unix://"):
            socket_path = uri[len("unix://") :]
            return AsyncUnixServer(socket_path)

        if uri.startswith("tcp://"):
            host, port_str = uri[len("tcp://") :].split(":")
            port = int(port_str)
            return AsyncTcpServer(host, port)

        raise ValueError("Only unix:// or tcp:// are supported")

    async def _handler_callback(
        self,
        handler_factory: HandlerFactory,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ):
        handler = handler_factory(reader, writer)
        task = asyncio.create_task(handler.run())
        self._tasks.add(task)
        task.add_done_callback(self._tasks.discard)


class AsyncTcpServer(AsyncServer):
    """Wyoming server over TCP."""

    def __init__(self, host: str, port: int) -> None:
        super().__init__()
        self.host = host
        self.port = port

    async def run(self, handler_factory: HandlerFactory) -> None:
        handler_callback = partial(self._handler_callback, handler_factory)
        server = await asyncio.start_server(
            handler_callback, host=self.host, port=self.port
        )

        await server.serve_forever()


class AsyncUnixServer(AsyncServer):
    """Wyoming server over a Unix domain socket."""

    def __init__(self, socket_path: Union[str, Path]) -> None:
        super().__init__()
        self.socket_path = Path(socket_path)
        self.tasks: Set[asyncio.Task] = set()

    async def run(self, handler_factory: HandlerFactory) -> None:
        # Need to unlink socket file if it exists
        self.socket_path.unlink(missing_ok=True)

        handler_callback = partial(self._handler_callback, handler_factory)
        server = await asyncio.start_unix_server(
            handler_callback, path=self.socket_path
        )

        try:
            await server.serve_forever()
        finally:
            # Unlink when we're done
            self.socket_path.unlink(missing_ok=True)
