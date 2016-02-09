# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import os
import unittest
from pov.texture.ColorMap import ColorMap
from pov.texture.ColorMap import ColourMap
from pov.texture.Normal import Normal
from pov.texture.Pigment import Pigment
from pov.texture.Texture import Texture
from pov.texture.Finish import Finish
from pov.basic.BlockObject import BlockObject
from pov.basic.SceneItem import SceneItem
from pov.basic.Color import Color
from pov.basic.Vector import Vector


class FinishTestCase(unittest.TestCase):
    """Test Finish class."""

    def setUp(self):
        """Setup test environment."""
        self.sut = Finish(ambient=0.1, diffuse=0.9)

    def test_creation(self):
        """Test creation of Finish object."""
        self.assertIsInstance(self.sut, Finish)
        self.assertIsInstance(self.sut, BlockObject)
        self.assertIsInstance(self.sut, SceneItem)

    def test_to_string(self):
        """Test converting Finish object to string (__str__ magic method)."""
        lsp = os.linesep
        first = str(self.sut)

        second = "finish {" + lsp
        second += '  ambient 0.1' + lsp
        second += '  diffuse 0.9' + lsp
        second += '}' + lsp

        self.assertEqual(first, second)


class ColorMapTestCase(unittest.TestCase):
    """Test Colormap class."""

    def setUp(self):
        """Setup test environment."""
        self.sut = ColorMap({0.3: Color(rgb=Vector(0.1, 0.2, 0.3))})

    def test_creation(self):
        """Test creation of Colormap object."""
        self.assertIsInstance(self.sut, ColorMap)
        self.assertIsInstance(self.sut, BlockObject)
        self.assertIsInstance(self.sut, SceneItem)

    def test_creation_british(self):
        """Test creation of Colourmap object."""
        self.sut = ColourMap({'foo': 'bar'})
        self.assertIsInstance(self.sut, ColourMap)
        self.assertIsInstance(self.sut, BlockObject)
        self.assertIsInstance(self.sut, SceneItem)

    def test_to_string(self):
        """Test converting Finish object to string (__str__ magic method)."""
        lsp = os.linesep
        first = str(self.sut)
        second = 'color_map {' + lsp
        second += '  [0.3 color rgb <0.1, 0.2, 0.3>]' + lsp
        second += '}' + lsp

        self.assertEqual(first, second)


class NormalTestCase(unittest.TestCase):
    """Test Normal class."""

    def setUp(self):
        """Setup test environment."""
        self.sut = Normal(bumps=0.1, diffuse=0.9)

    def test_creation(self):
        """Test creation of Normal object."""
        self.assertIsInstance(self.sut, Normal)
        self.assertIsInstance(self.sut, BlockObject)
        self.assertIsInstance(self.sut, SceneItem)


class PigmentTestCase(unittest.TestCase):
    """Test Pigment class."""

    def setUp(self):
        """Setup test environment."""
        self.sut = Pigment()

    def test_creation(self):
        """Test creation of Pigment object."""
        self.assertIsInstance(self.sut, Pigment)
        self.assertIsInstance(self.sut, BlockObject)
        self.assertIsInstance(self.sut, SceneItem)


class TextureTestCase(unittest.TestCase):
    """Test Texture class."""

    def setUp(self):
        """Setup test environment."""
        self.sut = Texture()

    def test_creation(self):
        """Test creation of Texture object."""
        self.assertIsInstance(self.sut, Texture)
        self.assertIsInstance(self.sut, BlockObject)
        self.assertIsInstance(self.sut, SceneItem)
