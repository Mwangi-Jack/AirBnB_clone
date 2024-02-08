#!/usr/bin/python3

"""This module defines the BaseModel class, which serves as the base model for other classes."""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
                id (str): Unique identifier for the instance.
                created_at (str): ISO formatted string representing the creation date and time.

        If kwargs is provided, the instance attributes are initialized using the provided values,
        otherwise, new values are generated for id and created_at attributes.

        Returns:
            None
        """

        if not kwargs["id"]:
            storage.new(kwargs)

        if kwargs:
            self.id = kwargs["id"]
            self.created_at = kwargs["created_at"]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()



        self.__dict__["__class__"] = type(self).__name__
        self.updated_at = datetime.now().isoformat()


    def save(self):
        """
        Updates the updated_at attribute with the current date and time.

        Returns:
            str: Updated value of updated_at attribute (ISO formatted string).
        """
        self.updated_at = datetime.now().isoformat()
        storage.save()
        # return self.updated_at

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.

        Returns:
            dict: Dictionary containing instance attributes.
        """
        return self.__dict__

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: String representation of the instance.
        """
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}]"
