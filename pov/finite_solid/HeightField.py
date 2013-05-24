# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from pov.other import SdlSyntaxException
from pov.object_modifier.ObjectModifier import *
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
            water_level float
    '''
    def __init__(self, filename, *opts, **kwargs):
        '''
            Construct a HeightField object

            @param filename: Input file name
            @param type: string

            @TODO: Check that file really exists
            @TODO: check if file matches given type
            @TODO: make sure superclass constructor gets all params in the right form
            @TODO: test __str__
        '''

        # param syntax checking
        if not type(filename) == str:
            raise SdlSyntaxException('String expected for param "filename"')

        # make sure only valid object modifiers are passed
        for i in range(len(opts)):
            if not isinstance(opts[i], ObjectModifier):
                raise SdlSyntaxException('Only ObjectModifier objects may be passed as options')

        # kwargs syntax checking
        for key, val in kwargs.items():
            # allowed keywords
            if not key in ['hf_type', 'hierarchy', 'smooth', 'water_level']:
                raise SdlSyntaxException('Invalid key: ' + str(key))

            if (key in ['hierarchy', 'smooth']) and (not type(val) == bool):
                raise SdlSyntaxException('Key %s expected boolean value, got %s', (key, type(val)))
            if (key == 'hf_type') and (not type(val) == str):
                raise SdlSyntaxException('Key %s expected string value, got %s', (key, type(val)))
            if (key == 'hf_type') and (not val in ['gif', 'tga', 'pot', 'png', 'pgm', 'ppm', 'jpeg', 'tiff', 'sys', 'function']):
                raise SdlSyntaxException('Value %s of key %s is not valid' % (val, key))
            if (key == 'water_level') and (not type(val) == float):
                raise SdlSyntaxException('Key %s expected float value, got %s', (key, type(val)))

        # call superclass constructor
        super(HeightField, self).__init__(
            "height_field",
            (filename),
            opts, **kwargs
        )
