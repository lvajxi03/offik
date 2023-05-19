#!/usr/bin/env python3

"""
Board.PLAYER module
"""

from offik.ctypes import BoardState
from offik.boards.standard import PlainBoard


class BoardPlayer(PlainBoard):
    """
    Board.PLAYER main supporting class
    """
    def __init__(self, arena):
        """
        Construct an instance of Player class
        :param arena: arena handler
        """
        super().__init__(arena)
        self.state = BoardState.READY

    def paint(self):
        """
        Default paint handler for Board.PLAYER
        """
        super().paint()
        self.label_manager.draw("board-titles", "select-player", self.arena.lang)
