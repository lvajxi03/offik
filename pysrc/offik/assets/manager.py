#!/usr/bin/env python3

"""
Asset manager classes
"""

import json
import os
from pyglet import image
from pyglet.text import Label
from pyglet.gl import *


class LabelManager:
    """
    Manage your labels
    """

    def __init__(self, path: str, autoload=True):
        """
        Create LabelManager instance
        :param path: resource root directory
        :param autoload: if True, create labels as described in layout
        """
        self.labels = {}
        self.path = path
        if autoload:
            self.create()

    def create(self):
        """
        Create labels with layout loaded from default directory
        """
        self.create_from_dir(self.path)

    def create_from_dir(self, path: str):
        """
        Create labels with layout loaded from a given path
        :param path: resource root directory

        Remark: manager is expecting `labels.json` file in given subdirectory
        """
        path = os.path.join(path, "labels.json")
        langs = ["pl", "en", "ua"]
        try:
            with open(path) as fh:
                layout = json.load(fh)
                for key in layout:
                    for label in layout[key]:
                        for lang in langs:
                            lab = Label(layout[key][label][lang],
                                        font_name=layout[key][label]["font-face"],
                                        font_size=layout[key][label]["font-size"],
                                        color=(layout[key][label]["front-color"][0],
                                               layout[key][label]["front-color"][1],
                                               layout[key][label]["front-color"][2],
                                               layout[key][label]["front-color"][3]),
                                        anchor_x=layout[key][label]["anchor_x"],
                                        anchor_y=layout[key][label]["anchor_y"])
                            if key not in self.labels:
                                self.labels[key] = {}
                            if label not in self.labels[key]:
                                self.labels[key][label] = {}
                            if lang not in self.labels[key][label]:
                                self.labels[key][label][lang] = {}
                            self.labels[key][label][lang]["front"] = lab
                            sha = Label(layout[key][label][lang],
                                        font_name=layout[key][label]["font-face"],
                                        font_size=layout[key][label]["font-size"],
                                        color=(layout[key][label]["shadow-color"][0],
                                               layout[key][label]["shadow-color"][1],
                                               layout[key][label]["shadow-color"][2],
                                               layout[key][label]["shadow-color"][3]),
                                        anchor_x=layout[key][label]["anchor_x"],
                                        anchor_y=layout[key][label]["anchor_y"])
                            self.labels[key][label][lang]["shadow"] = sha
        except IOError:
            pass

    def draw(self, key: str, label: str, lang: str):
        """
        Draw specific label

        """
        shadow_label = None
        front_label = None
        try:
            shadow_label = self.labels[key][label][lang]["shadow"]
        except KeyError:
            pass
        try:
            front_label = self.labels[key][label][lang]["front"]
        except KeyError:
            pass
        if shadow_label:
            shadow_label.draw()
        if front_label:
            front_label.draw()

    def move_to(self, key: str, label: str, lang: str, x: int, y: int):
        """
        Move label to specific location
        """
        shadow_label = None
        front_label = None
        try:
            shadow_label = self.labels[key][label][lang]["shadow"]
        except KeyError:
            pass
        try:
            front_label = self.labels[key][label][lang]["front"]
        except KeyError:
            pass
        if shadow_label:
            shadow_label.x = x + 5
            shadow_label.y = y - 5
        if front_label:
            front_label.x = x
            front_label.y = y

    def get_pos(self, key: str, label: str, lang: str):
        """
        Get label position
        """
        lab = None
        try:
            lab = self.labels[key][label][lang]["front"]
        except KeyError:
            pass
        if lab:
            return lab.x, lab.y
        return -1, -1

    def get_size(self, key: str, label: str, lang: str):
        """
        Get label size
        """
        lab = None
        try:
            lab = self.labels[key][label][lang]["front"]
        except KeyError:
            pass
        if lab:
            return lab.content_width, lab.content_height
        return -1, -1

    def get_font_size(self, key: str, label: str) -> int:
        """
        Get font size that was used to create this label
        :param key: section key name
        :param label: label name
        :return: font size in px or -1 if no such label
        """
        lab = None
        try:
            lab = self.labels[key][label]["pl"]["front"]
        except KeyError:
            pass
        if lab:
            return lab.font_size
        return -1

    def set_font_size(self, key: str, label: str, new_size: int):
        """
        TODO.
        """
        if new_size > 0:
            try:
                langs = self.labels[key][label]
                for lang in langs:
                    langs[lang]["front"].font_size = new_size
                    langs[lang]["shadow"].font_size = new_size
            except KeyError:
                pass

    def move_by(self, key: str, label: str, lang: str, dx: int, dy: int):
        """
        Move label by specific distance (dx and dy)
        :param key: section key name
        :param label: label name
        :param lang: language identifier
        :param dx: x-axis distance
        :param dy: y-axis distance
        """
        shadow_label = None
        front_label = None
        try:
            shadow_label = self.labels[key][label][lang]["shadow"]
        except KeyError:
            pass
        try:
            front_label = self.labels[key][label][lang]["front"]
        except KeyError:
            pass
        if shadow_label:
            shadow_label.x += dx
            shadow_label.y += dy
        if front_label:
            front_label.x += dx
            front_label.y += dy


class ImageManager:
    """
    Manage your images
    """

    def __init__(self, path: str, autoload=True):
        """
        Create ImageManager instance
        :param path: resource root directory
        :param autoload: if True, load images as described in layout
        """
        self.images = {}
        self.path = path
        if autoload:
            self.load()

    def load_from_dir(self, path):
        """
        Load image assets from given directory
        :param path: directory to look into

        Remark: manager is expecting `images.json` file in given subdirectory
        """
        layout_file = os.path.join(path, "images.json")
        try:
            fh = open(layout_file)
            js = json.load(fh)
            # Traverse through layout dictionary:
            for section in js:
                if section not in self.images:
                    self.images[section] = {}
                for key in js[section]:
                    self.images[section][key] = image.load(os.path.join(path, js[section][key]))
        except IOError:
            pass

    def load(self):
        """
        Load image assets from default directory
        """
        self.load_from_dir(self.path)

    def get(self, section: str, key: str):
        """
        Get specific image
        """
        result = None
        if section in self.images:
            if key in self.images[section]:
                result = self.images[section][key]
        return result

    def draw(self, section: str, key: str, x: int, y: int, z: int):
        """
        Draw image at given coordinates
        """
        try:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            self.images[section][key].blit(x, y, z)
        except KeyError:
            pass

    def draw_centered(self, section: str, key: str, x: int, y: int, z: int):
        """
        Draw specified image, but centered at (x, y)
        """
        try:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            image = self.images[section][key]
            x -= image.width/2
            y -= image.height/2
            image.blit(x, y, z)
        except KeyError:
            pass
