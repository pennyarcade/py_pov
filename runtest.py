# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

Unittests File

"""

import unittest
from pov.test import BasicTest
from pov.test import FiniteSolidTest
from pov.test import LanguageDirectiveTest


def suite():
	'''
		Test Suite
	'''
    tsuite = unittest.TestSuite()

    tsuite.addTests(unittest.TestLoader.loadTestsFromModule(BasicTest))
    tsuite.addTests(unittest.TestLoader.loadTestsFromModule(FiniteSolidTest))
    tsuite.addTests(
        unittest.TestLoader.loadTestsFromModule(LanguageDirectiveTest)
    )

    return tsuite


if __name__ == '__main__':
    suite().run()
