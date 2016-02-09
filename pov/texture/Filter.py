# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import os
from pov.basic.BlockObject import BlockObject


class Filter(BlockObject):
    """@Todo: Docstring."""

    def __init__(self, color, value, *opts, **kwargs):
        """
        Create Filter object.

        @todo: implement
        @todo: Syntax checks
        """
        super(Filter, self).__init__(
            'filter', [color, value], opts, kwargs
        )

    def __str__(self):
        """@Todo: DocString."""
        code = ''
        code += "  " * self._get_indent() + self.name + ' '
        code += str(self.args[0]) + ' ' + str(self.args[1]) + os.linesep
        return code
