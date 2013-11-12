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

        @todo: How to treat transformations? keyword/object
    '''

    def __init__(self, *opts, **kwargs):
        '''
            Create SkySphere object
        '''
        super(SkySphere, self).__init__('sky_sphere', [], opts, kwargs)

    def _check_arguments(self):
        '''
            Argument Syntax checks
        '''
        valid_args = ['']

        self._validate_args(valid_args)

    def _check_opts(self):
        '''
            Option Syntax checks
        '''
        valid_opts = ['Pigment', 'Transformation']

        self._validate_opts(valid_opts)

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks

            @Todo: Finish syntax checks
        '''

        valid_kw = {}

        self._validate_kwargs(valid_kw)
