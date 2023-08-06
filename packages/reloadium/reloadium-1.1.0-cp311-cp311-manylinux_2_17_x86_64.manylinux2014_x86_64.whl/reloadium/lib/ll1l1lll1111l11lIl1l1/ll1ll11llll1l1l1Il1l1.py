from contextlib import contextmanager
import os
from pathlib import Path
import sys
import types
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Tuple, Type

from reloadium.lib.environ import env
from reloadium.corium.ll1ll11111l11l1lIl1l1 import lll1111l11l1lll1Il1l1
from reloadium.lib.ll1l1lll1111l11lIl1l1.ll111llllllll1llIl1l1 import ll11l1111l1lll11Il1l1, lll1l11l111llll1Il1l1
from reloadium.lib.ll1l1lll1111l11lIl1l1.ll1lll11111lllllIl1l1 import lllll1ll111111l1Il1l1
from reloadium.corium.l1l11ll1l111l111Il1l1 import llll1111ll1lll1lIl1l1, ll1lll11l111111lIl1l1, l111l1ll1l111lllIl1l1, l1ll111l1lllllllIl1l1, llll1l11l1111l11Il1l1
from reloadium.corium.ll11l11111lll1llIl1l1 import l1l1l11ll11l1l1lIl1l1, llll111l11111lllIl1l1
from reloadium.corium.l1l11111l111l1l1Il1l1 import lll1l1l1111llll1Il1l1
from reloadium.corium.l1ll1111l11l11l1Il1l1 import l1ll11111l111lllIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field

    from django.db import transaction
    from django.db.transaction import Atomic
else:
    from reloadium.vendored.dataclasses import dataclass, field


__RELOADIUM__ = True


@dataclass(**llll1l11l1111l11Il1l1)
class l1llllll1ll1ll11Il1l1(l1ll111l1lllllllIl1l1):
    ll1l111llll11lllIl1l1 = 'Field'

    @classmethod
    def ll1l11ll111lllllIl1l1(ll1ll1l1l11lll11Il1l1, l1l1llll1lll11llIl1l1: lll1l1l1111llll1Il1l1.l11ll11ll1lllll1Il1l1, lll1l1lll111l1llIl1l1: Any, lllll11l11l1l1l1Il1l1: ll1lll11l111111lIl1l1) -> bool:
        from django.db.models.fields import Field

        if ((hasattr(lll1l1lll111l1llIl1l1, 'field') and isinstance(lll1l1lll111l1llIl1l1.field, Field))):
            return True

        return False

    def ll111l11ll1l1ll1Il1l1(ll11l11lll111l1lIl1l1, l1l1l11111l1l11lIl1l1: l111l1ll1l111lllIl1l1) -> bool:
        return True

    @classmethod
    def lllll111l1ll1lllIl1l1(ll1ll1l1l11lll11Il1l1) -> int:
        return 200


@dataclass(repr=False)
class lll11l11111ll1llIl1l1(ll11l1111l1lll11Il1l1):
    l1l11ll1l1lll1llIl1l1: "Atomic" = field(init=False)

    ll1l1l1l1l11llllIl1l1: bool = field(init=False, default=False)

    def llll1l11ll1ll11lIl1l1(ll11l11lll111l1lIl1l1) -> None:
        super().llll1l11ll1ll11lIl1l1()
        from django.db import transaction

        ll11l11lll111l1lIl1l1.l1l11ll1l1lll1llIl1l1 = transaction.atomic()
        ll11l11lll111l1lIl1l1.l1l11ll1l1lll1llIl1l1.__enter__()

    def l111l11l11ll1111Il1l1(ll11l11lll111l1lIl1l1) -> None:
        super().l111l11l11ll1111Il1l1()
        if (ll11l11lll111l1lIl1l1.ll1l1l1l1l11llllIl1l1):
            return 

        ll11l11lll111l1lIl1l1.ll1l1l1l1l11llllIl1l1 = True
        from django.db import transaction

        transaction.set_rollback(True)
        ll11l11lll111l1lIl1l1.l1l11ll1l1lll1llIl1l1.__exit__(None, None, None)

    def lll111l11lll1l1lIl1l1(ll11l11lll111l1lIl1l1) -> None:
        super().lll111l11lll1l1lIl1l1()

        if (ll11l11lll111l1lIl1l1.ll1l1l1l1l11llllIl1l1):
            return 

        ll11l11lll111l1lIl1l1.ll1l1l1l1l11llllIl1l1 = True
        ll11l11lll111l1lIl1l1.l1l11ll1l1lll1llIl1l1.__exit__(None, None, None)

    def __repr__(ll11l11lll111l1lIl1l1) -> str:
        return 'DbMemento'


