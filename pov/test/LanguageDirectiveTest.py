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
from pov.basic.SceneItem import SceneItem
from pov.language_directive.LanguageDirective import LanguageDirective
from pov.language_directive.Default import Default
from pov.language_directive.Version import Version
from pov.language_directive.Include import Include
from pov.texture.Finish import Finish
from pov.other.SdlSyntaxException import SdlSyntaxException


class LanguageDirectiveTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = LanguageDirective('#foo')

    def test_Creation(self):
        self.assertIsInstance(self.SUT, LanguageDirective)
        self.assertIsInstance(self.SUT, SceneItem)

    def test_str(self):
        second = '#foo'

        self.assertEqual(str(self.SUT), second)


class IncludeTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Include('fixture/test.inc')

    def test_create(self):
        self.assertIsInstance(self.SUT, Include)
        self.assertIsInstance(self.SUT, LanguageDirective)

    def test_str(self):
        le = os.linesep
        second = '#include "fixture/test.inc"' + le

        self.assertEqual(str(self.SUT), second)

    def test_create_non_existant_file(self):
        with self.assertRaisesRegexp(IOError, 'No such file: %s%s%s' % (os.getcwd(), os.sep, 'fixture/nonexistant.inc')):
            self.SUT = Include('fixture/nonexistant.inc')


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

    def test_create_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of Argument 0 is expectet to be type float but got str'):
            self.SUT = Version('foo')


class DefaultTestCase(unittest.TestCase):
    def setUp(self):
        debug('---------------------------------')
        self.SUT = Default(Finish(ambient=0.43))

    def test_creation(self):
        self.assertIsInstance(self.SUT, Default)
        self.assertIsInstance(self.SUT, LanguageDirective)

    def test_toString(self):
        debug('---------------------------------')
        le = os.linesep
        first = str(self.SUT)
        second = '#default {' + le
        second += '  finish {' + le
        second += '    ambient 0.43' + le
        second += '  }' + le
        second += '}' + le

        self.assertEqual(first, second)
