# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import debug

from pov.language_directive.LanguageDirective import LanguageDirective


class Include(LanguageDirective):
    """
        INCLUDE_DIRECTIVE:
            #include FILE_NAME
        File inclusion may be nested at most 10 levels deep.

        FILE_NAME:
            STRING
    """
    def __init__(self, filename):
        '''
            Construct an Include statement

            @param filename: Full name of file to be included
            @type filename: string
        '''

        super(Include, self).__init__("include", [filename], [], [])

    def __str__(self):
        '''
            Generate PoV source code
        '''
        code = self._get_line('#' + 'include \"%s\"' % self.args[0])

        debug('Include.__str__: %s \n%s' % (self.args[0], code))

        return code

    def _check_arguments(self):
        '''
            Argument Syntax checks
        '''
        valid_args = ['str']

        self._validate_args(valid_args)

        # param syntax checks
#        if not os.path.isfile(self.args[0]):
#            raise IOError(
#                'No such file: %s%s%s' % (os.getcwd(), os.sep, self.args[0])
#            )
