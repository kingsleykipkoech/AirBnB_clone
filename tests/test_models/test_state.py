#!/usr/bin/python3
"""Unittest for State class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test suite for State."""

    def test_inheritance(self):
        """Test State inherits from BaseModel."""
        s = State()
        self.assertIsInstance(s, BaseModel)

    def test_attributes(self):
        """Test State has correct attributes."""
        s = State()
        self.assertEqual(s.name, "")

    def test_to_dict(self):
        """Test State to_dict."""
        s = State()
        d = s.to_dict()
        self.assertEqual(d["__class__"], "State")


if __name__ == "__main__":
    unittest.main()
