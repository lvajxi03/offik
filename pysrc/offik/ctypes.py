#!/usr/bin/env python3

"""
Common types
"""

import enum


@enum.unique
class Board(enum.IntEnum):
    """
    Board representation
    """
    NONE = -1
    LOADING = 0
    WELCOME = 1
    MENU = 2
    PLAYER = 3
    GAME = 4
    LOAD = 5
    OPTIONS = 6
    HISCORES = 7
    SETUP = 8
    HELP = 9
    ABOUT = 10
    QUIT = 11
    NEWSCORE = 12


@enum.unique
class Mode(enum.IntEnum):
    """
    Game mode representation
    """
    NONE = -1
    INIT = 0
    PREPARE = 1
    PLAY = 2
    PAUSED = 3
    KILLED = 4
    GAMEOVER = 5
    CONGRATS = 6
    SHOP = 7
    CHALLENGE = 8
    PLAYER = 9
    SAVE = 10


@enum.unique
class BoardState(enum.IntEnum):
    """
    Board State type
    READY: accepting user events,
    SHIFT: animating objects, no events
    """
    READY = 0
    SHIFT = 1
