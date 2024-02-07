"""import unittest module"""
import unittest

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Set up instances for the BaseModel Class"""

    def setUp(self):
        self.inst_1 = BaseModel()
        self.insta_2 = BaseModel()




if __name__ == '__main__':
    unittest.main()
