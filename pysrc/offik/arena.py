#!/usr/bin/env python3

import sys
import importlib.resources as resources
import pyglet.window
from offik.defs import APPLICATION_TITLE, ARENA_WIDTH, ARENA_HEIGHT
from offik.game import Game
from pyglet.graphics import Batch
from offik.ctypes import Board
from offik.objects.primi import create_welcome_rectangles
from offik.assets.manager import ImageManager, LabelManager
from offik.boards.menu import Menu
from offik.boards.player import Player
from offik.boards.quit import Quit
from offik.boards.standard import About, Help
from offik.events.manager import EventManager
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
        self.batch = Batch()
        assets = resources.path(__package__, "assets")
        self.rectangles = create_welcome_rectangles(30, self.batch)
        self.game = Game(self)
        self.image_manager = ImageManager(assets)
        self.label_manager = LabelManager(assets)
        self.event_manager = EventManager(self)
        self.menu = Menu(self, self.label_manager, self.image_manager)
        self.about = About(self, self.label_manager, self.image_manager)
        self.help = Help(self, self.label_manager, self.image_manager)
        self.player = Player(self, self.label_manager, self.image_manager)
        self.quit = Quit(self, self.label_manager, self.image_manager)
        self.painters = {
            Board.LOADING: self.paint_loading,
            Board.WELCOME: self.paint_welcome,
            Board.MENU: self.menu.paint,
            Board.ABOUT: self.about.paint,
            Board.HELP: self.help.paint,
            Board.PLAYER: self.player.paint,
            Board.QUIT: self.quit.paint
        }
        self.keyrelease = {
            Board.LOADING: self.keyrelease_loading,
            Board.WELCOME: self.keyrelease_welcome,
            Board.MENU: self.menu.keyrelease,
            Board.ABOUT: self.about.keyrelease,
            Board.HELP: self.help.keyrelease,
            Board.PLAYER: self.help.keyrelease,
            Board.QUIT: self.quit.keyrelease
        }
        self.mouserelease = {
            Board.MENU: self.menu.mouserelease,
            Board.ABOUT: self.about.mouserelease,
            Board.HELP: self.help.mouserelease,
            Board.PLAYER: self.player.mouserelease,
            Board.QUIT: self.quit.mouserelease
        }

    def change_lang(self, lang):
        """
        Change game language
        :param lang: new language
        """
        if lang in ["pl", "en", "ua"] and lang != self.lang:
            self.lang = lang
            # TODO: recalculate rectangles?

    def on_draw(self):
        """

        """
        try:
            painter = self.painters[self.game.board]
            painter()
        except KeyError:
            pass

    def paint_loading(self):
        """
        Painter for Board.LOADING
        """
        self.batch.draw()

    def paint_welcome(self):
        """
        Painter for Board.WELCOME
        """
        self.image_manager.draw("common", "background", 0, 0, 0)
        self.label_manager.draw("common", "title", self.lang)

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Handle mouse-release event
        """
        try:
            handler = self.mouserelease[self.game.board]
            handler(x, y, button, modifiers)
        except KeyError:
            pass

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            return True

    def on_key_release(self, symbol, modifiers):
        try:
            handler = self.keyrelease[self.game.board]
            return handler(symbol, modifiers)
        except KeyError:
            return True

    def keyrelease_loading(self, symbol, modifiers):
        """
        Handle key-release event in loading board
        """
        self.game.change_board(Board.WELCOME)

    def keyrelease_welcome(self, symbol, modifiers):
        """

        """
        self.event_manager.stop_timer_welcome()
        if symbol == pyglet.window.key.Q:
            self.game.change_board(Board.QUIT)
        else:
            self.game.change_board(Board.MENU)

    def quit_application(self):
        self.appconfig.save_default()
        self.close()
