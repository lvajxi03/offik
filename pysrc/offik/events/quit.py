#!/usr/bin/env python3

"""
Event managers for Board.QUIT
"""

import pyglet.clock
from offik.ctypes import QuitState


class QuitManager:
    """
    Main event manager for Board.QUIT
    """
    def __init__(self, quit):
        self.quit = quit

    def start_timer_shift_left(self):
        """
        Shift left starts when LEFT ARROW is pressed
        (unlike the menu board behavior)
        """
        self.quit.state = QuitState.SHIFT
        pyglet.clock.schedule_interval(self.timer_shift_left, 1.0/60)

    def stop_timer_shift_left(self):
        """
        Stop shift-left timer
        """
        pyglet.clock.unschedule(self.timer_shift_left)
        self.quit.state = QuitState.READY
        self.quit.exit = True

    def timer_shift_left(self, dt):
        """
        Timer shift left callback method
        """
        if self.quit.distance > -640:
            self.quit.distance -= 32
        else:
            self.stop_timer_shift_left()

    def start_timer_shift_right(self):
        """
        Shift right is when RIGHT ARROW is pressed
        (unlike the menu board behavior)
        """
        self.quit.state = QuitState.SHIFT
        pyglet.clock.schedule_interval(self.timer_shift_right, 1.0/60)

    def stop_timer_shift_right(self):
        """
        Stop shift-right timer
        """
        pyglet.clock.unschedule(self.timer_shift_right)
        self.quit.state = QuitState.READY
        self.quit.exit = False

    def timer_shift_right(self, dt):
        """
        Timer shift right callback method
        """
        if self.quit.distance < 0:
            self.quit.distance += 32
        else:
            self.stop_timer_shift_right()
