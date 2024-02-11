#!/usr/bin/python3

import uuid
from datetime import datetime

from models import storage


class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """initialization of an instance"""
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime.strptime(kwargs['created_at'],
                                                self.DATE_FORMAT)
            self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                self.DATE_FORMAT)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        updates the public instance attribute 'updated_at'
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creates a dictionary representation of the class """
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()

        return obj

    def __str__(self):
        """"returns a string representation of an instance """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
