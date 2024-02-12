#!/usr/bin/python3

import unittest
import os
import json
from unittest.mock import MagicMock
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up a FileStorage instance for testing."""
        self.file_storage = FileStorage()

    def tearDown(self):
        """Clean up after each test."""
        # Delete the file.json created during testing
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_all(self):
        """Test the all method of the FileStorage class."""
        # Add a dummy object to __objects
        obj = BaseModel()
        self.file_storage.new(obj)
        # Check if the returned dictionary matches the expected result
        self.assertEqual(self.file_storage.all(), {'BaseModel.' + obj.id: obj})

    def test_new(self):
        """Test the new method of the FileStorage class."""
        # Mock a BaseModel object
        obj = MagicMock(spec=BaseModel)
        obj.__class__.__name__ = 'BaseModel'
        obj.id = 'test_id'
        # Call the new method
        self.file_storage.new(obj)
        # Check if the object is correctly added to __objects
        self.assertEqual(self.file_storage.all(), {'BaseModel.test_id': obj})

    def test_save(self):
        """Test the save method of the FileStorage class."""
        # Mock a BaseModel object
        obj = MagicMock(spec=BaseModel)
        obj.__class__.__name__ = 'BaseModel'
        obj.id = 'test_id'
        # Add the object to __objects
        self.file_storage.new(obj)
        # Call the save method
        self.file_storage.save()
        # Check if file.json is created and contains the correct data
        self.assertTrue(os.path.exists('file.json'))
        with open('file.json', 'r') as file:
            data = json.load(file)
            self.assertEqual(data, {'BaseModel.test_id': obj.to_dict()})

    def test_reload(self):
        """Test the reload method of the FileStorage class."""
        # Create a dummy data file
        data = {'BaseModel.test_id': {'id': 'test_id'}}
        with open('file.json', 'w') as file:
            json.dump(data, file)
        # Call the reload method
        self.file_storage.reload()
        # Check if the objects are correctly loaded into __objects
        self.assertEqual(len(self.file_storage.all()), 1)


if __name__ == '__main__':
    unittest.main()
