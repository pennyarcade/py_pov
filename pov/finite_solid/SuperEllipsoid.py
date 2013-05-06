# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from FiniteSolid import *
from pov.basic.Vector import *


class SuperEllipsoid(FiniteSolid):
    '''
        SUPERELLIPSOID:
            superellipsoid
            {
                <Value_E, Value_N>
                [OBJECT_MODIFIERS...]
            }
    '''

