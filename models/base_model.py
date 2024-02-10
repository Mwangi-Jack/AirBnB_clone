#!/usr/bin/python3

import uuid
from datetime import date, datetime

class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    def __init__(self):
        """initialization of an instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """updates the public instance attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """creates a dictionary representation of the class """
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj

    def __str__(self):
        """"returns a string representation of an instance """
        return f"[{self.__class__.__name__}] {self.id} {self.__dict__}"

