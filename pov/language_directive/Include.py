# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from LanguageDirective import *


class Include(LanguageDirective):
    """
        INCLUDE_DIRECTIVE:
            #include FILE_NAME
        File inclusion may be nested at most 10 levels deep.

        FILE_NAME:
            STRING
    """
    def __init__(self, filename):
        '''
            Construct an Include statement

            @param filename: Full name of file to be included
            @type filename: string

            @TODO: assert that filename points o a real file
        '''
        self.filename = filename
        #super(Include, self).__init__('include')

    def __str__(self):
        '''
            Generate PoV source code
        '''
        code = self._getLine('#' + 'include \"' + self.filename + '\"')

        return code


