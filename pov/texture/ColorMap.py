# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import BlockObject
from pov.other.SdlSyntaxException import SdlSyntaxException


class ColorMap(BlockObject):
    '''
        COLOR_MAP:
            color_map { COLOR_MAP_BODY } [BLEND_MAP_MODIFIERS] |
            colour_map { COLOR_MAP_BODY } [BLEND_MAP_MODIFIERS]

        COLOR_MAP_BODY:
            COLOR_MAP_IDENTIFIER | COLOR_MAP_ENTRY...
            There may be from 2 to 256 map entries.

        COLOR_MAP_ENTRY:
            [ FLOAT COLOR ]
            The brackets here are part of the map entry.
    '''

    def __init__(self, map, *opts, **kwargs):
        '''
            Create ColorMap object
        '''
        super(ColorMap, self).__init__('color_map', [map], opts, kwargs)


class ColourMap(ColorMap):
    '''
        COLOR_MAP:
            color_map { COLOR_MAP_BODY } [BLEND_MAP_MODIFIERS] |
            colour_map { COLOR_MAP_BODY } [BLEND_MAP_MODIFIERS]

        COLOR_MAP_BODY:
            COLOR_MAP_IDENTIFIER | COLOR_MAP_ENTRY...
            There may be from 2 to 256 map entries.

        COLOR_MAP_ENTRY:
            [ FLOAT COLOR ]
            The brackets here are part of the map entry.
    '''

    def __init__(self, map, *opts, **kwargs):
        '''
            Create ColorMap object
        '''
        super(ColorMap, self).__init__('colour_map', [map], opts, kwargs)