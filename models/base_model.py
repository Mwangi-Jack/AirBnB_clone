#!/usr/bin/python3


from datetime import datetime
import uuid


class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Updates the public instance attribute 'updated_at with the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary representation of the instance"""
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['create_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj

    def __str__(self):
        """Returns a string representatioin of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
