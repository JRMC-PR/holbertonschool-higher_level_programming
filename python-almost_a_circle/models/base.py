#!/usr/bin/python3
""" Base class """


class Base:
    """atts for the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method for base class
        Args:
            id (int): id of the object
            """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """static methods"""

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method to return json string representation
        Args:
            list_dictionaries (list): list of dictionaries
        """
        import json
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        return json.dumps(list_dictionaries)
