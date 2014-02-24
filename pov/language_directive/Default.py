
# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import debug
from pov.basic.BlockObject import BlockObject
from pov.language_directive.LanguageDirective import LanguageDirective


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
            create a "default" language directive object
        """
        # Syntax checking

        super(Default, self).__init__("#default", [], opts, kwargs)

    def __str__(self):
        """
            Return PoV source code
        """
        code = super(Default, self).__str__()
        debug('Default.__str__: %s \n%s' % (self.name, code))
        return code

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks
        '''

        valid_kw = {}
        self._validate_kwargs(valid_kw)

    def _check_opts(self):
        '''
            Optional Argument Syntax checks
        '''

        valid_kw = [
            'Texture', 'Pigment', 'Normal', 'Finish'
        ]

        self._validate_kwargs(valid_kw)
