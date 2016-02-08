# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import debug

from pov.basic.BlockObject import BlockObject
from pov.basic.Vector import Vector
from pov.object_modifier.ObjectModifier import ObjectModifier
from pov.other.SdlSyntaxException import SdlSyntaxException


class Cone(BlockObject):
    """
    Cone object.

    CONE:
        cone
        {
            <Base_Point>, Base_Radius, <Cap_Point>, Cap_Radius
            [ open ][OBJECT_MODIFIERS...]
        }
    """

    def __init__(
            self, basepoint, baseradius, cappoint, capradius, *opts, **kwargs
    ):
        """
        Construct a cone object.

        @param basepoint: Base point of cone
        @type  basepoint: Vector
        @param baseradius: Base radius of cone
        @type  baseradius: Float
        @param cappoint: Cap point of cone
        @type  cappoint: Vector
        @param capradius: Cap radius of cone
        @type  capradius: Float

        @Todo: use Syntax Checking Methods (See juliaFractal)
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
        if type(baseradius) not in (int, float):
            raise SdlSyntaxException(
                'Param base radius is not of type int or float'
            )
        if not isinstance(cappoint, Vector):
            raise SdlSyntaxException(
                'Parameter cappoint is not of type Vector'
            )
        if not len(cappoint) == 3:
            raise SdlSyntaxException(
                'Cap point Vector has more or less than 3 dimensions'
            )
        if type(capradius) not in (int, float):
            raise SdlSyntaxException(
                'Param cap radius is not of type int or float'
            )

        # Make sure only valid Object Modifiers are passed
        for i, item in enumerate(opts):
            if not isinstance(item, ObjectModifier):
                raise SdlSyntaxException(
                    'Only ObjectModifier objects may be passed as options'
                )
            debug(i)

        for key, val in kwargs.items():
            if key not in ['open']:
                raise SdlSyntaxException('Invalid keyword: ' + str(key))
            if type(val) != bool:
                raise SdlSyntaxException(
                    'Value of keyword %s is not boolean' % key
                )

        super(Cone, self).__init__(
            "cone",
            (basepoint, baseradius, cappoint, capradius),
            opts, kwargs
        )
