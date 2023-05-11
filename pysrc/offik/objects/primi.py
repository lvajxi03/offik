#!/usr/bin/env python

"""
Primitives drawing
"""

import random
import pyglet.shapes
from offik.defs import ARENA_WIDTH, ARENA_HEIGHT


def create_welcome_rectangles(num, batch):
    """
    Create random rectangles, used by Board.LOADING
    :param num: how many rectangles
    :param batch: batch to draw rectangles at once
    """
    height = ARENA_HEIGHT // num
    rectangles = []
    for i in range(num):
        rec = pyglet.shapes.Rectangle(0,
                                    i * height,
                                    ARENA_WIDTH,
                                    height,
                                    color=(
                                        random.randint(0, 255),
                                        random.randint(0, 255),
                                        random.randint(0, 255),
                                        255
                                    ),
                                    batch=batch)
        rectangles.append(rec)
    return rectangles
