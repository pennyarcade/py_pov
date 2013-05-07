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
from pov.basic import SceneItem
from pov.language_directive import *


class LanguageDirectiveTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = LanguageDirective('foo')

    def test_Creation(self):
        self.assertIsInstance(self.SUT, LanguageDirective)
        self.assertIsInstance(self.SUT, SceneItem)

    def test_str(self):
        le = os.linesep
        second = '#foo' + le

        self.assertEqual(str(self.SUT), second)


class IncludeTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Include('test.inc')

    def test_create(self):
        self.assertIsInstance(self.SUT, Include)
        self.assertIsInstance(self.SUT, LanguageDirective)

    def test_str(self):
        le = os.linesep
        second = '#include "test.inc"' + le

        self.assertEqual(str(self.SUT), second)


class VersionTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Version(3.6)

    def test_create(self):
        self.assertIsInstance(self.SUT, Version)
        self.assertIsInstance(self.SUT, LanguageDirective)

    def test_str(self):
        le = os.linesep
        second = '#version 3.6;' + le

        self.assertEqual(str(self.SUT), second)
