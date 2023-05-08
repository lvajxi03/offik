#!/usr/bin/env python3

"""
Primitive types
"""


class Rect:
    """
    Generic rectangle class
    """
    def __init__(self, x, y, w, h):
        """
        Create rectangle
        :param x: bottom x coordinate
        :param y: bottom y coordinate
        :param w: width
        :param h: height
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, x, y) -> bool:
        """
        Check if rectangle contains a point
        :param x: point x coordinate
        :param y: point y coordinate
        :return: True if rectangle contains a point, False otherwise
        """
        if self.x <= x <= self.x + self.w:
            if self.y <= y <= self.y + self.h:
                return True
        return False

    def set_size(self, w, h) -> None:
        """
        Set new size
        :param w: new width
        :param h: new height
        :return: None
        """
        if w > 0:
            self.w = w
        if h > 0:
            self.h = h

    def move_to(self, x, y) -> None:
        """
        Move to a specific location
        :param x: specific location x
        :param y: specific location y
        :return: None
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy) -> None:
        """
        Move by a specific distance
        :param dx: distance length
        :param dy: distance height
        :return: None
        """
        self.x += dx
        self.y += dy

    def move(self) -> None:
        """
        Abstract method
        :return: None
        """

    def collides(self, rect) -> bool:
        """
        Check if collides with another rectangle
        :param rect: Rectangle to check
        :return: True if collides, false otherwise
        """
        if rect is not None:
            if self.x >= rect.x + rect.w or self.x + self.w <= rect.x:
                return False
            if self.y >= rect.y + rect.h or self.y + self.h <= rect.y:
                return False
            return True
        return False
