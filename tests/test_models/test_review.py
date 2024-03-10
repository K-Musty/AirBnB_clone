#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from datetime import datetime
import time
from models.review import Review
import re
from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel

class TestReview(unittest.TestCase):

    """Test Cases for the Review class."""

    k = Review()

    def setUp(self):
        """test for testing Reviews"""
        FileStorage._FileStorage__file_path = "test.json"
        self.rev = Review()
        self.rev.place_id = "666"
        self.rev.user_id = "666"
        self.rev.text = "666"
        self.rev.save()

    def test_atrr_type_review(self):
        """test attribute type for Review"""
        self.assertEqual(type(self.k.place_id), str)
        self.assertEqual(type(self.k.user_id), str)
        self.assertEqual(type(self.k.text), str)

    def test_attribute_place_id(self):
        """ Tests attr """
        self.assertEqual(hasattr(self.k, "place_id"), True)
        self.assertEqual(hasattr(self.k, "user_id"), True)
        self.assertEqual(hasattr(self.k, "text"), True)

    def test_subcls_Review(self):
        """test   subclass  BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)
        self.assertIsInstance(self.rev, Review)

    def test_docstring_Review(self):
        """checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def testpublic(self):
        self.assertEqual(str, type(Review().id))


if __name__ == "__main__":
    unittest.main()
