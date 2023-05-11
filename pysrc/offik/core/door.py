#!/usr/bin/env python3

"""
Door module
"""


class Door:
    """
    Door class
    """
    def __init__(self, name: str):
        self.name = name
        self.binding = None

    def bind(self, other_door):
        """
        Bind other door
        :param other_door: other door to bind
        """
        self.binding = other_door
        other_door.binding = self

    def unbind(self):
        """
        Unbind other door
        """
        if self.binding:
            self.binding.binding = None
            self.binding = None
