# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

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
    """Test Default class."""

    def setUp(self):
        """Setup test environment."""
        self.sut = GlobalSettings()

    def test_creation(self):
        """Test creation of Translate object."""
        self.assertIsInstance(self.sut, GlobalSettings)
        self.assertIsInstance(self.sut, SceneItem)

    def test_create_option_wrong_type(self):
        """
        Create GlobalSettings object with wrong type param.

        Expect SdlSyntaxException
        """
        with self.assertRaises(
            SdlSyntaxException,
        ):
            self.sut = GlobalSettings('foo', 'bar')
