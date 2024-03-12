#!/usr/bin/python3


import unittest
from models import Review
from datetime import datetime
import os
from models.base_model import BaseModel
from tests.test_models.test_base_model import JSON_FILE_PATH


class TestReviewModel(unittest.TestCase):
    def setUp(self):
        self.review_instance = Review()

    def tearDown(self):
        del self.review_instance

    def test_review_instance_creation(self):
        self.assertIsInstance(self.review_instance, Review)
        self.assertTrue(hasattr(self.review_instance, 'id'))
        self.assertTrue(hasattr(self.review_instance, 'created_at'))
        self.assertTrue(hasattr(self.review_instance, 'updated_at'))
        self.assertTrue(hasattr(self.review_instance, 'place_id'))
        self.assertTrue(hasattr(self.review_instance, 'user_id'))
        self.assertTrue(hasattr(self.review_instance, 'text'))

    def test_review_string_representation(self):
        string_representation = str(self.review_instance)
        self.assertIn("[Review]", string_representation)
        self.assertIn("id", string_representation)
        self.assertIn("created_at", string_representation)
        self.assertIn("updated_at", string_representation)
        self.assertIn("place_id", string_representation)
        self.assertIn("user_id", string_representation)
        self.assertIn("text", string_representation)

    def test_review_to_dict_conversion(self):
        review_dict = self.review_instance.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('place_id', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('text', review_dict)


if __name__ == '__main__':
    unittest.main()


"""This module tests the Review model."""


class TestReviewModel(unittest.TestCase):
    """Tests the Review model."""

    __expected_attributes = {
        "place_id": "",
        "user_id": "",
        "text": "",
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
        self.review1 = Review()
        self.review2 = Review()

    def test_presence_of_class_attributes(self) -> None:
        """Tests the presence of the required class attributes."""

        for attribute in self.__expected_attributes:
            self.assertTrue(hasattr(self.review1, attribute))

    def test_save(self) -> None:
        """Tests the inherited `save()` method."""
        Review().save()

        self.assertTrue(os.path.exists(JSON_FILE_PATH))

    def test_unique_objects(self) -> None:
        """Tests to ensure no two instances are the same."""
        self.assertNotEqual(self.review1, self.review2)

    def test_default_class_attribute_values(self) -> None:
        """Tests the default values for the public class attributes."""
        for attribute, value in self.__expected_attributes.items():
            self.assertTrue(getattr(self.review1, attribute) == value)
            self.assertTrue(getattr(self.review2, attribute) == value)

    def test_instance_of_object(self) -> None:
        """Tests the classes the Review model is an instance of."""
        self.assertIsInstance(self.review2, Review)
        self.assertIsInstance(self.review2, BaseModel)

    def test_subclass_of(self) -> None:
        """Tests to ensure Review model objects are sub classes of BaseModel"""
        self.assertTrue(issubclass(self.review1.__class__, BaseModel))
        self.assertTrue(issubclass(self.review2.__class__, BaseModel))
        self.assertTrue(issubclass(Review, BaseModel))

    def test_nonexistent_attribute(self) -> None:
        """Tests for non-existent attribute."""
        self.assertFalse(hasattr(self.review1, "node_string"))

    def test_nonexistent_method(self) -> None:
        """Tests for non-existent method."""
        self.assertFalse(hasattr(self.review1, "op_review()"))
