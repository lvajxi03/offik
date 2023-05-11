#!/usr/bin/env python3

"""
Asset manager classes
"""

import json
import os
from pyglet import image
from pyglet.text import Label
from pyglet.gl import glEnable, glBlendFunc, GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA


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
                            if key not in self.labels:
                                self.labels[key] = {}
                            if label not in self.labels[key]:
                                self.labels[key][label] = {}
                            if lang not in self.labels[key][label]:
                                self.labels[key][label][lang] = {}
                            try:
                                lab = Label(layout[key][label][lang],
                                            font_name=layout[key][label]['font-face'],
                                            font_size=layout[key][label]["font-size"],
                                            color=(layout[key][label]["front-color"][0],
                                               layout[key][label]["front-color"][1],
                                               layout[key][label]['front-color'][2],
                                               layout[key][label]["front-color"][3]),
                                            anchor_x=layout[key][label]["anchor_x"],
                                            anchor_y=layout[key][label]["anchor_y"],
                                            x=layout[key][label]["x"],
                                            y=layout[key][label]["y"])
                                self.labels[key][label][lang]["front"] = lab
                                sha = Label(layout[key][label][lang],
                                        font_name=layout[key][label]["font-face"],
                                        font_size=layout[key][label]["font-size"],
                                        color=(layout[key][label]["shadow-color"][0],
                                               layout[key][label]["shadow-color"][1],
                                               layout[key][label]["shadow-color"][2],
                                               layout[key][label]["shadow-color"][3]),
                                        anchor_x=layout[key][label]["anchor_x"],
                                        anchor_y=layout[key][label]["anchor_y"],
                                        x=layout[key][label]["x"]+5,
                                        y=layout[key][label]["y"]-5)
                                self.labels[key][label][lang]["shadow"] = sha
                            except KeyError:
                                pass
        except IOError:
            pass

    def draw(self, key: str, label: str, lang: str):
        """
        Draw specific label

        """
        try:
            shadow_label = self.labels[key][label][lang]["shadow"]
            shadow_label.draw()
        except KeyError:
            pass
        try:
            front_label = self.labels[key][label][lang]["front"]
            front_label.draw()
        except KeyError:
            pass

    def move_to(self, key: str, label: str, x: int, y: int):
        """
        Move label to specific location
        """
        for lang in ["pl", "en", "ua"]:
            try:
                shadow_label = self.labels[key][label][lang]["shadow"]
                shadow_label.x = x + 5
                shadow_label.y = y - 5
            except KeyError:
                pass
            try:
                front_label = self.labels[key][label][lang]["front"]
                front_label.x = x
                front_label.y = y
            except KeyError:
                pass

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
        try:
            lab = self.labels[key][label][lang]["front"]
            return lab.content_width, lab.content_height
        except KeyError:
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

    def move_by(self, key: str, label: str, dx: int, dy: int):
        """
        Move label by specific distance (dx and dy)
        :param key: section key name
        :param label: label name
        :param lang: language identifier
        :param dx: x-axis distance
        :param dy: y-axis distance
        """
        for lang in ["pl", "en", "ua"]:
            try:
                shadow_label = self.labels[key][label][lang]["shadow"]
                shadow_label.x += dx
                shadow_label.y += dy
            except KeyError:
                pass
            try:
                front_label = self.labels[key][label][lang]["front"]
                front_label.x += dx
                front_label.y += dy
            except KeyError:
                pass


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
            b_image = self.images[section][key]
            x -= b_image.width/2
            y -= b_image.height/2
            b_image.blit(x, y, z)
        except KeyError:
            pass
