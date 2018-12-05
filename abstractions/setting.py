"""Represents a module setting"""

import logging
import uuid


class Setting:

    def __init__(self, text, value, doc=""):
        """doc   - documentation for a setting"""
        self.__text = text
        self.__value = value
        self.doc = doc
        self.__key = uuid.uuid4()

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def test_valid(self, pipeline):
        pass
