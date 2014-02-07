# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.csg.Csg import Csg


class Intersection(Csg):
    """
        INTERSECTION:
            intersection { SOLID_OBJECT SOLID_OBJECT... [INTERSECTION_MODIFIERS] }
        SOLID_OBJECT:
            FINITE_SOLID_OBJECT | INFINITE_SOLID_OBJECT | ISOSURFACE | CSG_OBJECT
        INTERSECTION_MODIFIERS:
            [cutaway_textures] & [OBJECT_MODIFIERS]
         @Todo: Implement
    """

    def __init__(self, *opts, **kwargs):
        '''
            Create Intersection object
        '''
        super(Intersection, self).__init__('intersection', [], opts, kwargs)
