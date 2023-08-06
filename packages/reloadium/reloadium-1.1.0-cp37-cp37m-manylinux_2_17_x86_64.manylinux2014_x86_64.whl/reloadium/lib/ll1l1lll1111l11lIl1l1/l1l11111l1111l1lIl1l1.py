from contextlib import contextmanager
from pathlib import Path
import types
from typing import TYPE_CHECKING, Any, Dict, Generator, List, Tuple, Type

from reloadium.lib.environ import env
from reloadium.corium.ll1ll11111l11l1lIl1l1 import lll1111l11l1lll1Il1l1
from reloadium.lib.ll1l1lll1111l11lIl1l1.ll1lll11111lllllIl1l1 import lllll1ll111111l1Il1l1
from reloadium.corium.l1l11ll1l111l111Il1l1 import ll1lll11l111111lIl1l1, l111l1ll1l111lllIl1l1, l1ll111l1lllllllIl1l1, llll1l11l1111l11Il1l1
from reloadium.corium.l1l11111l111l1l1Il1l1 import lll1l1l1111llll1Il1l1
from reloadium.corium.l1ll1111l11l11l1Il1l1 import l1ll11111l111lllIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass
else:
    from reloadium.vendored.dataclasses import dataclass


__RELOADIUM__ = True


@dataclass(**llll1l11l1111l11Il1l1)
class l1llll1l1l1ll1l1Il1l1(l1ll111l1lllllllIl1l1):
    ll1l111llll11lllIl1l1 = 'FlaskApp'

    @classmethod
    def ll1l11ll111lllllIl1l1(ll1ll1l1l11lll11Il1l1, l1l1llll1lll11llIl1l1: lll1l1l1111llll1Il1l1.l11ll11ll1lllll1Il1l1, lll1l1lll111l1llIl1l1: Any, lllll11l11l1l1l1Il1l1: ll1lll11l111111lIl1l1) -> bool:
        import flask

        if (isinstance(lll1l1lll111l1llIl1l1, flask.Flask)):
            return True

        return False

    def lll111l111ll1l11Il1l1(ll11l11lll111l1lIl1l1) -> bool:
        return True

    @classmethod
    def lllll111l1ll1lllIl1l1(ll1ll1l1l11lll11Il1l1) -> int:
        return (super().lllll111l1ll1lllIl1l1() + 10)


@dataclass(**llll1l11l1111l11Il1l1)
class l111l1lll111lll1Il1l1(l1ll111l1lllllllIl1l1):
    ll1l111llll11lllIl1l1 = 'Request'

    @classmethod
    def ll1l11ll111lllllIl1l1(ll1ll1l1l11lll11Il1l1, l1l1llll1lll11llIl1l1: lll1l1l1111llll1Il1l1.l11ll11ll1lllll1Il1l1, lll1l1lll111l1llIl1l1: Any, lllll11l11l1l1l1Il1l1: ll1lll11l111111lIl1l1) -> bool:
        if (repr(lll1l1lll111l1llIl1l1) == '<LocalProxy unbound>'):
            return True

        return False

    def lll111l111ll1l11Il1l1(ll11l11lll111l1lIl1l1) -> bool:
        return True

    @classmethod
    def lllll111l1ll1lllIl1l1(ll1ll1l1l11lll11Il1l1) -> int:

        return int(10000000000.0)


