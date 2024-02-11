#!/usr/bin/python3

import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
import sys
import os
from models.base_model import BaseModel

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)






class TestBaseModel(unittest.TestCase):
    """Test class for the BaseModel class"""
    def setUp(self):
        """
        Set up a new instance of BaseModel for each test.
        """
        self.base_model = BaseModel()

    def test_id_created_at_updated_at(self):
        """
        Test if BaseModel instance has id, created_at,
        and updated_at attributes.
        """
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    @patch('models.storage')
    def test_init_with_args(self, mock_storage):
        """
        Test initialization of BaseModel with arguments.
        """
        test_id = 'test-id'
        test_created_at = datetime.now().strftime(BaseModel.DATE_FORMAT)
        test_updated_at = datetime.now().strftime(BaseModel.DATE_FORMAT)
        base_model = BaseModel(id=test_id, created_at=test_created_at,
                               updated_at=test_updated_at)
        self.assertEqual(base_model.id, test_id)
        self.assertEqual(base_model.created_at.strftime(BaseModel.DATE_FORMAT),
                         test_created_at)
        self.assertEqual(base_model.updated_at.strftime(BaseModel.DATE_FORMAT),
                         test_updated_at)
        mock_storage.new.assert_not_called()

    @patch('models.storage')
    def test_init_without_args(self, mock_storage):
        """
        Test initialization of BaseModel without arguments.
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        # mock_storage.new.assert_called_once()

    @patch('models.storage')
    def test_save(self, mock_storage):
        """
        Test the save method of BaseModel.
        """
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, original_updated_at)
        # mock_storage.save.assert_called_once()

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        """
        expected_dict = {
            'id': self.base_model.id,
            '__class__': 'BaseModel',
            'created_at':
                self.base_model.created_at.isoformat(),
            'updated_at':
                self.base_model.updated_at.isoformat()
        }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)

    def test_str(self):
        """
        Test the string representation of BaseModel.
        """
        str = f"[BaseModel] {self.base_model.id} {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), str)


if __name__ == '__main__':
    unittest.main()
