#!/usr/bin/python3
"""Unittest for City class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test suite for City."""

    def test_inheritance(self):
        """Test City inherits from BaseModel."""
        c = City()
        self.assertIsInstance(c, BaseModel)

    def test_attributes(self):
        """Test City has correct attributes."""
        c = City()
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")

    def test_to_dict(self):
        """Test City to_dict."""
        c = City()
        d = c.to_dict()
        self.assertEqual(d["__class__"], "City")


if __name__ == "__main__":
    unittest.main()
