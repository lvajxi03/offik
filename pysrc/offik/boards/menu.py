#!/usr/bin/env python3

"""
Board.MENU handlers
"""

from collections import deque
from pyglet.window import key
from offik.defs import ARENA_WIDTH, ARENA_HEIGHT
from offik.ctypes import BoardState
from offik.events.menu import MenuManager
from offik.ctypes import Board
from offik.boards.standard import PlainBoard


class BoardMenu(PlainBoard):
    """
    Main menu handler class
    """
    def __init__(self, arena):
        """
        Default menu constructor
        :param arena: parent handler
        """
        super().__init__(arena)
        self.keys = ["new-game", "options", "load-game", "hiscores", "settings",
                     "help", "about", "quit"]
        self.queue = deque([6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5])
        self.pos2board = [Board.PLAYER, Board.OPTIONS, Board.LOAD, Board.HISCORES,
                          Board.SETUP, Board.HELP, Board.ABOUT, Board.QUIT]
        self.menu_manager = MenuManager(self)
        self.position = 0
        self.distance = 512
        self.state = BoardState.READY

    def key_release(self, symbol, modifiers):
        """
        Default keyrelease event handler for menu
        """
        if symbol == key.Q:
            self.arena.change_board(Board.QUIT)
        else:
            if self.state == BoardState.READY:
                if symbol == key.RIGHT:
                    self.menu_manager.start_timer_shift_right()
                elif symbol == key.LEFT:
                    self.menu_manager.start_timer_shift_left()
                elif symbol == key.ENTER:
                    board = self.pos2board[self.position]
                    self.arena.change_board(board)

    def paint(self):
        """
        Default paint method
        """
        super().paint()
        self.label_manager.draw("common", "title", self.arena.lang)

        i = 0
        for elem in self.queue:
            kev = self.keys[elem]
            self.image_manager.draw_centered(
                "menu", f"{kev}-shadow", ARENA_WIDTH / 2 - 512 - self.distance + 5 + i * 512,
                ARENA_HEIGHT / 2 - 5)
            self.image_manager.draw_centered(
                "menu", kev, ARENA_WIDTH / 2 - 512 - self.distance + i * 512,
                ARENA_HEIGHT / 2)
            i += 1
        # Focused item
        kev = self.keys[self.queue[2]]
        self.label_manager.move_to("menu", kev, ARENA_WIDTH / 2, 200)
        self.label_manager.draw("menu", kev, self.arena.lang)
        self.image_manager.draw(
            "menu", "target1-shadow", (ARENA_WIDTH-512)/2 + 5, (ARENA_HEIGHT-512)/2 - 5)
        self.image_manager.draw(
            "menu", "target1", (ARENA_WIDTH - 512) / 2, (ARENA_HEIGHT - 512) / 2)

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
