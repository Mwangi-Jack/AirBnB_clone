#!/usr/bin/python3

import unittest
import os
import sys
from datetime import datetime
import time

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """"Class for testing the BaseModel class"""

    def test_init(self):
        """Test initialization with no arguments"""
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.created_at, str)
        self.assertIsInstance(model.updated_at, str)

        # Test initialization with provided id and created_at
        model_with_data = BaseModel(id='123', created_at='2022-01-01T12:00:00')
        self.assertEqual(model_with_data.id, '123')
        self.assertEqual(model_with_data.created_at, '2022-01-01T12:00:00')

    def test_save(self):
        """"Test for time update"""
        model = BaseModel()
        initial_updated_at = model.updated_at
        time.sleep(1)  # Wait for a second to simulate a delay
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test __dict__ method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at)
        self.assertEqual(model_dict['updated_at'], model.updated_at)

    def test_str(self):
        """"Test __str__ method"""
        model = BaseModel()
        str_representation = str(model)
        self.assertTrue('[BaseModel]' in str_representation)
        self.assertTrue(model.id in str_representation)
        self.assertTrue(model.created_at in str_representation)
        self.assertTrue(model.updated_at in str_representation)

if __name__ == '__main__':
    unittest.main()
