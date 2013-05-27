# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.PoVObject import PoVObject
from pov.other.SdlSyntaxException import SdlSyntaxException

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


            @TODO: Param Syntax checking
            @todo test __str__
            @todo: add transformations
            @Todo: are there any valid options at all?
    """

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks
        '''

        valid_kw = {
            'camera_type': ['perspective',
                            'orthographic',
                            'fisheye',
                            'ultra_wide_angle',
                            'omnimax',
                            'panoramic',
                            'spherical',
                            'cylinder 1',
                            'cylinder 2',
                            'cylinder 3',
                            'cylinder 4'
                            ],
            'location': 'Vector',
            'right': 'Vector',
            'up': 'Vector',
            'direction': 'Vector',
            'sky': 'Vector',
            'angle': range(360),
            'look_at': 'Vector',
            'aperture': 'float',
            'blur_samples': 'int',
            'focal_point': 'Vector',
            'confidence': 'float',
            'variance': 'float'
        }

        # kwargs syntax checking
        for key, val in self.kwargs.items():
            # allowed keywords
            if not key in valid_kw:
                raise SdlSyntaxException('Invalid key: ' + str(key))
