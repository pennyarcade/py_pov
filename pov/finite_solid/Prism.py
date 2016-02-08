# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.
"""

from pov.basic.BlockObject import BlockObject


class Prism(BlockObject):
    """
    Prism Object.

    PRISM:
        prism
        {
            [PRISM_ITEMS...] Height_1, Height_2, Number_Of_Points,
            <Point_1>, <Point_2>, ... <Point_n>
            [ open ] [PRISM_MODIFIERS...]
        }
    PRISM_ITEM:
        linear_spline | quadratic_spline | cubic_spline |
        bezier_spline | linear_sweep | conic_sweep
    PRISM_MODIFIER:
        sturm | OBJECT_MODIFIER

    @Todo: Implement
    @Todo: Syntax Checks
    """
