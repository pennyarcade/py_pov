# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import os
import unittest
#import difflib
#import copy
from logging import *
from pov.basic import *
from pov.other import SdlSyntaxException
from pov.global_settings import *


class GlobalSettingsTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = GlobalSettings()

    def test_creation(self):
        self.assertIsInstance(self.SUT, GlobalSettings)
        self.assertIsInstance(self.SUT, SceneItem)


class AssumedGammaTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = AssumedGamma(0.75)

    def test_creation(self):
        self.assertIsInstance(self.SUT, GlobalSettingsItem)
        self.assertIsInstance(self.SUT, SceneItem)
        self.assertIsInstance(self.SUT, AssumedGamma)

    def test_toString(self):
        le = os.linesep
        first = str(self.SUT)
        second = 'assumed_gamma 0.75' + le
        self.assertEqual(first, second)

    def test_create_wrong_type(self):
        try:
            self.SUT = AssumedGamma('foo')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')
