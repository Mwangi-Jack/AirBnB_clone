#!/usr/bin/python3

import unittest
from unittest.mock import patch
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up a User instance for testing."""
        self.user = User()

    def test_inheritance(self):
        """Test if User class inherits from BaseModel class."""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test if User instance has the expected attributes."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    @patch('models.storage')
    def test_new(self, mock_storage):
        """Test if new method correctly adds the User object to storage."""
        user = User()
        self.assertEqual(len(mock_storage.new.call_args_list), 1)
        self.assertEqual(mock_storage.new.call_args[0][0], user)

    @patch('models.storage')
    def test_init_with_args(self, mock_storage):
        """Test if User initialization with arguments works correctly."""
        data = {
            'id': 'test_id',
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**data)
        self.assertEqual(user.id, data['id'])
        self.assertEqual(user.email, data['email'])
        self.assertEqual(user.password, data['password'])
        self.assertEqual(user.first_name, data['first_name'])
        self.assertEqual(user.last_name, data['last_name'])
        self.assertEqual(len(mock_storage.new.call_args_list), 1)
        self.assertEqual(mock_storage.new.call_args[0][0], user)


if __name__ == '__main__':
    unittest.main()
