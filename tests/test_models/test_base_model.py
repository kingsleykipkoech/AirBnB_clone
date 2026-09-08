#!/usr/bin/python3
"""Unittest for BaseModel class."""
from datetime import datetime
import time
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test suite for BaseModel."""

    def test_docstrings(self):
        """Test docstrings present."""
        import models.base_model as bm
        self.assertIsNotNone(bm.__doc__)
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_instantiation(self):
        """Test basic instantiation of BaseModel."""
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertIsInstance(b.id, str)
        self.assertIsInstance(b.created_at, datetime)
        self.assertIsInstance(b.updated_at, datetime)

    def test_unique_id(self):
        """Test that two instances have unique IDs."""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_str_representation(self):
        """Test __str__ output formatting."""
        b = BaseModel()
        expected = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(str(b), expected)

    def test_save_updates_timestamp(self):
        """Test that save method updates updated_at timestamp."""
        b = BaseModel()
        old_updated = b.updated_at
        time.sleep(0.01)
        b.save()
        self.assertGreater(b.updated_at, old_updated)

    def test_to_dict(self):
        """Test dictionary conversion method."""
        b = BaseModel()
        b.name = "AirBnB"
        b.number = 89
        d = b.to_dict()

        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["name"], "AirBnB")
        self.assertEqual(d["number"], 89)
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())

    def test_kwargs_instantiation(self):
        """Test creating BaseModel from dictionary kwargs."""
        b1 = BaseModel()
        b1.name = "My Model"
        b1.my_number = 42
        b1_dict = b1.to_dict()

        b2 = BaseModel(**b1_dict)
        self.assertEqual(b1.id, b2.id)
        self.assertEqual(b1.created_at, b2.created_at)
        self.assertEqual(b1.updated_at, b2.updated_at)
        self.assertEqual(b2.name, "My Model")
        self.assertEqual(b2.my_number, 42)
        self.assertIsNot(b1, b2)


if __name__ == "__main__":
    unittest.main()
