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

        assert isinstance(basepoint, Vector)
        assert len(basepoint.v) == 3
        assert isinstance(cappoint, Vector)
        assert len(cappoint.v) == 3
        assert type(radius) in (int, float)
        # TODO: Make sure only valid Object Modifiers are passed
        for i in range(len(opts)):
            assert isinstance(opts[i], ObjectModifier)
        for key, val in kwargs.items():
            assert key in ['open']
            assert type(val) == bool

        super(Cylinder, self).__init__(
            "cylinder",
            (basepoint, cappoint, radius),
            opts, **kwargs
        )

