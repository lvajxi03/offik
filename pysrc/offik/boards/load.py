#!/usr/bin/env python3

"""
Board.LOAD handler module
"""

from offik.boards.standard import PlainBoard


class BoardLoad(PlainBoard):
    """
    Board.SAVE handler class
    """
    def paint(self):
        super().paint()
        self.label_manager.draw("board-titles", "load-game", self.arena.lang)
