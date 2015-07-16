# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import unittest
import os
from logging import debug
from pov.basic.SceneItem import SceneItem
from pov.language_directive.LanguageDirective import LanguageDirective
from pov.language_directive.Default import Default
from pov.language_directive.Version import Version
from pov.language_directive.Include import Include
from pov.texture.Finish import Finish
from pov.other.SdlSyntaxException import SdlSyntaxException


class LanguageDirectiveTestCase(unittest.TestCase):
    '''
        @Todo: DocString
    '''
    def setUp(self):
        '''
            @Todo: DocString
        '''
        self.sut = LanguageDirective('#foo')

    def test_creation(self):
        '''
            @Todo: DocString
        '''
        self.assertIsInstance(self.sut, LanguageDirective)
        self.assertIsInstance(self.sut, SceneItem)

    def test_str(self):
        '''
            @Todo: DocString
        '''
        second = '#foo'

        self.assertEqual(str(self.sut), second)


class IncludeTestCase(unittest.TestCase):
    '''
        @Todo: DocString
    '''
    def setUp(self):
        '''
            @Todo: DocString
        '''
        self.sut = Include('fixture/test.inc')

    def test_create(self):
        '''
            @Todo: DocString
        '''
        self.assertIsInstance(self.sut, Include)
        self.assertIsInstance(self.sut, LanguageDirective)

    def test_str(self):
        '''
            @Todo: DocString
        '''
        lsp = os.linesep
        second = '#include "fixture/test.inc"' + lsp

        self.assertEqual(str(self.sut), second)

    def test_create_non_existant_file(self):
        '''
            @Todo: DocString
        '''
        with self.assertRaisesRegexp(
            IOError,
            'No such file: %s%s%s' % (
                os.getcwd(), os.sep, 'fixture/nonexistant.inc'
            )
        ):
            self.sut = Include('pov/tests/fixture/nonexistant.inc')


class VersionTestCase(unittest.TestCase):
    '''
        @Todo: DocString
    '''
    def setUp(self):
        '''
            @Todo: DocString
        '''
        self.sut = Version(3.6)

    def test_create(self):
        '''
            @Todo: DocString
        '''
        self.assertIsInstance(self.sut, Version)
        self.assertIsInstance(self.sut, LanguageDirective)

    def test_str(self):
        '''
            @Todo: DocString
        '''
        lsp = os.linesep
        second = '#version 3.6;' + lsp

        self.assertEqual(str(self.sut), second)

    def test_create_wrong_type(self):
        '''
            @Todo: DocString
        '''
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Value of Argument 0 is expectet to be type float but got str'
        ):
            self.sut = Version('foo')


class DefaultTestCase(unittest.TestCase):
    '''
        @Todo: DocString
    '''
    def setUp(self):
        '''
            @Todo: DocString
        '''
        debug('---------------------------------')
        self.sut = Default(Finish(ambient=0.43))

    def test_creation(self):
        '''
            @Todo: DocString
        '''
        self.assertIsInstance(self.sut, Default)
        self.assertIsInstance(self.sut, LanguageDirective)

    def test_tostring(self):
        '''
            @Todo: DocString
        '''
        debug('---------------------------------')
        lsp = os.linesep
        first = str(self.sut)
        second = '#default {' + lsp
        second += '  finish {' + lsp
        second += '    ambient 0.43' + lsp
        second += '  }' + lsp
        second += '}' + lsp

        self.assertEqual(first, second)
