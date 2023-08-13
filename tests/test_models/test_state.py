#!/usr/bin/python3
"""Unittest for State
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """unittest_State"""

    def test_attributes(self):
        """test for State attributes"""

        my_model = State()

        self.assertEqual(my_model.name, '')
