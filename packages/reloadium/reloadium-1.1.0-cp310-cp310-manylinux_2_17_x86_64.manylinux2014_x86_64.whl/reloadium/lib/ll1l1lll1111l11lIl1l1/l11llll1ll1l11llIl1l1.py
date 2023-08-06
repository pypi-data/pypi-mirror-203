import re
from contextlib import contextmanager
import os
import sys
import types
from pathlib import Path
from textwrap import dedent
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Set, Tuple, Union

from reloadium.corium.ll1ll11111l11l1lIl1l1 import lll1111l11l1lll1Il1l1
from reloadium.lib.ll1l1lll1111l11lIl1l1.ll111llllllll1llIl1l1 import ll1lll111lll11l1Il1l1, ll11l1111l1lll11Il1l1
from reloadium.corium.ll11l11111lll1llIl1l1 import l1l1l11ll11l1l1lIl1l1
from reloadium.corium.l1ll1111l11l11l1Il1l1 import l1ll11111l111lllIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field

    from sqlalchemy.engine.base import Engine, Transaction
    from sqlalchemy.orm.session import Session
else:
    from reloadium.vendored.dataclasses import dataclass, field


__RELOADIUM__ = True


@dataclass(repr=False)
class lll11l11111ll1llIl1l1(ll11l1111l1lll11Il1l1):
    ll111llllllll1llIl1l1: "l1l11ll11ll11ll1Il1l1"
    l1l1lllll1lll1l1Il1l1: List["Transaction"] = field(init=False, default_factory=list)

    def llll1l11ll1ll11lIl1l1(ll11l11lll111l1lIl1l1) -> None:
        from sqlalchemy.orm.session import _sessions

        super().llll1l11ll1ll11lIl1l1()

        l11l1l1lll111111Il1l1 = list(_sessions.values())

        for l1llll11ll111111Il1l1 in l11l1l1lll111111Il1l1:
            if ( not l1llll11ll111111Il1l1.is_active):
                continue

            ll1l1l1ll1llll11Il1l1 = l1llll11ll111111Il1l1.begin_nested()
            ll11l11lll111l1lIl1l1.l1l1lllll1lll1l1Il1l1.append(ll1l1l1ll1llll11Il1l1)

    def __repr__(ll11l11lll111l1lIl1l1) -> str:
        return 'DbMemento'

    def l111l11l11ll1111Il1l1(ll11l11lll111l1lIl1l1) -> None:
        super().l111l11l11ll1111Il1l1()

        while ll11l11lll111l1lIl1l1.l1l1lllll1lll1l1Il1l1:
            ll1l1l1ll1llll11Il1l1 = ll11l11lll111l1lIl1l1.l1l1lllll1lll1l1Il1l1.pop()
            if (ll1l1l1ll1llll11Il1l1.is_active):
                try:
                    ll1l1l1ll1llll11Il1l1.rollback()
                except :
                    pass

    def lll111l11lll1l1lIl1l1(ll11l11lll111l1lIl1l1) -> None:
        super().lll111l11lll1l1lIl1l1()

        while ll11l11lll111l1lIl1l1.l1l1lllll1lll1l1Il1l1:
            ll1l1l1ll1llll11Il1l1 = ll11l11lll111l1lIl1l1.l1l1lllll1lll1l1Il1l1.pop()
            if (ll1l1l1ll1llll11Il1l1.is_active):
                try:
                    ll1l1l1ll1llll11Il1l1.commit()
                except :
                    pass


