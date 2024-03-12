#!/usr/bin/python3

import unittest
from models import Place
from datetime import datetime
import os


class TestPlaceModel(unittest.TestCase):
    def setUp(self):
        self.place_instance = Place()

    def tearDown(self):
        del self.place_instance

    def test_place_instance_creation(self):
        self.assertIsInstance(self.place_instance, Place)
        self.assertTrue(hasattr(self.place_instance, 'id'))
        self.assertTrue(hasattr(self.place_instance, 'created_at'))
        self.assertTrue(hasattr(self.place_instance, 'updated_at'))
        self.assertTrue(hasattr(self.place_instance, 'city_id'))
        self.assertTrue(hasattr(self.place_instance, 'user_id'))
        self.assertTrue(hasattr(self.place_instance, 'name'))
        self.assertTrue(hasattr(self.place_instance, 'description'))
        self.assertTrue(hasattr(self.place_instance, 'number_rooms'))
        self.assertTrue(hasattr(self.place_instance, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place_instance, 'max_guest'))
        self.assertTrue(hasattr(self.place_instance, 'price_by_night'))
        self.assertTrue(hasattr(self.place_instance, 'latitude'))
        self.assertTrue(hasattr(self.place_instance, 'longitude'))
        self.assertTrue(hasattr(self.place_instance, 'amenity_ids'))

    def test_place_string_representation(self):
        string_representation = str(self.place_instance)
        self.assertIn("[Place]", string_representation)
        self.assertIn("id", string_representation)
        self.assertIn("created_at", string_representation)
        self.assertIn("updated_at", string_representation)
        self.assertIn("city_id", string_representation)
        self.assertIn("user_id", string_representation)
        self.assertIn("name", string_representation)
        self.assertIn("description", string_representation)
        self.assertIn("number_rooms", string_representation)
        self.assertIn("number_bathrooms", string_representation)
        self.assertIn("max_guest", string_representation)
        self.assertIn("price_by_night", string_representation)
        self.assertIn("latitude", string_representation)
        self.assertIn("longitude", string_representation)
        self.assertIn("amenity_ids", string_representation)

    def test_place_to_dict_conversion(self):
        place_dict = self.place_instance.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)


if __name__ == '__main__':
    unittest.main()

