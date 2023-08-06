from abc import ABC
from contextlib import contextmanager
from pathlib import Path
import sys
import types
from typing import TYPE_CHECKING, Any, ClassVar, Dict, Generator, List, Optional, Tuple, Type

from reloadium.corium.ll1ll1lll11l11l1Il1l1 import l11ll11111l1l11lIl1l1, ll1ll1lll11l11l1Il1l1
from reloadium.corium.l1l11ll1l111l111Il1l1 import llll1111ll1lll1lIl1l1, l111l1ll1l111lllIl1l1
from reloadium.corium.ll11l11111lll1llIl1l1 import l1l1l11ll11l1l1lIl1l1, llll111l11111lllIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field

    from reloadium.lib.ll1l1lll1111l11lIl1l1.ll1l11ll1lllll1lIl1l1 import l1lll1l1ll1lll11Il1l1
else:
    from reloadium.vendored.dataclasses import dataclass, field


__RELOADIUM__ = True


@dataclass
class ll1lll111lll11l1Il1l1:
    ll1l11ll1lllll1lIl1l1: "l1lll1l1ll1lll11Il1l1"

    l1111ll11l1lll11Il1l1: ClassVar[str] = NotImplemented
    l1l11lll1ll11l1lIl1l1: bool = field(init=False, default=False)

    lll111llll11ll11Il1l1: l11ll11111l1l11lIl1l1 = field(init=False)

    def __post_init__(ll11l11lll111l1lIl1l1) -> None:
        ll11l11lll111l1lIl1l1.lll111llll11ll11Il1l1 = ll1ll1lll11l11l1Il1l1.l1ll1l111llllll1Il1l1(ll11l11lll111l1lIl1l1.l1111ll11l1lll11Il1l1)
        ll11l11lll111l1lIl1l1.lll111llll11ll11Il1l1.l1lll11l11l1l11lIl1l1('Creating extension')
        ll11l11lll111l1lIl1l1.ll1l11ll1lllll1lIl1l1.l1l1lll1ll1ll1llIl1l1.l11ll11111llll1lIl1l1.l1ll1ll1l1l1lll1Il1l1(ll11l11lll111l1lIl1l1.ll1l111ll1l1ll1lIl1l1())

    def ll1l111ll1l1ll1lIl1l1(ll11l11lll111l1lIl1l1) -> List[Type[l111l1ll1l111lllIl1l1]]:
        l1l1l1l11ll111llIl1l1 = []
        l1l11ll1l111l111Il1l1 = ll11l11lll111l1lIl1l1.lll1l111l1l111llIl1l1()
        for l1l11ll11lll1111Il1l1 in l1l11ll1l111l111Il1l1:
            l1l11ll11lll1111Il1l1.l11l1l1l11ll1ll1Il1l1 = ll11l11lll111l1lIl1l1.l1111ll11l1lll11Il1l1

        l1l1l1l11ll111llIl1l1.extend(l1l11ll1l111l111Il1l1)
        return l1l1l1l11ll111llIl1l1

    def ll1lllll1lll1lllIl1l1(ll11l11lll111l1lIl1l1) -> None:
        ll11l11lll111l1lIl1l1.l1l11lll1ll11l1lIl1l1 = True

    def ll111l111ll11l1lIl1l1(ll11l11lll111l1lIl1l1, l1lllll1111l1ll1Il1l1: types.ModuleType) -> None:
        pass

    @classmethod
    def ll111ll1ll111l11Il1l1(ll1ll1l1l11lll11Il1l1, l1lllll1111l1ll1Il1l1: types.ModuleType) -> bool:
        if ( not hasattr(l1lllll1111l1ll1Il1l1, '__name__')):
            return False

        l1l1l1l11ll111llIl1l1 = l1lllll1111l1ll1Il1l1.__name__.split('.')[0].lower() == ll1ll1l1l11lll11Il1l1.l1111ll11l1lll11Il1l1.lower()
        return l1l1l1l11ll111llIl1l1

    @contextmanager
    def l1ll11l1l111111lIl1l1(ll11l11lll111l1lIl1l1) -> Generator[None, None, None]:
        yield 

    def ll1l1l1ll1lll11lIl1l1(ll11l11lll111l1lIl1l1) -> None:
        pass

    def ll1lll111l1l1ll1Il1l1(ll11l11lll111l1lIl1l1, ll1111lll1l11111Il1l1: Exception) -> None:
        pass

    def llllllll11111ll1Il1l1(ll11l11lll111l1lIl1l1, l1l1lll111l1llllIl1l1: str) -> Optional[l1l1l11ll11l1l1lIl1l1]:
        return None

    async def lllll11111lll1l1Il1l1(ll11l11lll111l1lIl1l1, l1l1lll111l1llllIl1l1: str) -> Optional[llll111l11111lllIl1l1]:
        return None

    def l11l1111l11lll11Il1l1(ll11l11lll111l1lIl1l1, l1l1lll111l1llllIl1l1: str) -> Optional[l1l1l11ll11l1l1lIl1l1]:
        return None

    async def ll11111111l111l1Il1l1(ll11l11lll111l1lIl1l1, l1l1lll111l1llllIl1l1: str) -> Optional[llll111l11111lllIl1l1]:
        return None

    def ll11ll111l1ll1l1Il1l1(ll11l11lll111l1lIl1l1, l1111lllll111111Il1l1: Path) -> None:
        pass

    def l1lll111l11l11llIl1l1(ll11l11lll111l1lIl1l1, l1111lllll111111Il1l1: Path) -> None:
        pass

    def lllll1ll1ll1ll1lIl1l1(ll11l11lll111l1lIl1l1, l1111lllll111111Il1l1: Path, l1llll1l11111ll1Il1l1: List[llll1111ll1lll1lIl1l1]) -> None:
        pass

    def __eq__(ll11l11lll111l1lIl1l1, llll1l1l1ll111l1Il1l1: Any) -> bool:
        return id(llll1l1l1ll111l1Il1l1) == id(ll11l11lll111l1lIl1l1)

    def lll1l111l1l111llIl1l1(ll11l11lll111l1lIl1l1) -> List[Type[l111l1ll1l111lllIl1l1]]:
        return []

    def ll111l111ll1llllIl1l1(ll11l11lll111l1lIl1l1, l1lllll1111l1ll1Il1l1: types.ModuleType, l1l1lll111l1llllIl1l1: str) -> bool:
        l1l1l1l11ll111llIl1l1 = (hasattr(l1lllll1111l1ll1Il1l1, '__name__') and l1lllll1111l1ll1Il1l1.__name__ == l1l1lll111l1llllIl1l1)
        return l1l1l1l11ll111llIl1l1


@dataclass(repr=False)
class ll11l1111l1lll11Il1l1(l1l1l11ll11l1l1lIl1l1):
    ll111llllllll1llIl1l1: ll1lll111lll11l1Il1l1

    def __repr__(ll11l11lll111l1lIl1l1) -> str:
        return 'ExtensionMemento'


@dataclass(repr=False)
class lll1l11l111llll1Il1l1(llll111l11111lllIl1l1):
    ll111llllllll1llIl1l1: ll1lll111lll11l1Il1l1

    def __repr__(ll11l11lll111l1lIl1l1) -> str:
        return 'AsyncExtensionMemento'
