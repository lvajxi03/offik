#!/usr/bin/env python

"""
Standard board managers
"""

from pyglet.shapes import Rectangle
from offik.ctypes import Board
from offik.defs import ARENA_WIDTH
from offik.core.primi import Rect


class PlainBoard:
    """
    Plain board class stub
    """
    def __init__(self, arena):
        self.arena = arena
        self.label_manager = self.arena.label_manager
        self.image_manager = self.arena.image_manager
        self.lang_rects = {
            "pl": Rect(ARENA_WIDTH - 240, 0, 80, 60),
            "en": Rect(ARENA_WIDTH - 160, 0, 80, 60),
            "ua": Rect(ARENA_WIDTH - 80, 0, 80, 60)}
        self.status_bar = Rectangle(0, 0, ARENA_WIDTH, 66, color=(0, 0, 0, 127))

    def start(self):
        """
        Generic start method.
        Triggered when changing to/entering this board
        """

    def stop(self):
        """
        Generic stop method.
        Triggered when leaving this board
        """

    def paint(self):
        """
        Paint method stub
        """
        self.image_manager.draw("common", "background", 0, 0)
        self.status_bar.draw()
        self.image_manager.draw("common", "flag-pl", ARENA_WIDTH - 240, 5)
        self.image_manager.draw("common", "flag-en", ARENA_WIDTH - 160, 5)
        self.image_manager.draw("common", "flag-ua", ARENA_WIDTH - 80, 5)

    def key_release(self, symbol, modifiers):
        """
        Key release method stub
        """
        self.arena.change_board(Board.MENU)

    def mouse_release(self, x, y, button, modifiers):
        """
        Default mouse release handler for plain boards
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
            self.arena.change_board(Board.MENU)


class BoardAbout(PlainBoard):
    """
    Board.ABOUT handler class
    """
    def paint(self):
        """
        Default paint handler for Board.ABOUT
        """
        super().paint()
        self.label_manager.draw("board-titles", "about", self.arena.lang)


class BoardHelp(PlainBoard):
    """
    Board.HELP manager
    """
    def paint(self):
        """
        Default paint handler for Board.ABOUT
        """
        super().paint()
        self.label_manager.draw("board-titles", "help", self.arena.lang)


class BoardHiscores(PlainBoard):
    """
    Board.HISCORES handler class
    """
    def paint(self):
        """
        Default paint handler for Board.HISCORES
        """
        super().paint()
        self.label_manager.draw("board-titles", "hiscores", self.arena.lang)
