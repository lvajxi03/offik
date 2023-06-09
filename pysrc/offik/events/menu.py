#!/usr/bin/env python3

"""
Event managers for Board.MENU
"""
import pyglet.clock
from offik.ctypes import BoardState


class MenuManager:
    """
    Main event manager for Board.MENU
    """
    def __init__(self, menu):
        """
        Initialize manager object
        :param menu: menu object to handle events
        """
        self.menu = menu

    def start_timer_shift_left(self):
        """
        Shift left is when RIGHT ARROW is pressed
        """
        self.menu.state = BoardState.SHIFT
        pyglet.clock.schedule_interval(self.timer_shift_left, 1.0/60)

    def stop_timer_shift_left(self):
        """
        Stop timer shift left
        """
        pyglet.clock.unschedule(self.timer_shift_left)
        self.menu.shift_left()
        self.menu.state = BoardState.READY

    def timer_shift_left(self, dt):
        """
        Shift left timer handler
        """
        if self.menu.distance > 0:
            self.menu.distance -= 32
        else:
            self.stop_timer_shift_left()

    def start_timer_shift_right(self):
        """
        Shift right is when LEFT ARROW is pressed
        """
        self.menu.state = BoardState.SHIFT
        pyglet.clock.schedule_interval(self.timer_shift_right, 1.0/60)

    def stop_timer_shift_right(self):
        """
        Stop timer shift right
        """
        pyglet.clock.unschedule(self.timer_shift_right)
        self.menu.shift_right()
        self.menu.state = BoardState.READY

    def timer_shift_right(self, dt):
        """
        Timer shift right handler
        """
        if self.menu.distance < 1024:
            self.menu.distance += 32
        else:
            self.stop_timer_shift_right()
