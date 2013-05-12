
# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from ..basic import BlockObject
from LanguageDirective import *


class Default(LanguageDirective, BlockObject):
    """
        Specify a default texture, pigment, normal or finish:

        DEFAULT_DIRECTIVE:
            #default { DEFAULT_ITEM }
        DEFAULT_ITEM:
            PLAIN_TEXTURE | PIGMENT | NORMAL | FINISH
    """

    def __init__(self, *opts, **kwargs):
        """
            @TODO: constructor apidoc
            @TODO: Syntax checking
        """
        super(Default, self).__init__("default", args=[], opts=[], **kwargs)
