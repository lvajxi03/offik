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
from offik.events.manager import EventManager


class Arena(pyglet.window.Window):
    """
    Main game arena
    """

    def __init__(self):
        super().__init__(ARENA_WIDTH, ARENA_HEIGHT)
        self.set_caption(APPLICATION_TITLE)
        self.batch = Batch()
        assets = resources.path(__package__, "assets")
        self.rectangles = create_welcome_rectangles(30, self.batch)
        self.game = Game(self)
        self.image_manager = ImageManager(assets)
        self.label_manager = LabelManager(assets)
        self.event_manager = EventManager(self)
        self.menu = Menu(self, self.label_manager, self.image_manager)
        self.painters = {
            Board.LOADING: self.paint_loading,
            Board.WELCOME: self.paint_welcome,
            Board.MENU: self.menu.paint
        }
        self.keyrelease = {
            Board.LOADING: self.keyrelease_loading,
            Board.WELCOME: self.keyrelease_welcome,
            Board.MENU: self.menu.keyrelease
        }
        

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
        self.label_manager.draw("common", "title", "pl")

    def paint_menu(self):
        """

        """
        self.image_manager.draw("common", "background", 0, 0, 0)
        self.label_manager.draw("common", "title", "pl")
        self.image_manager.draw("common", "flag-pl", ARENA_WIDTH - 240, 5, 0)
        self.image_manager.draw("common", "flag-en", ARENA_WIDTH - 160, 5, 0)
        self.image_manager.draw("common", "flag-ua", ARENA_WIDTH - 80, 5, 0)
        self.image_manager.draw_centered("menu", "exit-shadow", ARENA_WIDTH / 2 - 507, ARENA_HEIGHT / 2 - 5, 0)
        self.image_manager.draw_centered("menu", "exit", ARENA_WIDTH / 2 - 512, ARENA_HEIGHT / 2, 0)
        self.image_manager.draw_centered("menu", "running-shadow", ARENA_WIDTH/2 + 5, ARENA_HEIGHT/2 - 5, 0)
        self.image_manager.draw_centered("menu", "running", ARENA_WIDTH / 2, ARENA_HEIGHT / 2, 0)
        self.image_manager.draw_centered("menu", "gear-shadow", ARENA_WIDTH / 2 + 517, ARENA_HEIGHT / 2 - 5, 0)
        self.image_manager.draw_centered("menu", "gear", ARENA_WIDTH / 2 + 512, ARENA_HEIGHT / 2, 0)
        self.image_manager.draw("menu", "target1-shadow", (ARENA_WIDTH-512)/2 + 5, (ARENA_HEIGHT-512)/2 - 5, 0)
        self.image_manager.draw("menu", "target1", (ARENA_WIDTH - 512) / 2, (ARENA_HEIGHT - 512) / 2, 0)

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
        print(symbol, modifiers)
        if symbol == pyglet.window.key.Q:
            sys.exit(1)
