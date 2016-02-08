# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import debug
from math import sqrt
from pov.other.SdlSyntaxException import SdlSyntaxException


class Vector(object):
    """
    Generalized Vector class.

    Handles arbitrary component vectors.
    """
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], Vector):
                self.values = args[0].values
            else:
                self.values = list(args[0])
        else:
            self.values = list(args)
        float(self.values[0])    # cast to float

    def __str__(self):
        """@Todo: ApiDoc."""
        return "<%s>" % (", ".join([str(item)for item in self.values]))

    def __repr__(self):
        """@Todo: ApiDoc."""
        return "Vector%s" % (tuple(self.values),)

    def __setitem__(self, i, item):
        """@Todo: ApiDoc."""
        debug("__setitem__: %s %s %s", str(self.values), i, item)
        self.values[i] = item

    def __getitem__(self, i):
        """@Todo: ApiDoc."""
        return self.values[i]

    def __mul__(self, other):
        """scalar multiplication."""
        if type(other) not in (float, int):
            raise SdlSyntaxException('Parameter not of type float or int')
        return Vector([r * other for r in self.values])

    def __rmul__(self, other):
        """scalar multiplication."""
        if type(other) not in (float, int):
            raise SdlSyntaxException('Parameter not of type float or int')
        return Vector([r * other for r in self.values])

    def __div__(self, other):
        """@Todo: ApiDoc."""
        if type(other) not in (float, int):
            raise SdlSyntaxException('Parameter not of type float or int')
        return Vector([r / other for r in self.values])

    def __add__(self, other):
        """@Todo: ApiDoc."""
        if not isinstance(other, Vector):
            raise SdlSyntaxException('Parameter not of type Vector')
        return Vector(
            [self.values[i] + other.values[i] for i in range(len(self.values))]
        )

    def __sub__(self, other):
        """@Todo: ApiDoc."""
        if not isinstance(other, Vector):
            raise SdlSyntaxException('Parameter not of type Vector')
        return Vector(
            [self.values[i]-other.values[i] for i in range(len(self.values))]
        )

    def __neg__(self):
        """@Todo: ApiDoc."""
        return Vector([-item for item in self.values])

    def __eq__(self, other):
        """@Todo: ApiDoc."""
        return self.values == other.values

    def norm(self):
        """Compute norm of vector."""
        result = 0.0
        for item in self.values:
            result += item*item
        return sqrt(result)

    def normalize(self):
        """Normalize a vector."""
        div = self.norm()
        result = Vector([item / div for item in self.values])
        return result

    def dot(self, other):
        """Dot product of two vectors."""
        if not isinstance(other, Vector):
            raise SdlSyntaxException('Parameter not of type Vector')
        result = 0.0
        for i in range(len(self.values)):
            result += self.values[i]*other.values[i]
        return result

    def __len__(self):
        return len(self.values)


# Predefine basic vectors
x = Vector(1.0, 0.0, 0.0)
y = Vector(0.0, 1.0, 0.0)
z = Vector(0.0, 0.0, 1.0)
