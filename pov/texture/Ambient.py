# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

Unittests for basic classes

"""

from FinishItem import FinishItem
from logging import *


class Ambient(FinishItem):
    """
        FINISH_ITEMS:
            [ambient COLOR]
    """

    def __init__(self, ambient):
        '''
            Construct a ambient finish item

            @param ambient: Ambient light float or color vector
            @type ambient: float || color vector

            @TODO: make color vectors possible
        '''
        assert type(ambient) == float
        self.ambient = ambient

        super(Ambient, self).__init__("ambient", [], [])

    def __str__(self):
        '''
            Generate PoV source code
        '''
        code = self._getLine('ambient ' + str(self.ambient))

        info('Ambient.str(): ' + code)

        return code
