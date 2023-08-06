import flask
import zrlog

import clusterman.main.orm as orm
import zirconium as zr
from autoinject import injector
import pathlib
import os


ROOT_DIR = pathlib.Path(__file__).absolute().parent.parent


def create_app():
    @zr.configure
    def add_config_files(config: zr.ApplicationConfig):
        config_paths = [
            ROOT_DIR,
            pathlib.Path("~").expanduser().absolute(),
            pathlib.Path(".").absolute()
        ]
        config_paths.extend(os.environ.get("CLUSTERMAN_CONFIG_PATHS", default="").split(";"))
        config.register_files(config_paths,
                              [".clusterman.toml"],
                              [".clusterman.defaults.toml"])
    zrlog.init_logging()
    app = flask.Flask(__name__)
    init_app(app)
    return app


@injector.inject
def init_app(app, config: zr.ApplicationConfig = None):
    sd = config.as_path(("clusterman", "storage_dir"))
    if not sd:
        raise ValueError("Storage directory is required")
    if not sd.exists():
        raise ValueError("Storage directory must exist")
    if "flask" in config:
        app.config.update(config["flask"])
    if "SQLALCHEMY_BINDS" not in app.config:
        app.config["SQLALCHEMY_BINDS"] = {}
    if "local_map_db" not in app.config["SQLALCHEMY_BINDS"]:
        app.config["SQLALCHEMY_BINDS"]["local_map_db"] = f"sqlite:///{(sd / 'maps.db').absolute()}"
    if "local_lock_db" not in app.config["SQLALCHEMY_BINDS"]:
        app.config["SQLALCHEMY_BINDS"]["local_lock_db"] = f"sqlite:///{(sd / 'locks.db').absolute()}"

    orm.db.init_app(app)

    from .cli import clusterman
    app.cli.commands.update(clusterman.commands)
