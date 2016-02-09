# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import sys
import os
import unittest

sys.path.append('../../')

from pov.include import colors_inc


class ColorsIncTestCase(unittest.TestCase):
    """Test colors_inc.py."""

    def test_red(self):
        """Test a random color definition."""
        self.assertEqual(
            str(colors_inc.RED),
            'color rgb <1, 0, 0>' + os.linesep
        )
