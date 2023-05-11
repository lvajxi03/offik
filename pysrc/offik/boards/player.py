#!/usr/bin/env python3

"""
Board.PLAYER module
"""

from pyglet.window import key
from pyglet.shapes import Rectangle
from offik.defs import ARENA_WIDTH, ARENA_HEIGHT
from offik.core.primi import Rect
from offik.ctypes import Board, BoardState


class Player:
    """
    Board.PLAYER main supporting class
    """
    def __init__(self, arena, label_manager, image_manager):
        """
        Construct an instance of Player class
        :param arena: arena handler
        :param image_manager: image manager handler
        :param label_manager: label manager handler
        """
        self.arena = arena
        self.image_manager = image_manager
        self.label_manager = label_manager
        self.lang_rects = {
            "pl": Rect(ARENA_WIDTH - 240, 0, 80, 60),
            "en": Rect(ARENA_WIDTH - 160, 0, 80, 60),
            "ua": Rect(ARENA_WIDTH - 80, 0, 80, 60)}
        self.status_bar = Rectangle(0, 0, ARENA_WIDTH, 66, color=(0, 0, 0, 127))
        self.state = BoardState.SHIFT

    def paint(self):
        """
        Default paint handler for Board.PLAYER
        """
        self.image_manager.draw("common", "background", 0, 0, 0)
        self.status_bar.draw()
        self.image_manager.draw("common", "flag-pl", ARENA_WIDTH - 240, 5, 0)
        self.image_manager.draw("common", "flag-en", ARENA_WIDTH - 160, 5, 0)
        self.image_manager.draw("common", "flag-ua", ARENA_WIDTH - 80, 5, 0)
        self.label_manager.draw("board-titles", "select-player", self.arena.lang)

    def keyrelease(self, symbol, modifiers):
        """
        Default keyrelease handler for Board.PLAYER
        """
        self.arena.game.change_board(Board.MENU)

    def mouserelease(self, x, y, button, modifiers):
        """
        Default mouse release method
        :param x: x coordinate of mouse pointer
        :param y: y coordinate of mouse pointer
        :param button: button pressed
        :param modifiers: all modifiers used
        """
        for lang in self.lang_rects:
            rect = self.lang_rects[lang]
            if rect.contains(x, y):
                self.arena.change_lang(lang)
