#!/usr/bin/python3
"""Unittest for Amenity class."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test suite for Amenity."""

    def test_inheritance(self):
        """Test Amenity inherits from BaseModel."""
        a = Amenity()
        self.assertIsInstance(a, BaseModel)

    def test_attributes(self):
        """Test Amenity has correct attributes."""
        a = Amenity()
        self.assertEqual(a.name, "")

    def test_to_dict(self):
        """Test Amenity to_dict."""
        a = Amenity()
        d = a.to_dict()
        self.assertEqual(d["__class__"], "Amenity")


if __name__ == "__main__":
    unittest.main()
