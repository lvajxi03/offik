#!/usr/bin/env python

import random
import pyglet.shapes
from offik.defs import ARENA_WIDTH, ARENA_HEIGHT


def create_welcome_rectangles(num, batch):
    height = ARENA_HEIGHT // num
    rectangles = []
    for i in range(num):
        r = pyglet.shapes.Rectangle(0,
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
        rectangles.append(r)
    return rectangles
