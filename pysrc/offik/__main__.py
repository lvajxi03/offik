#!/usr/bin/env python3

"""
Main program module
"""

import random
import pyglet
from offik.arena import Arena
from offik.ctypes import Board

if __name__ == "__main__":
    display = pyglet.canvas.get_display()
    scr = display.get_default_screen()
    mod = scr.get_mode()
    random.seed()
    arena = Arena(mod)
    arena.change_board(Board.LOADING)
    pyglet.app.run()
