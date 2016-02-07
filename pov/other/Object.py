# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import BlockObject


class Object(BlockObject):
    """
    PoV Object.

    object {
      OBJECT_IDENTIFIER | OBJECT {}
      LIST_ITEM_A, LIST_ITEM_B
    }
    @Todo: Implement
    """

    def __init__(self, *opts, **kwargs):
        """Create object object."""
        super(Object, self).__init__('object', [], opts, kwargs)
