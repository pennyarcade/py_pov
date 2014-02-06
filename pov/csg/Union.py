# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import *


class Union(Csg):
    """
        UNION:
            union { UNION_OBJECT UNION_OBJECT... [UNION_MODIFIERS] }
        UNION_OBJECT:
            OBJECT | LIGHT
        UNION_MODIFIERS:
            [split_union BOOL] & [OBJECT_MODIFIERS]
         @Todo: Implement
    """