@dataclass
class l11lll11lll1ll11Il1l1(lllll1ll111111l1Il1l1):
    l1111ll11l1lll11Il1l1 = 'Flask'

    @contextmanager
    def l1ll11l1l111111lIl1l1(ll11l11lll111l1lIl1l1) -> Generator[None, None, None]:




        from flask import Flask as FlaskLib 

        def l1l1l111llllll1lIl1l1(*ll11lll111lll1llIl1l1: Any, **ll1lllll1l1llll1Il1l1: Any) -> Any:
            def lllllll11l1llll1Il1l1(l1l11lll1l1l11l1Il1l1: Any) -> Any:
                return l1l11lll1l1l11l1Il1l1

            return lllllll11l1llll1Il1l1

        ll1lll11llll1l1lIl1l1 = FlaskLib.route
        FlaskLib.route = l1l1l111llllll1lIl1l1  # type: ignore

        try:
            yield 
        finally:
            FlaskLib.route = ll1lll11llll1l1lIl1l1  # type: ignore

    def lll1l111l1l111llIl1l1(ll11l11lll111l1lIl1l1) -> List[Type[l111l1ll1l111lllIl1l1]]:
        return [l1llll1l1l1ll1l1Il1l1, l111l1lll111lll1Il1l1]

    def ll111l111ll11l1lIl1l1(ll11l11lll111l1lIl1l1, lll1l1ll1l1l1111Il1l1: types.ModuleType) -> None:
        if (ll11l11lll111l1lIl1l1.ll111l111ll1llllIl1l1(lll1l1ll1l1l1111Il1l1, 'flask.app')):
            ll11l11lll111l1lIl1l1.l11llllll1lll111Il1l1()
            ll11l11lll111l1lIl1l1.ll111l111111l111Il1l1()
            ll11l11lll111l1lIl1l1.ll1ll1111ll1l11lIl1l1()

        if (ll11l11lll111l1lIl1l1.ll111l111ll1llllIl1l1(lll1l1ll1l1l1111Il1l1, 'flask.cli')):
            ll11l11lll111l1lIl1l1.lllllllll111ll11Il1l1()

    def l11llllll1lll111Il1l1(ll11l11lll111l1lIl1l1) -> None:
        try:
            import werkzeug.serving
            import flask.cli
        except ImportError:
            return 

        l1l111111l11111lIl1l1 = werkzeug.serving.run_simple

        def lll1ll1ll111lll1Il1l1(*ll11lll111lll1llIl1l1: Any, **ll1lllll1l1llll1Il1l1: Any) -> Any:
            with lll1111l11l1lll1Il1l1():
                llll1l11ll111l11Il1l1 = ll1lllll1l1llll1Il1l1.get('port')
                if ( not llll1l11ll111l11Il1l1):
                    llll1l11ll111l11Il1l1 = ll11lll111lll1llIl1l1[1]

                ll11l11lll111l1lIl1l1.lll1llll1ll111llIl1l1 = ll11l11lll111l1lIl1l1.l1lll1lll11111llIl1l1(llll1l11ll111l11Il1l1)
                if (env.page_reload_on_start):
                    ll11l11lll111l1lIl1l1.lll1llll1ll111llIl1l1.l11l111l111llll1Il1l1(1.0)
            l1l111111l11111lIl1l1(*ll11lll111lll1llIl1l1, **ll1lllll1l1llll1Il1l1)

        l1ll11111l111lllIl1l1.ll1llll1lll1lll1Il1l1(werkzeug.serving, 'run_simple', lll1ll1ll111lll1Il1l1)
        l1ll11111l111lllIl1l1.ll1llll1lll1lll1Il1l1(flask.cli, 'run_simple', lll1ll1ll111lll1Il1l1)

    def ll1ll1111ll1l11lIl1l1(ll11l11lll111l1lIl1l1) -> None:
        try:
            import flask
        except ImportError:
            return 

        l1l111111l11111lIl1l1 = flask.app.Flask.__init__

        def lll1ll1ll111lll1Il1l1(lll1l1l1ll1l1111Il1l1: Any, *ll11lll111lll1llIl1l1: Any, **ll1lllll1l1llll1Il1l1: Any) -> Any:
            l1l111111l11111lIl1l1(lll1l1l1ll1l1111Il1l1, *ll11lll111lll1llIl1l1, **ll1lllll1l1llll1Il1l1)
            with lll1111l11l1lll1Il1l1():
                lll1l1l1ll1l1111Il1l1.config['TEMPLATES_AUTO_RELOAD'] = True

        l1ll11111l111lllIl1l1.ll1llll1lll1lll1Il1l1(flask.app.Flask, '__init__', lll1ll1ll111lll1Il1l1)

    def ll111l111111l111Il1l1(ll11l11lll111l1lIl1l1) -> None:
        try:
            import waitress  # type: ignore
        except ImportError:
            return 

        l1l111111l11111lIl1l1 = waitress.serve


        def lll1ll1ll111lll1Il1l1(*ll11lll111lll1llIl1l1: Any, **ll1lllll1l1llll1Il1l1: Any) -> Any:
            with lll1111l11l1lll1Il1l1():
                llll1l11ll111l11Il1l1 = ll1lllll1l1llll1Il1l1.get('port')
                if ( not llll1l11ll111l11Il1l1):
                    llll1l11ll111l11Il1l1 = int(ll11lll111lll1llIl1l1[1])

                llll1l11ll111l11Il1l1 = int(llll1l11ll111l11Il1l1)

                ll11l11lll111l1lIl1l1.lll1llll1ll111llIl1l1 = ll11l11lll111l1lIl1l1.l1lll1lll11111llIl1l1(llll1l11ll111l11Il1l1)
                if (env.page_reload_on_start):
                    ll11l11lll111l1lIl1l1.lll1llll1ll111llIl1l1.l11l111l111llll1Il1l1(1.0)

            l1l111111l11111lIl1l1(*ll11lll111lll1llIl1l1, **ll1lllll1l1llll1Il1l1)

        l1ll11111l111lllIl1l1.ll1llll1lll1lll1Il1l1(waitress, 'serve', lll1ll1ll111lll1Il1l1)

    def lllllllll111ll11Il1l1(ll11l11lll111l1lIl1l1) -> None:
        try:
            from flask import cli
        except ImportError:
            return 

        l1llll11ll11l1l1Il1l1 = Path(cli.__file__).read_text(encoding='utf-8')
        l1llll11ll11l1l1Il1l1 = l1llll11ll11l1l1Il1l1.replace('.tb_next', '.tb_next.tb_next')

        exec(l1llll11ll11l1l1Il1l1, cli.__dict__)

    def l1l111llll1l11l1Il1l1(ll11l11lll111l1lIl1l1) -> None:
        super().l1l111llll1l11l1Il1l1()
        import flask.app

        l1l111111l11111lIl1l1 = flask.app.Flask.dispatch_request

        def lll1ll1ll111lll1Il1l1(*ll11lll111lll1llIl1l1: Any, **ll1lllll1l1llll1Il1l1: Any) -> Any:
            l1l1ll11ll1l1ll1Il1l1 = l1l111111l11111lIl1l1(*ll11lll111lll1llIl1l1, **ll1lllll1l1llll1Il1l1)

            if ( not ll11l11lll111l1lIl1l1.lll1llll1ll111llIl1l1):
                return l1l1ll11ll1l1ll1Il1l1

            if (isinstance(l1l1ll11ll1l1ll1Il1l1, str)):
                l1l1l1l11ll111llIl1l1 = ll11l11lll111l1lIl1l1.lll1llll1ll111llIl1l1.l1l11111l1l1l1llIl1l1(l1l1ll11ll1l1ll1Il1l1)
                return l1l1l1l11ll111llIl1l1
            elif ((isinstance(l1l1ll11ll1l1ll1Il1l1, flask.app.Response) and 'text/html' in l1l1ll11ll1l1ll1Il1l1.content_type)):
                l1l1ll11ll1l1ll1Il1l1.data = ll11l11lll111l1lIl1l1.lll1llll1ll111llIl1l1.l1l11111l1l1l1llIl1l1(l1l1ll11ll1l1ll1Il1l1.data.decode('utf-8')).encode('utf-8')
                return l1l1ll11ll1l1ll1Il1l1
            else:
                return l1l1ll11ll1l1ll1Il1l1

        flask.app.Flask.dispatch_request = lll1ll1ll111lll1Il1l1  # type: ignore
