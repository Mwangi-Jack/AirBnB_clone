#!/usr/bin/python3

import unittest
import json
import os
import sys
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)


class TestFileStorage(unittest.TestCase):
    """
    Test class for the FileStorage class.
    """
    def setUp(self):
        """
        Set up method to create FileStorage instance and a test object.
        """
        self.storage = FileStorage()
        self.test_obj = BaseModel()
        self.test_obj.id = "test_id"
        self.storage.new(self.test_obj)

    def tearDown(self):
        """
        Tear down method to remove the JSON file created during testing.
        """
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_new(self):
        """
        Test whether the new method correctly adds the
        object to the __objects dictionary.
        """
        obj_key = f"{self.test_obj.__class__.__name__}.{self.test_obj.id}"
        self.assertIn(obj_key, self.storage.all())

    def test_save_and_reload(self):
        """
        Test whether saving and reloading the FileStorage
        instance correctly persists and retrieves objects from the JSON file.
        """
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        obj_key = f"{self.test_obj.__class__.__name__}.{self.test_obj.id}"
        self.assertIn(obj_key, new_storage.all())
        self.assertIsInstance(new_storage.all()[obj_key], BaseModel)
        self.assertEqual(new_storage.all()[obj_key].id, self.test_obj.id)


if __name__ == '__main__':
    unittest.main()
