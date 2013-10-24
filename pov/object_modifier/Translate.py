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


class Translate(ObjectModifier):
    '''
        translate VECTOR
    '''

    def __init__(self, tvector):
        '''
            Create Translate object
        '''

        # Syntax checking
        if not isinstance(tvector, Vector):
            raise SdlSyntaxException('Parameter tvector is not of type Vector')
        if not len(tvector.v) == 3:
            raise SdlSyntaxException('TVector has more or less than 3 dimensions')

        super(Translate, self).__init__('translate', [tvector], [], [])

    def __str__(self):
        code = ''

        code += "  " * self._getIndent() + self.name + ' ' + str(self.args[0]) + os.linesep

        return code
