#!/usr/bin/python3
"""Unittest for Review class."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test suite for Review."""

    def test_inheritance(self):
        """Test Review inherits from BaseModel."""
        r = Review()
        self.assertIsInstance(r, BaseModel)

    def test_attributes(self):
        """Test Review has correct attributes."""
        r = Review()
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")

    def test_to_dict(self):
        """Test Review to_dict."""
        r = Review()
        d = r.to_dict()
        self.assertEqual(d["__class__"], "Review")


if __name__ == "__main__":
    unittest.main()
