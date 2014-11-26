# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import BlockObject


class Texture(BlockObject):
    '''
        TEXTURE:
            PLAIN_TEXTURE | LAYERED_TEXTURE | PATTERNED_TEXTURE

        PLAIN_TEXTURE:
            texture { PLAIN_TEXTURE_BODY }

            PLAIN_TEXTURE_BODY:
                [PLAIN_TEXTURE_IDENT] [PNF_IDENTIFIERS] [PNF_ITEMS]

            PNF_IDENTIFIERS:
                [PIGMENT_IDENTIFIER] & [NORMAL_IDENTIFIER]
                    & [FINISH_IDENTIFIER]

            PNF_ITEMS:
                [PIGMENT] & [NORMAL] & [FINISH] & [TRANSFORMATION...]

        LAYERED_TEXTURE:
            texture { LAYERED_TEXTURE_IDENT } |
            PLAIN_TEXTURE PLAIN_TEXTURE...

        PATTERNED_TEXTURE:
            texture { PATTERNED_TEXTURE_BODY }

            PATTERNED_TEXTURE_BODY:
                PATTERNED_TEXTURE_IDENT [TRANSFORMATION...]
                    | TEXTURE_PATTERN [PATTERN_MODIFIERS]
                    | MATERIAL_MAP [TRANSFORMATION...]

            TEXTURE_PATTERN:
                TEXTURE_LIST_PATTERN | MAP_PATTERN TEXTURE_MAP

            TEXTURE_LIST_PATTERN:
                brick TEXTURE, TEXTURE [BRICK_ITEMS] |
                checker TEXTURE, TEXTURE |
                hexagon TEXTURE, TEXTURE, TEXTURE |
                object { LIST_OBJECT TEXTURE, TEXTURE }

            BRICK_ITEMS:
                [brick_size VECTOR] & [mortar FLOAT]

            LIST_OBJECT:
                UNTEXTURED_SOLID_OBJECT | UNTEXTURED_SOLID_OBJECT_IDENT

            TEXTURE_MAP:
                texture_map { TEXTURE_MAP_BODY } [BLEND_MAP_MODIFIERS]

            TEXTURE_MAP_BODY:
                TEXTURE_MAP_IDENTIFIER | TEXTURE_MAP_ENTRY...
                There may be from 2 to 256 map entries.

            TEXTURE_MAP_ENTRY:
                [ FLOAT TEXTURE_BODY ]
                The brackets here are part of the map entry.

            TEXTURE_BODY:
                PLAIN_TEXTURE_BODY | LAYERED_TEXTURE_IDENT
                    | PATTERNED_TEXTURE_BODY

            MATERIAL_MAP:
                material_map { BITMAP_IMAGE [BITMAP_MODIFIERS] TEXTURE... }
    '''

    def __init__(self, *opts, **kwargs):
        '''
            Create Texture object

            @Todo: Syntax Checks
        '''
        super(Texture, self).__init__('texture', [], opts, kwargs)
