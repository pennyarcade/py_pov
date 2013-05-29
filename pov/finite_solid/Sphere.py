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


class Sphere(BlockObject):
    '''
        SPHERE:
            sphere
            {
                <Center>, Radius
                [OBJECT_MODIFIERS...]
            }
    '''

    def __init__(self, center, radius, *opts, **kwargs):
        '''
            Create Sphere object
        '''
        super(Sphere, self).__init__('sphere', [center, radius], opts, kwargs)
