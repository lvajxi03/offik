#!/usr/bin/env python3

"""
Core types
"""

import enum


@enum.unique
class Orientation(enum.IntEnum):
    """
    General orientation enum type
    """
    HORIZONTAL = 0
    VERTICAL = 1

    def change(self):
        """
        Change orientation to the other one
        """
        return Orientation.HORIZONTAL if self.value \
                                         == Orientation.VERTICAL else Orientation.VERTICAL


@enum.unique
class Direction(enum.IntEnum):
    "General direction enum type"
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def rotate_left(self):
        """
        Rotate left and return new value
        :return: Direction after being rotated
        """
        val = self.value - 1
        val %= 4
        return Direction(val)

    def rotate_right(self):
        """
        Rotate right and return new value
        :return: Direction after being rotated
        """
        val = self.value + 1
        val %= 4
        return Direction(val)
