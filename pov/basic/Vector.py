# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import *
from math import sqrt


class Vector:
    """Generalized Vector class.

    Handles arbitrary component vectors."""
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], Vector):
                self.v = args[0].v
            else:
                self.v = list(args[0])
        else:
            self.v = list(args)
        float(self.v[0])    # assert

    def __str__(self):
        return "<%s>" % (", ".join([str(x)for x in self.v]))

    def __repr__(self):
        return "Vector%s" % (tuple(self.v),)

    def __setitem__(self, i, item):
        debug("__setitem__: %s %s %s", str(self.v), i, item)
        self.v[i] = item

    def __getitem__(self, i):
        return self.v[i]

    def __mul__(self, other):
        " scalar multiplication "
        assert type(other) in (float, int)
        return Vector([r*other for r in self.v])

    def __rmul__(self, other):
        " scalar multiplication "
        assert type(other) in (float, int)
        return Vector([r*other for r in self.v])

    def __div__(self, other):
        assert type(other) in (float, int)
        return Vector([r/other for r in self.v])

    def __add__(self, other):
        assert isinstance(other, Vector)
        return Vector([self.v[i]+other.v[i] for i in range(len(self.v))])

    def __sub__(self, other):
        assert isinstance(other, Vector)
        return Vector([self.v[i]-other.v[i] for i in range(len(self.v))])

    def __neg__(self):
        return Vector([-x for x in self.v])

    def __eq__(self, other):
        return self.v == other.v

    def norm(self):
        """Compute norm of vector."""
        r = 0.0
        for x in self.v:
            r += x*x
        return sqrt(r)

    def normalize(self):
        """Normalize a vector"""
        r = self.norm()
        v = Vector([x/r for x in self.v])
        return v

    def dot(self, other):
        """Dot product of two vectors"""
        assert isinstance(other, Vector)
        r = 0.0
        for i in range(len(self.v)):
            r += self.v[i]*other.v[i]
        return r
