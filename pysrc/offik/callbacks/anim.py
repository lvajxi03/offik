#!/usr/bin/env python3

import random


def callback_loading(rectangles):
    """
    Recalculate rectangles when in Board.LOADING
    """
    for rect in rectangles:
        rect.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            255)
