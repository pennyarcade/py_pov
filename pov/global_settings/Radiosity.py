# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import os
from pov.basic.BlockObject import BlockObject


class Radiosity(BlockObject):
    """
        RADIOSITY:
            radiosity { [RADIOSITY_ITEMS] }
        RADIOSITY_ITEMS:
            [adc_bailout FLOAT] &
            [always_sample BOOL] &
            [brightness FLOAT] &
            [count INT] &
            [error_bound FLOAT] &
            [gray_threshold FLOAT] &
            [load_file FILE_NAME] &
            [low_error_factor FLOAT] &
            [max_sample FLOAT] &
            [media BOOL] &
            [minimum_reuse FLOAT] &
            [nearest_count INT] &
            [normal BOOL] &
            [pretrace_end FLOAT] &
            [pretrace_start FLOAT] &
            [recursion_limit INT] &
            [save_file FILE_NAME]

        @Todo: Implement
    """


    def _check_arguments(self):
        '''
            Argument Syntax checks
        '''
        valid_args = ['str']

        self._validate_args(valid_args)

        # param syntax checks
        if not os.path.isfile(self.args[0]):
            raise IOError(
                'No such file: %s%s%s' % (os.getcwd(), os.sep, self.args[0])
            )
        #@TODO: check file type

    def _check_opts(self):
        '''
            Option Syntax checks

            @Todo: get rid of Object Modifier superclass?
        '''
        valid_opts = ['ObjectModifier']

        self._validate_opts(valid_opts)

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks
        '''

        valid_kw = {
            'hf_type': 'str',
            'hierarchy': 'bool',
            'smooth': 'bool',
            'water_level': 'float',
            # Object modifier kw
            'no_shadow': 'bool',
            'no_image': 'bool',
            'no_reflection': 'bool',
            'inverse': 'bool',
            'double_illuminate': 'bool',
            'hollow': 'bool'
        }

        self._validate_kwargs(valid_kw)

        valid_types = [
            'gif', 'tga', 'pot', 'png', 'pgm',
            'ppm', 'jpeg', 'tiff', 'sys', 'function'
        ]
        self._checkKwargValue('hf_type', valid_types)
