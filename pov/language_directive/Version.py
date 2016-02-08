# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

Unittests for basic classes
"""

from logging import debug
from pov.language_directive.LanguageDirective import LanguageDirective


class Version(LanguageDirective):
    """
    Version Object.

    VERSION_DIRECTIVE:
        #version FLOAT;
    """

    def __init__(self, version):
        """
        Construct a Version directive.

        @param version: Full name of file to be included
        @type version: float
        """
        super(Version, self).__init__('#version', [version], [], {})

    def __str__(self):
        """Generate PoV source code."""
        code = self._get_line('#' + 'version ' + str(self.args[0]) + ';')
        debug("Version.__str__(): %s\n%s" % (self.args[0], code))
        return code

    def _check_arguments(self):
        """
        Argument Syntax checks.

        to be overwritten in subclasses
        """
        valid_args = ['float']
        self._validate_args(valid_args)
