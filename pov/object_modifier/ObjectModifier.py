# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

Unittests File
"""

from pov.basic.SceneItem import SceneItem


class ObjectModifier(SceneItem):
    """
    ObjectModifier Object.

    OBJECT_MODIFIERS:
        [OBJECT_PHOTONS] |
        [CLIPPED_BY] |
        [BOUNDED_BY] |
        [MATERIAL] |
        [INTERIOR] |
        [INTERIOR_TEXTURE] |
        [TEXTURE] |
        [PIGMENT] |
        [NORMAL] |
        [FINISH] |
        [TRANSFORMATION...] |
        [no_shadow] |
        [no_image[BOOL]] |
        [no_reflection{BOOL]] |
        [inverse] |
        [double_illuminate[BOOL]] |
        [hollow [BOOL]]

    OBJECT_PHOTONS:
        photons { OBJECT_PHOTON_ITEMS }

    @Todo: Implement subclasses
    """
