# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import sys
# import os
import unittest
# import traceback
# from logging import *

sys.path.append('../../')

# @Todo: translate
import pov.include.colors_inc


class ColorsIncTestCase(unittest.TestCase):
    '''
        Test colors_inc.py
    '''
    def test_red(self):
        '''
            @Todo: DocString
        '''
        self.assertEqual(
            str(colors_inc.RED),
            'rgb <1.0, 0.0, 0.0>'
        )
