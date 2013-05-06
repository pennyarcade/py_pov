# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from pov.PoVObject import *
from pov.basic.Vector import *


class FiniteSolid(PoVObject):
    """
        FINITE_SOLID_OBJECT:
            BLOB | BOX | CONE | CYLINDER | HEIGHT_FIELD | JULIA_FRACTAL |
            LATHE | PRISM | SPHERE | SPHERESWEEP | SUPERELLIPSOID | SOR |
            TEXT | TORUS
    """
