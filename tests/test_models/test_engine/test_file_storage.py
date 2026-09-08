#!/usr/bin/python3
"""
Unittest for FileStorage class.
"""
import json
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test suite for models.engine.file_storage.FileStorage
    """

    def setUp(self):
        """Clean file.json before tests."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean file.json after tests."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_docstrings(self):
        """Test docstrings present across module and class."""
        import models.engine.file_storage as fs
        self.assertIsNotNone(fs.__doc__)
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all_returns_dict(self):
        """Test that all() returns the dictionary of objects."""
        self.assertIsInstance(storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new() adds an object to __objects."""
        b = BaseModel()
        key = "BaseModel.{}".format(b.id)
        self.assertIn(key, storage.all())
        self.assertIs(storage.all()[key], b)

    def test_save_creates_json_file(self):
        """Test that save() writes objects to file.json."""
        b = BaseModel()
        b.name = "Test Save"
        storage.save()

        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            key = "BaseModel.{}".format(b.id)
            self.assertIn(key, data)
            self.assertEqual(data[key]["name"], "Test Save")

    def test_reload_loads_objects(self):
        """Test that reload() recreates objects from JSON file."""
        b = BaseModel()
        b.name = "Test Reload"
        b.save()

        # Clear memory objects
        FileStorage._FileStorage__objects = {}
        self.assertEqual(len(storage.all()), 0)

        # Reload from file.json
        storage.reload()
        key = "BaseModel.{}".format(b.id)
        self.assertIn(key, storage.all())
        reloaded = storage.all()[key]
        self.assertEqual(reloaded.name, "Test Reload")
        self.assertEqual(reloaded.id, b.id)


if __name__ == "__main__":
    unittest.main()
