#!/usr/bin/python3
"""Unittest for BaseModel
"""


import unittest
from datetime import datetime

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """unittest_BaseModel"""

    def test_storage(self):
        """test for storage"""

        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]

        try:
            with open("file.json", "r", encoding='utf-8') as f:
                self.assertIsInstance(all_objs, dict)
                self.assertIsInstance(obj, BaseModel)
                val = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
                self.assertEqual(str(obj), val)
                self.assertEqual(f"{obj_id}",
                                 f"{obj.__class__.__name__}.{obj.id}")
        except FileNotFoundError:
            self.assertIsInstance(all_objs, dict)
            self.assertEqual(all_objs, {})

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
