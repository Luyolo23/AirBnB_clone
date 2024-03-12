#!/usr/bin/python3


import os
import unittest
import models
from models.base_model import BaseModel
from models.user import User
from time import sleep
from datetime import datetime
import sys
sys.path.insert(0, 'AirBnB_clone/tests/test_models/test_user.py')

class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user_instance = User()

    def tearDown(self):
        del self.user_instance

    def test_user_instance_creation(self):
        self.assertIsInstance(self.user_instance, User)
        self.assertTrue(hasattr(self.user_instance, 'id'))
        self.assertTrue(hasattr(self.user_instance, 'created_at'))
        self.assertTrue(hasattr(self.user_instance, 'updated_at'))
        self.assertTrue(hasattr(self.user_instance, 'email'))
        self.assertTrue(hasattr(self.user_instance, 'password'))
        self.assertTrue(hasattr(self.user_instance, 'first_name'))
        self.assertTrue(hasattr(self.user_instance, 'last_name'))

    def test_user_string_representation(self):
        user_string_representation = str(self.user_instance)
        self.assertIn("[User]", user_string_representation)
        self.assertIn("id", user_string_representation)
        self.assertIn("created_at", user_string_representation)
        self.assertIn("updated_at", user_string_representation)
        self.assertIn("email", user_string_representation)
        self.assertIn("password", user_string_representation)
        self.assertIn("first_name", user_string_representation)
        self.assertIn("last_name", user_string_representation)

    def test_user_to_dict_conversion(self):
        user_dict_representation = self.user_instance.to_dict()
        self.assertIsInstance(user_dict_representation, dict)
        self.assertEqual(user_dict_representation['__class__'], 'User')
        self.assertIn('id', user_dict_representation)
        self.assertIn('created_at', user_dict_representation)
        self.assertIn('updated_at', user_dict_representation)
        self.assertIn('email', user_dict_representation)
        self.assertIn('password', user_dict_representation)
        self.assertIn('first_name', user_dict_representation)
        self.assertIn('last_name', user_dict_representation)


if __name__ == '__main__':
    unittest.main()


"""This module tests the User model."""

import os
import unittest
from models.user import User
from models.base_model import BaseModel
from tests.test_models.test_base_model import JSON_FILE_PATH


class TestUserModel(unittest.TestCase):
    """Tests the User model."""

    __expected_attributes = {
        "email": "",
        "password": "",
        "first_name": "",
        "last_name": "",
    }

    @classmethod
    def setUpClass(cls) -> None:
        try:
            os.remove(JSON_FILE_PATH)
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls) -> None:
        try:
            os.remove(JSON_FILE_PATH)
        except FileNotFoundError:
            pass

    def setUp(self) -> None:
        self.user1 = User()
        self.user2 = User()

    def test_presence_of_class_attributes(self) -> None:
        """Tests the presence of the required class attributes."""
        for attribute in self.__expected_attributes:
            self.assertTrue(hasattr(self.user1, attribute))

    def test_save(self) -> None:
        """Tests the inherited `save()` method."""
        User().save()

        self.assertTrue(os.path.exists(JSON_FILE_PATH))

    def test_unique_objects(self) -> None:
        """Tests to ensure no two instances are the same."""
        self.assertNotEqual(self.user1, self.user2)

    def test_default_class_attribute_values(self) -> None:
        """Tests the default values for the public class attributes."""
        for attribute, value in self.__expected_attributes.items():
            self.assertTrue(getattr(self.user1, attribute) == value)
            self.assertTrue(getattr(self.user2, attribute) == value)

    def test_instance_of_object(self) -> None:
        """Tests the classes the User model is an instance of."""
        self.assertIsInstance(self.user2, User)
        self.assertIsInstance(self.user2, BaseModel)

    def test_subclass_of(self) -> None:
        """Tests to ensure User model objects are sub classes of BaseModel"""
        self.assertTrue(issubclass(self.user1.__class__, BaseModel))
        self.assertTrue(issubclass(self.user2.__class__, BaseModel))
        self.assertTrue(issubclass(User, BaseModel))

    def test_nonexistent_attribute(self) -> None:
        """Tests for non-existent attribute."""
        self.assertFalse(hasattr(self.user1, "user_id"))

    def test_nonexistent_method(self) -> None:
        """Tests for non-existent method."""
        self.assertFalse(hasattr(self.user2, "get_user_id()"))

