# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from pov.basic.BlockObject import BlockObject
from pov.basic.Vector import Vector


class Lathe(BlockObject):
    '''
        LATHE:
            lathe
            {
                [SPLINE_TYPE] Number_Of_Points, <Point_1>
                <Point_2>... <Point_n>
                [LATHE_MODIFIER...]
            }
        SPLINE_TYPE:
            linear_spline | quadratic_spline | cubic_spline | bezier_spline
        LATHE_MODIFIER:
            sturm | OBJECT_MODIFIER

        @TODO: Implement
    '''
