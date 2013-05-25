# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.SceneItem import *
from pov.basic.Vector import *


class BlockObject(SceneItem):
    '''
        provides methods to generate code blocks
    '''
    def __str__(self):
        """
            return PoV code as string representation
        """
        debug("BlockObject.__str__ %s, %s, %s", self.name, self.args, self.opts)

        code = ""
        code += self._getBeginCode()
        for opt in self.opts:
            if isinstance(opt, SceneItem):
                code += str(opt)
            else:
                code += self._getLine(str(opt))
        code += self._getEndCode()

        debug("BlockObject.__str__ Code: \n%s", code)

        return code

    def _getBeginCode(self):
        """
            Start block of code
        """
        global indentation

        code = "  " * self._getIndent() + self.name + self._block_begin()
        if self.args:
            code = code + self._getLine(", ".join([str(arg) for arg in self.args]))
        return code

    def _getEndCode(self):
        """
            End block of code
        """
        code = ""

        #debug('kwargs: %s', self.kwargs)
        kwargs = self.kwargs.items()
        #debug('kwargs: %s', kwargs)
        kwargs.reverse()
        #debug('kwargs: %s', kwargs)

        for key, val in kwargs:
            code += self._getLine("%s %s" % (key, val))
        code += self._block_end()
        return code