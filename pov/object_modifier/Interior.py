# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from pov.object_modifier.ObjectModifier import ObjectModifier


class Interior(ObjectModifier):
    """interior VECTOR."""

    def __init__(self, *opts, **kwargs):
        """Create Interior object."""
        super(Interior, self).__init__('interior', [], opts, kwargs)

#    def _check_arguments(self):
#        """
#            Argument Syntax checks
#        """
#        valid_args = ['Vector']
#
#        self._validate_args(valid_args)
#
#        # param syntax checks
#        if not len(self.args[0].v) == 3:
#            raise SdlSyntaxException(
#                'Vector SVector has more or less than 3 dimensions')

#    def __str__(self):
#        code = ''
#
#        code += "  " * self._getIndent() + self.name + ' '
#        code += str(self.args[0]) + os.linesep
#
#        return code
