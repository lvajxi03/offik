#!/usr/bin/env python3

"""
Config module
"""

import json
import os

DEFAULT_FILENAME: str = "~/.offikrc"


class Config:
    """
    Main configuration class
    """
    def __init__(self):
        """
        Object constructor
        """
        self.data = {}

    def get(self, section: str, key: str):
        """
        Get section::key value or None
        :param section: section name
        :param key: key name
        :return: section::key value or None
        """
        try:
            return self.data[section][key]
        except KeyError:
            return None

    def set(self, section: str, key: str, value):
        """
        Set section::key value
        Create section and/or key if they do not exist
        :param section: section name
        :param key: key name
        :param value: value to set
        """
    def load(self, filename: str) -> bool:
        """
        Load configuration from given filename
        :param filename: filename to load data from
        :return: True if loaded successfully, False otherwise
        """
        try:
            with open(filename) as handle:
                self.data = json.load(handle)
                return True
        except IOError:
            return False

    def load_default(self) -> bool:
        """
        Load configuration from default file
        :return True if loaded successfully, False otherwise
        """
        filename = os.path.expanduser(DEFAULT_FILENAME)
        return self.load(filename)

    def save(self, filename: str) -> bool:
        """
        Save configuration to a given filename
        :param filename: filename to save data to
        :return: True if saved successfully, False otherwise
        """
        try:
            with open(filename, "w") as handle:
                json.dump(self.data, handle, indent=2)
                return True
        except IOError:
            return False

    def save_default(self) -> bool:
        """
        Save configuration to default filename
        :return: True if saved successfully, False otherwise
        """
        filename = os.path.expanduser(DEFAULT_FILENAME)
        return self.save(filename)