#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from datetime import datetime
import time
from models.state import State
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

class TestState(unittest.TestCase):

    """Test Cases for the State class."""
    
    def setUp(self):
        """setting up the
        test for testing States"""
        FileStorage._FileStorage__file_path = "test.json"
        self.state = State()
        self.state.name = "Florida"
        self.state.save()

    def test_docstring_State(self):
        """checks for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_instance_State(self):
        """checks for valid data type"""
        self.assertTrue(type(self.state.name) is str)

    def test_to_dict_State(self):
        """testing dictionary"""
        self.assertEqual('to_dict' in dir(self.state), True)

    def testpublic(self):
        self.assertEqual(str, type(State().id))

    def testHasAttributes(self):
        """verifying attributes existance"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == "__main__":
    unittest.main()
