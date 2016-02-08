# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import warn
from pov.basic.BlockObject import BlockObject
from pov.other.SdlSyntaxException import SdlSyntaxException


class Lathe(BlockObject):
    """
    Lathe Object.

    LATHE:
        lathe
        {
            [SPLINE_TYPE] Number_Of_Points, <Point_1>
            <Point_2>... <Point_n>
            [LATHE_MODIFIER...]
        }
    SPLINE_TYPE:
        linear_spline | quadratic_spline | cubic_spline | bezier_spline
    LATHE_MODIFIER:
        sturm | OBJECT_MODIFIER

    @TODO: Implement
    @Todo: Syntax Checks
    """

    def __init__(self, stype, number, points, *opts, **kwargs):
        """
        Construct a Lathe object.

        @Param stype: spline type
        @Type type: String
        @Param type: number of points
        @Type type: Int
        @Param type: points
        @Type type: List of Vector length 3
        """
        super(Lathe, self).__init__(
            "lathe", [stype, number, points], opts, kwargs
        )

    def _check_arguments(self):
        """Argument Syntax checks."""
        valid_args = ['str', 'int', 'Vector']

        warn(self.args)
        self._validate_args(valid_args)

        # param syntax checks
        valid = [
            'linear_spline',
            'quadratic_spline',
            'cubic_spline',
            'bezier_spline'
        ]
        if not self.args[0] in valid:
            raise SdlSyntaxException(
                'Invalid value for param stype got %s expected %s'
                % (self.args[0], valid)
            )

        if not self.args[1] > 0:
            raise SdlSyntaxException(
                'Invalid value for param number: got %s expected > 0'
                % (self.args[1])
            )

        for idx in range(2, len(self.args)):
            if not self.args[idx].__class__.__name__ == 'Vector':
                raise SdlSyntaxException(
                    ''.join([
                        'Invalid value for param points expected elements ',
                        'of type Vector but got %s'
                    ]) % (self.args[2].__class__.__name__)
                )

    def _check_opts(self):
        """
        Option Syntax checks.

        @Todo: get rid of Object Modifier superclass?
        """
        valid_opts = ['ObjectModifier']

        self._validate_opts(valid_opts)

    def _check_kwargs(self):
        """
        Keyword Argument Syntax checks.

        @Todo: Finish syntax checks
        """
        valid_kw = {
            'points': 'Vector',
            'sturm': 'bool',
            # Object modifier kw
            'no_shadow': 'bool',
            'no_image': 'bool',
            'no_reflection': 'bool',
            'inverse': 'bool',
            'double_illuminate': 'bool',
            'hollow': 'bool'
        }

        self._validate_kwargs(valid_kw)
