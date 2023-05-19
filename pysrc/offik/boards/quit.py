#!/usr/bin/env python3

"""
Board.QUIT handler
"""

from pyglet.window import key
from offik.defs import ARENA_WIDTH, ARENA_HEIGHT
from offik.ctypes import Board, BoardState
from offik.boards.standard import PlainBoard
from offik.events.quit import QuitManager


class BoardQuit(PlainBoard):
    """
    Board.QUIT main class
    """
    def __init__(self, arena):
        """
        Object constructor
        :param arena: arena handle
        """
        super().__init__(arena)
        self.exit = False
        self.state = BoardState.READY
        self.distance = 0
        self.quit_manager = QuitManager(self)

    def paint(self):
        """
        Default paint handler for Board.QUIT
        """
        super().paint()
        self.label_manager.draw("board-titles", "quit", self.arena.lang)
        self.image_manager.draw(
            "common", "yes-shadow", ARENA_WIDTH/2 - 507, ARENA_HEIGHT/2 - 133)
        self.image_manager.draw(
            "common", "yes", ARENA_WIDTH / 2 - 512, ARENA_HEIGHT / 2 - 128)
        self.image_manager.draw(
            "common", "no-shadow", ARENA_WIDTH/2 + 133, ARENA_HEIGHT/2 - 133)
        self.image_manager.draw(
            "common", "no", ARENA_WIDTH / 2 + 128, ARENA_HEIGHT / 2 - 128)
        self.image_manager.draw(
            "menu", "target1-shadow", ARENA_WIDTH/2 + self.distance + 5,
            (ARENA_HEIGHT - 512) / 2 - 5)
        self.image_manager.draw(
            "menu", "target1", ARENA_WIDTH/2 + self.distance,
            (ARENA_HEIGHT - 512) / 2)

    def key_release(self, symbol, modifiers):
        """
        Default keyrelease handler for Board.QUIT
        """
        if self.state == BoardState.READY:
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
                    self.arena.change_board(Board.MENU)
