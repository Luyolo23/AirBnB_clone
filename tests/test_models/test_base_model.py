#!/usr/bin/python3

import unittest
from datetime import datetime
from models import BaseModel
from models import storage

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.base_model = BaseModel()

    def test_init(self):
        """Test the initialization of a BaseModel instance."""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        """Test the string representation of a BaseModel instance."""
        expected_str = "[BaseModel] ({}) {{}}".format(self.base_model.id)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        """Test the save method of a BaseModel instance."""
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, initial_updated_at)
        self.assertIn(self.base_model, storage.all().values())

    def test_to_dict(self):
        """Test the to_dict method of a BaseModel instance."""
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)
        self.assertNotIn('name', base_model_dict)
        self.assertNotIn('my_number', base_model_dict)
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

