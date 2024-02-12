#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.new_model = BaseModel()

    def test_constructor(self):
        """Test the constructor of the BaseModel class."""
        self.assertIsInstance(self.new_model.id, str)
        self.assertIsInstance(self.new_model.created_at, datetime)
        self.assertIsInstance(self.new_model.updated_at, datetime)

    def test_save(self):
        """Test the save method of the BaseModel class."""
        previous_updated_at = self.new_model.updated_at
        self.new_model.save()
        self.assertNotEqual(previous_updated_at, self.new_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class."""
        expected_dict = {
            'id': self.new_model.id,
            'created_at': self.new_model.created_at.isoformat(),
            'updated_at': self.new_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(expected_dict, self.new_model.to_dict())

    def test_str(self):
        """Test the string representation of the BaseModel class."""
        _str = f"[BaseModel] ({self.new_model.id}) {self.new_model.__dict__}"
        self.assertEqual(_str, str(self.new_model))


if __name__ == '__main__':
    unittest.main()
