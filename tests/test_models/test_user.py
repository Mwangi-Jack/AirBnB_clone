#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_constructor(self):
        """Test the constructor of the User class."""
        user = User(email='test@example.com', password='password', first_name='John', last_name='Doe')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    @patch('models.storage')
    def test_new(self, mock_storage):
        """Test the new method of the User class."""
        user = MagicMock(spec=User)
        user.__class__.__name__ = 'User'
        user.id = 'test_id'
        user.email = 'test@example.com'
        user.password = 'password'
        user.first_name = 'John'
        user.last_name = 'Doe'
        User.__init__(user)  # Call __init__ manually since patching __init__ might not work in this context
        mock_storage.new.assert_called_once_with(user)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test the save method of the User class."""
        user = User()
        user.save()
        self.assertEqual(user.updated_at, user.created_at)  # Check if updated_at is updated
        mock_storage.save.assert_called_once()  # Ensure that storage.save() is called

    @patch('models.storage')
    def test_to_dict(self, mock_storage):
        """Test the to_dict method of the User class."""
        user = User(email='test@example.com', password='password', first_name='John', last_name='Doe')
        expected_dict = {
            'id': user.id,
            'created_at': user.created_at.isoformat(),
            'updated_at': user.updated_at.isoformat(),
            '__class__': 'User',
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        self.assertDictEqual(user.to_dict(), expected_dict)  # Check if to_dict() returns the correct dictionary

    @patch('models.storage')
    def test_str(self, mock_storage):
        """Test the __str__ method of the User class."""
        user = User(email='test@example.com', password='password', first_name='John', last_name='Doe')
        expected_str = f"[User] ({user.id}) {'email': 'test@example.com', 'password': 'password', 'first_name': 'John', 'last_name': 'Doe'}"
        self.assertEqual(str(user), expected_str)  # Check if __str__() returns the correct string


if __name__ == '__main__':
    unittest.main()
