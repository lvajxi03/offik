#!/usr/bin/env python3

"""
Main program module
"""

import random
import pyglet
from offik.arena import Arena
from offik.ctypes import Board
from offik.defs import ARENA_WIDTH, ARENA_HEIGHT
from pyglet.gl import *

if __name__ == "__main__":
    mode = None
    screen = None
    display = pyglet.canvas.get_display()
    screen = display.get_default_screen()
    mode = screen.get_mode()
    random.seed()
    arena = Arena(mode)
    glEnable(GL_BLEND)
    arena.game.change_board(Board.LOADING)
    pyglet.app.run()


