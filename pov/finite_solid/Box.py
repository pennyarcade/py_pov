# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from FiniteSolid import FiniteSolid
from pov.basic.Vector import Vector
from pov.object_modifier.ObjectModifier import ObjectModifier
from pov.other.SdlSyntaxException import SdlSyntaxException


class Box(FiniteSolid):
    """
        BOX:
            box
            {
                <Corner_1>, <Corner_2>
                [OBJECT_MODIFIERS...]
            }

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

    """
    def __init__(self, v1, v2, *opts, **kwargs):
        """
            Construct a box object

            @param v1: vertex of box
            @type v1: Vector()
            @param v2: opposing vertex of box
            @type v2: Vector()
        """

        # Syntax checking
        if not isinstance(v1, Vector):
            raise SdlSyntaxException('Parameter v1 not of type Vector')
        if not len(v1.v) == 3:
            raise SdlSyntaxException('Vector v1 has more or less than 3 dimensions')
        if not isinstance(v2, Vector):
            raise SdlSyntaxException('Parameter v2 not of type Vector')
        if not len(v2.v) == 3:
            raise SdlSyntaxException('Vector v2 has more or less than 3 dimensions')

        # make sure only valid object modifiers are passed
        for i in range(len(opts)):
            if not isinstance(opts[i], ObjectModifier):
                raise SdlSyntaxException('Only ObjectModifier objects may be passed as options')

        super(Box, self).__init__("box", [v1, v2], opts, kwargs)
