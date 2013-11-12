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


class Fog(PoVObject):
    '''
        FOG:
            CONSTANT_FOG | GROUND_FOG

            CONSTANT_FOG:
                fog { [FOG_IDENTIFIER] [fog_type 1] FOG_ITEMS }

            FOG_ITEMS:
                distance FLOAT & COLOR & [TURBULENCE [turb_depth FLOAT]]

            GROUND_FOG:
                fog { [FOG_IDENTIFIER] fog_type 2 GROUND_FOG_ITEMS }

            GROUND_FOG_ITEMS:
                FOG_ITEMS & fog_offset FLOAT & fog_alt FLOAT &
                [up VECTOR [TRANSFORMATION...]]

    '''

    def __init__(self, *opts, **kwargs):
        '''
            Create Fog object
        '''
        super(Fog, self).__init__('fog', [], opts, kwargs)

    def _check_arguments(self):
        '''
            Argument Syntax checks
        '''
        valid_args = []

        self._validate_args(valid_args)

    def _check_opts(self):
        '''
            Option Syntax checks
        '''
        valid_opts = ['Color', 'Turbulence', 'Transformation']

        self._validate_opts(valid_opts)

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks

            @Todo: How to treat transformation kwargs/objects?
        '''

        valid_kw = {
            'distance': ('float', 'int'),
            'turb_depth': ('float', 'int'),
            'fog_type': 'int',
            'fog_offset': ('float', 'int'),
            'fog_alt': ('float', 'int'),
            'inverse': 'bool',
            'up': 'Vector'
        }

        self._validate_kwargs(valid_kw)

        self._checkKwargValue('fog_type', (1, 2))
