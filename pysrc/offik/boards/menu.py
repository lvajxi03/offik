#!/usr/bin/env python3

"""
Board.MENU handlers
"""

from pyglet.window import key
from pyglet.shapes import Rectangle
from collections import deque
from offik.defs import ARENA_WIDTH, ARENA_HEIGHT
from offik.ctypes import MenuState
from offik.events.menu import MenuManager
from offik.core.primi import Rect
from offik.ctypes import Board


class Menu:
    """
    Main menu handler class
    """
    def __init__(self, arena, labelmanager, imagemanager):
        """
        Default menu constructor
        :param arena: parent handler
        :param labelmanager: label management
        :param imagemanager: image management
        """
        self.arena = arena
        self.lang_rects = {
            "pl": Rect(ARENA_WIDTH - 240, 0, 80, 60),
            "en": Rect(ARENA_WIDTH - 160, 0, 80, 60),
            "ua": Rect(ARENA_WIDTH - 80, 0, 80, 60)}
        self.keys = ["new-game", "options", "load-game", "hiscores", "settings", "help", "about", "quit"]
        self.queue = deque([6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5])
        self.pos2board = [Board.PLAYER, Board.OPTIONS, Board.LOAD, Board.HISCORES, Board.SETUP, Board.HELP, Board.ABOUT, Board.QUIT]
        self.label_manager = labelmanager
        self.image_manager = imagemanager
        self.menu_manager = MenuManager(self)
        self.position = 0
        self.distance = 512
        self.state = MenuState.READY
        self.status_bar = Rectangle(0, 0, ARENA_WIDTH, 66, color=(0, 0, 0, 127))

    def keyrelease(self, symbol, modifiers):
        """
        Default keyrelease event handler for menu
        """
        if symbol == key.Q:
            self.arena.game.change_board(Board.QUIT)
        else:
            if self.state == MenuState.READY:
                if symbol == key.RIGHT:
                    self.menu_manager.start_timer_shift_right()
                elif symbol == key.LEFT:
                    self.menu_manager.start_timer_shift_left()
                elif symbol == key.ENTER:
                    board = self.pos2board[self.position]
                    self.arena.game.change_board(board)

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

    def paint(self):
        """
        Default paint method
        """
        self.image_manager.draw("common", "background", 0, 0, 0)
        self.status_bar.draw()
        self.image_manager.draw("common", "flag-pl", ARENA_WIDTH - 240, 5, 0)
        self.image_manager.draw("common", "flag-en", ARENA_WIDTH - 160, 5, 0)
        self.image_manager.draw("common", "flag-ua", ARENA_WIDTH - 80, 5, 0)
        self.label_manager.draw("common", "title", self.arena.lang)

        i = 0
        for elem in self.queue:
            key = self.keys[elem]
            self.image_manager.draw_centered("menu", f"{key}-shadow", ARENA_WIDTH / 2 - 512 - self.distance + 5 + i * 512, ARENA_HEIGHT / 2 - 5, 0)
            self.image_manager.draw_centered("menu", key, ARENA_WIDTH / 2 - 512 - self.distance + i * 512, ARENA_HEIGHT / 2, 0)
            i += 1
        # Focused item
        key = self.keys[self.queue[2]]
        self.label_manager.move_to("menu", key, ARENA_WIDTH / 2, 200)
        self.label_manager.draw("menu", key, self.arena.lang)
        self.image_manager.draw("menu", "target1-shadow", (ARENA_WIDTH-512)/2 + 5, (ARENA_HEIGHT-512)/2 - 5, 0)
        self.image_manager.draw("menu", "target1", (ARENA_WIDTH - 512) / 2, (ARENA_HEIGHT - 512) / 2, 0)        

    def shift_left(self):
        """
        Shift left is when you press RIGHT arrow
        """
        self.queue.rotate(1)
        self.distance = 512
        self.position = self.queue[2]

    def shift_right(self):
        """
        Shift right is when you press LEFT arrow
        """
        self.queue.rotate(-1)
        self.distance = 512
        self.position = self.queue[2]
