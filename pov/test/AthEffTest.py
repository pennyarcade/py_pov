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
from logging import *

from ..atmeff.AthEff import AthEff
from ..basic import *


class AthEffTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = AthEff('foo')
        pass

    #@unittest.skip
    def test_creation(self):
        self.assertIsInstance(self.SUT, AthEff)
        self.assertIsInstance(self.SUT, SceneItem)
