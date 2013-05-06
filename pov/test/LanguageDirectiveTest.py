# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import unittest
from pov.language_directive.LanguageDirective import *


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
