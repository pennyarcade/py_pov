# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import unittest
import os
# import logging
from pov.object_modifier.Translate import Translate
from pov.object_modifier.ObjectModifier import ObjectModifier
from pov.basic.Vector import Vector
from pov.other.SdlSyntaxException import SdlSyntaxException


class TranslateTestCase(unittest.TestCase):
    """Test Translate class."""

    def setUp(self):
        """Setup test environment."""
        self.sut = Translate(Vector(1, 2, 3))

    def test_creation(self):
        """Test creation of Translate object."""
        self.assertIsInstance(self.sut, Translate)
        self.assertIsInstance(self.sut, ObjectModifier)

    def test_str(self):
        """Test converting Finish object to string (__str__ magic method)."""
        second = 'translate <1, 2, 3>' + os.linesep
        self.assertEqual(str(self.sut), second)

    def test_create_arg_wrong_type(self):
        """Test creation of Translate object."""
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Value of Argument 0 is expectet to be type Vector but got str'
        ):
            Translate('foo')

    def test_create_wrong_length_vector(self):
        """Test creation of Translate object."""
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Vector TVector has more or less than 3 dimensions'
        ):
            Translate(Vector(1, 2, 3, 4))
