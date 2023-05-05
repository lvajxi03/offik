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
    GAME = 3
    LOAD = 4
    OPTIONS = 5
    HISCORES = 6
    SETUP = 7
    HELP = 8
    ABOUT = 9
    QUIT = 10
    NEWSCORE = 11


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
class MenuState(enum.IntEnum):
    """
    Menu state representation
    """
    READY = 0
    SHIFT = 1
