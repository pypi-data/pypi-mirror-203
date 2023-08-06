from pathlib import Path
import sys
import threading
from types import CodeType, FrameType, ModuleType
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Set, cast

from reloadium.corium import l1llllll11111ll1Il1l1, ll1ll11111l11l1lIl1l1, public, ll111lll1l1l111lIl1l1, l1ll1111l11l11l1Il1l1
from reloadium.corium.l11111111ll1l1l1Il1l1 import l1l1ll1lll11lll1Il1l1, lll1l1111ll1l1llIl1l1
from reloadium.corium.ll1ll11111l11l1lIl1l1 import l1l111l1l1111ll1Il1l1, lll1111l11l1lll1Il1l1
from reloadium.corium.lllllllll1l11111Il1l1 import l1l11l1111l1ll1lIl1l1
from reloadium.corium.ll1ll1lll11l11l1Il1l1 import ll1ll1lll11l11l1Il1l1
from reloadium.corium.ll11l11l11ll11l1Il1l1 import llllll1l1l11ll11Il1l1
from reloadium.corium.ll11l11111lll1llIl1l1 import l1l1l11ll11l1l1lIl1l1, llll111l11111lllIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field
else:
    from reloadium.vendored.dataclasses import dataclass, field


__RELOADIUM__ = True

__all__ = ['llll1ll11111ll1lIl1l1', 'lll1ll111l1l1l11Il1l1', 'l11ll11111lll1l1Il1l1']


l11llll1l1l1l1llIl1l1 = ll1ll1lll11l11l1Il1l1.l1ll1l111llllll1Il1l1(__name__)


class llll1ll11111ll1lIl1l1:
    @classmethod
    def l1111l1l1111l111Il1l1(ll11l11lll111l1lIl1l1) -> Optional[FrameType]:
        ll1ll1llllll1111Il1l1: FrameType = sys._getframe(2)
        l1l1l1l11ll111llIl1l1 = next(l1ll1111l11l11l1Il1l1.ll1ll1llllll1111Il1l1.lll1l1l1l1l11ll1Il1l1(ll1ll1llllll1111Il1l1))
        return l1l1l1l11ll111llIl1l1


class lll1ll111l1l1l11Il1l1(llll1ll11111ll1lIl1l1):
    @classmethod
    def lll1l1l1111l1lllIl1l1(ll1ll1l1l11lll11Il1l1, ll11lll111lll1llIl1l1: List[Any], ll1lllll1l1llll1Il1l1: Dict[str, Any], lll1lll1ll1l1l1lIl1l1: List[l1l1l11ll11l1l1lIl1l1]) -> Any:  # type: ignore
        with lll1111l11l1lll1Il1l1():
            assert l1l11l1111l1ll1lIl1l1.l1l1lll1ll1ll1llIl1l1.l11llll1lll1llllIl1l1
            ll1ll1llllll1111Il1l1 = l1l11l1111l1ll1lIl1l1.l1l1lll1ll1ll1llIl1l1.l11llll1lll1llllIl1l1.ll11l11lll11l1llIl1l1.l1ll1ll1l1111lllIl1l1()
            ll1ll1llllll1111Il1l1.lll1l11l1lll1lllIl1l1()

            l1l1111ll1ll11llIl1l1 = l1l11l1111l1ll1lIl1l1.l1l1lll1ll1ll1llIl1l1.lll11lll1lll1111Il1l1.ll1l1lll11l11ll1Il1l1(ll1ll1llllll1111Il1l1.l1ll1ll11ll1l1llIl1l1, ll1ll1llllll1111Il1l1.ll11l1l111ll11l1Il1l1.l11111lllll1111lIl1l1())
            assert l1l1111ll1ll11llIl1l1
            l1ll11l1l11l111lIl1l1 = ll1ll1l1l11lll11Il1l1.l1111l1l1111l111Il1l1()

            for l1l1l111llllll11Il1l1 in lll1lll1ll1l1l1lIl1l1:
                l1l1l111llllll11Il1l1.l111l11l11ll1111Il1l1()

            for l1l1l111llllll11Il1l1 in lll1lll1ll1l1l1lIl1l1:
                l1l1l111llllll11Il1l1.lll111l11lll1l1lIl1l1()


        l1l1l1l11ll111llIl1l1 = l1l1111ll1ll11llIl1l1(*ll11lll111lll1llIl1l1, **ll1lllll1l1llll1Il1l1);        ll1ll1llllll1111Il1l1.ll1lllll1ll1l11lIl1l1.additional_info.pydev_step_stop = l1ll11l1l11l111lIl1l1  # type: ignore

        return l1l1l1l11ll111llIl1l1

    @classmethod
    async def lll11l11llll1l11Il1l1(ll1ll1l1l11lll11Il1l1, ll11lll111lll1llIl1l1: List[Any], ll1lllll1l1llll1Il1l1: Dict[str, Any], lll1lll1ll1l1l1lIl1l1: List[llll111l11111lllIl1l1]) -> Any:  # type: ignore
        with lll1111l11l1lll1Il1l1():
            assert l1l11l1111l1ll1lIl1l1.l1l1lll1ll1ll1llIl1l1.l11llll1lll1llllIl1l1
            ll1ll1llllll1111Il1l1 = l1l11l1111l1ll1lIl1l1.l1l1lll1ll1ll1llIl1l1.l11llll1lll1llllIl1l1.ll11l11lll11l1llIl1l1.l1ll1ll1l1111lllIl1l1()
            ll1ll1llllll1111Il1l1.lll1l11l1lll1lllIl1l1()

            l1l1111ll1ll11llIl1l1 = l1l11l1111l1ll1lIl1l1.l1l1lll1ll1ll1llIl1l1.lll11lll1lll1111Il1l1.ll1l1lll11l11ll1Il1l1(ll1ll1llllll1111Il1l1.l1ll1ll11ll1l1llIl1l1, ll1ll1llllll1111Il1l1.ll11l1l111ll11l1Il1l1.l11111lllll1111lIl1l1())
            assert l1l1111ll1ll11llIl1l1
            l1ll11l1l11l111lIl1l1 = ll1ll1l1l11lll11Il1l1.l1111l1l1111l111Il1l1()

            for l1l1l111llllll11Il1l1 in lll1lll1ll1l1l1lIl1l1:
                await l1l1l111llllll11Il1l1.l111l11l11ll1111Il1l1()

            for l1l1l111llllll11Il1l1 in lll1lll1ll1l1l1lIl1l1:
                await l1l1l111llllll11Il1l1.lll111l11lll1l1lIl1l1()


        l1l1l1l11ll111llIl1l1 = await l1l1111ll1ll11llIl1l1(*ll11lll111lll1llIl1l1, **ll1lllll1l1llll1Il1l1);        ll1ll1llllll1111Il1l1.ll1lllll1ll1l11lIl1l1.additional_info.pydev_step_stop = l1ll11l1l11l111lIl1l1  # type: ignore

        return l1l1l1l11ll111llIl1l1


