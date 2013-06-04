# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import BlockObject
from pov.other.SdlSyntaxException import SdlSyntaxException


class Plane(BlockObject):
    '''
        PLANE:
            plane { V_NORMAL, F_DISTANCE [OBJECT_MODIFIERS] }
    '''

    def __init__(self, normal, distance, *opts, **kwargs):
        '''
            Create plane object
        '''
        super(Plane, self).__init__('plane', [normal, distance], opts, kwargs)

        if 'hollow' in self.kwargs and self.kwargs['hollow'] is True:
            del self.kwargs['hollow']
            self.opts.append('hollow')
