#!/usr/bin/python3

import json
import os

class FileStorage:
    """This class does the serialization/deserialization from and to JSON format"""

    def __init__(self):
        """initialization
        This method initializes an instance with  file path and an
        empty object 'objects'
        """
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """This returns the dictionary 'objects'"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        print("OBJECT TO SAVE:::::::", obj)
        key = f"{obj.__class__.__name__}.{obj['id']}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding='utf-8') as json_file:
            json.dump(self.__objects, json_file, indent= 4)

    def reload(self):
        """deserializes  the JSON file to __object only if __file_path exists"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as json_file:
                self.__objects = json.load(json_file)


