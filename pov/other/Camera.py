# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import BlockObject


class Camera(BlockObject):
    """
        CAMERA:
            camera { [CAMERA_TYPE] [CAMERA_ITEMS] [CAMERA_MODIFIERS] } |
            camera { CAMERA_IDENTIFIER [TANSFORMATIONS ...] }
        CAMERA_TYPE:
            perspective |
            orthographic |
            fisheye |
            ultra_wide_angle |
            omnimax |
            panoramic |
            spherical |
            cylinder CYLINDER_TYPE
        CYLINDER_TYPE:
            1 | 2 | 3 | 4
        CAMERA_ITEMS:
            [location VECTOR] &
            [right VECTOR] &
            [up VECTOR] &
            [direction VECTOR] &
            [sky VECTOR]
        CAMERA_MODIFIERS:
            [angle [F_HORIZONTAL] [,F_VERTICAL]] &
            [look_at VECTOR] &
            [FOCAL_BLUR] &
            [NORMAL] &
            [TRANSFORMATION...]
        FOCAL_BLUR:
            aperture FLOAT &
            blur_samples INT &
            [focal_point VECTOR] &
            [confidence FLOAT] &
            [variance FLOAT]

            @todo test __str__
            @todo: add transformations
    """

    def __init__(self, *opts, **kwargs):
        '''
            Create camera object
        '''
        super(Camera, self).__init__('camera', [], opts, kwargs)

    def _check_arguments(self):
        '''
            Argument Syntax checks
        '''
        valid_args = []

        self._validate_args(valid_args)

    def _check_opts(self):
        '''
            Option Syntax checks

            @Todo: get rid of Object Modifier superclass?
        '''
        valid_opts = ['Angle', 'Normal', 'Transformation']

        self._validate_opts(valid_opts)

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks
        '''

        valid_kw = {
            'camera_type': 'string',
            'location': 'Vector',
            'right': 'Vector',
            'up': 'Vector',
            'direction': 'Vector',
            'sky': 'Vector',
            'angle': 'int',
            'look_at': 'Vector',
            'aperture': 'float',
            'blur_samples': 'int',
            'focal_point': 'Vector',
            'confidence': 'float',
            'variance': 'float'
        }

        self._validate_kwargs(valid_kw)

        # @TODO: Implement Camera type checking
        # camera_type = [
        #     'perspective',
        #     'orthographic',
        #     'fisheye',
        #     'ultra_wide_angle',
        #     'omnimax',
        #     'panoramic',
        #     'spherical',
        #     'cylinder 1',
        #     'cylinder 2',
        #     'cylinder 3',
        #     'cylinder 4'
        # ]
