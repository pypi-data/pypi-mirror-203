import sys

__RELOADIUM__ = True


def ll1lll1lll11111lIl1l1(lll1l1l1ll1l1111Il1l1, l11ll111l11111llIl1l1):
    from pathlib import Path
    from multiprocessing import util, spawn
    from multiprocessing.context import reduction, set_spawning_popen
    import io
    import os

    def l1ll1111lll1l1l1Il1l1(*l1l111ll11111lllIl1l1):

        for l1111ll11111lll1Il1l1 in l1l111ll11111lllIl1l1:
            os.close(l1111ll11111lll1Il1l1)

    if (sys.version_info > (3, 8, )):
        from multiprocessing import resource_tracker as tracker 
    else:
        from multiprocessing import semaphore_tracker as tracker 

    lll11l111111ll1lIl1l1 = tracker.getfd()
    lll1l1l1ll1l1111Il1l1._fds.append(lll11l111111ll1lIl1l1)
    l11ll1l1llllll11Il1l1 = spawn.get_preparation_data(l11ll111l11111llIl1l1._name)
    l11lll11ll11l1llIl1l1 = io.BytesIO()
    set_spawning_popen(lll1l1l1ll1l1111Il1l1)

    try:
        reduction.dump(l11ll1l1llllll11Il1l1, l11lll11ll11l1llIl1l1)
        reduction.dump(l11ll111l11111llIl1l1, l11lll11ll11l1llIl1l1)
    finally:
        set_spawning_popen(None)

    l1111llll11l1l11Il1l1l11l11ll111ll11lIl1l1l1111ll111111ll1Il1l1l11ll111llll1111Il1l1 = None
    try:
        (l1111llll11l1l11Il1l1, l11l11ll111ll11lIl1l1, ) = os.pipe()
        (l1111ll111111ll1Il1l1, l11ll111llll1111Il1l1, ) = os.pipe()
        l11l1llll111ll11Il1l1 = spawn.get_command_line(tracker_fd=lll11l111111ll1lIl1l1, pipe_handle=l1111ll111111ll1Il1l1)


        ll1lll11l11ll1llIl1l1 = str(Path(l11ll1l1llllll11Il1l1['sys_argv'][0]).absolute())
        l11l1llll111ll11Il1l1 = [l11l1llll111ll11Il1l1[0], '-B', '-m', 'reloadium_launcher', 'spawn_process', str(lll11l111111ll1lIl1l1), 
str(l1111ll111111ll1Il1l1), ll1lll11l11ll1llIl1l1]
        lll1l1l1ll1l1111Il1l1._fds.extend([l1111ll111111ll1Il1l1, l11l11ll111ll11lIl1l1])
        lll1l1l1ll1l1111Il1l1.pid = util.spawnv_passfds(spawn.get_executable(), 
l11l1llll111ll11Il1l1, lll1l1l1ll1l1111Il1l1._fds)
        lll1l1l1ll1l1111Il1l1.sentinel = l1111llll11l1l11Il1l1
        with open(l11ll111llll1111Il1l1, 'wb', closefd=False) as l1l11lll1l1l11l1Il1l1:
            l1l11lll1l1l11l1Il1l1.write(l11lll11ll11l1llIl1l1.getbuffer())
    finally:
        lllllllll11lll11Il1l1 = []
        for l1111ll11111lll1Il1l1 in (l1111llll11l1l11Il1l1, l11ll111llll1111Il1l1, ):
            if (l1111ll11111lll1Il1l1 is not None):
                lllllllll11lll11Il1l1.append(l1111ll11111lll1Il1l1)
        lll1l1l1ll1l1111Il1l1.finalizer = util.Finalize(lll1l1l1ll1l1111Il1l1, l1ll1111lll1l1l1Il1l1, lllllllll11lll11Il1l1)

        for l1111ll11111lll1Il1l1 in (l1111ll111111ll1Il1l1, l11l11ll111ll11lIl1l1, ):
            if (l1111ll11111lll1Il1l1 is not None):
                os.close(l1111ll11111lll1Il1l1)


