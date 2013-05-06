# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from FiniteSolid import *
from pov.basic.Vector import *


class HeightField(FiniteSolid):
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
            water_level Level
    '''
    def __init__(self, filename, *opts, **kwargs):
        '''
            Construct a HeightField object

            @TODO: Param Apidoc
            @TODO: Syntax Checking
        '''

        super(HeightField, self).__init__(
            "height_field",
            (filename),
            opts, **kwargs
        )
