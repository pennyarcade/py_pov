# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

#import os
import unittest
#import difflib
#import copy
#import traceback
from logging import *

from pov.basic.SceneItem import *
from pov.other.Camera import *


class CameraTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Camera()

    def test_creation(self):
        self.assertIsInstance(self.SUT, Camera)
        self.assertIsInstance(self.SUT, SceneItem)
