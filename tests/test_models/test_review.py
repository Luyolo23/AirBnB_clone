#!/usr/bin/python3

import unittest
from models import Review
from datetime import datetime
import os


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

