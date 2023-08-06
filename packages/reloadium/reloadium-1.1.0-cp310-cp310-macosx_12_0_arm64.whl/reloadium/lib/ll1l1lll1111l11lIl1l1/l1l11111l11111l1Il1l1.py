import types
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Tuple, Type, Union, cast

from reloadium.lib.ll1l1lll1111l11lIl1l1.ll111llllllll1llIl1l1 import ll1lll111lll11l1Il1l1
from reloadium.lib import llllll1lll111l11Il1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field
else:
    from reloadium.vendored.dataclasses import dataclass, field


__RELOADIUM__ = True


@dataclass
class l1lll1l11l1111llIl1l1(ll1lll111lll11l1Il1l1):
    l1111ll11l1lll11Il1l1 = 'Multiprocessing'

    def __post_init__(ll11l11lll111l1lIl1l1) -> None:
        super().__post_init__()

    def ll111l111ll11l1lIl1l1(ll11l11lll111l1lIl1l1, l1lllll1111l1ll1Il1l1: types.ModuleType) -> None:
        if (ll11l11lll111l1lIl1l1.ll111l111ll1llllIl1l1(l1lllll1111l1ll1Il1l1, 'multiprocessing.popen_spawn_posix')):
            ll11l11lll111l1lIl1l1.l1lllllll1llllllIl1l1(l1lllll1111l1ll1Il1l1)

        if (ll11l11lll111l1lIl1l1.ll111l111ll1llllIl1l1(l1lllll1111l1ll1Il1l1, 'multiprocessing.popen_spawn_win32')):
            ll11l11lll111l1lIl1l1.l111ll1ll11l1ll1Il1l1(l1lllll1111l1ll1Il1l1)

    def l1lllllll1llllllIl1l1(ll11l11lll111l1lIl1l1, l1lllll1111l1ll1Il1l1: types.ModuleType) -> None:
        import multiprocessing.popen_spawn_posix
        multiprocessing.popen_spawn_posix.Popen._launch = llllll1lll111l11Il1l1.l1l11111l11111l1Il1l1.ll1lll1lll11111lIl1l1  # type: ignore

    def l111ll1ll11l1ll1Il1l1(ll11l11lll111l1lIl1l1, l1lllll1111l1ll1Il1l1: types.ModuleType) -> None:
        import multiprocessing.popen_spawn_win32
        multiprocessing.popen_spawn_win32.Popen.__init__ = llllll1lll111l11Il1l1.l1l11111l11111l1Il1l1.__init__  # type: ignore
