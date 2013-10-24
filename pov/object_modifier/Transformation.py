# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from pov.basic.BlockObject import BlockObject
from pov.basic.Vector import Vector
from pov.object_modifier.ObjectModifier import ObjectModifier
from pov.other.SdlSyntaxException import SdlSyntaxException


class Transformation(BlockObject):
    '''
        TRANSFORMATION:
            rotate VECTOR | scale VECTOR | translate VECTOR | TRANSFORM | MATRIX
        TRANSFORM:
            transform TRANSFORM_IDENTIFIER | transform { [TRANSFORM_ITEM...] }
        TRANSFORM_ITEM:
            TRANSFORM_IDENTIFIER | TRANSFORMATION | inverse
        MATRIX:
            matrix < F_VAL00, F_VAL01, F_VAL02, F_VAL10, F_VAL11, F_VAL12, F_VAL20, F_VAL21, F_VAL22, F_VAL30, F_VAL31, F_VAL32 >
    '''

    def __init__(self, *opts, **kwargs):
        '''
            Create Transformation object
        '''

        super(Transformation, self).__init__('transformation', opts, kwargs)
