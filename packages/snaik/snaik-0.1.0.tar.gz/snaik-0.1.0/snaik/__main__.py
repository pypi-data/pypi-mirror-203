import logging
import os
from pathlib import Path

import click
import pyqtgraph as pg
from qtpy import QtCore

from snaik import __version__
from snaik.window import SnaikWindow


def main(**kwargs):
    logging.basicConfig(level=logging.INFO)

    pg.mkQApp()
    win = SnaikWindow(**kwargs)
    win.show()

    # safeSpawnDevConsole(window=win, **locals())
    pg.exec()


def main_headless(**kwargs):
    logging.basicConfig(level=logging.INFO)
    os.environ["QT_QPA_PLATFORM"] = "offscreen"
    font_path = Path(__file__).resolve().parent / "resources"
    os.environ.setdefault("QT_QPA_FONTDIR", font_path.as_posix())

    app = pg.mkQApp()

    win = SnaikWindow(**kwargs)
    win.show()
    single_shot = QtCore.QTimer(win)
    single_shot.setSingleShot(True)

    def run():
        win.game.run_full_game(abort_on_error=True, **kwargs)
        app.exit(0)

    single_shot.timeout.connect(run)
    single_shot.start(0)
    pg.exec()


@click.command()
@click.version_option(__version__, message="%(version)s")
@click.option("--grid-size", type=(int, int), default=(12, 12))
@click.option("--brain", "-b", "snake_brains", multiple=True, default=["keyboard"])
@click.option("--n-food-points", type=int, default=None)
@click.option("--json-path", type=str, default="")
@click.option("--frames-path", type=str, default="")
@click.option("--gif-path", type=str, default="")
@click.option("--headless", default=False, is_flag=True)
def main_cli(**kwargs):
    if kwargs.pop("headless", False):
        main_headless(**kwargs)
    else:
        main(**kwargs)


if __name__ == "__main__":
    main_cli()
