#!/usr/bin/env python3

"""
Board.LOADING class
"""

import random
from pyglet.shapes import Rectangle
from pyglet.graphics import Batch
from offik.ctypes import Board
from offik.defs import ARENA_WIDTH, ARENA_HEIGHT
from offik.boards.standard import PlainBoard
from offik.events.loading import LoadingEventManager


class BoardLoading(PlainBoard):
    """
    Board.LOADING main class
    """
    def __init__(self, arena):
        super().__init__(arena)
        self.batch = Batch()
        self.event_manager = LoadingEventManager(self)
        self.rectangles = self.create_welcome_rectangles(30)

    def paint(self):
        self.batch.draw()

    def key_release(self, symbol, modifiers):
        """
        Overriden key release event handler
        """
        self.arena.change_board(Board.WELCOME)

    def create_welcome_rectangles(self, num):
        """
        Create random rectangles, used by Board.LOADING
        :param num: how many rectangles
        """
        height = ARENA_HEIGHT // num
        rectangles = []
        for i in range(num):
            rec = Rectangle(
                    0,
                    i * height,
                    ARENA_WIDTH,
                    height,
                    color=(
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255),
                        255
                        ),
                    batch=self.batch)
            rectangles.append(rec)
        return rectangles

    def start(self):
        self.event_manager.start_timer_loading()
        self.event_manager.start_timer_loading_end()

    def stop(self):
        self.event_manager.stop_timer_loading()
        self.event_manager.stop_timer_loading_end()
