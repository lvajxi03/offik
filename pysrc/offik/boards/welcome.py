#!/usr/bin/env python3

"""
Board.WELCOME class
"""

from offik.boards.standard import PlainBoard
from offik.events.welcome import WelcomeEventManager


class BoardWelcome(PlainBoard):
    """
    Board.WELCOME main class
    """
    def __init__(self, arena):
        super().__init__(arena)
        self.event_manager = WelcomeEventManager(self)

    def paint(self):
        self.image_manager.draw("common", "background", 0, 0)
        self.label_manager.draw("common", "title", self.arena.lang)

    def start(self):
        self.event_manager.start_timer_welcome()

    def stop(self):
        self.event_manager.stop_timer_welcome()
