# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

Unittests for basic classes

"""

from FinishItem import *


class Diffuse(FinishItem):
    """
        FINISH_ITEMS:
            [diffuse FLOAT]
    """

    def __init__(self, diffusion):
        '''
            Construct a Diffuse directive

            @param diffusion: Full name of file to be included
            @type diffusion: float; 0 < x < 1

        '''
        assert type(diffusion) == float
        assert 0 < diffusion < 1

        self.diffusion = diffusion

    def __str__(self):
        '''
            Generate PoV source code
        '''
        code = self._getLine('diffusion ' + str(self.diffusion))

        info('Diffuse.str(): ' + code)

        return code
