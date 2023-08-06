from pathlib import Path
import types
from typing import TYPE_CHECKING, Any, List

from reloadium.lib.ll1l1lll1111l11lIl1l1.ll111llllllll1llIl1l1 import ll1lll111lll11l1Il1l1
from reloadium.corium.l1l11ll1l111l111Il1l1 import llll1111ll1lll1lIl1l1
from reloadium.corium.l1ll1111l11l11l1Il1l1 import l1ll11111l111lllIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field
else:
    from reloadium.vendored.dataclasses import dataclass, field


__RELOADIUM__ = True


@dataclass
class lll111lllll11lllIl1l1(ll1lll111lll11l1Il1l1):
    l1111ll11l1lll11Il1l1 = 'PyGame'

    lll11l1l1111ll11Il1l1: bool = field(init=False, default=False)

    def ll111l111ll11l1lIl1l1(ll11l11lll111l1lIl1l1, lll1l1ll1l1l1111Il1l1: types.ModuleType) -> None:
        if (ll11l11lll111l1lIl1l1.ll111l111ll1llllIl1l1(lll1l1ll1l1l1111Il1l1, 'pygame.base')):
            ll11l11lll111l1lIl1l1.ll1lllll11ll1lllIl1l1()

    def ll1lllll11ll1lllIl1l1(ll11l11lll111l1lIl1l1) -> None:
        import pygame.display

        lll1l11lll1l11l1Il1l1 = pygame.display.update

        def l11111l11lll1ll1Il1l1(*ll11lll111lll1llIl1l1: Any, **ll1lllll1l1llll1Il1l1: Any) -> None:
            if (ll11l11lll111l1lIl1l1.lll11l1l1111ll11Il1l1):
                l1ll11111l111lllIl1l1.lll1111lll11llllIl1l1(0.1)
                return None
            else:
                return lll1l11lll1l11l1Il1l1(*ll11lll111lll1llIl1l1, **ll1lllll1l1llll1Il1l1)

        pygame.display.update = l11111l11lll1ll1Il1l1

    def l1lll111l11l11llIl1l1(ll11l11lll111l1lIl1l1, l1111lllll111111Il1l1: Path) -> None:
        ll11l11lll111l1lIl1l1.lll11l1l1111ll11Il1l1 = True

    def lllll1ll1ll1ll1lIl1l1(ll11l11lll111l1lIl1l1, l1111lllll111111Il1l1: Path, l1llll1l11111ll1Il1l1: List[llll1111ll1lll1lIl1l1]) -> None:
        ll11l11lll111l1lIl1l1.lll11l1l1111ll11Il1l1 = False

    def ll1lll111l1l1ll1Il1l1(ll11l11lll111l1lIl1l1, ll1111lll1l11111Il1l1: Exception) -> None:
        ll11l11lll111l1lIl1l1.lll11l1l1111ll11Il1l1 = False
