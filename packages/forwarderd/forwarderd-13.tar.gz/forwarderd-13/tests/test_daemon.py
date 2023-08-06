from forwarderd import _daemon, _shared

import pytest


async def test_unix_servers_spawn():
    try:
        _shared.start_unix_server
    except AttributeError:
        pytest.skip('Unix sockets are not available')

    async def callback(r, w):
        w.write(b'\x00')
        w.close()
        await w.wait_closed()

    # should start both unix and tcp servers
    run_task = await _shared.start_server(callback)

    r, w = await _shared.connect_tcp()
    data = await r.read()
    assert data == b'\x00'

    r, w = await _shared.connect_unix()
    data = await r.read()
    assert data == b'\x00'

    # should stop both servers
    run_task.cancel()

    with pytest.raises(OSError):
        await _shared.connect_tcp()

    with pytest.raises(OSError):
        await _shared.connect_unix()
