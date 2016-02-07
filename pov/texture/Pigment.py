# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Toennishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import BlockObject


class Pigment(BlockObject):
    """
    Pigment Object.

    PIGMENT:
        pigment { PIGMENT_BODY }

        PIGMENT_BODY:
            [PIGMENT_IDENTIFIER] [PIGMENT_TYPE] [PIGMENT_MODIFIERS]

        PIGMENT_TYPE:
            COLOR | COLOR_LIST_PATTERN | PIGMENT_LIST_PATTERN |
            IMAGE_MAP | MAP_PATTERN [COLOR_MAP] | MAP_PATTERN PIGMENT_MAP

        COLOR_LIST_PATTERN:
            brick [COLOR [, COLOR]] [BRICK_ITEMS] |
            checker [COLOR [, COLOR]] |
            hexagon [COLOR [, COLOR [, COLOR]]] |
            object { LIST_OBJECT [COLOR [, COLOR]] }

        PIGMENT_LIST_PATTERN:
            brick PIGMENT, PIGMENT [BRICK_ITEMS] |
            checker PIGMENT, PIGMENT |
            hexagon PIGMENT, PIGMENT, PIGMENT |
            object { LIST_OBJECT PIGMENT, PIGMENT }

        IMAGE_MAP:
            image_map {BITMAP_IMAGE [IMAGE_MAP_MODIFIER...]
                [BITMAP_MODIFIERS] }

        IMAGE_MAP_MODIFIER:
            filter I_PALETTE, F_AMOUNT | filter all F_AMOUNT |
            transmit I_PALETTE, F_AMOUNT | transmit all F_AMOUNT

        COLOR_MAP:
            color_map { COLOR_MAP_BODY } [BLEND_MAP_MODIFIERS] |
            colour_map { COLOR_MAP_BODY } [BLEND_MAP_MODIFIERS]

        COLOR_MAP_BODY:
            COLOR_MAP_IDENTIFIER | COLOR_MAP_ENTRY...
            There may be from 2 to 256 map entries.

        COLOR_MAP_ENTRY:
            [ FLOAT COLOR ]
            The brackets here are part of the map entry.

        PIGMENT_MAP:
            pigment_map { PIGMENT_MAP_BODY } [BLEND_MAP_MODIFIERS]

        PIGMENT_MAP_BODY:
            PIGMENT_MAP_IDENTIFIER | PIGMENT_MAP_ENTRY...
            There may be from 2 to 256 map entries.

        PIGMENT_MAP_ENTRY:
            [ FLOAT PIGMENT_BODY ]
            The brackets here are part of the map entry.

        PIGMENT_MODIFIERS:
            [QUICK_COLOR] & [PATTERN_MODIFIERS]

        QUICK_COLOR:
            quick_color COLOR | quick_colour COLOR
    """

    def __init__(self, *opts, **kwargs):
        """
        Create Pigment object.

        @todo: Syntax checks
        """
        super(Pigment, self).__init__('pigment', [], opts, kwargs)

        if 'bozo' in self.kwargs and self.kwargs['bozo'] is True:
            del self.kwargs['bozo']
            self.args.append('bozo')

        if 'checker' in self.kwargs and self.kwargs['checker'] is True:
            del self.kwargs['checker']
            self.args.append('checker')
