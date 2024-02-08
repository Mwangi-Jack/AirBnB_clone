#!/usr/bin/python3

import json
import os

"""This class simply serializes instaces to a JSON file and deserializes JSON file to instnaces"""

class FileStorage:
    """FileStorage class"""

    def __init__(self, *args, **kwargs):
        self.__file_path = "file.json"
        self.__objects = {}


    def all(self):
        """returns  a dictionary of all the objects in the __objects attribute"""
        return self.__objects

    def new(self,obj):
        """sets in __objects the obj with the key <obj class name>.id

        Args:
			obj: Object to be added to __objects

		Returns:
			None
        """
        class_name = obj['__class__']
        obj_id = obj["id"]
        key = f"{class_name}.{obj_id}"
        self.__objects[key] = obj

    def save(self):
        """To serialize __objects to the JSON file"""
        with open(self.__file_path, 'w', encoding='utf-8') as json_file:
            json.dump(self.__objects, json_file, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists other wise it does nothing)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as json_file:
                self.__objects = json.load(json_file)

