# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from pov.basic.BlockObject import *
from pov.basic.Vector import *


class Blob(BlockObject):
    """
        BLOB:
            blob { BLOB_ITEM... [BLOB_MODIFIERS...]}
        BLOB_ITEM:
            sphere{<Center>, Radius,
                   [ strength ] Strength[COMPONENT_MODIFIER...] } |
            cylinder{<End1>, <End2>, Radius,
                     [ strength ] Strength [COMPONENT_MODIFIER...] } |
            component Strength, Radius, <Center> |
            threshold Amount
        COMPONENT_MODIFIER:
            TEXTURE | PIGMENT | NORMAL | FINISH | TRANSFORMATION
        BLOB_MODIFIER:
            hierarchy [Boolean] | sturm [Boolean] | OBJECT_MODIFIER
    """

    def __init__(self, opts=[], **kwargs):
        """
            Create a Blob Object

            @TODO: How to deal with Comopnent Modifiers?
        """

        super(Blob, self).__init__("blob", [], opts, kwargs)

    def _check_arguments(self):
        '''
            Argument Syntax checks
        '''
        valid_args = ['']

        self._validate_args(valid_args)

    def _check_opts(self):
        '''
            Option Syntax checks

            @Todo: get rid of Object Modifier superclass?
        '''
        valid_opts = ['Sphere', 'Cylinder', 'Component', 'ObjectModifier']

        self._validate_opts(valid_opts)

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks
        '''

        valid_kw = {
            'threshold': 'float',
            'hierarchy': 'bool',
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
