#!/usr/bin/env python3

"""
Image assets loading
"""

import pyglet.image


def load_images():
    images = {
        'default-bg':pyglet.image.load('assets/images/default-bg.jpg')
    }
    return images
