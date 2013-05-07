# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.SceneItem import *


class GlobalSettings(SceneItem):
    """
        GLOBAL_SETTINGS:
            global_settings { GLOBAL_SETTING_ITEMS }
        GLOBAL_SETTING_ITEMS:
            [adc_bailout FLOAT] &
            [ambient_light COLOR] &
            [assumed_gamma FLOAT] &
            [hf_gray_16 [BOOL]] &
            [irid_wavelength COLOR] &
            [charset GLOBAL_CHARSET] &
            [max_intersections INT] &
            [max_trace_level INT] &
            [number_of_waves INT] &
            [noise_generator NG_TYPE] &
            [RADIOSITY] &
            [PHOTONS]
        GLOBAL_CHARSET:
            ascii | utf8 | sys
        NG_TYPE:
            1 | 2 | 3
    """
    def __init__(self, arg):
        #super(GlobalSettings, self).__init__()
        #self.arg = arg
        pass
