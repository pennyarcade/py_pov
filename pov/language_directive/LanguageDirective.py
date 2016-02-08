# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import debug

from pov.basic.SceneItem import SceneItem


class LanguageDirective(SceneItem):
    """
    Language Directive Object.

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

    @Todo: Is this superclass deprecated?
    @Todo: Implement subclasses
    """

    def __init__(self, name, args=None, opts=None, kwargs=None):
        """@Todo: DocString."""
        debug("%s: LanguageDirective.__init__(): %s, %s, %s, %s" %
              (self.__class__.__name__, name, args, opts, kwargs))

        if args is None:
            args = []
        if opts is None:
            opts = []
        if kwargs is None:
            kwargs = []

        super(LanguageDirective, self).__init__(name, args, opts, kwargs)

    def __str__(self):
        """@Todo: DocString."""
        code = super(LanguageDirective, self).__str__()
        debug('%s: LanguageDirective.__str__(): %s\n %s' %
              (self.__class__.__name__, self.name, code))
        return code
