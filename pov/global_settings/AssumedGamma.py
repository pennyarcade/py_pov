# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from GlobalSettingsItem import *


class AssumedGamma(GlobalSettingsItem):
    """
        GLOBAL_SETTING_ITEMS:
            [assumed_gamma FLOAT] &
    """
    def __init__(self, value):
        '''
            Construct an Include statement

            @param value: Full name of file to be included
            @type value: float

        '''

        assert type(value) == float
        self.value = value

        super(GlobalSettingsItem, self).__init__('assumed_gamma', [], [])

    def __str__(self):
        '''
            Generate PoV source code
        '''
        code = self._getLine('assumed_gamma %s' % self.value)

        info('AssumedGamma.str(): ' + code)

        return code
