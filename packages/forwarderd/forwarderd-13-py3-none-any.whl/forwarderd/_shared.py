import os
import json
import asyncio

from enum import Enum
from dataclasses import dataclass, asdict  # pyright: reportUnusedImport=false


IP_ADDR = ('localhost', 19567)
SOCK_PATH = '/var/run/forwarderd.sock'


async def connect_tcp():
    return await asyncio.open_connection(*IP_ADDR)


async def _run_server(server):
    try:
        await server.serve_forever()
    except asyncio.CancelledError:
        server.close()
        await server.wait_closed()


async def start_tcp_server(cb):
    server = await asyncio.start_server(cb, *IP_ADDR)
    return asyncio.create_task(_run_server(server))


if hasattr(asyncio, 'open_unix_connection'):
    async def connect_unix():
        return await asyncio.open_unix_connection(SOCK_PATH)  # type: ignore

    async def start_unix_server(cb):
        os.makedirs(os.path.dirname(SOCK_PATH), exist_ok=True)
        server = await asyncio.start_unix_server(cb, SOCK_PATH)  # type: ignore
        os.chmod(SOCK_PATH, 0o777)
        return asyncio.create_task(_run_server(server))

    async def connect():
        try:
            return await connect_unix()
        except OSError:
            return await connect_tcp()



    async def start_server(cb) -> asyncio.Future:
        from ._daemon import logger

        tasks = []
        for coro in [start_unix_server(cb), start_tcp_server(cb)]:
            try:
                tasks.append(await coro)
            except OSError as e:
                logger.error(f'Failed to {coro.__name__}: {e!r}')

        if not tasks:
            raise OSError('Unable to start servers')

        async def run_task():
            await tasks.pop()
            while tasks:
                task = tasks.pop()
                task.cancel()
                await task

        return asyncio.create_task(run_task())

else:
    connect = connect_tcp
    start_server = start_tcp_server


def dump_frame(type: 'MessageType', data: dict) -> bytes:
    str_dump = json.dumps([type, data], ensure_ascii=False)
    return str_dump.encode('utf-8') + b'\n'


def load_frame(data: bytes) -> 'tuple[MessageType, dict]':
    return tuple(json.loads(data[:-1]))


class MessageType(int, Enum):
    SPAWN_TUNNEL = 1

    OK = 15
    ERROR = 16


@dataclass
class SpawnTunnelRequest:
    ssh_addr: str
    ssh_user: str
    ssh_identity_file: str
    remote_addr: str
    local_addr: str = ''


@dataclass
class SpawnTunnelResponse:
    host: str
    port: int
