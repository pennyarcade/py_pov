# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from pov.basic.BlockObject import *
from pov.basic.SceneItem import *
from pov.basic.Vector import *


class PoVObject(BlockObject):
    """
        OBJECT:
            FINITE_SOLID_OBJECT | FINITE_PATCH_OBJECT |
            INFINITE_SOLID_OBJECT | ISOSURFACE_OBJECT | PARAMETRIC_OBJECT |
            CSG_OBJECT | LIGHT_SOURCE |
            object { OBJECT_IDENTIFIER [OBJECT_MODIFIERS...] }
    """


