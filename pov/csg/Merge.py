# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.csg.Csg import Csg


class Merge(Csg):
    """
    Merge object.

    merge { SOLID_OBJECT SOLID_OBJECT... [OBJECT_MODIFIERS] }
    @Todo: Implement
    """

    def __init__(self, *opts, **kwargs):
        """Create Merge object."""
        super(Merge, self).__init__('merge', [], opts, kwargs)
