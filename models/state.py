#!/usr/bin/python3


from models.base_model import BaseModel


class State(BaseModel):
    """Class State inheriting from the BaseModel class"""

    def __init__(self):
        super().__init__()
        self.name = ""
