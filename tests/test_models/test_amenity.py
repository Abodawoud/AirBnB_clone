#!/usr/bin/python3
"""Unittest for Amenity
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """unittest_Amenity"""

    def test_attributes(self):
        """test for Amenity attributes"""

        my_model = Amenity()

        self.assertEqual(my_model.name, '')
