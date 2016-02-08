# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from pov.basic.BlockObject import BlockObject


class FinitePatch(BlockObject):
    """
    Finite Patch object.

    FINITE_PATCH_OBJECT:
        BICUBIC_PATCH | DISC | MESH | MESH2 | POLYGON | TRIANGLE |
        SMOOTH_TRIANGLE

    @TODO: Implement
    @Todo: Deprecate initePatch Superclass
    """
