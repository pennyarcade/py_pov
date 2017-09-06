# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import os
from pov.other.SdlSyntaxException import SdlSyntaxException
from pov.object_modifier.ObjectModifier import ObjectModifier


class Scale(ObjectModifier):
    """
    scale VECTOR.

    @Todo: ApiDoc
    """

    def __init__(self, svector):
        """Create Scale object."""
        super(Scale, self).__init__('scale', [svector], [], [])

    def _check_arguments(self):
        """
        Argument Syntax checks.

        @Todo: ApiDoc
        """
        valid_args = ['Vector']
        self._validate_args(valid_args)

        # param syntax checks
        if not len(self.args[0]) == 3:
            raise SdlSyntaxException(
                'Vector SVector has more or less than 3 dimensions'
            )

    def __str__(self):
        """@Todo: DocString."""
        code = ''
        code += "  " * self.indentation.get() + self.name + ' '
        code += str(self.args[0]) + os.linesep
        return code
