#!/usr/bin/python3

import json
import os

class FileStorage:
    """This class Serializes/Deserializes JSON files"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary representation of __objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __object to the JSON file"""
        with open(self.__file_path, 'r', encoding='utf-8') as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file __file_path exists)
        """
        if os.path.exists(self.__file_path):
            pass
