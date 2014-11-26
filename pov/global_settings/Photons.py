# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import BlockObject


class Photons(BlockObject):
    """
        PHOTONS:
            photons { PHOTON_QUANTITY [PHOTON_ITEMS] }
        PHOTON_QUANTITY:
            spacing FLOAT |
            count INT
        PHOTON_ITEMS:
            [gather I_MIN, I_MAX] &
            [media I_MAX_STEPS [, F_FACTOR]] &
            [jitter FLOAT] &
            [max_trace_level INT] &
            [adc_bailout FLOAT] &
            [save_file FILE_NAME] &
            [load_file FILE_NAME] &
            [autostop FLOAT] &
            [expand_thresholds F_INCREASE, F_MIN] &
            [radius [FLOAT, FLOAT, FLOAT, FLOAT]]
    """

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
        valid_opts = ['Gather', 'Media', 'ExpandThresholds']
        self._validate_opts(valid_opts)

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks
        '''
        valid_kw = {
            'spacing': ('float', 'int'),
            'count': 'int',
            'jitter': ('float', 'int'),
            'max_trace_level': 'int',
            'adc_bailout': ('float', 'int'),
            'save_file': 'str',
            'load_file': 'str',
            'autostop': ('float', 'int'),
            'radius': 'Vector'
        }

        self._validate_kwargs(valid_kw)

        # self._checkKwargValue('hf_type', ['gif', 'tga', 'pot', 'png', 'pgm',
        # 'ppm', 'jpeg', 'tiff', 'sys', 'function'])
