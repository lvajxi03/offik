#!/usr/bin/env python3

"""
Main program module
"""

import random
import pyglet.app
from offik.arena import Arena
from offik.ctypes import Board
from pyglet.gl import *

if __name__ == "__main__":
    random.seed()
    arena = Arena()
    glEnable(GL_BLEND)
    arena.game.change_board(Board.LOADING)
    pyglet.app.run()


