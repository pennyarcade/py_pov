# coding=UTF-8
"""
    Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

    based on:
    PyPov-0.0.X Copyright (c) Simon Burton, 2003
    See LICENSE file.

    Some modifications by W.T. Bridgman, 2006-2007.

"""

import unittest
# import traceback
# from logging import *
from pov.basic.SceneItem import SceneItem
from pov.global_settings.GlobalSettings import GlobalSettings
from pov.other.SdlSyntaxException import SdlSyntaxException


class GlobalSettingsTestCase(unittest.TestCase):
    """
        @Todo: DocString
    """
    def setUp(self):
        """
            @Todo: DocString
        """
        self.sut = GlobalSettings()

    def test_creation(self):
        """
            @Todo: DocString
        """
        self.assertIsInstance(self.sut, GlobalSettings)
        self.assertIsInstance(self.sut, SceneItem)

    def test_create_Option_wrong_type(self):
        """
            @Todo: DocString
        """
        with self.assertRaises(
            SdlSyntaxException,
        ):
            self.sut = GlobalSettings('foo', 'bar')

