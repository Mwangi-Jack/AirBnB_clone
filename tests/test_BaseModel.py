#!/usr/bin/python3

import unittest
import os
import sys
from datetime import datetime

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Set up instances for the BaseModel Class"""

    def setUp(self):
        self.inst_1 = BaseModel()
        self.insta_2 = BaseModel()

    def test_init(self):
        """Test initialization of BaseModel"""
        self.assertIsInstance(self.inst_1, BaseModel)

    def test_save(self):
        """test for time update"""
        prev_time = self.inst_1.updated_at
        updated_time = self.inst_1.save()
        self.assertNotEqual(prev_time, updated_time)


if __name__ == '__main__':
    unittest.main()
