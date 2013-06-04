# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import os
import unittest
import difflib
from logging import *

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


#@unittest.skip
class EndToEndTestCase(unittest.TestCase):
    def test_Scene1(self):
        '''
            Example taken from:
            http://www.f-lohmueller.de/pov_tut/basic/povkurs3.htm
        '''
        le = os.linesep

        ref = "#version 3.6;" + le
        ref += "global_settings {" + le
        ref += "  assumed_gamma 1.0" + le
        ref += "}" + le
        ref += "#default {" + le
        ref += "  finish {" + le
        ref += "    ambient 0.1" + le
        ref += "    diffuse 0.9" + le
        ref += "  }" + le
        ref += "}" + le
        ref += "#include \"colors.inc\"" + le
        ref += "#include \"textures.inc\"" + le
        ref += "camera {" + le
        ref += "  location <0.0, 1.0, -3.0>" + le
        ref += "  angle 75" + le
        ref += "  right <1.33333333333, 0.0, 0.0>" + le
        ref += "  look_at <0.0, 1.0, 0.0>" + le
        ref += "}" + le
        ref += "light_source {" + le
        ref += "  <1500, 3000, -2500>" + le
        ref += "  color White" + le
        ref += "}" + le
        ref += "plane {" + le
        ref += "  <0.0, 1.0, 0.0>, 1.0" + le
        ref += "  texture {" + le
        ref += "    pigment {" + le
        ref += "      color_map {" + le
        ref += "        [0.0 rgb <0.05, 0.15, 0.45>]" + le
        ref += "        [0.5 rgb <0.05, 0.15, 0.45>]" + le
        ref += "        [0.85 rgb <0.2, 0.2, 0.2>]" + le
        ref += "        [1.0 rgb <0.5, 0.5, 0.5>]" + le
        ref += "        [0.7 rgb <1.0, 1.0, 1.0>]" + le
        ref += "      }" + le
        ref += "      bozo" + le
        ref += "      scale <2.5, 2.5, 3.75>" + le
        ref += "      translate <0.0, 0.0, 0.0>" + le
        ref += "      turbulence 0.92" + le
        ref += "    }" + le
        ref += "    finish {" + le
        ref += "      ambient 1.0" + le
        ref += "      diffuse 0.0" + le
        ref += "    }" + le
        ref += "  }" + le
        ref += "  hollow" + le
        ref += "  scale 10000.0" + le
        ref += "}" + le
        ref += "fog {" + le
        ref += "  fog_type 2.0" + le
        ref += "  fog_offset 0.1" + le
        ref += "  fog_alt 1.5" + le
        ref += "  turbulence 1.8" + le
        ref += "  color rgb <0.8, 0.8, 0.8>" + le
        ref += "  distance 50.0" + le
        ref += "}" + le
        ref += "plane {" + le
        ref += "  <0.0, 1.0, 0.0>, 0.0" + le
        ref += "  texture {" + le
        ref += "    pigment {" + le
        ref += "      color rgb <0.22, 0.45, 0.0>" + le
        ref += "    }" + le
        ref += "    normal {" + le
        ref += "      scale 0.015" + le
        ref += "      bumps 0.75" + le
        ref += "    }" + le
        ref += "    finish {" + le
        ref += "      phong 0.1" + le
        ref += "    }" + le
        ref += "  }" + le
        ref += "}" + le
        ref += "sphere {" + le
        ref += "  <0.0, 0.0, 0.0>, 0.75" + le
        ref += "  texture {" + le
        ref += "    pigment {" + le
        ref += "      color rgb <0.9, 0.55, 0.0>" + le
        ref += "    }" + le
        ref += "    finish {" + le
        ref += "      phong 1.0" + le
        ref += "    }" + le
        ref += "  }" + le
        ref += "  translate <0.85, 1.1, 0.0>" + le
        ref += "}" + le

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

        #----------------------------------------------------
        msg = '\n' + ''.join(difflib.ndiff(
            ref.splitlines(1),
            str(fix).splitlines(1)
        ))

        self.assertEqual(ref, str(fix), msg)
