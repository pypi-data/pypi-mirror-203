from flask import Flask

from . import build


def register_router(app: Flask):
    app.register_blueprint(build.nightly_blue)
