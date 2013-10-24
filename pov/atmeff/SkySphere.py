# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.PoVObject import PoVObject
from pov.other.SdlSyntaxException import SdlSyntaxException


class SkySphere(PoVObject):
    '''
        SKY_SPHERE:
            sky_sphere { [SKY_SPHERE_IDENTIFIER] [SKY_SPHERE_ITEM...] }
        SKY_SPHERE_ITEM:
            PIGMENT | TRANSFORMATION
    '''

    def __init__(self, *opts, **kwargs):
        '''
            Create SkySphere object
            @todo: Syntax checks
        '''
        super(SkySphere, self).__init__('sky_sphere', [], opts, kwargs)
