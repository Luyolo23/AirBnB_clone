#!/usr/bin/python3

import os
import unittest
from models import Amenity
from datetime import datetime


class TestAmenityModel(unittest.TestCase):
    def setUp(self):
        self.amenity_instance = Amenity()

    def tearDown(self):
        del self.amenity_instance

    def test_amenity_instance_creation(self):
        self.assertIsInstance(self.amenity_instance, Amenity)
        self.assertTrue(hasattr(self.amenity_instance, 'id'))
        self.assertTrue(hasattr(self.amenity_instance, 'created_at'))
        self.assertTrue(hasattr(self.amenity_instance, 'updated_at'))
        self.assertTrue(hasattr(self.amenity_instance, 'name'))

    def test_amenity_string_representation(self):
        string_representation = str(self.amenity_instance)
        self.assertIn("[Amenity]", string_representation)
        self.assertIn("id", string_representation)
        self.assertIn("created_at", string_representation)
        self.assertIn("updated_at", string_representation)
        self.assertIn("name", string_representation)

    def test_amenity_to_dict_conversion(self):
        amenity_dict = self.amenity_instance.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertIn('name', amenity_dict)


if __name__ == '__main__':
    unittest.main()

