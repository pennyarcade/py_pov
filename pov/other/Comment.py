# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import os
from logging import debug
from pov.basic.SceneItem import SceneItem


class Comment(SceneItem):
    """
         /* Comment */

         @Todo: Implement
    """

    def __init__(self, comment):
        '''
            Create comment object
        '''
        super(Comment, self).__init__('', [comment], [], [])

    def __str__(self):
        """
            return PoV code as string representation

            this method is meant to be overridden in subclasses
        """
        debug("%s: SceneItem.__str__(): %s, %s, %s" %
              (self.__class__.__name__, self.name, self.args, self.opts))

        return '/*' + str(self.args[0]) + "*/" + os.linesep
