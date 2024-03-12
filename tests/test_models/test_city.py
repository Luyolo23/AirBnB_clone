#!/usr/bin/python3

import unittest
from models import City
from datetime import datetime
import os


class TestCityModel(unittest.TestCase):
    def setUp(self):
        self.city_instance = City()

    def tearDown(self):
        del self.city_instance

    def test_city_instance_creation(self):
        self.assertIsInstance(self.city_instance, City)
        self.assertTrue(hasattr(self.city_instance, 'id'))
        self.assertTrue(hasattr(self.city_instance, 'created_at'))
        self.assertTrue(hasattr(self.city_instance, 'updated_at'))
        self.assertTrue(hasattr(self.city_instance, 'state_id'))
        self.assertTrue(hasattr(self.city_instance, 'name'))

    def test_city_string_representation(self):
        string_representation = str(self.city_instance)
        self.assertIn("[City]", string_representation)
        self.assertIn("id", string_representation)
        self.assertIn("created_at", string_representation)
        self.assertIn("updated_at", string_representation)
        self.assertIn("state_id", string_representation)
        self.assertIn("name", string_representation)

    def test_city_to_dict_conversion(self):
        city_dict = self.city_instance.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)


if __name__ == '__main__':
    unittest.main()

