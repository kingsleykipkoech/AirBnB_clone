#!/usr/bin/python3
"""Defines FileStorage class."""
import json
import os


class FileStorage:
    """FileStorage class."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Set obj in __objects with key <obj class name>.id."""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file."""
        json_objects = {}
        for key, obj in FileStorage.__objects.items():
            json_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserialize JSON file to __objects."""
        if not os.path.exists(FileStorage.__file_path):
            return

        from models.base_model import BaseModel

        classes = {
            "BaseModel": BaseModel
        }

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                saved_objects = json.load(f)
                for key, obj_data in saved_objects.items():
                    class_name = obj_data["__class__"]
                    if class_name in classes:
                        FileStorage.__objects[key] = classes[class_name](**obj_data)
        except Exception:
            pass
