# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import unittest

from pov.basic.SceneItem import SceneItem
from pov.other.Camera import Camera
from pov.other.LightSource import LightSource


class CameraTestCase(unittest.TestCase):
    """Test Camera class."""

    def setUp(self):
        """Setup test environment."""
        self.sut = Camera()

    def test_creation(self):
        """Test creation of Camera object."""
        self.assertIsInstance(self.sut, Camera)
        self.assertIsInstance(self.sut, SceneItem)


class LightSourceTestCase(unittest.TestCase):
    """Test LightSource class."""

    def setUp(self):
        """Setup test environment."""
        self.sut = LightSource((1, 2, 3))

    def test_creation(self):
        """Test creation of LightSource object."""
        self.assertIsInstance(self.sut, LightSource)
        self.assertIsInstance(self.sut, SceneItem)
