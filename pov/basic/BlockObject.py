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


class BlockObject(SceneItem):
    """provides methods to generate code blocks."""

    def __str__(self):
        """return PoV code as string representation."""
        debug(
            "BlockObject.__str__ %s, %s, %s",
            self.name, self.args, self.opts
        )

        code = ""
        code += self._get_begin_code()
        for opt in self.opts:
            if isinstance(opt, SceneItem):
                code += str(opt)
            else:
                code += self._get_line(str(opt))
        code += self._get_end_code()

        debug("BlockObject.__str__ Code: \n%s", code)

        return code

    def _get_begin_code(self):
        """Start block of code."""
        code = "  " * self._get_indent() + self.name + self._block_begin()
        if self.args:
            code = code + self._get_line(
                ", ".join([str(arg) for arg in self.args])
            )
        return code

    def _get_end_code(self):
        """End block of code."""
        code = ""

        # debug('kwargs: %s', self.kwargs)
        kwargs = self.kwargs.items()
        # debug('kwargs: %s', kwargs)
        kwargs.reverse()
        # debug('kwargs: %s', kwargs)

        for key, val in kwargs:
            if val is True:
                code += self._get_line("%s" % (key))
            else:
                code += self._get_line("%s %s" % (key, str(val).strip()))
        code += self._block_end()
        return code
