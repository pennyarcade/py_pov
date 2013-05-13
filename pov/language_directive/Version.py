# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

Unittests for basic classes

"""

from LanguageDirective import *


class Version(LanguageDirective):
    """
        VERSION_DIRECTIVE:
            #version FLOAT;
    """

    def __init__(self, version):
        '''
            Construct a Version directive

            @param version: Full name of file to be included
            @type version: float

        '''
        if not type(version) == float:
            raise SdlSyntaxException('Parameter not of type float')
        self.version = version

    def __str__(self):
        '''
            Generate PoV source code
        '''
        code = self._getLine('#' + 'version ' + str(self.version) + ';')

        info ('Version.str(): ' + code)

        return code
