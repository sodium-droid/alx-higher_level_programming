#!/usr/bin/python3
"""

This is a module that containts a clas that avoids
dynmaically created attributes

"""


class LockedClass:
    """

    LockedClass with no class or object attribute, that prevents
    user from dynamically creating new instance attributes
    except if the new instance attribute is called first_name

    """
    __slots__ = ["first_name"]

    def __init__(self, first_name):
        """
        Method to initialize objects
        Args:
            first_name: name of Individual (Object)

        """
        self.first_name = first_name