def __init__(lll1l1l1ll1l1111Il1l1, l11ll111l11111llIl1l1):
    from multiprocessing import util, spawn
    from multiprocessing.context import reduction, set_spawning_popen
    from multiprocessing.popen_spawn_win32 import TERMINATE, WINEXE, WINSERVICE, WINENV, _path_eq
    from pathlib import Path
    import os
    import msvcrt
    import sys
    import _winapi

    if (sys.version_info > (3, 8, )):
        from multiprocessing import resource_tracker as tracker 
        from multiprocessing.popen_spawn_win32 import _close_handles
    else:
        from multiprocessing import semaphore_tracker as tracker 
        _close_handles = _winapi.CloseHandle

    l11ll1l1llllll11Il1l1 = spawn.get_preparation_data(l11ll111l11111llIl1l1._name)







    (lll11llll11ll111Il1l1, lllll1lll111lll1Il1l1, ) = _winapi.CreatePipe(None, 0)
    l1l11111ll111l11Il1l1 = msvcrt.open_osfhandle(lllll1lll111lll1Il1l1, 0)
    lll11l1lll111l1lIl1l1 = spawn.get_executable()
    ll1lll11l11ll1llIl1l1 = str(Path(l11ll1l1llllll11Il1l1['sys_argv'][0]).absolute())
    l11l1llll111ll11Il1l1 = ' '.join([lll11l1lll111l1lIl1l1, '-B', '-m', 'reloadium_launcher', 'spawn_process', str(os.getpid()), 
str(lll11llll11ll111Il1l1), ll1lll11l11ll1llIl1l1])



    if ((WINENV and _path_eq(lll11l1lll111l1lIl1l1, sys.executable))):
        lll11l1lll111l1lIl1l1 = sys._base_executable
        l1l11l1l111l11l1Il1l1 = os.environ.copy()
        l1l11l1l111l11l1Il1l1['__PYVENV_LAUNCHER__'] = sys.executable
    else:
        l1l11l1l111l11l1Il1l1 = None

    with open(l1l11111ll111l11Il1l1, 'wb', closefd=True) as l1l1l1l1l1llll1lIl1l1:

        try:
            (l111l11l1lll1111Il1l1, l11ll1ll111lll1lIl1l1, ll1l11l1l1l1111lIl1l1, ll111l11llll1l1lIl1l1, ) = _winapi.CreateProcess(lll11l1lll111l1lIl1l1, l11l1llll111ll11Il1l1, None, None, False, 0, l1l11l1l111l11l1Il1l1, None, None)


            _winapi.CloseHandle(l11ll1ll111lll1lIl1l1)
        except :
            _winapi.CloseHandle(lll11llll11ll111Il1l1)
            raise 


        lll1l1l1ll1l1111Il1l1.pid = ll1l11l1l1l1111lIl1l1
        lll1l1l1ll1l1111Il1l1.returncode = None
        lll1l1l1ll1l1111Il1l1._handle = l111l11l1lll1111Il1l1
        lll1l1l1ll1l1111Il1l1.sentinel = int(l111l11l1lll1111Il1l1)
        if (sys.version_info > (3, 8, )):
            lll1l1l1ll1l1111Il1l1.finalizer = util.Finalize(lll1l1l1ll1l1111Il1l1, _close_handles, (lll1l1l1ll1l1111Il1l1.sentinel, int(lll11llll11ll111Il1l1), 
))
        else:
            lll1l1l1ll1l1111Il1l1.finalizer = util.Finalize(lll1l1l1ll1l1111Il1l1, _close_handles, (lll1l1l1ll1l1111Il1l1.sentinel, ))



        set_spawning_popen(lll1l1l1ll1l1111Il1l1)
        try:
            reduction.dump(l11ll1l1llllll11Il1l1, l1l1l1l1l1llll1lIl1l1)
            reduction.dump(l11ll111l11111llIl1l1, l1l1l1l1l1llll1lIl1l1)
        finally:
            set_spawning_popen(None)
