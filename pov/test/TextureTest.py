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
from pov.texture import *
from pov.basic import *
from pov.other import *


class FinishTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Finish(Ambient(0.1))

    def test_creation(self):
        self.assertIsInstance(self.SUT, Finish)
        self.assertIsInstance(self.SUT, BlockObject)
        self.assertIsInstance(self.SUT, SceneItem)


class FinishItemTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = FinishItem('foo')

    def test_creation(self):
        self.assertIsInstance(self.SUT, FinishItem)
        self.assertIsInstance(self.SUT, SceneItem)


class AmbientTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Ambient(0.34)

    def test_creation(self):
        self.assertIsInstance(self.SUT, FinishItem)
        self.assertIsInstance(self.SUT, SceneItem)
        self.assertIsInstance(self.SUT, Ambient)

    def test_creation_wrong_param(self):
        try:
            self.SUT[2] = Ambient('baz')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s' % type(e))
        else:
            self.fail('ExpectedException not thrown')

    def test_toString(self):
        le = os.linesep
        first = str(self.SUT)

        second = "ambient 0.34" + le

        self.assertEqual(first, second)


class DiffuseTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Diffuse(0.34)

    def test_creation(self):
        self.assertIsInstance(self.SUT, FinishItem)
        self.assertIsInstance(self.SUT, SceneItem)
        self.assertIsInstance(self.SUT, Diffuse)

    def test_creation_wrong_param(self):
        try:
            self.SUT[2] = Diffuse('baz')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s' % type(e))
        else:
            self.fail('ExpectedException not thrown')

    def test_creation_param_smaller_zero(self):
        try:
            self.SUT[2] = Diffuse(-0.1)
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s' % type(e))
        else:
            self.fail('ExpectedException not thrown')

    def test_creation_param_bigger_one(self):
        try:
            self.SUT[2] = Diffuse(1.1)
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown:' % type(e))
        else:
            self.fail('ExpectedException not thrown')

    def test_toString(self):
        le = os.linesep
        first = str(self.SUT)

        second = "diffusion 0.34" + le

        self.assertEqual(first, second)
