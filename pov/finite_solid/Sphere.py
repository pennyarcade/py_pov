# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import *
from pov.basic.BlockObject import BlockObject
from pov.basic.Vector import Vector
from pov.basic.SceneItem import SceneItem
from pov.object_modifier.ObjectModifier import ObjectModifier
from pov.other.SdlSyntaxException import SdlSyntaxException


class Sphere(BlockObject):
    '''
        SPHERE:
            sphere
            {
                <Center>, Radius
                [OBJECT_MODIFIERS...]
            }

        @Todo: Syntax Checking
    '''

    def __init__(self, center, radius, *opts, **kwargs):
        '''
            Create Sphere object
        '''

        # Syntax checking
        if not isinstance(center, Vector):
            raise SdlSyntaxException('Parameter center is not of type Vector')
        if not len(center.v) == 3:
            raise SdlSyntaxException('Center point Vector has more or less than 3 dimensions')
        if not type(radius) in (int, float):
            raise SdlSyntaxException('Param radius is not of type int or float')

        # Make sure only valid Object Modifiers are passed
        for i in range(len(opts)):
            if not opts[i].__class__.__name__ in self._object_modifiers:
                warn(str(type(opts[i])))
                raise SdlSyntaxException('Only ObjectModifier objects may be passed as options')

        for key, val in kwargs.items():
            if not key in []:
                raise SdlSyntaxException('Invalid key: ' + str(key))
#            if not type(val) == bool:
#                raise SdlSyntaxException('Value of key %s is not boolean', key)

        super(Sphere, self).__init__('sphere', [center, radius], opts, kwargs)
