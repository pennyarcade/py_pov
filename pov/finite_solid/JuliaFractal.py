# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from FiniteSolid import *
from pov.basic.Vector import *


class JuliaFractal(FiniteSolid):
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

            @TODO: Param Syntax checking
            @TODO: make sure superclass constructor gets all params in the right form
            @todo test __str__
        '''

        # param syntax checks
        if not isinstance(param4d, Vector):
            raise SdlSyntaxException('Parameter param4d not of type Vector')
        if not len(param4d.v) == 4:
            raise SdlSyntaxException('Vector param4d has more or less than 4 dimensions')

        # make sure only valid object modifiers are passed
        for i in range(len(opts)):
            if not isinstance(opts[i], ObjectModifier):
                raise SdlSyntaxException('Only ObjectModifier objects may be passed as options')

        # kwargs syntax checking
        for key, val in kwargs.items():
            # allowed keywords
            if not key in ['quaternion', 'hypercomplex', 'sqr', 'cube', '']:
                raise SdlSyntaxException('Invalid key: ' + str(key))

        super(JuliaFractal, self).__init__("julia_fractal", (param4d), opts, **kwargs)
