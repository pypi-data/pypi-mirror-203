# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

import signal
import socket
import asyncio

from typing import List

from hagworm import hagworm_slogan
from hagworm import __version__ as hagworm_version
from hagworm.extend.asyncio.base import Utils, install_uvloop
from hagworm.extend.interface import RunnableInterface

from ..error import RouterError


class Router:

    def __init__(self, root=r''):

        self._root = root
        self._reg_func = {}

    def __repr__(self):

        return self._reg_func.__repr__()

    def __call__(self, method, *args, **kwargs):

        func = self._reg_func.get(method)

        if not func:
            raise RouterError(f'{method} not exists')

        return func(*args, **kwargs)

    def _reg(self, method, func):

        _method = f'{self._root}{method}'

        if _method in self._reg_func:
            raise RouterError(f'{method} has exists')

        self._reg_func[_method] = func

    def reg(self, method):

        def _reg_func(func):
            self._reg(method, func)
            return func

        return _reg_func

    def items(self):

        return self._reg_func.items()

    def include(self, router):

        for method, func in router.items():
            self._reg(method, func)


class SocketConfig:

    __slots__ = [r'client_connected_cb', r'address', r'family', r'backlog', r'reuse_port', r'buffer_limit']

    def __init__(self, client_connected_cb, address, family, backlog, reuse_port, buffer_limit):

        self.client_connected_cb = client_connected_cb
        self.address = address
        self.family = family
        self.backlog = backlog
        self.reuse_port = reuse_port
        self.buffer_limit = buffer_limit


class AsyncTcpServer(RunnableInterface):

    def __init__(
            self, client_connected_cb, address, *,
            family=socket.AF_INET, backlog=None, reuse_port=True, buffer_limit=0xffffff,
            on_startup=None, on_shutdown=None
    ):

        self._listeners: List[SocketConfig] = [
            SocketConfig(
                client_connected_cb, address,
                family, backlog, reuse_port, buffer_limit
            )
        ]

        self._on_startup = on_startup
        self._on_shutdown = on_shutdown

        self._servers = []
        self._server_tasks = []

        signal.signal(signal.SIGINT, self._exit)
        signal.signal(signal.SIGTERM, self._exit)

    async def __aenter__(self):

        for server in self._servers:
            await server.__aenter__()

        return self

    async def __aexit__(self, exc_type, exc_value, _traceback):

        for server in self._servers:
            await server.__aexit__(exc_type, exc_value, _traceback)

    def add_listener(
            self, client_connected_cb, address, *,
            family=socket.AF_INET, backlog=None, reuse_port=True, buffer_limit=0xffffff
    ):

        self._listeners.append(
            SocketConfig(
                client_connected_cb, address,
                family, backlog, reuse_port, buffer_limit
            )
        )

    def run(self):

        environment = Utils.environment()

        Utils.log.info(
            f'{hagworm_slogan}'
            f'hagworm {hagworm_version}\n'
            f'python {environment["python"]}\n'
            f'system {" ".join(environment["system"])}'
        )

        install_uvloop()

        asyncio.run(self._run())

    async def _run(self):

        if self._on_startup is not None:
            await self._on_startup()

        for config in self._listeners:

            if config.family == socket.AF_UNIX:

                _socket_server = await asyncio.start_unix_server(
                    config.client_connected_cb, config.address, limit=config.buffer_limit
                )

                Utils.log.success(f'unix server [pid:{Utils.getpid()}] startup complete: {config.address}')

            else:

                _socket = socket.create_server(
                    config.address, family=config.family, backlog=config.backlog, reuse_port=config.reuse_port
                )

                _socket_server = await asyncio.start_server(
                    config.client_connected_cb,
                    limit=config.buffer_limit, sock=_socket
                )

                Utils.log.success(f'socket server [pid:{Utils.getpid()}] startup complete: {config.address}')

            self._servers.append(_socket_server)

        async with self:

            for _server in self._servers:
                self._server_tasks.append(
                    asyncio.create_task(_server.serve_forever())
                )

            for _server_task in self._server_tasks:

                try:
                    await _server_task
                except asyncio.CancelledError as _:
                    pass

        if self._on_shutdown is not None:
            await self._on_shutdown()

    def _exit(self, *_):

        for _server_task in self._server_tasks:
            _server_task.cancel()
