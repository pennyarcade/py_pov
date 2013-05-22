# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import *
from pov.basic.SceneItem import *


class LanguageDirective(SceneItem):
    """
        LANGUAGE_DIRECTIVE:
            INCLUDE_DIRECTIVE |
            IDENTIFIER_DECLARATION |
            UNDEF_DIRECTIVE |
            FOPEN_DIRECTIVE |
            FCLOSE_DIRECTIVE |
            READ_DIRECTIVE |
            WRITE_DIRECTIVE |
            DEFAULT_DIRECTIVE |
            VERSION_DIRECTIVE |
            IF_DIRECTIVE |
            IFDEF_DIRECTIVE |
            IFNDEF_DIRECTIVE |
            SWITCH_DIRECTIVE |
            WHILE_DIRECTIVE |
            TEXT_STREAM_DIRECTIVE |
            MACRO_DEFINITION
    """
    def __init__(self, name, args=[], opts=[], kwargs=[]):
        debug('LanguageDirective.__init__: %s' % name)
        super(LanguageDirective, self).__init__(name, [], opts, kwargs)

    def __str__(self):
        code = super(LanguageDirective, self).__str__()
        debug('LanguageDirective.__str__: %s\n %s' % (self.name, code))
        return code

