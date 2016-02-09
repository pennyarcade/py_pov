# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

# import os
import unittest
# import difflib
# import copy
# from logging import *

from pov.atmeff.Fog import Fog
from pov.atmeff.SkySphere import SkySphere
from pov.texture.Pigment import Pigment
from pov.basic.Color import Color
from pov.basic.Vector import Vector


class FogTestCase(unittest.TestCase):
    """@Todo: DocString."""

    def setUp(self):
        """@Todo: DocString."""
        self.sut = Fog(Color(rgb=Vector(100, 100, 100)))

    def test_creation(self):
        """@Todo: DocString."""
        self.assertIsInstance(self.sut, Fog)


class SkySphereTestCase(unittest.TestCase):
    """@Todo: DocString."""

    def setUp(self):
        """@Todo: DocString."""
        self.sut = SkySphere(Pigment())

    def test_creation(self):
        """@Todo: DocString."""
        self.assertIsInstance(self.sut, SkySphere)
