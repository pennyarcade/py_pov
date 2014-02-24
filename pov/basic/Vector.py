# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import debug
from math import sqrt
from pov.other.SdlSyntaxException import SdlSyntaxException


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
        float(self.v[0])    # cast to float

    def __str__(self):
        return "<%s>" % (", ".join([str(item)for item in self.v]))

    def __repr__(self):
        return "Vector%s" % (tuple(self.v),)

    def __setitem__(self, i, item):
        debug("__setitem__: %s %s %s", str(self.v), i, item)
        self.v[i] = item

    def __getitem__(self, i):
        return self.v[i]

    def __mul__(self, other):
        " scalar multiplication "
        if not type(other) in (float, int):
            raise SdlSyntaxException('Parameter not of type float or int')
        return Vector([r*other for r in self.v])

    def __rmul__(self, other):
        " scalar multiplication "
        if not type(other) in (float, int):
            raise SdlSyntaxException('Parameter not of type float or int')
        return Vector([r*other for r in self.v])

    def __div__(self, other):
        if not type(other) in (float, int):
            raise SdlSyntaxException('Parameter not of type float or int')
        return Vector([r/other for r in self.v])

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise SdlSyntaxException('Parameter not of type Vector')
        return Vector([self.v[i]+other.v[i] for i in range(len(self.v))])

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise SdlSyntaxException('Parameter not of type Vector')
        return Vector([self.v[i]-other.v[i] for i in range(len(self.v))])

    def __neg__(self):
        return Vector([-item for item in self.v])

    def __eq__(self, other):
        return self.v == other.v

    def norm(self):
        """Compute norm of vector."""
        result = 0.0
        for item in self.v:
            result += item*item
        return sqrt(result)

    def normalize(self):
        """Normalize a vector"""
        div = self.norm()
        result = Vector([item/div for item in self.v])
        return result

    def dot(self, other):
        """Dot product of two vectors"""
        if not isinstance(other, Vector):
            raise SdlSyntaxException('Parameter not of type Vector')
        result = 0.0
        for i in range(len(self.v)):
            result += self.v[i]*other.v[i]
        return result

# Predefine basic vectors
x = Vector(1.0, 0.0, 0.0)
y = Vector(0.0, 1.0, 0.0)
z = Vector(0.0, 0.0, 1.0)
