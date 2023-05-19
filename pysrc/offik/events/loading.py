#!/usr/bin/env python3

"""
Board.LOADING event manager
"""

import random
import pyglet.clock
from offik.ctypes import Board


class LoadingEventManager:
    """
    Loading Event Manager
    """
    def __init__(self, board):
        """
        LoadingEventManager constructor
        :param board:
        """
        self.board = board

    def start_timer_loading(self):
        """
        Start default timer for Board.LOADING
        """
        pyglet.clock.schedule_interval(self.timer_loading, 1.0/20)

    def start_timer_loading_end(self):
        """
        Schedule few seconds Board.LOADING termination
        """
        pyglet.clock.schedule_interval(self.timer_loading_end, 5)

    def stop_timer_loading(self):
        """
        Stop default timer for Board.LOADING
        """
        pyglet.clock.unschedule(self.timer_loading)

    def stop_timer_loading_end(self):
        """
        Stop ending timer for Board.LOADING
        """
        pyglet.clock.unschedule(self.timer_loading_end)

    def timer_loading(self, dt):
        """
        Default timer handler for Board.LOADING
        """
        for rect in self.board.rectangles:
            rect.color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
                255)

    def timer_loading_end(self, dt):
        """
        Timer to change Board.LOADING to Board.WELCOME
        """
        self.stop_timer_loading()
        self.stop_timer_loading_end()
        self.board.arena.change_board(Board.WELCOME)
