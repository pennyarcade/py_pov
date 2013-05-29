# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from pov.basic.BlockObject import BlockObject
from pov.other.SdlSyntaxException import SdlSyntaxException


class JuliaFractal(BlockObject):
    '''
        JULIA_FRACTAL:
            julia_fractal
            {
                <4D_Julia_Parameter>
                [JF_ITEM...]
                [OBJECT_MODIFIER...]
            }
        JF_ITEM:
            ALGEBRA_TYPE | FUNCTION_TYPE | max_iteration Count |
            precision Amt | slice <4D_Normal>, Distance
        ALGEBRA_TYPE:
            quaternion | hypercomplex
        FUNCTION_TYPE:
            QUATERNATION:
                 sqr | cube
            HYPERCOMPLEX:
                 sqr | cube | exp | reciprocal | sin | asin | sinh |
                 asinh | cos | acos | cosh | acosh | tan | atan |tanh |
                 atanh | ln | pwr( X_Val, Y_Val )
    '''
    def __init__(self, param4d, *opts, **kwargs):
        '''
            Construct a Julia Fractal object

            @Param param4d: four dimensional vector
            @Type param4d: Vector

            @todo test __str__
        '''
        super(JuliaFractal, self).__init__("julia_fractal", [param4d], opts, kwargs)

    def _check_arguments(self):
        '''
            Argument Syntax checks
        '''
        valid_args = ['Vector']

        self._validate_args(valid_args)

        # param syntax checks
        if not len(self.args[0].v) == 4:
            raise SdlSyntaxException('Vector param4d has more or less than 4 dimensions')

    def _check_opts(self):
        '''
            Option Syntax checks

            @Todo: get rid of Object Modifier superclass?
        '''
        valid_opts = ['ObjectModifier']

        self._validate_opts(valid_opts)

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks
        '''

        valid_kw = {
            'algebra_type': 'string',
            'function_type': 'string',
            'max_iteration': 'int',
            'precision': 'float',
            'slice': 'list',
            # Object modifier kw
            'no_shadow': 'bool',
            'no_image': 'bool',
            'no_reflection': 'bool',
            'inverse': 'bool',
            'double_illuminate': 'bool',
            'hollow': 'bool'
        }

        self._validate_kwargs(valid_kw)

        algebra_type = ['quaternion', 'hypercomplex']
        function_type = ['sqr', 'cube', 'exp', 'reciprocal', 'sin', 'asin',
                         'sinh', 'asinh', 'cos', 'acos', 'cosh', 'acosh', 'tan',
                         'atan', 'tanh', 'atanh', 'ln', 'pwr']
