#!/usr/bin/env python3

"""
Game business logic
"""

from offik.ctypes import Board, Mode


class Game:
    """
    Business logic of the game
    """
    def __init__(self, arena):
        """
        Game object constructor
        :param arena: Arena handler
        """
        self.mode = Mode.NONE
        self.board = Board.NONE
        self.arena = arena
        self.board_initializers = {
            Board.LOADING: self.initialize_board_loading,
            Board.WELCOME: self.initialize_board_welcome,
            Board.MENU: self.initialize_board_menu
        }
        self.mode_initializers = {
            Mode.INIT: self.initialize_mode_init,
            Mode.PREPARE: self.initialize_mode_prepare,
            Mode.PLAY: self.initialize_mode_play
        }

    def change_board(self, new_board):
        """
        Change board to a new one.
        Only if it differs from current board
        :param new_board: new board to change to
        """
        if self.board != new_board:
            try:
                initializer = self.board_initializers[new_board]
                initializer()
            except KeyError:
                pass
            self.board = new_board

    def change_mode(self, new_mode):
        """
        Change game mode to a new one.
        Only if it's different from current mode
        :param new_mode: new mode to change to
        """
        if self.mode != new_mode:
            try:
                initializer = self.mode_initializers[new_mode]
                initializer()
            except KeyError:
                pass
            self.mode = new_mode

    def initialize_board_welcome(self):
        """
        Initializer for Board.WELCOME
        """
        self.arena.event_manager.stop_timer_loading()
        self.arena.event_manager.stop_timer_loading_end()
        self.arena.event_manager.start_timer_welcome()

    def initialize_board_loading(self):
        """
        Initialize board loading
        """
        self.arena.event_manager.start_timer_loading()
        self.arena.event_manager.start_timer_loading_end()

    def initialize_board_menu(self):
        """
        Initialize menu board
        """

    def initialize_mode_init(self):
        """
        Initializer for Mode.Init
        """

    def initialize_mode_prepare(self):
        """
        Initializer for Mode.PREPARE
        """

    def initialize_mode_play(self):
        """
        Initializer for Mode.PLAY
        """
