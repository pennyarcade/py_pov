# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import unittest
from logging import *
from pov.infinite_solid.Plane import Plane
from pov.basic.SceneItem import SceneItem


class PlaneTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Plane(
            (1, 2, 3),
            4,
            hollow=True
        )

    def test_creation(self):
        self.assertIsInstance(self.SUT, Plane)
        self.assertIsInstance(self.SUT, SceneItem)
