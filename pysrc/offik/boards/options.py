#!/usr/bin/env python3

"""
Board.OPTIONS main class
"""

from offik.boards.standard import PlainBoard


class BoardOptions(PlainBoard):
    """
    Board.OPTIONS main supporting class
    """
    def paint(self):
        """
        Default paint handler for Board.OPTIONS
        """
        super().paint()
        self.label_manager.draw("board-titles", "options", self.arena.lang)
