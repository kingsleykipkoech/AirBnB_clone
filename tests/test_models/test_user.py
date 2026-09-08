#!/usr/bin/python3
"""Unittest for User class."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test suite for User."""

    def test_inheritance(self):
        """Test User inherits from BaseModel."""
        u = User()
        self.assertIsInstance(u, BaseModel)

    def test_attributes(self):
        """Test User has correct attributes."""
        u = User()
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")

    def test_to_dict(self):
        """Test User to_dict."""
        u = User()
        d = u.to_dict()
        self.assertEqual(d["__class__"], "User")


if __name__ == "__main__":
    unittest.main()
