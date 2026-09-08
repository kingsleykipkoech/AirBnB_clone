#!/usr/bin/python3
"""Defines BaseModel class."""
from datetime import datetime
import models
import uuid


class BaseModel:
    """BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save instance and update timestamp."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Dictionary representation."""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
