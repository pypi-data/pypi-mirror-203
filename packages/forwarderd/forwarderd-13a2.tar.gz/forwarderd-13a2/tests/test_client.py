import os
import time
import multiprocessing

import forwarderd

import pytest


def getenv(name: str):
    value = os.getenv(name)
    if value is None:
        pytest.fail('Environment variable \'{name}\' not set')
    return value



def setup_module(module):
    from forwarderd._daemon import run_daemon

    module.daemon_process = multiprocessing.get_context('spawn').Process(
        target=run_daemon, daemon=True
    )
    module.daemon_process.start()
    time.sleep(1)


@pytest.mark.asyncio
async def test_spawn():
    local_host = getenv('LOCAL_HOST')
    local_port = int(getenv('LOCAL_PORT'))

    resp = await forwarderd.spawn_tunnel(
        forwarderd.SpawnTunnelRequest(
            ssh_addr=getenv("SSH_ADDR"),
            ssh_user=getenv("SSH_USER"),
            ssh_identity_file=getenv("SSH_IDENTITY_FILE"),

            remote_addr=getenv("REMOTE_ADDR"),
            local_addr=f'{local_host}:{local_port}',
        )
    )

    assert (resp.host, resp.port) == (local_host, local_port), \
        'Wanted and actual addresses differs'


@pytest.mark.asyncio
async def test_unknown_message_type():
    with pytest.raises(forwarderd.DaemonError):
        await forwarderd._make_request(1024, None)


def teardown_module(module):
    module.daemon_process.terminate()
    module.daemon_process.join()
