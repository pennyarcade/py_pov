# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import os
from pov.other.SdlSyntaxException import SdlSyntaxException
from pov.object_modifier.ObjectModifier import ObjectModifier


class Rotate(ObjectModifier):
    '''
        rotate VECTOR
    '''

    def __init__(self, rvector):
        '''
            Create Rotate object
        '''

        super(Rotate, self).__init__('rotate', [rvector], [], [])

    def _check_arguments(self):
        '''
            Argument Syntax checks
        '''
        valid_args = ['Vector']

        self._validate_args(valid_args)

        # param syntax checks
        if not len(self.args[0]) == 3:
            raise SdlSyntaxException(
                'Vector RVector has more or less than 4 dimensions'
            )

    def __str__(self):
        code = ''

        code += "  " * self._get_indent() + self.name + ' '
        code += str(self.args[0]) + os.linesep

        return code
