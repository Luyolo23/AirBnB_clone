#!/usr/bin/python3

"""A module that defines the BaseModel class"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represent the BaseModel of the project."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    continue

                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)

                    self.updated_at = datetime.now()
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation for an instance of BaseModel."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save the instance and updates the `updated_at`"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
    """Returns the dictionary containing all the key/values of `__dict__`
    of the instance.

    The `updated_at` and `created_at` instance attributes are converted to
    ISO format. A new key named `__class__` is added to the dictionary.

    Returns:
    dict: The dictionary containing all the key/values of `__dict__`
    of the instance.
    """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__

        # update time to ISO format
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict
