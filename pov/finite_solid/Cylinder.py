# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from FiniteSolid import *
from pov.basic.Vector import *
from pov.object_modifier.ObjectModifier import *

class Cylinder(FiniteSolid):
    """
       CYLINDER:
            cylinder
            {
                <Base_Point>, <Cap_Point>, Radius
                [ open ][OBJECT_MODIFIERS...]
            }
    """
    def __init__(self, basepoint, cappoint, radius, *opts, **kwargs):
        """
            Construct a cylinder Object

            @param basepoint: Base point of cylinder
            @type  basepoint: Vector
            @param cappoint: Cap point of cylinder
            @type  cappoint: Vector
            @param radius: Radius of cylinder
            @type  radius: Float
        """

        # Syntax checking
        if not isinstance(basepoint, Vector):
            raise SdlSyntaxException('Parameter basepoint is not of type Vector')
        if not len(basepoint.v) == 3:
            raise SdlSyntaxException('Base point Vector has more or less than 3 dimensions')
        if not isinstance(cappoint, Vector):
            raise SdlSyntaxException('Parameter cappoint is not of type Vector')
        if not len(cappoint.v) == 3:
            raise SdlSyntaxException('Cap point Vector has more or less than 3 dimensions')
        if not type(radius) in (int, float):
            raise SdlSyntaxException('Param radius is not of type int or float')

        # Make sure only valid Object Modifiers are passed
        for i in range(len(opts)):
            if not isinstance(opts[i], ObjectModifier):
                raise SdlSyntaxException('Only ObjectModifier objects may be passed as options')

        for key, val in kwargs.items():
            if not key in ['open']:
                raise SdlSyntaxException('Invalid key: ' + str(key))
            if not type(val) == bool:
                raise SdlSyntaxException('Value of key %s is not boolean', key)

        super(Cylinder, self).__init__(
            "cylinder",
            (basepoint, cappoint, radius),
            opts, **kwargs
        )

