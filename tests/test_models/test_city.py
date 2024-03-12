#!/usr/bin/python3

import unittest
from models import City
from datetime import datetime
import os
from models.city import City
from models.base_model import BaseModel
from tests.test_models.test_base_model import JSON_FILE_PATH


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

"""This module tests the City model."""


class TestCityModel(unittest.TestCase):
    """Tests the City model."""

    __expected_attributes = {"state_id": "", "name": ""}

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
        self.city1 = City()
        self.city2 = City()

    def test_presence_of_class_attributes(self) -> None:
        """Tests the presence of the required class attributes."""
        for attribute in self.__expected_attributes:
            self.assertTrue(hasattr(self.city1, attribute))

    def test_save(self) -> None:
        """Tests the inherited `save()` method."""
        City().save()

        self.assertTrue(os.path.exists(JSON_FILE_PATH))

    def test_unique_objects(self) -> None:
        """Tests to ensure no two instances are the same."""
        self.assertNotEqual(self.city1, self.city2)

    def test_default_class_attribute_values(self) -> None:
        """Tests the default values for the public class attributes."""
        for attribute, value in self.__expected_attributes.items():
            self.assertTrue(getattr(self.city1, attribute) == value)
            self.assertTrue(getattr(self.city2, attribute) == value)

    def test_instance_of_object(self) -> None:
        """Tests the classes the City model is an instance of."""
        self.assertIsInstance(self.city2, City)
        self.assertIsInstance(self.city2, BaseModel)

    def test_subclass_of(self) -> None:
        """Tests to ensure City model objects are subclasses of BaseModel"""
        self.assertTrue(issubclass(self.city1.__class__, BaseModel))
        self.assertTrue(issubclass(self.city2.__class__, BaseModel))
        self.assertTrue(issubclass(City, BaseModel))

    def test_nonexistent_attribute(self) -> None:
        """Tests for non-existent attribute."""
        self.assertFalse(hasattr(self.city1, "city_id"))

    def test_nonexistent_method(self) -> None:
        """Tests for non-existent method."""
        self.assertFalse(hasattr(self.city1, "get_city()"))
