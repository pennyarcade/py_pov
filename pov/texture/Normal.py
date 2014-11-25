# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import BlockObject


class Normal(BlockObject):
    '''
        NORMAL:
            normal { NORMAL_BODY }

            NORMAL_BODY:
                [NORMAL_IDENTIFIER] [NORMAL_TYPE] [NORMAL_MODIFIERS]

            NORMAL_TYPE:
                NORMAL_PATTERN | BUMP_MAP

            NORMAL_PATTERN:
                NORMAL_LIST_PATTERN |
                MAP_PATTERN [F_DEPTH] [SLOPE_MAP] |
                MAP_PATTERN NORMAL_MAP

            NORMAL_LIST_PATTERN:
                brick NORMAL, NORMAL [BRICK_ITEMS]
                    | brick [F_DEPTH] [BRICK_ITEMS] |
                checker NORMAL, NORMAL | checker [F_DEPTH] |
                hexagon NORMAL, NORMAL, NORMAL | hexagon [F_DEPTH] |
                object { LIST_OBJECT NORMAL, NORMAL }
                    | object { LIST_OBJECT } [F_DEPTH]

            NORMAL_MAP:
                normal_map { NORMAL_MAP_BODY } [BLEND_MAP_MODIFIERS]

            NORMAL_MAP_BODY:
                NORMAL_MAP_IDENTIFIER | NORMAL_MAP_ENTRY...
                There may be from 2 to 256 map entries.

                NORMAL_MAP_ENTRY:
                    [ FLOAT NORMAL_BODY ]
                    The brackets here are part of the map entry.

            SLOPE_MAP:
                slope_map { SLOPE_MAP_BODY } [BLEND_MAP_MODIFIERS]

                SLOPE_MAP_BODY:
                    SLOPE_MAP_IDENTIFIER | SLOPE_MAP_ENTRY...
                    There may be from 2 to 256 map entries.

                SLOPE_MAP_ENTRY:
                    [ FLOAT, < F_HEIGHT, F_SLOPE > ]
                    The brackets here are part of the map entry.

            BUMP_MAP:
                bump_map { BITMAP_IMAGE [BUMP_MAP_MODIFIERS] }

                BUMP_MAP_MODIFIERS:
                [BITMAP_MODIFIERS] & [BUMP_METHOD] & [bump_size FLOAT]

                BUMP_METHOD:
                    use_index | use_color | use_colour

            NORMAL_MODIFIERS:
                [PATTERN_MODIFIERS] & [bump_size FLOAT] &
                [no_bump_scale [BOOL]] & [accuracy FLOAT]
    '''

    def __init__(self, *opts, **kwargs):
        '''
            Create Normal object

            @todo: implement
            @todo: Syntax checks
        '''
        super(Normal, self).__init__('normal', [], opts, kwargs)

        if 'bumps' in self.kwargs:
            self.args.append('bumps %s' % self.kwargs['bumps'])
            del self.kwargs['bumps']
