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
from pov.basic.Vector import Vector
from pov.other.SdlSyntaxException import SdlSyntaxException
from pov.object_modifier.ObjectModifier import ObjectModifier


class HeightField(BlockObject):
    '''
        HEIGHT_FIELD:
            height_field{
              [HF_TYPE]
              "filename"
              [HF_MODIFIER...]
              [OBJECT_MODIFIER...]
            }
        HF_TYPE:
            gif | tga | pot | png | pgm | ppm | jpeg | tiff | sys | function
        HF_MODIFIER:
            hierarchy [Boolean]  |
            smooth               |
            water_level float
    '''
    def __init__(self, filename, *opts, **kwargs):
        '''
            Construct a HeightField object

            @param filename: Input file name
            @param type: string

            @TODO: check if file matches given type
        '''

        # call superclass constructor
        super(HeightField, self).__init__(
            "height_field",
            [filename],
            opts,
            kwargs
        )

    def _getBeginCode(self):
        """
            Start block of code
        """
        code = "  " * self._getIndent() + self.name + self._block_begin()
        code = code + self._getLine('"' + str(self.args[0]) + '"')
        return code

    def _check_arguments(self):
        '''
            Argument Syntax checks
        '''
        valid_args = ['str']

        self._validate_args(valid_args)

        # param syntax checks
        if not os.path.isfile(self.args[0]):
            raise IOError('No sutch file: %s%s%s' % (os.getcwd(), os.sep, self.args[0]))
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

        self._checkKwargValue(self, 'hf_type', ['gif', 'tga', 'pot', 'png', 'pgm', 'ppm', 'jpeg', 'tiff', 'sys', 'function'])