@dataclass(repr=False)
class lllll11111lll11lIl1l1(lll1l11l111llll1Il1l1):
    l1l11ll1l1lll1llIl1l1: "Atomic" = field(init=False)

    ll1l1l1l1l11llllIl1l1: bool = field(init=False, default=False)

    async def llll1l11ll1ll11lIl1l1(ll11l11lll111l1lIl1l1) -> None:
        await super().llll1l11ll1ll11lIl1l1()
        from django.db import transaction
        from asgiref.sync import sync_to_async

        ll11l11lll111l1lIl1l1.l1l11ll1l1lll1llIl1l1 = transaction.atomic()
        await sync_to_async(ll11l11lll111l1lIl1l1.l1l11ll1l1lll1llIl1l1.__enter__)()

    async def l111l11l11ll1111Il1l1(ll11l11lll111l1lIl1l1) -> None:
        from asgiref.sync import sync_to_async

        await super().l111l11l11ll1111Il1l1()
        if (ll11l11lll111l1lIl1l1.ll1l1l1l1l11llllIl1l1):
            return 

        ll11l11lll111l1lIl1l1.ll1l1l1l1l11llllIl1l1 = True
        from django.db import transaction

        def l11ll1l111llll1lIl1l1() -> None:
            transaction.set_rollback(True)
            ll11l11lll111l1lIl1l1.l1l11ll1l1lll1llIl1l1.__exit__(None, None, None)
        await sync_to_async(l11ll1l111llll1lIl1l1)()

    async def lll111l11lll1l1lIl1l1(ll11l11lll111l1lIl1l1) -> None:
        from asgiref.sync import sync_to_async

        await super().lll111l11lll1l1lIl1l1()

        if (ll11l11lll111l1lIl1l1.ll1l1l1l1l11llllIl1l1):
            return 

        ll11l11lll111l1lIl1l1.ll1l1l1l1l11llllIl1l1 = True
        await sync_to_async(ll11l11lll111l1lIl1l1.l1l11ll1l1lll1llIl1l1.__exit__)(None, None, None)

    def __repr__(ll11l11lll111l1lIl1l1) -> str:
        return 'AsyncDbMemento'


