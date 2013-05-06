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


class Box(FiniteSolid):
    """
        BOX:
            box
            {
                <Corner_1>, <Corner_2>
                [OBJECT_MODIFIERS...]
            }
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
        assert isinstance(v1, Vector)
        assert len(v1.v) == 3
        assert isinstance(v2, Vector)
        assert len(v2.v) == 3
        # TODO: make sure only valid object modifiers are passed
        for i in range(len(opts)):
            assert isinstance(opts[i], ObjectModifier)

        super(Box, self).__init__("box", (v1, v2), opts, **kwargs)
