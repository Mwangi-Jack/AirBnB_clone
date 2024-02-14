#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up a User instance for testing."""
        self.user = User()

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_initialization(self):
        """Test the initialization of the User class."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    # @patch('models.storage')
    # def test_new(self, mock_storage):
    #     """Test the new method of the User class."""
    #     # Mock a BaseModel object
    #     obj = MagicMock()
    #     # Call the new method
    #     user = User()
    #     # Check if storage.new() is called
    #     mock_storage.new.assert_called_once_with(user)


if __name__ == '__main__':
    unittest.main()
