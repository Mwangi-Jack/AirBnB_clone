#!/usr/bin/python3

"""This is a base model class it defines all common attributes/methods for  other classes"""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel Class"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        self.__dict__["__class__"] = type(self).__name__

    def save(self):
        """updates the updated_at attribute with the current time"""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        # class_object = self.__dict__[__class__] = type(self).__name__
        return self.__dict__


    def __str__(self):
        """This Returns a string representation of an instance"""
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}]"
