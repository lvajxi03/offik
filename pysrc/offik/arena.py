#!/usr/bin/env python3

"""
Main arena module
"""

from importlib import resources
import pyglet.window
from offik.defs import APPLICATION_TITLE, ARENA_WIDTH, ARENA_HEIGHT
from offik.game import Game
from offik.ctypes import Board
from offik.assets.manager import ImageManager, LabelManager
from offik.boards.menu import BoardMenu
from offik.boards.player import BoardPlayer
from offik.boards.quit import BoardQuit
from offik.boards.standard import BoardAbout, BoardHelp, BoardHiscores
from offik.boards.loading import BoardLoading
from offik.boards.welcome import BoardWelcome
from offik.core.config import Config


class Arena(pyglet.window.Window):
    """
    Main game arena
    """

    def __init__(self, mode):
        """
        Arena initialization
        :param mode: current screen mode
        """
        super().__init__(ARENA_WIDTH, ARENA_HEIGHT, style='borderless', )
        self.set_caption(APPLICATION_TITLE)
        x = int((mode.width - ARENA_WIDTH) / 2)
        y = int((mode.height - ARENA_HEIGHT) / 2)
        self.set_location(int(x), int(y))
        self.set_visible(True)
        self.appconfig = Config()
        self.lang = "en"
        assets = resources.path(__package__, "assets")
        self.game = Game()
        self.image_manager = ImageManager(assets)
        self.label_manager = LabelManager(assets)
        self.boards = {
            Board.LOADING: BoardLoading(self),
            Board.WELCOME: BoardWelcome(self),
            Board.MENU: BoardMenu(self),
            Board.ABOUT: BoardAbout(self),
            Board.HELP: BoardHelp(self),
            Board.PLAYER: BoardPlayer(self),
            Board.QUIT: BoardQuit(self),
            Board.HISCORES: BoardHiscores(self)
        }
        self.board = None

    def change_board(self, new_board):
        """
        Change board to a new one
        :param new_board: board to change to
        """
        nbo = self.boards[new_board]
        if nbo != self.board:
            if self.board:
                self.board.stop()
            self.board = nbo
            self.board.start()

    def change_lang(self, lang):
        """
        Change game language
        :param lang: new language
        """
        if lang in ["pl", "en", "ua"] and lang != self.lang:
            self.lang = lang

    def on_draw(self):
        """
        General painter dispatcher
        """
        self.board.paint()

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Handle mouse-release event
        """
        self.board.mouse_release(x, y, button, modifiers)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            return True
        return False

    def on_key_release(self, symbol, modifiers):
        self.board.key_release(symbol, modifiers)

    def quit_application(self):
        """
        Save config, exit Em^H^Happlication
        """
        self.appconfig.save_default()
        self.close()
