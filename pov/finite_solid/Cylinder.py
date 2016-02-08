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


class Cylinder(BlockObject):
    """
    Cylinder object.

   CYLINDER:
        cylinder
        {
            <Base_Point>, <Cap_Point>, Radius
            [ open ][OBJECT_MODIFIERS...]
        }
    """
    def __init__(self, basepoint, cappoint, radius, *opts, **kwargs):
        """
        Construct a cylinder Object.

        @param basepoint: Base point of cylinder
        @type  basepoint: Vector
        @param cappoint: Cap point of cylinder
        @type  cappoint: Vector
        @param radius: Radius of cylinder
        @type  radius: Float

        @Todo: Use Syntax checking Methods (See JuliaFractal)
        """
        # Syntax checking
        if not isinstance(basepoint, Vector):
            raise SdlSyntaxException(
                'Parameter basepoint is not of type Vector'
            )
        if not len(basepoint) == 3:
            raise SdlSyntaxException(
                'Base point Vector has more or less than 3 dimensions'
            )
        if not isinstance(cappoint, Vector):
            raise SdlSyntaxException(
                'Parameter cappoint is not of type Vector'
            )
        if not len(cappoint) == 3:
            raise SdlSyntaxException(
                'Cap point Vector has more or less than 3 dimensions'
            )
        if type(radius) not in (int, float):
            raise SdlSyntaxException(
                'Param radius is not of type int or float'
            )

        # Make sure only valid Object Modifiers are passed
        for i in enumerate(opts):
            if not isinstance(opts[i], ObjectModifier):
                raise SdlSyntaxException(
                    'Only ObjectModifier objects may be passed as options'
                )

        for key, val in kwargs.items():
            if key not in ['open']:
                raise SdlSyntaxException('Invalid keyword: ' + str(key))
            if type(val) != bool:
                raise SdlSyntaxException(
                    'Value of keyword %s is not boolean' % key
                )

        super(Cylinder, self).__init__(
            "cylinder",
            (basepoint, cappoint, radius),
            opts, kwargs
        )
