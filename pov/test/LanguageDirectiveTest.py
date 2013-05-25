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
from pov.basic.Vector import Vector
from pov.language_directive.LanguageDirective import LanguageDirective
from pov.language_directive.Default import Default
from pov.language_directive.Version import Version
from pov.language_directive.Include import Include
from pov.other.SdlSyntaxException import SdlSyntaxException


class LanguageDirectiveTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = LanguageDirective('#foo')

    def test_Creation(self):
        self.assertIsInstance(self.SUT, LanguageDirective)
        self.assertIsInstance(self.SUT, SceneItem)

    def test_str(self):
        le = os.linesep
        second = '#foo'

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

    def test_create_wrong_type(self):
        try:
            self.SUT = Version('foo')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')


class DefaultTestCase(unittest.TestCase):
    def setUp(self):
        debug('---------------------------------')
        self.SUT = Default(ambient=0.43)

    def test_creation(self):
        self.assertIsInstance(self.SUT, Default)
        self.assertIsInstance(self.SUT, LanguageDirective)

    def test_toString(self):
        debug('---------------------------------')
        le = os.linesep
        first = str(self.SUT)
        second = '#default {' + le
        second += '  ambient 0.43' + le
        second += '}' + le

        self.assertEqual(first, second)

