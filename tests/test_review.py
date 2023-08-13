#!/usr/bin/python3
"""Unittest for Review
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """unittest_Review"""

    def test_attributes(self):
        """test for Review attributes"""

        my_model = Review()

        self.assertEqual(my_model.place_id, '')
        self.assertEqual(my_model.user_id, '')
        self.assertEqual(my_model.text, '')
