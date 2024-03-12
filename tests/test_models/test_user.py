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

