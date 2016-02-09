# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import BlockObject


class ImageMap(BlockObject):
    """@Todo: Docstring."""

    def __init__(self, btype, bfile, *opts, **kwargs):
        """
        Create ImageMap object.

        @todo: implement
        @todo: Syntax checks
        """
        arg = str(btype) + ' "' + str(bfile) + '"'
        super(ImageMap, self).__init__(
            'image_map', [arg], opts, kwargs
        )
