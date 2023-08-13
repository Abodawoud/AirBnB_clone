#!/usr/bin/python3
"""Unittest for City
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """unittest_City"""

    def test_attributes(self):
        """test for City attributes"""

        my_model = City()

        self.assertEqual(my_model.name, '')
        self.assertEqual(my_model.state_id, '')
