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
from offik.boards.standard import About
from offik.events.manager import EventManager


class Arena(pyglet.window.Window):
    """
    Main game arena
    """

    def __init__(self):
        super().__init__(ARENA_WIDTH, ARENA_HEIGHT)
        self.set_caption(APPLICATION_TITLE)

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
        self.painters = {
            Board.LOADING: self.paint_loading,
            Board.WELCOME: self.paint_welcome,
            Board.MENU: self.menu.paint,
            Board.ABOUT: self.about.paint
        }
        self.keyrelease = {
            Board.LOADING: self.keyrelease_loading,
            Board.WELCOME: self.keyrelease_welcome,
            Board.MENU: self.menu.keyrelease,
            Board.ABOUT: self.about.keyrelease
        }
        self.mouserelease = {
            Board.MENU: self.menu.mouserelease,
            Board.ABOUT: self.about.mouserelease
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
        if symbol == pyglet.window.key.Q:
            sys.exit(1)
