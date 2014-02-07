# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import os
from pov.basic.Vector import Vector
from pov.other.SdlSyntaxException import SdlSyntaxException
from pov.object_modifier.ObjectModifier import ObjectModifier


class Matrix(ObjectModifier):
    '''
        MATRIX:
            matrix < F_VAL00, F_VAL01, F_VAL02, F_VAL10, F_VAL11, F_VAL12, F_VAL20, F_VAL21, F_VAL22, F_VAL30, F_VAL31, F_VAL32 >
    '''

    def __init__(self, rvector):
        '''
            Create Matrix object
        '''

        super(Matrix, self).__init__('matrix', [rvector], [], [])

    def _check_arguments(self):
        '''
            Argument Syntax checks
        '''
        valid_args = ['Vector']

        self._validate_args(valid_args)

        # param syntax checks
        if not len(self.args[0].v) == 12:
            raise SdlSyntaxException('Vector RVector has more or less than 12 dimensions')

    def __str__(self):
        code = ''

        code += "  " * self._getIndent() + self.name + ' ' + str(self.args[0]) + os.linesep

        return code

