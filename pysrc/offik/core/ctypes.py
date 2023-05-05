#!/usr/bin/env python3

"""
Core types
"""

import enum


@enum.unique
class Orientation(enum.IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1

    def change(self):
        return Orientation.HORIZONTAL if self.value == Orientation.VERTICAL else Orientation.VERTICAL


@enum.unique
class Direction(enum.IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def rotate_left(self):
        v = self.value - 1
        v %= 4
        return Direction(v)

    def rotate_right(self):
        v = self.value + 1
        v %= 4
        return Direction(v)
