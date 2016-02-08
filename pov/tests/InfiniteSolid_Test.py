# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import unittest
# from logging import debug
from pov.infinite_solid.Plane import Plane
from pov.basic.SceneItem import SceneItem
from pov.other.SdlSyntaxException import SdlSyntaxException


class PlaneTestCase(unittest.TestCase):
    """
        Test Plane class
    """
    def setUp(self):
        self.sut = Plane(
            (1, 2, 3),
            4,
            hollow=True
        )

    def test_creation(self):
        """
            Test creation and inheritance of object
        """
        self.assertIsInstance(self.sut, Plane)
        self.assertIsInstance(self.sut, SceneItem)

    def test_creation_vector_to_big(self):
        """
            Test vector parameter
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Normal vector has more or less than 3 dimensions'
        ):
            self.sut = Plane((1, 2, 3, 4), 5)
