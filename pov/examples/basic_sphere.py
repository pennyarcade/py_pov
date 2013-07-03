# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""
import sys
from logging import *

sys.path.append('../')

from pov.atmeff.Fog import Fog
from pov.basic.SceneFile import SceneFile
from pov.basic.Vector import *
from pov.basic.Color import Color
from pov.global_settings.GlobalSettings import GlobalSettings
from pov.finite_solid.Sphere import Sphere
from pov.infinite_solid.Plane import Plane
from pov.language_directive.Version import Version
from pov.language_directive.Default import Default
from pov.language_directive.Include import Include
from pov.other.Camera import Camera
from pov.other.LightSource import LightSource
from pov.texture.Finish import Finish
from pov.texture.Texture import Texture
from pov.texture.Pigment import Pigment
from pov.texture.ColorMap import ColorMap
from pov.texture.Normal import Normal



fix = SceneFile('test.pov')
fix.append(Version(3.6))
fix.append(
    GlobalSettings(assumed_gamma=1.0)
)
fix.append(
    Default(
        Finish(
            ambient=0.1,
            diffuse=0.9
        )
    )
)
fix.append(
    Include('colors.inc'),
    Include('textures.inc')
)

#@TODO: Read from Config
image_width = 800
#@TODO: Read from Config
image_height = 600

fix.append(
    Camera(
        location=Vector(0.0, 1.0, -3.0),
        look_at=Vector(0.0, 1.0, 0.0),
        right=(x * image_width / image_height),
        angle=75
    ),
    LightSource(
        Vector(1500, 3000, -2500),
        color='White'
    )
)

fix.append(
    Plane(
        Vector(0.0, 1.0, 0.0),
        1.0,
        Texture(
            Pigment(
                ColorMap({
                    0.00: Color(rgb=Vector(0.05, 0.15, 0.45)),
                    0.50: Color(rgb=Vector(0.05, 0.15, 0.45)),
                    0.70: Color(rgb=Vector(1.0, 1.0, 1.0)),
                    0.85: Color(rgb=Vector(0.2, 0.2, 0.2)),
                    1.00: Color(rgb=Vector(0.5, 0.5, 0.5))
                }),
                bozo=True,
                turbulence=0.92,
                scale=Vector(1.0, 1.0, 1.5) * 2.5,
                translate=Vector(0.0, 0.0, 0.0)
            ),
            Finish(
                ambient=1.0,
                diffuse=0.0
            )
        ),
        hollow=True,
        scale=10000.0
    )
)

fix.append(
    Fog(
        fog_type=2.0,
        distance=50.0,
        # @Todo: make colors multiplyable
        color=Color(rgb=Vector(1, 1, 1))*0.8,
        fog_offset=0.1,
        fog_alt=1.5,
        turbulence=1.8
    )
)

fix.append(
    Plane(
        Vector(0.0, 1.0, 0.0),
        0.0,
        Texture(
            Pigment(
                color=Color(rgb=Vector(0.22, 0.45, 0.0))
            ),
            Normal(
                bumps=0.75,
                scale=0.015
            ),
            Finish(
                phong=0.1
            )
        )
    ),
    Sphere(
        Vector(0.0, 0.0, 0.0),
        0.75,
        Texture(
            Pigment(
                color=Color(rgb=Vector(0.9, 0.55, 0.0))
            ),
            Finish(
                phong=1.0
            )
        ),
        translate=Vector(0.85, 1.1, 0.0)
    )
)

# print everything to stdout for now
print str(fix)
