#!/usr/bin/env python3

"""
Board.SETUP handler module
"""

from offik.boards.standard import PlainBoard


class BoardSetup(PlainBoard):
    """
    Board.SAVE handler class
    """
    def paint(self):
        super().paint()
        self.label_manager.draw("board-titles", "settings", self.arena.lang)
