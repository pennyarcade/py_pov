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

        @todo: Syntax checks
    '''

    def __init__(self, *opts, **kwargs):
        '''
            Create Fog object
        '''
        super(Fog, self).__init__('fog', [], opts, kwargs)
