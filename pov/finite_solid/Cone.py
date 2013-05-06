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


class Cone(FiniteSolid):
    """
        CONE:
            cone
            {
                <Base_Point>, Base_Radius, <Cap_Point>, Cap_Radius
                [ open ][OBJECT_MODIFIERS...]
            }
    """
    def __init__(self, basepoint, baseradius, cappoint, capradius, *opts, **kwargs):
        """
            Construct a cone object

            @param basepoint: Base point of cone
            @type  basepoint: Vector
            @param baseradius: Base radius of cone
            @type  baseradius: Float
            @param cappoint: Cap point of cone
            @type  cappoint: Vector
            @param capradius: Cap radius of cone
            @type  capradius: Float
        """

        # Syntax checking
        assert isinstance(basepoint, Vector)
        assert len(basepoint.v) == 3
        assert type(baseradius) in (int, float)
        assert isinstance(cappoint, Vector)
        assert len(cappoint.v) == 3
        assert type(capradius) in (int, float)
        # TODO: Make sure only valid Object Modifiers are passed
        for i in range(len(opts)):
            assert isinstance(opts[i], ObjectModifier)
        for key, val in kwargs.items():
            assert key in ['open']
            assert type(val) == bool

        super(Cone, self).__init__(
            "cone",
            (basepoint, baseradius, cappoint, capradius),
            opts, **kwargs
        )

