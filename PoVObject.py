"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from SceneItem import *


class PoVObject(SceneItem):
    """docstring for PoVObject"""
    def __init__(self, arg):
        super(PoVObject, self).__init__()
        self.arg = arg


class FiniteSolid(PoVObject):
    """docstring for FiniteSolid"""
    def __init__(self, arg):
        super(FiniteSolid, self).__init__()
        self.arg = arg


class FinitePatch(PoVObject):
    """docstring for FinitePatch"""
    def __init__(self, arg):
        super(FinitePatch, self).__init__()
        self.arg = arg


class IsoSurface(PoVObject):
    """docstring for IsoSurface"""
    def __init__(self, arg):
        super(IsoSurface, self).__init__()
        self.arg = arg


class ParametricObj(PoVObject):
    """docstring for ParametricObj"""
    def __init__(self, arg):
        super(ParametricObj, self).__init__()
        self.arg = arg


class Object(PoVObject):
    """docstring for Object"""
    def __init__(self, arg):
        super(Object, self).__init__()
        self.arg = arg


class InfiniteSolid(PoVObject):
    """docstring for InfiniteSolid"""
    def __init__(self, arg):
        super(InfiniteSolid, self).__init__()
        self.arg = arg


class Csg(PoVObject):
    """docstring for Csg"""
    def __init__(self, arg):
        super(Csg, self).__init__()
        self.arg = arg









