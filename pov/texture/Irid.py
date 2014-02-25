# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import BlockObject


class Irid(BlockObject):
    '''
        @TODO: Docstring
    '''

    def __init__(self, *opts, **kwargs):
        '''
            Create Irid object

            @todo: implement
            @todo: Syntax checks
        '''
        super(Irid, self).__init__('irid', [], opts, kwargs)
