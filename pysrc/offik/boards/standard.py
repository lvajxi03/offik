#!/usr/bin/env python

"""
Standard board managers
"""

from pyglet.shapes import Rectangle
from offik.ctypes import Board
from offik.defs import ARENA_WIDTH, ARENA_HEIGHT
from offik.core.primi import Rect


class About:
    """
    Board.ABOUT handler class
    """

    def __init__(self, arena, labelmanager, imagemanager):
        """
        Instance constructor
        """
        self.arena = arena
        self.label_manager = labelmanager
        self.image_manager = imagemanager
        self.lang_rects = {
            "pl": Rect(ARENA_WIDTH - 240, 0, 80, 60),
            "en": Rect(ARENA_WIDTH - 160, 0, 80, 60),
            "ua": Rect(ARENA_WIDTH - 80, 0, 80, 60)}
        self.status_bar = Rectangle(0, 0, ARENA_WIDTH, 66, color=(0, 0, 0, 127))

    def keyrelease(self, symbol, modifiers):
        """
        Default keyrelease handler for Board.ABOUT
        """
        self.arena.game.change_board(Board.MENU)

    def paint(self):
        """
        Default paint handler for Board.ABOUT
        """
        self.image_manager.draw("common", "background", 0, 0, 0)
        self.status_bar.draw()
        self.image_manager.draw("common", "flag-pl", ARENA_WIDTH - 240, 5, 0)
        self.image_manager.draw("common", "flag-en", ARENA_WIDTH - 160, 5, 0)
        self.image_manager.draw("common", "flag-ua", ARENA_WIDTH - 80, 5, 0)
        self.label_manager.draw("board-titles", "about", self.arena.lang)

    def mouserelease(self, x, y, button, modifiers):
        """
        Default mouse release handler for Board.ABOUT
        :param x: x coordinate of mouse pointer
        :param y: y coordinate of mouse pointer
        :param button: button pressed
        :param modifiers: all modifiers used
        """
        found = False
        for key in self.lang_rects:
            rect = self.lang_rects[key]
            if rect.contains(x, y):
                self.arena.change_lang(key)
                found = True
        if not found:
            self.arena.game.change_board(Board.MENU)


class Help:
    """
    Board.HELP manager
    """
    def __init__(self, arena, labelmgr, imagemgr):
        """
        Instance constructor
        """
        self.arena = arena
        self.label_manager = labelmgr
        self.image_manager = imagemgr
        self.lang_rects = {
            "pl": Rect(ARENA_WIDTH - 240, 0, 80, 60),
            "en": Rect(ARENA_WIDTH - 160, 0, 80, 60),
            "ua": Rect(ARENA_WIDTH - 80, 0, 80, 60)}
        self.status_bar = Rectangle(0, 0, ARENA_WIDTH, 66, color=(0, 0, 0, 127))

    def keyrelease(self, symbol, modifiers):
        """
        Default keyrelease handler for Board.ABOUT
        """
        self.arena.game.change_board(Board.MENU)

    def paint(self):
        """
        Default paint handler for Board.ABOUT
        """
        self.image_manager.draw("common", "background", 0, 0, 0)
        self.status_bar.draw()
        self.image_manager.draw("common", "flag-pl", ARENA_WIDTH - 240, 5, 0)
        self.image_manager.draw("common", "flag-en", ARENA_WIDTH - 160, 5, 0)
        self.image_manager.draw("common", "flag-ua", ARENA_WIDTH - 80, 5, 0)
        self.label_manager.draw("board-titles", "help", self.arena.lang)

    def mouserelease(self, x, y, button, modifiers):
        """
        Default mouse release handler for Board.ABOUT
        :param x: x coordinate of mouse pointer
        :param y: y coordinate of mouse pointer
        :param button: button pressed
        :param modifiers: all modifiers used
        """
        found = False
        for key in self.lang_rects:
            rect = self.lang_rects[key]
            if rect.contains(x, y):
                self.arena.change_lang(key)
                found = True
        if not found:
            self.arena.game.change_board(Board.MENU)
