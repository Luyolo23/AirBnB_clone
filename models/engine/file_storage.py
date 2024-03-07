#!/usr/bin/python3

"""
This module defines the File Storage class that serializes instances to JSON
files deserializes JSON files to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    """Defines the file storage model."""

    __file_path = "file.json"
    __objects = {}
    __models = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def all(self):
        """Returns all the objects in the dictionary"""
        return self.__objects

    def new(self, obj):
        """
        Saves a new instance to the objects dictionary

        Args:
            obj (Any): The object save in dictionary
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes the objects dictionary and save it to a JSON file."""
        serialized_objects = {}

        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the json objects into their respective models."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_dict = value
                    obj_instance = self.__models[class_name](**obj_dict)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
