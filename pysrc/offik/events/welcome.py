#!/usr/bin/env python3

"""
Board.WELCOME event manager
"""

import pyglet.clock
from offik.ctypes import Board
from offik.defs import ARENA_WIDTH


class WelcomeEventManager:
    """
    Board.WELCOME event manager
    """
    def __init__(self, board):
        self.board = board

    def start_timer_welcome(self):
        """
        Start default timer for Board.WELCOME
        """
        w, h = self.board.arena.label_manager.get_size("common", "title", self.board.arena.lang)
        self.board.arena.label_manager.move_to("common", "title", ARENA_WIDTH + w/2, h/2 + 15)
        pyglet.clock.schedule_interval(self.timer_welcome, 1.0/60)

    def stop_timer_welcome(self):
        """
        Stop default timer for Board.WELCOME
        """
        pyglet.clock.unschedule(self.timer_welcome)
        self.board.arena.label_manager.set_font_size("common", "title", 96)
        self.board.arena.label_manager.move_to("common", "title", ARENA_WIDTH/2, 1000)

    def timer_welcome(self, dt):
        """
        Default timer handler for Board.WELCOME
        """
        x, y = self.board.arena.label_manager.get_pos("common", "title", self.board.arena.lang)
        w, h = self.board.arena.label_manager.get_size("common", "title", self.board.arena.lang)
        if y < 1000:
            if x <= ARENA_WIDTH/2:
                self.board.arena.label_manager.move_by("common", "title", 0, 10)
            else:
                self.board.arena.label_manager.move_by("common", "title", -10, 0)
        else:
            size = self.board.arena.label_manager.get_font_size("common", "title")
            if size > 96:
                self.board.arena.label_manager.set_font_size("common", "title", size-4)
            else:
                # Stop timer, change to Board.MENU
                self.stop_timer_welcome()
                self.board.arena.change_board(Board.MENU)
