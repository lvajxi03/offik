#!/usr/bin/env python3

"""
Board.QUIT handler
"""

from pyglet.window import key
from pyglet.shapes import Rectangle
from collections import deque
from offik.defs import ARENA_WIDTH, ARENA_HEIGHT
from offik.ctypes import QuitState
from offik.core.primi import Rect
from offik.ctypes import Board
from offik.events.quit import QuitManager

class Quit:
    """
    Board.QUIT main class
    """
    def __init__(self, arena, label_manager, image_manager):
        """
        Object constructor
        :param arena: arena handle
        :param label_manager: label manager handler
        :param image_manager: image manager handler
        """
        self.arena = arena
        self.exit = False
        self.state = QuitState.READY
        self.distance = 0
        self.image_manager = image_manager
        self.label_manager = label_manager
        self.lang_rects = {
            "pl": Rect(ARENA_WIDTH - 240, 0, 80, 60),
            "en": Rect(ARENA_WIDTH - 160, 0, 80, 60),
            "ua": Rect(ARENA_WIDTH - 80, 0, 80, 60)}
        self.status_bar = Rectangle(0, 0, ARENA_WIDTH, 66, color=(0, 0, 0, 127))
        self.quit_manager = QuitManager(self)

    def paint(self):
        """
        Default paint handler for Board.QUIT
        """
        self.image_manager.draw("common", "background", 0, 0, 0)
        self.status_bar.draw()
        self.image_manager.draw("common", "flag-pl", ARENA_WIDTH - 240, 5, 0)
        self.image_manager.draw("common", "flag-en", ARENA_WIDTH - 160, 5, 0)
        self.image_manager.draw("common", "flag-ua", ARENA_WIDTH - 80, 5, 0)
        self.label_manager.draw("board-titles", "quit", self.arena.lang)
        self.image_manager.draw("common", "yes-shadow", ARENA_WIDTH/2 - 507, ARENA_HEIGHT/2 - 133, 0)
        self.image_manager.draw("common", "yes", ARENA_WIDTH / 2 - 512, ARENA_HEIGHT / 2 - 128, 0)
        self.image_manager.draw("common", "no-shadow", ARENA_WIDTH/2 + 133, ARENA_HEIGHT/2 - 133, 0)
        self.image_manager.draw("common", "no", ARENA_WIDTH / 2 + 128, ARENA_HEIGHT / 2 - 128, 0)
        self.image_manager.draw("menu", "target1-shadow", ARENA_WIDTH/2 + self.distance + 5, (ARENA_HEIGHT - 512) / 2 - 5,
                                    0)
        self.image_manager.draw("menu", "target1", ARENA_WIDTH/2 + self.distance, (ARENA_HEIGHT - 512) / 2, 0)


    def keyrelease(self, symbol, modifiers):
        """
        Default keyrelease handler for Board.QUIT
        """
        if self.state == QuitState.READY:
            if symbol == key.RIGHT:
                if self.exit:
                    self.quit_manager.start_timer_shift_right()
            elif symbol == key.LEFT:
                if not self.exit:
                    self.quit_manager.start_timer_shift_left()
            elif symbol == key.ENTER:
                if self.exit:
                    self.arena.quit_application()
                else:
                    self.arena.game.change_board(Board.MENU)

    def mouserelease(self, x, y, button, modifiers):
        """
        Default mouse release method
        :param x: x coordinate of mouse pointer
        :param y: y coordinate of mouse pointer
        :param button: button pressed
        :param modifiers: all modifiers used
        """
        for key in self.lang_rects:
            rect = self.lang_rects[key]
            if rect.contains(x, y):
                self.arena.change_lang(key)
