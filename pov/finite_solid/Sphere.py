# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import *
from pov.basic.BlockObject import BlockObject
from pov.basic.Vector import Vector
from pov.basic.SceneItem import SceneItem
from pov.object_modifier.ObjectModifier import ObjectModifier
from pov.other.SdlSyntaxException import SdlSyntaxException


class Sphere(BlockObject):
    '''
        SPHERE:
            sphere
            {
                <Center>, Radius
                [OBJECT_MODIFIERS...]
            }

    '''

    def __init__(self, center, radius, *opts, **kwargs):
        '''
            Create Sphere object
        '''

        super(Sphere, self).__init__('sphere', [center, radius], opts, kwargs)

    def _check_arguments(self):
        '''
            Argument Syntax checks

            @Todo: How to allow int and float as type
        '''
        valid_args = ['Vector', ('float', 'int')]

        self._validate_args(valid_args)

        # param syntax checks
        if not len(self.args[0].v) == 3:
            raise SdlSyntaxException('Center point Vector has more or less than 3 dimensions')

    def _check_opts(self):
        '''
            Option Syntax checks

            @Todo: get rid of Object Modifier superclass?
        '''
        valid_opts = ['ObjectModifier', 'Texture', 'Translate']

        self._validate_opts(valid_opts)

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks

        '''

        valid_kw = {
            # Object modifier kw
            'no_shadow': 'bool',
            'no_image': 'bool',
            'no_reflection': 'bool',
            'inverse': 'bool',
            'double_illuminate': 'bool',
            'hollow': 'bool'
        }

        self._validate_kwargs(valid_kw)
