# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import os
from pov.basic.Vector import Vector
from pov.basic.BlockObject import BlockObject
from pov.other.SdlSyntaxException import SdlSyntaxException
from pov.object_modifier.ObjectModifier import ObjectModifier


class ClippedBy(ObjectModifier, BlockObject):
    '''
        CLIPPED_BY:
            clipped_by { UNTEXTURED_SOLID_OBJECT... } |
            clipped_by { bounded_by }
        UNTEXTURED_SOLID_OBJECT:
            FINITE_SOLID_OBJECT | INFINITE_SOLID_OBJECT
            Note, neither with a texture applied.
    '''

    def __init__(self, *opts, **kwargs):
        '''
            Create ClippedBy object
        '''

        super(ClippedBy, self).__init__('clipped_by', [], opts, kwargs)
