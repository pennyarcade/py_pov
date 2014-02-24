# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import sys
import os
import unittest
import traceback
from logging import *

sys.path.append('../../')

from pov.include.colors_inc import *


class ColorsIncTestCase(unittest.TestCase):
    def test_Red(self):
        self.assertEqual(
            str(Red),
            'rgb <1.0, 0.0, 0.0>'
        )
