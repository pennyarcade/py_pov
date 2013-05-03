"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from SceneItem import *


class LanguageDirective(SceneItem):
    """docstring for LanguageDirective"""
    def __init__(self, arg):
        super(LanguageDirective, self).__init__()
        self.arg = arg


class Break(LanguageDirective):
    """docstring for Break"""
    def __init__(self, arg):
        super(Break, self).__init__()
        self.arg = arg


class Case(LanguageDirective):
    """docstring for Case"""
    def __init__(self, arg):
        super(Case, self).__init__()
        self.arg = arg


class Debug(LanguageDirective):
    """docstring for Debug"""
    def __init__(self, arg):
        super(Debug, self).__init__()
        self.arg = arg


class Declare(LanguageDirective):
    """docstring for Declare"""
    def __init__(self, arg):
        super(Declare, self).__init__()
        self.arg = arg


