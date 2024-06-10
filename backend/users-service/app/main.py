from litestar import Litestar

from app.server.__factory__ import configure_app


def create_app() -> Litestar:
    return configure_app()
