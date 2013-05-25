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
from pov.texture.Finish import Finish
from pov.basic.BlockObject import BlockObject
from pov.basic.SceneItem import SceneItem
from pov.other.SdlSyntaxException import SdlSyntaxException


class FinishTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Finish(ambient=0.1, diffuse=0.9)

    def test_creation(self):
        self.assertIsInstance(self.SUT, Finish)
        self.assertIsInstance(self.SUT, BlockObject)
        self.assertIsInstance(self.SUT, SceneItem)

    def test_toString(self):
        le = os.linesep
        first = str(self.SUT)

        second = "finish {" + le
        second += '  ambient 0.1' + le
        second += '  diffuse 0.9' + le
        second += '}' + le

        self.assertEqual(first, second)

