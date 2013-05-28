# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.PoVObject import PoVObject
from pov.global_settings.Radiosity import Radiosity
from pov.global_settings.Photons import Photons
from pov.other.SdlSyntaxException import SdlSyntaxException


class GlobalSettings(PoVObject):
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
    def __init__(self, *opts, **kwargs):
        '''
            Construct a GlobalSettings object

            @Todo: test __str__
            @Todo: check there are no valid params??
        '''

        super(GlobalSettings, self).__init__("global_settings", [], opts, kwargs)

    def _check_opts(self):
        '''
            Option Syntax checks

            @Todo: generalize checks
        '''
        for i in range(len(self.opts)):
            if not (isinstance(opts[i], Radiosity) or isinstance(opts[i], Photons)):
                raise SdlSyntaxException('Only Radiosity or Photons objects may be passed as options')

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks

            @Todo: how to check values in a generalized way?
        '''

        valid_kw = {
            'ambient_light': 'Color',
            'assumed_gamma': 'float',
            'hf_gray_16': 'bool',
            'irid_wavelength': 'Color',
            'charset': 'string',
            'max_intersections': 'int',
            'max_trace_level': 'int',
            'number_of_waves': 'int',
            'noise_generator': 'int'
        }

        self._validate_kwargs(valid_kw)
