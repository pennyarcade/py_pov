# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import BlockObject


class Photons(BlockObject):
    """
        PHOTONS:
            photons { PHOTON_QUANTITY [PHOTON_ITEMS] }
        PHOTON_QUANTITY:
            spacing FLOAT |
            count INT
        PHOTON_ITEMS:
            [gather I_MIN, I_MAX] &
            [media I_MAX_STEPS [, F_FACTOR]] &
            [jitter FLOAT] &
            [max_trace_level INT] &
            [adc_bailout FLOAT] &
            [save_file FILE_NAME] &
            [load_file FILE_NAME] &
            [autostop FLOAT] &
            [expand_thresholds F_INCREASE, F_MIN] &
            [radius [FLOAT, FLOAT, FLOAT, FLOAT]]

        @Todo: Implement
    """
