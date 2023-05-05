#!/usr/bin/env python3

"""
Timers and events for Board.WELCOME
"""

import pyglet.clock
from offik.timers.loading import timer_loading
from offik.ctypes import Board


def timer_welcome_init(dt, arena):
    pyglet.clock.unschedule(timer_loading)
    arena.game.change_board(Board.WELCOME)