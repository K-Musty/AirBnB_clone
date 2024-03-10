#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel

class Test_Amenity(unittest.TestCase):
    """ Test for
    Amenity Class """

    examplee = Amenity()

    def setUp(self):
        """set up the
        test for testing amenities auto"""
        FileStorage._FileStorage__file_path = "test.json"
        self.amenity = Amenity()
        self.amenity.name = "remarkable"
        self.amenity.save()

    def test_class_existance(self):
        """tests if class exists or null"""
        result = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.examplee)), result)

    def testpublic(self):
        self.assertEqual(str, type(Amenity().id))

    def test_instance_User(self):
        """ Test subclasses of BaseModel """
        self.assertIsInstance(self.examplee, Amenity)

    def test_atrr_type_Amenity(self):
        """test attributes of type for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    def test_attribute_name(self):
        """ Checks for  name """
        self.assertEqual(hasattr(self.examplee, "name"), True)

    def test_types(self):
        """ test for types """
        self.assertEqual(type(self.examplee.name), str)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.examplee, 'name'))
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.examplee, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

