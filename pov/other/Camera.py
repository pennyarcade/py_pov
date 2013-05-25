# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.PoVObject import PoVObject


class Camera(PoVObject):
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

    """
    def __init__(self, *opts, **kwargs):
        '''
            Construct a Camera object

            @TODO: Param Syntax checking
            @TODO: make sure superclass constructor gets all params in the right form
            @todo test __str__
            @todo: add transformations
            @Todo: are there any valid options at all?
        '''

        valid_kw = ['ctype', 'location', 'right', 'up', 'direction', 'sky',
                    'angle', 'look_at', 'aperture', 'blur_samples', 'focal_point',
                    'confidence', 'variance']

        # kwargs syntax checking
        for key, val in kwargs.items():
            # allowed keywords
            if not key in valid_kw:
                raise SdlSyntaxException('Invalid key: ' + str(key))

        super(Camera, self).__init__("camera", [], opts, kwargs)