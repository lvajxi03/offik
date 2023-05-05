#!/usr/bin/env python3

from offik.callbacks.anim import callback_loading

"""
Timers and events for Board.LOADING
"""


def timer_loading(dt, arena):
    callback_loading(arena.rectangles)
