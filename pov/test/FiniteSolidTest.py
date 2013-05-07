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

from pov.basic.PoVObject import *
from pov.basic.Vector import *
from pov.object_modifier.ObjectModifier import *

from pov.finite_solid import *


class BlobTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Blob()

    def test_create(self):
        self.assertIsInstance(self.SUT, Blob)
        self.assertIsInstance(self.SUT, SceneItem)

        le = os.linesep
        second = 'blob' + le + '  {' + le + '  }' + le

        self.assertEqual(str(self.SUT), second)


class BoxTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Box(Vector(1, 2, 3), Vector(4, 5, 6))

    def test_create(self):
        self.assertIsInstance(self.SUT, Box)
        self.assertIsInstance(self.SUT, SceneItem)

        le = os.linesep
        second = 'box' + le + '  {' + le
        second += '  <1, 2, 3>, <4, 5, 6>' + le + '  }' + le

        self.assertEqual(
            str(self.SUT),
            second
        )

    def test_createWithOption(self):
        SUT = Box(Vector(1, 2, 3), Vector(4, 5, 6), ObjectModifier('foo'))

        self.assertIsInstance(SUT, Box)
        self.assertIsInstance(SUT, SceneItem)


class ConeTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Cone(
            Vector(1, 2, 3),
            4,
            Vector(5, 6, 7),
            8
        )

    def test_creation(self):
        self.assertIsInstance(self.SUT, Cone)
        self.assertIsInstance(self.SUT, SceneItem)

        le = os.linesep
        second = 'cone' + le + '  {' + le
        second += '  <1, 2, 3>, 4, <5, 6, 7>, 8' + le + '  }' + le

        self.assertEqual(
            str(self.SUT),
            second
        )

    def test_creationWithOptionAndKwarg(self):
        SUT = Cone(
            Vector(1, 2, 3),
            4,
            Vector(5, 6, 7),
            8,
            ObjectModifier('foo'),
            open=True
        )

        self.assertIsInstance(SUT, Cone)
        self.assertIsInstance(SUT, SceneItem)


class CylinderTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Cylinder(
            Vector(1, 2, 3),
            Vector(5, 6, 7),
            8
        )

    def test_creation(self):
        self.assertIsInstance(self.SUT, Cylinder)
        self.assertIsInstance(self.SUT, SceneItem)

        le = os.linesep
        second = 'cylinder' + le + '  {' + le
        second += '  <1, 2, 3>, <5, 6, 7>, 8' + le + '  }' + le

        self.assertEqual(
            str(self.SUT),
            second
        )

    def test_creationWithOptionAndKwarg(self):
        SUT = Cylinder(
            Vector(1, 2, 3),
            Vector(5, 6, 7),
            8,
            ObjectModifier('foo'),
            open=True
        )

        self.assertIsInstance(SUT, Cylinder)
        self.assertIsInstance(SUT, SceneItem)


class HeightFieldTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = HeightField('foo.gif')

    def test_creation(self):
        self.assertIsInstance(self.SUT, HeightField)
        self.assertIsInstance(self.SUT, SceneItem)


class JuliaFractalTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = JuliaFractal((1, 2, 3, 4))

    def test_creation(self):
        self.assertIsInstance(self.SUT, JuliaFractal)
        self.assertIsInstance(self.SUT, SceneItem)
