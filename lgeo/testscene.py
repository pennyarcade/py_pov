"""
Persistence of Vision Ray Tracer Scene Description File.

File: main.pov
Vers: 3.6
Desc: Main file for testing scenes
Link:
Date: 04/2013
Auth: Chocokiko
"""


# ***************************************************************************
# Includes
# ***************************************************************************

# ==== py_pov Inchudes
from pov.atmeff.SkySphere import SkySphere

from pov.basic.SceneFile import SceneFile
from pov.basic.Color import Color
from pov.basic.Vector import Vector, x, y

from pov.global_settings.GlobalSettings import GlobalSettings

from pov.csg.Union import Union

from pov.language_directive.Version import Version

from pov.object_modifier.Translate import Translate

from pov.other.Camera import Camera
from pov.other.LightSource import LightSource
from pov.other.Comment import Comment
# from pov.other.Object import Object

from pov.texture.ColorMap import ColorMap
# from pov.texture.Normal import Normal
from pov.texture.Pigment import Pigment

from pov.texture.pattern.Gradient import Gradient

from lgeo.include.common.lg_color import LG_WHITE

# ==== Custom Includes ====
from lgeo.include.common.custom_macros import std_brick

from lgeo.include.brick import lg_3853


def main():
    """@Todo: DocString."""
    fix = SceneFile('test.pov')
    fix.append(Version(3.6))
    
    part = lg_3853

    # ***********************************************************************
    # Settings --> After Includes to overwrite presets
    # ***********************************************************************

    # @TODO: Read from Config
    image_width = 1600
    # @TODO: Read from Config
    image_height = 1200

    fix.append(
        GlobalSettings(
            assumed_gamma=1.5,
            ambient_light=Color(rgb=Vector(1, 1, 1))
        )
    )

    # ***********************************************************************
    # Camera
    # ***********************************************************************
    fix.append(
        Camera(
            location=Vector(0, 500, 0),
            direction=Vector(0, 25, 0),
            right=x * image_width / image_height,
            look_at=(0.0, 0.0, 0.0)
        )
    )

    # ***********************************************************************
    # Background
    # ***********************************************************************
    fix.append(
        SkySphere(
            Pigment(
                Gradient(y * 0.8),
                ColorMap({
                    0.00: Color(rgb=Vector(0.6, 0.7, 1.0)),
                    0.70: Color(rgb=Vector(0.0, 0.1, 0.8))
                }),
            )
        )
    )

    # ***********************************************************************
    # Light
    # ***********************************************************************
    fix.append(
        Union(
            LightSource(
                Vector(0, 0, 0),      # light's position (translated below)
                Color(rgb=(1, 1, 1)),  # light's color
                Translate(
                    Vector(-300, 300, -300)
                )
            ),

            LightSource(
                Vector(0, 0, 0),      # light's position (translated below)
                Color(rgb=Vector(1, 1, 1)),  # light's color
                Translate(
                    Vector(300, 300, 300)
                )
            )
        )
    )

    # ***********************************************************************
    # Ground plane
    # ***********************************************************************
    # fix.append(
    #     Plane(
    #         y, -5.01,
    #         Pigment(
    #             Color(rgb=Vector(0.5, 0.5, 0.5))
    #         )
    #     )
    # )

    fix.append(
        Union(
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                9, 0, 8,
                45, 0, 45),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                3, 0, 8,
                135, 0, 45),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                -3, 0, 8,
                215, 0, -45),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                -9, 0, 8,
                315, 0, -45),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                9, 0, 3,
                45, 45, 0),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                3, 0, 3,
                45, 135, 0),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                -3, 0, 3,
                -45, 215, 0),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                -9, 0, 3,
                -45, 315, 0),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                9, 0, -2,
                45, 0, 45,),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                3, 0, -2,
                45, 0, 135),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                -3, 0, -2,
                -45, 0, 215),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                -9, 0, -2,
                -45, 0, 315),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                9, 0, -7,
                0, 0, 0,),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                3, 0, -7,
                90, 0, 0),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                -3, 0, -7,
                180, 0, 0),
            Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
            std_brick(
                part.solid(),
                LG_WHITE,
                -9, 0, -7,
                270, 0, 0),
        )
    )

    return fix
