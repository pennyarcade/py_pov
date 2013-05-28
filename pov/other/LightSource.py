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


class LightSource(PoVObject):
    '''
        LIGHT:
            LIGHT_SOURCE | LIGHT_GROUP
            Describe the position, type and properties of a light source for the scene:

        LIGHT_SOURCE:
            light_source { V_LOCATION, COLOR [LIGHT_SOURCE_ITEMS] }

        LIGHT_SOURCE_ITEMS:
            [LIGHT_TYPE] & [AREA_LIGHT_ITEMS] & [LIGHT_MODIFIERS]

        LIGHT_TYPE:
            spotlight [SPOTLIGHT_ITEMS] | cylinder [SPOTLIGHT_ITEMS]

        SPOTLIGHT_ITEMS:
            [radius FLOAT] & [falloff FLOAT] & [tightness FLOAT] & [point_at VECTOR]

        AREA_LIGHT_ITEMS:
            area_light V_AXIS1, V_AXIS2, I_SIZE1, I_SIZE2 [AREA_LIGHT_MODIFIERS]

        AREA_LIGHT_MODIFIERS:
            [adaptive INT] & [jitter] & [circular] & [orient]

        LIGHT_MODIFIERS:
            [LIGHT_PHOTONS] & [looks_like { OBJECT }] & [TRANSFORMATION...] & [fade_distance FLOAT] & [fade_power FLOAT] & [media_attenuation [BOOL]] & [media_interaction [BOOL]] & [shadowless] & [projected_through { OBJECT_IDENTIFIER }] & [parallel [point_at VECTOR]]
            Specify how a light source should interact with photons:

        LIGHT_PHOTONS:
            photons { LIGHT_PHOTON_ITEMS }

        LIGHT_PHOTON_ITEMS:
            [refraction BOOL] & [reflection BOOL] & [area_light]
    '''

    def __init__(self, location, *opts, **kwargs):
        '''
            Create camera object
        '''
        super(LightSource, self).__init__('light_source', [location], opts, kwargs)