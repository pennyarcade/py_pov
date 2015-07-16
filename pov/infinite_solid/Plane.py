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


class Plane(BlockObject):
    '''
        PLANE:
            plane { V_NORMAL, F_DISTANCE [OBJECT_MODIFIERS] }

        @TODO: Syntax checks
    '''

    def __init__(self, normal, distance, *opts, **kwargs):
        '''
            Create plane object
        '''

        super(Plane, self).__init__('plane', [normal, distance], opts, kwargs)

        # @Todo: Generalize handling of boolean keywords
        if 'hollow' in self.kwargs and self.kwargs['hollow'] is True:
            del self.kwargs['hollow']
            self.opts.append('hollow')

    def _check_arguments(self):
        '''
            Argument Syntax checks
        '''
        valid_args = ['Vector', ('float', 'int')]

        self._validate_args(valid_args)

        # param syntax checks
        if not len(self.args[0]) == 3:
            raise SdlSyntaxException(
                'Normal vector has more or less than 3 dimensions'
            )

    def _check_opts(self):
        '''
            Option Syntax checks

            @Todo: get rid of Object Modifier superclass?
        '''
        valid_opts = ['ObjectModifier', 'Texture', 'Pigment']

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
            'hollow': 'bool',
            'scale': ['int', 'float']
        }

        self._validate_kwargs(valid_kw)
