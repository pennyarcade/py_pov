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


class EmptyObject(SceneItem):
    """
    Empty object.

    does nothing, placeholder to prevent type mixups

     @Todo: Implement
    """

    def __init__(self):
        """Create empty object."""
        super(EmptyObject, self).__init__('', [], [], [])

    def __str__(self):
        """
        return PoV code as string representation.

        i.e. an empty string
        """
        debug("%s: SceneItem.__str__(): %s, %s, %s" %
              (self.__class__.__name__, self.name, self.args, self.opts))

        return ''
