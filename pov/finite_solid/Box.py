# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from pov.basic.BlockObject import BlockObject
from pov.basic.Vector import Vector
from pov.object_modifier.ObjectModifier import ObjectModifier
from pov.other.SdlSyntaxException import SdlSyntaxException


class Box(BlockObject):
    """
    Box object.

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

    def __init__(self, vector1, vector2, *opts, **kwargs):
        """
        Construct a box object.

        @param vector1: vertex of box
        @type vector1: Vector()
        @param vector2: opposing vertex of box
        @type vector2: Vector()

        @Todo: Use Syntax checking Methods (See JuliaFractal)
        """
        # Syntax checking
        if not isinstance(vector1, Vector):
            raise SdlSyntaxException('Parameter v1 not of type Vector')
        if not len(vector1) == 3:
            raise SdlSyntaxException(
                'Vector v1 has more or less than 3 dimensions'
            )
        if not isinstance(vector2, Vector):
            raise SdlSyntaxException('Parameter v2 not of type Vector')
        if not len(vector2) == 3:
            raise SdlSyntaxException(
                'Vector v2 has more or less than 3 dimensions'
            )

        # make sure only valid object modifiers are passed
        for i, item in enumerate(opts):
            if not isinstance(opts[i], ObjectModifier):
                raise SdlSyntaxException(
                    'Only ObjectModifier objects may be passed as options'
                )

        super(Box, self).__init__("box", [vector1, vector2], opts, kwargs)