class l11ll11111lll1l1Il1l1(llll1ll11111ll1lIl1l1):
    @classmethod
    def lll1l1l1111l1lllIl1l1(ll1ll1l1l11lll11Il1l1) -> Optional[ModuleType]:  # type: ignore
        with lll1111l11l1lll1Il1l1():
            assert l1l11l1111l1ll1lIl1l1.l1l1lll1ll1ll1llIl1l1.l11llll1lll1llllIl1l1
            ll1ll1llllll1111Il1l1 = l1l11l1111l1ll1lIl1l1.l1l1lll1ll1ll1llIl1l1.l11llll1lll1llllIl1l1.ll11l11lll11l1llIl1l1.l1ll1ll1l1111lllIl1l1()

            ll1lll11l11ll1llIl1l1 = Path(ll1ll1llllll1111Il1l1.lll1l1lll111l1llIl1l1.f_globals['__spec__'].origin).absolute()
            ll1llllll1l11ll1Il1l1 = ll1ll1llllll1111Il1l1.lll1l1lll111l1llIl1l1.f_globals['__name__']
            ll1ll1llllll1111Il1l1.lll1l11l1lll1lllIl1l1()
            l11llll11l11lll1Il1l1 = l1l11l1111l1ll1lIl1l1.l1l1lll1ll1ll1llIl1l1.lll11l1ll11lll1lIl1l1.ll11l1l11l1lll11Il1l1(ll1lll11l11ll1llIl1l1)

            if ( not l11llll11l11lll1Il1l1):
                l11llll1l1l1l1llIl1l1.ll11lll1l1ll1ll1Il1l1('Could not retrieve src.', l1l1lll11111ll1lIl1l1={'file': llllll1l1l11ll11Il1l1.l1111lllll111111Il1l1(ll1lll11l11ll1llIl1l1), 
'fullname': llllll1l1l11ll11Il1l1.ll1llllll1l11ll1Il1l1(ll1llllll1l11ll1Il1l1)})

            assert l11llll11l11lll1Il1l1

        try:
            l11llll11l11lll1Il1l1.l1l1l11ll1l11111Il1l1()
            l11llll11l11lll1Il1l1.lll1llll1111llllIl1l1(l1l111l11lll11l1Il1l1=False)
            l11llll11l11lll1Il1l1.l1llll11l1l1llllIl1l1(l1l111l11lll11l1Il1l1=False)
        except l1l111l1l1111ll1Il1l1 as l1l11l111l11l111Il1l1:
            ll1ll1llllll1111Il1l1.l1l1ll11111l111lIl1l1(l1l11l111l11l111Il1l1)
            return None

        import importlib.util

        ll1l11ll11ll11llIl1l1 = ll1ll1llllll1111Il1l1.lll1l1lll111l1llIl1l1.f_locals['__spec__']
        l1lllll1111l1ll1Il1l1 = importlib.util.module_from_spec(ll1l11ll11ll11llIl1l1)

        l11llll11l11lll1Il1l1.l1l1lll1ll11lll1Il1l1(l1lllll1111l1ll1Il1l1)
        return l1lllll1111l1ll1Il1l1


lll1l1111ll1l1llIl1l1.llll1ll1l111l1l1Il1l1(l1l1ll1lll11lll1Il1l1.llllllll111lllllIl1l1, lll1ll111l1l1l11Il1l1.lll1l1l1111l1lllIl1l1)
lll1l1111ll1l1llIl1l1.llll1ll1l111l1l1Il1l1(l1l1ll1lll11lll1Il1l1.ll11lll11111ll1lIl1l1, lll1ll111l1l1l11Il1l1.lll11l11llll1l11Il1l1)
lll1l1111ll1l1llIl1l1.llll1ll1l111l1l1Il1l1(l1l1ll1lll11lll1Il1l1.ll11l1ll1l1ll1l1Il1l1, l11ll11111lll1l1Il1l1.lll1l1l1111l1lllIl1l1)
