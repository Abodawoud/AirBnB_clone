#!/usr/bin/python3
"""Unittest for BaseModel
"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """unittest_BaseModel"""

    def test_types(self):
        """test for types"""

        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.name, str)
        self.assertIsInstance(my_model.__class__.__name__, str)
        self.assertEqual(my_model.__class__.__name__, 'BaseModel')
        self.assertIsInstance(my_model.my_number, int)

        my_model_json = my_model.to_dict()

        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertIsInstance(my_model_json['id'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['name'], str)
        self.assertIsInstance(my_model_json['__class__'], str)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertIsInstance(my_model_json['my_number'], int)
