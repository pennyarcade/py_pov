# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import os
from pov.basic.SceneItem import SceneItem
from pov.basic.Vector import Vector
from pov.other.SdlSyntaxException import SdlSyntaxException


class Color(SceneItem):
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

        @TODO: enable setting color by passing float options e.g. Color(0.0, 0.2, 0.75)
        @TODO: check syntax of kwargs
    '''

    def __init__(self, *opts, **kwargs):
        '''
            Create Color object

            @Todo: add properties for all color components @see colors_ink.py
        '''
        super(Color, self).__init__('color', [], opts, kwargs)

        if 'rgb' in self.kwargs:
            self.type = 'rgb'
            self.vector = self.kwargs['rgb']
        elif 'rgbt' in kwargs:
            self.type = 'rgbt'
            self.vector = self.kwargs['rgbt']
        elif 'rgbf' in kwargs:
            self.type = 'rgbf'
            self.vector = self.kwargs['rgbf']
        elif 'rgbft' in kwargs:
            self.type = 'rgbft'
            self.vector = self.kwargs['rgbft']
        else:
            # @todo: how to deal with separate color keywords
            self.type = 'none'
            self.vector = Vector(0, 0, 0)
            pass

    def __str__(self):
        code = ''

        if self.type in ['rgb', 'rgbt', 'rgbf', 'rgbft']:
            code += self.type + ' ' + str(self.vector) + os.linesep

        return code

    def __mul__(self, other):
        self.vector *= other
        return self

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
