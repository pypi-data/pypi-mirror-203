from __future__ import annotations

from pathlib import Path

import pyqtgraph as pg
import qtextras as qte
from qdarktheme import load_stylesheet
from qtpy import QtCore, QtGui, QtWidgets

from snaik.game import Game
from snaik.utils import LogMode

bind = qte.bindInteractorOptions


class Grid(QtWidgets.QGraphicsItem):
    def __init__(self, n_x_cells: int, n_y_cells: int):
        super().__init__()
        self.n_x_cells, self.n_y_cells = n_x_cells, n_y_cells
        self.pen = pg.mkPen("#eee", width=3)
        # Slightly offset so points appear centered
        self.setPos(-0.5, -0.5)

    def paint(self, painter, option, widget=None):
        painter.setPen(self.pen)
        rect = self.boundingRect()
        cell_width = rect.width() / self.n_x_cells
        cell_height = rect.height() / self.n_y_cells
        for ii in range(self.n_x_cells):
            for jj in range(self.n_y_cells):
                to_draw = QtCore.QRectF(
                    ii * cell_width, jj * cell_height, cell_width, cell_height
                )
                painter.drawRect(to_draw)

    def boundingRect(self):
        return QtCore.QRectF(0, 0, self.n_x_cells, self.n_y_cells)


class BoardWidget(pg.GraphicsView):
    def __init__(self, parent=None, *, grid_size: tuple[int, int] = (12, 12), **kwargs):
        super().__init__(parent)
        # Clean up unparented top window that spawns in super class
        self.viewbox = pg.ViewBox(
            defaultPadding=0.0125,
            enableMenu=False,
            lockAspect=True,
            enableMouse=False,
        )
        self.grid = Grid(*grid_size)
        path_kwargs = dict(
            json_path=kwargs.pop("json_path", ""),
            frames_path=kwargs.pop("frames_path", ""),
            gif_path=kwargs.pop("gif_path", ""),
        )
        self.game = game = Game(**kwargs, grid_size=grid_size)

        self.tools_editor = qte.ParameterEditor(name="Tools")
        interactive = self.tools_editor.registerFunction(
            game.recorder.update_properties,
            runOptions=qte.RunOptions.ON_CHANGED,
            **path_kwargs,
        )
        # Make sure parameters update when the function is called
        setattr(game.recorder, "update_properties", interactive)
        interactive()
        if game.recorder.json_states:
            game.set_board_state(game.recorder.json_states[-1])

        self.tools_editor.registerFunction(self.set_brains_gui, name="Update Brains...")

        for func in (game.run, game.pause, game.restart, game.tick):
            self.tools_editor.registerFunction(func)
        self.tools_editor.registerFunction(
            game.playback_history_gui, name="Playback History..."
        )

        self.setup_gui()
        self.setMinimumSize(500, 500)
        self.tools_editor.setMinimumWidth(300)

    def set_brains_gui(self):
        parameter = qte.ParameterEditor.defaultInteractor(self.game.set_snake_brains)
        qte.parameterDialog(parameter)

    def setup_gui(self):
        self.setCentralItem(self.viewbox)

        self.viewbox.addItem(self.grid)
        self.viewbox.addItem(self.game)


class SnaikWindow(QtWidgets.QMainWindow):
    def __init__(self, log_mode: LogMode | list[LogMode] = LogMode.GUI, **kwargs):
        super().__init__()
        resources_dir = Path(__file__).resolve().parent / "resources"
        self.setWindowIcon(QtGui.QIcon(str(resources_dir / "logo.svg")))
        self.setWindowTitle("snAIk")
        board = self.board = BoardWidget(parent=self, **kwargs)
        qte.EasyWidget.buildMainWindow(
            [
                board,
                [board.game.leaderboard, board.tools_editor],
            ],
            window=self,
            layout="H",
            useSplitter=True,
        )
        board.tools_editor.createActionsFromFunctions(menu=self.menuBar())
        self.game = board.game
        splitter: QtWidgets.QSplitter = self.easyChild.widget_  # noqa
        for ii in range(2):
            splitter.setCollapsible(ii, False)

        self.board.tools_editor.registerFunction(self.dev_console)
        with qte.makeDummySignal(self.board.tools_editor, "sigFunctionRegistered"):
            self.board.tools_editor.registerFunction(
                self.set_theme, runOptions=qte.RunOptions.ON_CHANGED, nest=False
            )
        self.set_theme()

        self.logger = qte.AppLogger.getAppLogger(__name__)
        if log_mode == LogMode.GUI or LogMode.GUI in log_mode:
            self.logger.registerExceptions(self)

    @bind(theme=dict(type="list", limits=["dark", "light"]))
    def set_theme(self, theme="dark"):
        if theme in ["dark", "light"]:
            self.setStyleSheet(load_stylesheet(theme))
        else:
            raise ValueError(f"Invalid theme: {theme}")

        background_map = dict(dark="k", light="w")
        background = background_map.pop(theme)
        other = pg.mkColor(background_map.popitem()[1])
        color = pg.mkColor(background)
        brush = pg.mkBrush(background)

        self.board.grid.pen.setColor(other)
        self.board.grid.update()
        self.game.leaderboard.leaderboard_item.setBrush(brush)
        self.game.leaderboard.setBackgroundBrush(brush)
        self.board.viewbox.setBackgroundColor(color)

    def dev_console(self):
        qte.safeSpawnDevConsole(self, game=self.game, board=self.board)
