# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.PoVObject import PoVObject
from pov.other.SdlSyntaxException import SdlSyntaxException


class Color(PoVObject):
    '''
        Color Expressions

        COLOR:
            [color] COLOR_BODY | colour COLOR_BODY

        COLOR_BODY:
            COLOR_VECTOR | COLOR_KEYWORD_GROUP | COLOR_IDENTIFIER

        COLOR_VECTOR:
            rgb 3D_VECTOR | rgbf 4D_VECTOR | rgbt 4D_VECTOR | [rgbft] 5D_VECTOR

        COLOR_KEYWORD_GROUP:
            [COLOR_IDENTIFIER] COLOR_KEYWORD_ITEMS

        COLOR_KEYWORD_ITEMS:
            [red FLOAT] & [green FLOAT] & [blue FLOAT] & [filter FLOAT] & [transmit FLOAT]
    '''

    def __init__(self, *opts, **kwargs):
        '''
            Create Color object
        '''
        super(Color, self).__init__('color', [], opts, kwargs)

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks
        '''

        valid_kw = {
            'rgb':  'Vector',
            'rgbf': 'Vector',
            'rgbt': 'Vector',
            'rgbft': 'Vector',
            'red': 'float',
            'green': 'float',
            'blue': 'float',
            'filter': 'float',
            'transmit': 'float'
        }

        self._validate_kwargs(valid_kw)

#-------------------------------------------------------------------
# Color Definitions
#-------------------------------------------------------------------

White = Color()
