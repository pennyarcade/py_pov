# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from pov.basic.BlockObject import BlockObject


class Transformation(BlockObject):
    """
    Transformation Object.

    TRANSFORMATION:
        rotate VECTOR | scale VECTOR | translate VECTOR
                | TRANSFORM | MATRIX
    TRANSFORM:
        transform TRANSFORM_IDENTIFIER | transform { [TRANSFORM_ITEM...] }
    TRANSFORM_ITEM:
        TRANSFORM_IDENTIFIER | TRANSFORMATION | inverse
    """

    def __init__(self, *opts, **kwargs):
        """Create Transformation object."""
        super(Transformation, self).__init__('transformation', opts, kwargs)
