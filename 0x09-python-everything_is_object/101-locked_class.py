#!/usr/bin/python3
"""

This is a module that containts a clas that avoids
dynmaically created attributes

"""


class LockedClass:
    __slots__ = ["first_name"]

    def __init__(self, first_name):
        """Method to initialize objects"""
        self.first_name = first_name
