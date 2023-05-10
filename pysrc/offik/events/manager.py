#!/usr/bin/env python3

"""
Various events managers
"""

import random
import pyglet.clock
from offik.ctypes import Board
from offik.defs import ARENA_WIDTH, ARENA_HEIGHT


class EventManager:
    """
    Default event manager
    """
    def __init__(self, dispatcher):
        """
        Create event manager object
        :param dispatcher: default dispatcher (action receiver)
        """
        self.dispatcher = dispatcher

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
        pyglet.clock.unschedule(self.timer_loading_end)

    def timer_loading(self, dt):
        """
        Default timer handler for Board.LOADING
        """
        for rect in self.dispatcher.rectangles:
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
        self.dispatcher.game.change_board(Board.WELCOME)

    def start_timer_welcome(self):
        """
        Start default timer for Board.WELCOME
        """
        w, h = self.dispatcher.label_manager.get_size("common", "title", self.dispatcher.lang)
        self.dispatcher.label_manager.move_to("common", "title", ARENA_WIDTH + w/2, h/2 + 15)
        pyglet.clock.schedule_interval(self.timer_welcome, 1.0/60)

    def stop_timer_welcome(self):
        """
        Stop default timer for Board.WELCOME
        """
        pyglet.clock.unschedule(self.timer_welcome)

    def timer_welcome(self, dt):
        """
        Default timer handler for Board.WELCOME
        """
        x, y = self.dispatcher.label_manager.get_pos("common", "title", self.dispatcher.lang)
        w, h = self.dispatcher.label_manager.get_size("common", "title", self.dispatcher.lang)
        if y < 1000:
            if x <= ARENA_WIDTH/2:
                self.dispatcher.label_manager.move_by("common", "title", 0, 10)
            else:
                self.dispatcher.label_manager.move_by("common", "title", -10, 0)
        else:
            size = self.dispatcher.label_manager.get_font_size("common", "title")
            if size > 96:
                self.dispatcher.label_manager.set_font_size("common", "title", size-4)
            else:
                # Stop timer, change to Board.MENU
                self.stop_timer_welcome()
                self.dispatcher.game.change_board(Board.MENU)
