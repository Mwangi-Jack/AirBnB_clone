#!/usr/bin/python3

import unittest
from datetime import datetime
from ..models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.base_model = BaseModel()

    def test_constructor(self):
        """Test the constructor of the BaseModel class."""
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        """Test the save method of the BaseModel class."""
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class."""
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(expected_dict, self.base_model.to_dict())

    def test_str(self):
        """Test the string representation of the BaseModel class."""
        exst = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(exst, str(self.base_model))


if __name__ == '__main__':
    unittest.main()
