# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from pov.basic.BlockObject import BlockObject


class SphereSweep(BlockObject):
    """
    Sphere Sweep Object.

    SPHERE_SWEEP:
        sphere_sweep {
            linear_spline | b_spline | cubic_spline
            NUM_OF_SPHERES,

            CENTER, RADIUS,
            CENTER, RADIUS,
            ...
            CENTER, RADIUS
            [tolerance DEPTH_TOLERANCE]
            [OBJECT_MODIFIERS]
        }

    @Todo: Implement
    """
