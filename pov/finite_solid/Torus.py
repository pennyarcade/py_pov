# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from pov.basic.BlockObject import BlockObject


class Torus(BlockObject):
    """
    Torus object.

    TORUS:
        torus
        {
            Major, Minor
            [TORUS_MODIFIER...]
        }
    TORUS_MODIFIER:
        sturm | OBJECT_MODIFIER

    @Todo: Implement
    """

    def __init__(self, major, minor, *opts, **kwargs):
        """Create Torus object."""
        super(Torus, self).__init__('torus', [major, minor], opts, kwargs)
