#!/usr/bin/python3

import json
import os

"""
This class simply serializes instaces to a JSON file and deserializes
JSON file to instnaces
"""


class FileStorage:
    """FileStorage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns  a dictionary of all the objects in the __objects attribute
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with the key <obj class name>.id
        """
        class_name = obj.__class__.__name__
        obj_id = obj.id
        key = f"{class_name}.{obj_id}"
        self.__objects[key] = obj

    def save(self):
        """To serialize __objects to the JSON file"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as json_file:
            json.dump(serialized_objects, json_file, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists other wise it does nothing)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    module = __import__('models.base_model',
                                        fromlist=[class_name])
                    cls = getattr(module, class_name)
                    self.__objects[key] = cls(**value)
