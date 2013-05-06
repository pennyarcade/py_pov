# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from SceneItem import *


class Camera(SceneItem):
    """docstring for Camera"""
    def __init__(self, arg):
        super(Camera, self).__init__()
        self.arg = arg
