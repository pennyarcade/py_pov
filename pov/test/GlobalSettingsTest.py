# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import unittest
import traceback
from logging import *
from pov.basic.SceneItem import SceneItem
from pov.global_settings.GlobalSettings import GlobalSettings
from pov.other.SdlSyntaxException import SdlSyntaxException


class GlobalSettingsTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = GlobalSettings()

    def test_creation(self):
        self.assertIsInstance(self.SUT, GlobalSettings)
        self.assertIsInstance(self.SUT, SceneItem)

    def test_create_Option_wrong_type(self):
        try:
            self.SUT = GlobalSettings('foo', 'bar')
        except SdlSyntaxException as e:
            if not str(e) == 'Invalid option type str not in allowed opts \n[\'Radiosity\', \'Photons\']':
                self.fail('SdlSyntaxException with wrong message: %s' % str(e))
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')