@dataclass
class l1llll1111l11lllIl1l1(lllll1ll111111l1Il1l1):
    l1111ll11l1lll11Il1l1 = 'Django'

    lll111lll11l1l1lIl1l1: Optional[int] = field(init=False)
    l1l11l111llll111Il1l1: Optional[Callable[..., Any]] = field(init=False, default=None)

    def __post_init__(ll11l11lll111l1lIl1l1) -> None:
        super().__post_init__()
        ll11l11lll111l1lIl1l1.lll111lll11l1l1lIl1l1 = None

    def lll1l111l1l111llIl1l1(ll11l11lll111l1lIl1l1) -> List[Type[l111l1ll1l111lllIl1l1]]:
        return [l1llllll1ll1ll11Il1l1]

    def ll1l1l1ll1lll11lIl1l1(ll11l11lll111l1lIl1l1) -> None:
        super().ll1l1l1ll1lll11lIl1l1()
        if ('runserver' in sys.argv):
            sys.argv.append('--noreload')

    def ll111l111ll11l1lIl1l1(ll11l11lll111l1lIl1l1, l1lllll1111l1ll1Il1l1: types.ModuleType) -> None:
        if (ll11l11lll111l1lIl1l1.ll111l111ll1llllIl1l1(l1lllll1111l1ll1Il1l1, 'django.core.management.commands.runserver')):
            ll11l11lll111l1lIl1l1.l111ll111111llllIl1l1()
            ll11l11lll111l1lIl1l1.ll1111llll1111llIl1l1()

    def llllllll11111ll1Il1l1(ll11l11lll111l1lIl1l1, l1l1lll111l1llllIl1l1: str) -> Optional["l1l1l11ll11l1l1lIl1l1"]:
        if ( not os.environ.get('DJANGO_SETTINGS_MODULE')):
            return None

        l1l1l1l11ll111llIl1l1 = lll11l11111ll1llIl1l1(l1l1lll111l1llllIl1l1=l1l1lll111l1llllIl1l1, ll111llllllll1llIl1l1=ll11l11lll111l1lIl1l1)
        l1l1l1l11ll111llIl1l1.llll1l11ll1ll11lIl1l1()
        return l1l1l1l11ll111llIl1l1

    async def lllll11111lll1l1Il1l1(ll11l11lll111l1lIl1l1, l1l1lll111l1llllIl1l1: str) -> Optional["llll111l11111lllIl1l1"]:
        if ( not os.environ.get('DJANGO_SETTINGS_MODULE')):
            return None

        l1l1l1l11ll111llIl1l1 = lllll11111lll11lIl1l1(l1l1lll111l1llllIl1l1=l1l1lll111l1llllIl1l1, ll111llllllll1llIl1l1=ll11l11lll111l1lIl1l1)
        await l1l1l1l11ll111llIl1l1.llll1l11ll1ll11lIl1l1()
        return l1l1l1l11ll111llIl1l1

    def l111ll111111llllIl1l1(ll11l11lll111l1lIl1l1) -> None:
        import django.core.management.commands.runserver

        l1l111111l11111lIl1l1 = django.core.management.commands.runserver.Command.handle

        def lll1ll1ll111lll1Il1l1(*ll11lll111lll1llIl1l1: Any, **llll11l1llllllllIl1l1: Any) -> Any:
            with lll1111l11l1lll1Il1l1():
                llll1l11ll111l11Il1l1 = llll11l1llllllllIl1l1.get('addrport')
                if ( not llll1l11ll111l11Il1l1):
                    llll1l11ll111l11Il1l1 = django.core.management.commands.runserver.Command.default_port

                llll1l11ll111l11Il1l1 = llll1l11ll111l11Il1l1.split(':')[ - 1]
                llll1l11ll111l11Il1l1 = int(llll1l11ll111l11Il1l1)
                ll11l11lll111l1lIl1l1.lll111lll11l1l1lIl1l1 = llll1l11ll111l11Il1l1

            return l1l111111l11111lIl1l1(*ll11lll111lll1llIl1l1, **llll11l1llllllllIl1l1)

        l1ll11111l111lllIl1l1.ll1llll1lll1lll1Il1l1(django.core.management.commands.runserver.Command, 'handle', lll1ll1ll111lll1Il1l1)

    def ll1111llll1111llIl1l1(ll11l11lll111l1lIl1l1) -> None:
        import django.core.management.commands.runserver

        l1l111111l11111lIl1l1 = django.core.management.commands.runserver.Command.get_handler

        def lll1ll1ll111lll1Il1l1(*ll11lll111lll1llIl1l1: Any, **llll11l1llllllllIl1l1: Any) -> Any:
            with lll1111l11l1lll1Il1l1():
                assert ll11l11lll111l1lIl1l1.lll111lll11l1l1lIl1l1
                ll11l11lll111l1lIl1l1.lll1llll1ll111llIl1l1 = ll11l11lll111l1lIl1l1.l1lll1lll11111llIl1l1(ll11l11lll111l1lIl1l1.lll111lll11l1l1lIl1l1)
                if (env.page_reload_on_start):
                    ll11l11lll111l1lIl1l1.lll1llll1ll111llIl1l1.l11l111l111llll1Il1l1(2.0)

            return l1l111111l11111lIl1l1(*ll11lll111lll1llIl1l1, **llll11l1llllllllIl1l1)

        l1ll11111l111lllIl1l1.ll1llll1lll1lll1Il1l1(django.core.management.commands.runserver.Command, 'get_handler', lll1ll1ll111lll1Il1l1)

    def l1l111llll1l11l1Il1l1(ll11l11lll111l1lIl1l1) -> None:
        super().l1l111llll1l11l1Il1l1()

        import django.core.handlers.base

        l1l111111l11111lIl1l1 = django.core.handlers.base.BaseHandler.get_response

        def lll1ll1ll111lll1Il1l1(l1111l1l1llll111Il1l1: Any, l1ll1ll11lll1l11Il1l1: Any) -> Any:
            l1l1ll11ll1l1ll1Il1l1 = l1l111111l11111lIl1l1(l1111l1l1llll111Il1l1, l1ll1ll11lll1l11Il1l1)

            if ( not ll11l11lll111l1lIl1l1.lll1llll1ll111llIl1l1):
                return l1l1ll11ll1l1ll1Il1l1

            l1ll111111ll111lIl1l1 = l1l1ll11ll1l1ll1Il1l1.get('content-type')

            if (( not l1ll111111ll111lIl1l1 or 'text/html' not in l1ll111111ll111lIl1l1)):
                return l1l1ll11ll1l1ll1Il1l1

            l1ll11l1111l1l1lIl1l1 = l1l1ll11ll1l1ll1Il1l1.content

            if (isinstance(l1ll11l1111l1l1lIl1l1, bytes)):
                l1ll11l1111l1l1lIl1l1 = l1ll11l1111l1l1lIl1l1.decode('utf-8')

            l111111l111l111lIl1l1 = ll11l11lll111l1lIl1l1.lll1llll1ll111llIl1l1.l1l11111l1l1l1llIl1l1(l1ll11l1111l1l1lIl1l1)

            l1l1ll11ll1l1ll1Il1l1.content = l111111l111l111lIl1l1.encode('utf-8')
            l1l1ll11ll1l1ll1Il1l1['content-length'] = str(len(l1l1ll11ll1l1ll1Il1l1.content)).encode('ascii')
            return l1l1ll11ll1l1ll1Il1l1

        django.core.handlers.base.BaseHandler.get_response = lll1ll1ll111lll1Il1l1  # type: ignore

    def l1lll111l11l11llIl1l1(ll11l11lll111l1lIl1l1, l1111lllll111111Il1l1: Path) -> None:
        super().l1lll111l11l11llIl1l1(l1111lllll111111Il1l1)

        from django.apps.registry import Apps

        ll11l11lll111l1lIl1l1.l1l11l111llll111Il1l1 = Apps.register_model

        def l11l1111111l111lIl1l1(*ll11lll111lll1llIl1l1: Any, **ll1lllll1l1llll1Il1l1: Any) -> Any:
            pass

        Apps.register_model = l11l1111111l111lIl1l1

    def lllll1ll1ll1ll1lIl1l1(ll11l11lll111l1lIl1l1, l1111lllll111111Il1l1: Path, l1llll1l11111ll1Il1l1: List[llll1111ll1lll1lIl1l1]) -> None:
        super().lllll1ll1ll1ll1lIl1l1(l1111lllll111111Il1l1, l1llll1l11111ll1Il1l1)

        if ( not ll11l11lll111l1lIl1l1.l1l11l111llll111Il1l1):
            return 

        from django.apps.registry import Apps

        Apps.register_model = ll11l11lll111l1lIl1l1.l1l11l111llll111Il1l1
