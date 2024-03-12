#!/usr/bin/python3

import unittest
from models import State
from datetime import datetime
import os


class TestStateModel(unittest.TestCase):
    def setUp(self):
        self.state_instance = State()

    def tearDown(self):
        del self.state_instance

    def test_state_instance_creation(self):
        self.assertIsInstance(self.state_instance, State)
        self.assertTrue(hasattr(self.state_instance, 'id'))
        self.assertTrue(hasattr(self.state_instance, 'created_at'))
        self.assertTrue(hasattr(self.state_instance, 'updated_at'))
        self.assertTrue(hasattr(self.state_instance, 'name'))

    def test_state_string_representation(self):
        state_string_representation = str(self.state_instance)
        self.assertIn("[State]", state_string_representation)
        self.assertIn("id", state_string_representation)
        self.assertIn("created_at", state_string_representation)
        self.assertIn("updated_at", state_string_representation)
        self.assertIn("name", state_string_representation)

    def test_state_to_dict_conversion(self):
        state_dict_representation = self.state_instance.to_dict()
        self.assertIsInstance(state_dict_representation, dict)
        self.assertEqual(state_dict_representation['__class__'], 'State')
        self.assertIn('id', state_dict_representation)
        self.assertIn('created_at', state_dict_representation)
        self.assertIn('updated_at', state_dict_representation)
        self.assertIn('name', state_dict_representation)


if __name__ == '__main__':
    unittest.main()