@dataclass
class l1l11ll11ll11ll1Il1l1(ll1lll111lll11l1Il1l1):
    l1111ll11l1lll11Il1l1 = 'Sqlalchemy'

    l11ll1l11llll111Il1l1: List["Engine"] = field(init=False, default_factory=list)
    l11l1l1lll111111Il1l1: Set["Session"] = field(init=False, default_factory=set)
    ll11l11ll11l1lllIl1l1: Tuple[int, ...] = field(init=False)

    def ll111l111ll11l1lIl1l1(ll11l11lll111l1lIl1l1, l1lllll1111l1ll1Il1l1: types.ModuleType) -> None:
        if (ll11l11lll111l1lIl1l1.ll111l111ll1llllIl1l1(l1lllll1111l1ll1Il1l1, 'sqlalchemy')):
            ll11l11lll111l1lIl1l1.l11l1l1llll1l1l1Il1l1(l1lllll1111l1ll1Il1l1)

        if (ll11l11lll111l1lIl1l1.ll111l111ll1llllIl1l1(l1lllll1111l1ll1Il1l1, 'sqlalchemy.engine.base')):
            ll11l11lll111l1lIl1l1.ll1llll11l11ll1lIl1l1(l1lllll1111l1ll1Il1l1)

    def l11l1l1llll1l1l1Il1l1(ll11l11lll111l1lIl1l1, l1lllll1111l1ll1Il1l1: Any) -> None:
        l1ll11l1111l1l1lIl1l1 = Path(l1lllll1111l1ll1Il1l1.__file__).read_text(encoding='utf-8')
        __version__ = re.findall('__version__\\s*?=\\s*?"(.*?)"', l1ll11l1111l1l1lIl1l1)[0]

        ll1111lll1111l1lIl1l1 = [int(ll1l11l1l11ll11lIl1l1) for ll1l11l1l11ll11lIl1l1 in __version__.split('.')]
        ll11l11lll111l1lIl1l1.ll11l11ll11l1lllIl1l1 = tuple(ll1111lll1111l1lIl1l1)

    def llllllll11111ll1Il1l1(ll11l11lll111l1lIl1l1, l1l1lll111l1llllIl1l1: str) -> Optional["l1l1l11ll11l1l1lIl1l1"]:
        l1l1l1l11ll111llIl1l1 = lll11l11111ll1llIl1l1(l1l1lll111l1llllIl1l1=l1l1lll111l1llllIl1l1, ll111llllllll1llIl1l1=ll11l11lll111l1lIl1l1)
        l1l1l1l11ll111llIl1l1.llll1l11ll1ll11lIl1l1()
        return l1l1l1l11ll111llIl1l1

    def ll1llll11l11ll1lIl1l1(ll11l11lll111l1lIl1l1, l1lllll1111l1ll1Il1l1: Any) -> None:
        lll11l1ll1ll1l1lIl1l1 = locals().copy()

        lll11l1ll1ll1l1lIl1l1.update({'original': l1lllll1111l1ll1Il1l1.Engine.__init__, 'reloader_code': lll1111l11l1lll1Il1l1, 'engines': ll11l11lll111l1lIl1l1.l11ll1l11llll111Il1l1})





        ll1l1l111l1lll11Il1l1 = dedent('\n            def patched(\n                    self2: Any,\n                    pool: Any,\n                    dialect: Any,\n                    url: Any,\n                    logging_name: Any = None,\n                    echo: Any = None,\n                    proxy: Any = None,\n                    execution_options: Any = None,\n                    hide_parameters: Any = None,\n            ) -> Any:\n                original(self2,\n                         pool,\n                         dialect,\n                         url,\n                         logging_name,\n                         echo,\n                         proxy,\n                         execution_options,\n                         hide_parameters\n                         )\n                with reloader_code():\n                    engines.append(self2)')
























        l1llllllll1ll1l1Il1l1 = dedent('\n            def patched(\n                    self2: Any,\n                    pool: Any,\n                    dialect: Any,\n                    url: Any,\n                    logging_name: Any = None,\n                    echo: Any = None,\n                    query_cache_size: Any = 500,\n                    execution_options: Any = None,\n                    hide_parameters: Any = False,\n            ) -> Any:\n                original(self2,\n                         pool,\n                         dialect,\n                         url,\n                         logging_name,\n                         echo,\n                         query_cache_size,\n                         execution_options,\n                         hide_parameters)\n                with reloader_code():\n                    engines.append(self2)\n        ')
























        if (ll11l11lll111l1lIl1l1.ll11l11ll11l1lllIl1l1 <= (1, 3, 24, )):
            exec(ll1l1l111l1lll11Il1l1, {**globals(), **lll11l1ll1ll1l1lIl1l1}, lll11l1ll1ll1l1lIl1l1)
        else:
            exec(l1llllllll1ll1l1Il1l1, {**globals(), **lll11l1ll1ll1l1lIl1l1}, lll11l1ll1ll1l1lIl1l1)

        l1ll11111l111lllIl1l1.ll1llll1lll1lll1Il1l1(l1lllll1111l1ll1Il1l1.Engine, '__init__', lll11l1ll1ll1l1lIl1l1['patched'])
