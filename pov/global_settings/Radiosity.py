# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import BlockObject


class Radiosity(BlockObject):
    """
        RADIOSITY:
            radiosity { [RADIOSITY_ITEMS] }
        RADIOSITY_ITEMS:
            [adc_bailout FLOAT] &
            [always_sample BOOL] &
            [brightness FLOAT] &
            [count INT] &
            [error_bound FLOAT] &
            [gray_threshold FLOAT] &
            [load_file FILE_NAME] &
            [low_error_factor FLOAT] &
            [max_sample FLOAT] &
            [media BOOL] &
            [minimum_reuse FLOAT] &
            [nearest_count INT] &
            [normal BOOL] &
            [pretrace_end FLOAT] &
            [pretrace_start FLOAT] &
            [recursion_limit INT] &
            [save_file FILE_NAME]

        @Todo: Implement
    """
