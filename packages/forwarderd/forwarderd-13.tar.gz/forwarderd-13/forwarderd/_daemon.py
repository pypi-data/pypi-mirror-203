import signal
import asyncio
import logging
import threading

from typing import cast
from traceback import format_exc

from paramiko import RSAKey
from sshtunnel import SSHTunnelForwarder

from ._shared import (
    MessageType,
    SpawnTunnelRequest,
    SpawnTunnelResponse,
    asdict, load_frame, dump_frame, start_server
)


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S'
)
logger = logging.getLogger()


spawn_lock = threading.Lock()
spawned: 'dict[tuple, SSHTunnelForwarder]' = {}


def _parse_addr_string(addr: str) -> 'tuple[str] | tuple[str, int]':
    host, _, port = addr.strip().partition(':')
    if not port:
        return (host,)
    if not port.isdigit():
        raise ValueError('Incorrect address: port is not number')
    return (host, int(port))


def _format_addr(addr: 'tuple[str] | tuple[str, int]') -> str:
    if len(addr) == 2:
        return f'{addr[0]}:{addr[1]}'
    else:
        return addr[0]


def blocking_spawn(data: SpawnTunnelRequest):
    with spawn_lock:
        forwarder_id = (data.ssh_addr, data.ssh_user, data.remote_addr)
        if spawned_forwarder := spawned.get(forwarder_id):
            if not spawned_forwarder.is_active:
                spawned_forwarder.restart()
            return spawned_forwarder

        if data.local_addr:
            local_addr = _parse_addr_string(data.local_addr)
        else:
            local_addr = ('localhost',)

        key = RSAKey.from_private_key_file(data.ssh_identity_file)
        forwarder = SSHTunnelForwarder(
            ssh_address_or_host=_parse_addr_string(data.ssh_addr),
            ssh_username=data.ssh_user,
            ssh_pkey=key,
            remote_bind_address=_parse_addr_string(data.remote_addr),
            local_bind_address=local_addr
        )
        forwarder.start()

        logger.info('New forwarder spawned '
                    '(ssh_addr=%s, local_addr=%s, remote_addr=%s)',
                    data.ssh_addr,
                    _format_addr(forwarder.local_bind_address),
                    data.remote_addr)

        spawned[forwarder_id] = forwarder
        return forwarder


async def spawn_tunnel(data: SpawnTunnelRequest):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, blocking_spawn, data)


async def handle_request(req_type: MessageType, data):
    if req_type == MessageType.SPAWN_TUNNEL:
        data = SpawnTunnelRequest(**data)
        forwarder = await spawn_tunnel(data)
        host, port = forwarder.local_bind_address
        response = SpawnTunnelResponse(host, port)
        return (MessageType.OK, asdict(response))

    else:
        raise ValueError(f'Unknown request {req_type!r}')


async def on_connect(r: asyncio.StreamReader, w: asyncio.StreamWriter):
    req_type, req_data = load_frame(await r.readline())
    try:
        resp_type, resp_data = await handle_request(req_type, req_data)
    except Exception as e:
        logger.error(format_exc())
        resp_type = MessageType.ERROR
        resp_data = {'error': repr(e)}

    w.write(dump_frame(resp_type, resp_data))
    await w.drain()
    w.write_eof()
    w.close()
    await w.wait_closed()


# TODO: reopen tunnels after service restart
def run_daemon():
    async def main():
        current_task = cast(asyncio.Task, asyncio.current_task())

        def stop(*_):
            current_task.cancel()
            # wake up the loop
            current_task.get_loop().call_soon_threadsafe(lambda: None)

        signal.signal(signal.SIGINT, stop)
        signal.signal(signal.SIGTERM, stop)

        run_task = await start_server(on_connect)
        logger.info('Server started!')

        await run_task
        logger.info('Server closed.')

    asyncio.run(main())
