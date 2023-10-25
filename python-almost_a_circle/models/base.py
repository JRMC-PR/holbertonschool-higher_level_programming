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

    @classmethod
    def create(cls, **dictionary):
        """ class method to return instance with attributes already set
        Args:
            dictionary (dict): dictionary of attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """ class method to write json string to file
        Args:
            list_objs (list): list of objects
        """
        import json
        filename = cls.__name__ + ".json"
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dict))

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

    @staticmethod
    def from_json_string(json_string):
        import json
        if json_string is None or json_string is []:
            return "[]"
        return json.loads(json_string)
