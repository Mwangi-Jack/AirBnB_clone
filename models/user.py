#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    """This is the user class which inherits from BaseModel class"""
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        storage.new(self)
