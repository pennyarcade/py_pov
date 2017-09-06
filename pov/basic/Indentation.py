# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.
Borg Pattern by Alex Martelli
"""
from logging import debug

from pov.basic.Borg import Borg
from pov.other.IllegalStateException import IllegalStateException


class Indentation(Borg):
    def __init__(self):
        Borg.__init__(self)
        if not hasattr(self, 'level'):
            self.level = 0

    def indent(self):
        """Indent PoV code."""
        self.level += 1

    def dedent(self):
        """Dedent PoV code."""
        if not self.level > 0:
            raise IllegalStateException('Indentation below zero')

        self.level -= 1
        debug("dedent: %s", self.level)

    def get(self):
        """Get INDENTATION."""
        return self.level

