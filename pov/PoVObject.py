# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from basic.SceneItem import *
from basic.Vector import *


class PoVObject(SceneItem):
    """
        OBJECT:
            FINITE_SOLID_OBJECT | FINITE_PATCH_OBJECT |
            INFINITE_SOLID_OBJECT | ISOSURFACE_OBJECT | PARAMETRIC_OBJECT |
            CSG_OBJECT | LIGHT_SOURCE |
            object { OBJECT_IDENTIFIER [OBJECT_MODIFIERS...] }
    """

    def __str__(self):
        """
            return PoV code as string representation
        """
        debug("Item.__str__ %s, %s, %s", self.name, self.args, self.opts)

        code = ""
        code += self._getBeginCode()
        for opt in self.opts:
            code += self._getLine(str(opt))
        code += self._getEndCode()
        return code

    def _getBeginCode(self):
        """
            Start block of code
        """
        code = self.name + os.linesep + self._block_begin()
        if self.args:
            code = code + self._getLine(", ".join([str(arg) for arg in self.args]))
        return code

    def _getEndCode(self):
        """
            End block of code
        """
        code = ""
        for key, val in self.kwargs.items():
            code += self._getLine("%s %s" % (key, val))
        code += self._block_end()
        return code


class FinitePatch(PoVObject):
    """
        FINITE_PATCH_OBJECT:
            BICUBIC_PATCH | DISC | MESH | MESH2 | POLYGON | TRIANGLE |
            SMOOTH_TRIANGLE
    """


class IsoSurface(PoVObject):
    """
        ISOSURFACE_OBJECT:
            ISOSURFACE
    """


class ParametricObj(PoVObject):
    """
        PARAMETRIC_OBJECT:
            PARAMETRIC
    """


class Object(PoVObject):
    """
         object {
           OBJECT_IDENTIFIER | OBJECT {}
           LIST_ITEM_A, LIST_ITEM_B
         }
    """


class InfiniteSolid(PoVObject):
    """
        INFINITE_SOLID_OBJECT:
            PLANE | POLY | CUBIC | QUARTIC | QUADRIC
    """


class Csg(PoVObject):
    """
        CSG_OBJECT:
            UNION | INTERSECTION | DIFFERENCE | MERGE
    """

