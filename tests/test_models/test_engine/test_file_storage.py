#!/usr/bin/python3

import unittest
from models import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage_instance = FileStorage()

    def tearDown(self):
        del self.file_storage_instance
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_method(self):
        objects_dict = self.file_storage_instance.all()
        self.assertIsInstance(objects_dict, dict)
        self.assertEqual(objects_dict, self.file_storage_instance._FileStorage__objects)

    def test_new_method(self):
        new_object_instance = BaseModel()
        self.file_storage_instance.new(new_object_instance)
        key = "{}.{}".format(new_object_instance.__class__.__name__, new_object_instance.id)
        self.assertIn(key, self.file_storage_instance._FileStorage__objects)
        self.assertEqual(
            self.file_storage_instance._FileStorage__objects[key],
            new_object_instance
        )

    def test_save_and_reload_methods(self):
        # Create and save objects
        obj1_instance = BaseModel()
        obj2_instance = User()
        obj3_instance = State()
        self.file_storage_instance.new(obj1_instance)
        self.file_storage_instance.new(obj2_instance)
        self.file_storage_instance.new(obj3_instance)
        self.file_storage_instance.save()

        # Check if the file is created
        self.assertTrue(os.path.exists("file.json"))

        # Clear the objects in memory
        del self.file_storage_instance._FileStorage__objects

        # Reload the objects from the file
        self.file_storage_instance.reload()

        # Check if the reloaded objects match the original ones
        key1 = "{}.{}".format(obj1_instance.__class__.__name__, obj1_instance.id)
        key2 = "{}.{}".format(obj2_instance.__class__.__name__, obj2_instance.id)
        key3 = "{}.{}".format(obj3_instance.__class__.__name__, obj3_instance.id)

        self.assertIn(key1, self.file_storage_instance._FileStorage__objects)
        self.assertIn(key2, self.file_storage_instance._FileStorage__objects)
        self.assertIn(key3, self.file_storage_instance._FileStorage__objects)
        self.assertEqual(
            self.file_storage_instance._FileStorage__objects[key1].to_dict(),
            obj1_instance.to_dict()
        )
        self.assertEqual(
            self.file_storage_instance._FileStorage__objects[key2].to_dict(),
            obj2_instance.to_dict()
        )
        self.assertEqual(
            self.file_storage_instance._FileStorage__objects[key3].to_dict(),
            obj3_instance.to_dict()
        )


if __name__ == '__main__':
    unittest.main()

