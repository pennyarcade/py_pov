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
from logging import *
from pov.object_modifier.Translate import Translate
from pov.object_modifier.ObjectModifier import ObjectModifier
from pov.basic.Vector import Vector
from pov.other.SdlSyntaxException import SdlSyntaxException


class TranslateTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Translate(Vector(1, 2, 3))

    def test_Creation(self):
        self.assertIsInstance(self.SUT, Translate)
        self.assertIsInstance(self.SUT, ObjectModifier)

    def test_str(self):
        second = 'translate <1, 2, 3>' + os.linesep
        self.assertEqual(str(self.SUT), second)

    def test_create_arg_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of Argument 0 is expectet to be type Vector but got str'):
            Translate('foo')

    def test_create_arg_wrong_length_vector(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Vector TVector has more or less than 4 dimensions'):
            Translate(Vector(1, 2, 3, 4))
