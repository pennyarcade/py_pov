# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""
'''
from pov import *

#import os
import unittest
#import difflib
#import copy
from logging import *

warn(str(dir()))
#warn(str(dir(pov)))
warn(str(dir(pov.ath_fx)))

'''
'''
class AthEff(SceneItem):
    """
        ATMOSPHERIC_EFFECT:
            MEDIA |
            BACKGROUND |
            FOG |
            SKY_SPHERE |
            RAINBOW
    """
'''

'''
class AthEffTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = AthEff('foo')

    def test_creation(self):
        self.assertIsInstance(self.SUT, AthEff)
        self.assertIsInstance(self.SUT, SceneItem)
'''