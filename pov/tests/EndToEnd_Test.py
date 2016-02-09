# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

@TODO: Add rendering tests that call povray to make sure it works

"""

import os
import unittest
import difflib

from pov.atmeff.Fog import Fog
from pov.atmeff.SkySphere import SkySphere
from pov.basic.SceneFile import SceneFile
from pov.basic.Vector import Vector, x, y, z
from pov.basic.Color import Color
from pov.global_settings.GlobalSettings import GlobalSettings
from pov.finite_solid.Sphere import Sphere
from pov.infinite_solid.Plane import Plane
from pov.language_directive.Version import Version
from pov.language_directive.Default import Default
from pov.language_directive.Include import Include
from pov.object_modifier.Translate import Translate
from pov.other.Camera import Camera
from pov.other.LightSource import LightSource
from pov.texture.Finish import Finish
from pov.texture.Texture import Texture
from pov.texture.Pigment import Pigment
from pov.texture.ColorMap import ColorMap
from pov.texture.Normal import Normal
from pov.texture.Reflection import Reflection
from pov.texture.ImageMap import ImageMap
from pov.texture.Filter import Filter


class EndToEndTestCase(unittest.TestCase):
    """End To End Tests."""

    # @unittest.skip
    def test_scene1(self):
        """
        Test Scene 1.

        Example taken from:
        http://www.f-lohmueller.de/pov_tut/basic/povkurs3.htm
        """
        lsep = os.linesep

        ref = "#version 3.6;" + lsep
        ref += "global_settings {" + lsep
        ref += "  assumed_gamma 1.0" + lsep
        ref += "}" + lsep
        ref += "#default {" + lsep
        ref += "  finish {" + lsep
        ref += "    ambient 0.1" + lsep
        ref += "    diffuse 0.9" + lsep
        ref += "  }" + lsep
        ref += "}" + lsep
        ref += "#include \"pov/tests/fixture/colors.inc\"" + lsep
        ref += "#include \"pov/tests/fixture/textures.inc\"" + lsep
        ref += "camera {" + lsep
        ref += "  location <0.0, 1.0, -3.0>" + lsep
        ref += "  angle 75" + lsep
        ref += "  right <1.33333333333, 0.0, 0.0>" + lsep
        ref += "  look_at <0.0, 1.0, 0.0>" + lsep
        ref += "}" + lsep
        ref += "light_source {" + lsep
        ref += "  <1500, 3000, -2500>" + lsep
        ref += "  color White" + lsep
        ref += "}" + lsep
        ref += "plane {" + lsep
        ref += "  <0.0, 1.0, 0.0>, 1.0" + lsep
        ref += "  texture {" + lsep
        ref += "    pigment {" + lsep
        ref += "      bozo" + lsep
        ref += "      color_map {" + lsep
        ref += "        [0.0 color rgb <0.05, 0.15, 0.45>]" + lsep
        ref += "        [0.5 color rgb <0.05, 0.15, 0.45>]" + lsep
        ref += "        [0.85 color rgb <0.2, 0.2, 0.2>]" + lsep
        ref += "        [1.0 color rgb <0.5, 0.5, 0.5>]" + lsep
        ref += "        [0.7 color rgb <1.0, 1.0, 1.0>]" + lsep
        ref += "      }" + lsep
        ref += "      scale <2.5, 2.5, 3.75>" + lsep
        ref += "      translate <0.0, 0.0, 0.0>" + lsep
        ref += "      turbulence 0.92" + lsep
        ref += "    }" + lsep
        ref += "    finish {" + lsep
        ref += "      ambient 1.0" + lsep
        ref += "      diffuse 0.0" + lsep
        ref += "    }" + lsep
        ref += "  }" + lsep
        ref += "  hollow" + lsep
        ref += "  scale 10000.0" + lsep
        ref += "}" + lsep
        ref += "fog {" + lsep
        ref += "  color rgb <0.8, 0.8, 0.8>" + lsep
        ref += "  turbulence 1.8" + lsep
        ref += "  fog_offset 0.1" + lsep
        ref += "  fog_alt 1.5" + lsep
        ref += "  fog_type 2" + lsep
        ref += "  distance 50.0" + lsep
        ref += "}" + lsep
        ref += "plane {" + lsep
        ref += "  <0.0, 1.0, 0.0>, 0.0" + lsep
        ref += "  texture {" + lsep
        ref += "    pigment {" + lsep
        ref += "      color rgb <0.22, 0.45, 0.0>" + lsep
        ref += "    }" + lsep
        ref += "    normal {" + lsep
        ref += "      bumps 0.75" + lsep
        ref += "      scale 0.015" + lsep
        ref += "    }" + lsep
        ref += "    finish {" + lsep
        ref += "      phong 0.1" + lsep
        ref += "    }" + lsep
        ref += "  }" + lsep
        ref += "}" + lsep
        ref += "sphere {" + lsep
        ref += "  <0.0, 0.0, 0.0>, 0.75" + lsep
        ref += "  texture {" + lsep
        ref += "    pigment {" + lsep
        ref += "      color rgb <0.9, 0.55, 0.0>" + lsep
        ref += "    }" + lsep
        ref += "    finish {" + lsep
        ref += "      phong 1.0" + lsep
        ref += "    }" + lsep
        ref += "  }" + lsep
        ref += "  translate <0.85, 1.1, 0.0>" + lsep
        ref += "}" + lsep

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
            Include('pov/tests/fixture/colors.inc'),
            Include('pov/tests/fixture/textures.inc')
        )

        # @TODO: Read from Config
        image_width = 800
        # @TODO: Read from Config
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
                Color(rgb=Vector(1, 1, 1)) * 0.8,
                fog_type=2,
                turbulence=1.8,
                fog_offset=0.1,
                fog_alt=1.5,
                distance=50.0
            )
        )

        fix.append(
            Plane(
                Vector(0.0, 1.0, 0.0),
                0.0,
                Texture(
                    Pigment(
                        Color(rgb=Vector(0.22, 0.45, 0.0))
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
                        Color(rgb=Vector(0.9, 0.55, 0.0))
                    ),
                    Finish(
                        phong=1.0
                    )
                ),
                Translate(Vector(0.85, 1.1, 0.0))
            )
        )

        # ----------------------------------------------------
        msg = '\n' + ''.join(difflib.ndiff(
            ref.splitlines(1),
            str(fix).splitlines(1)
        ))

        self.assertEqual(ref, str(fix), msg)

    # @unittest.skip
    def test_examples_basic_scene(self):
        """Test examples/basic_scene.pov."""
        lsep = os.linesep

        ref = '#version 3.6;' + lsep
        ref += '#include "pov/tests/fixture/colors.inc"' + lsep
        ref += 'global_settings {' + lsep
        ref += '  assumed_gamma 1.0' + lsep
        ref += '}' + lsep
        ref += 'camera {' + lsep
        ref += '  location <0.0, 0.5, -4.0>' + lsep
        ref += '  look_at <0.0, 0.0, 0.0>' + lsep
        ref += '  right <1.33333333333, 0.0, 0.0>' + lsep
        ref += '  direction <0.0, 0.0, 1.5>' + lsep
        ref += '}' + lsep
        ref += 'sky_sphere {' + lsep
        ref += '  pigment {' + lsep
        ref += '    color_map {' + lsep
        ref += '      [0.0 color rgb <0.6, 0.7, 1.0>]' + lsep
        ref += '      [0.7 color rgb <0.0, 0.1, 0.8>]' + lsep
        ref += '    }' + lsep
        ref += '    gradient <0.0, 1.0, 0.0>' + lsep
        ref += '  }' + lsep
        ref += '}' + lsep
        ref += 'light_source {' + lsep
        ref += '  <0.0, 0.0, 0.0>' + lsep
        ref += '  color rgb <1.0, 1.0, 1.0>' + lsep
        ref += '  translate <-30.0, 30.0, -30.0>' + lsep
        ref += '}' + lsep
        ref += 'plane {' + lsep
        ref += '  <0.0, 1.0, 0.0>, -1' + lsep
        ref += '  pigment {' + lsep
        ref += '    color rgb <0.7, 0.5, 0.3>' + lsep
        ref += '  }' + lsep
        ref += '}' + lsep
        ref += 'sphere {' + lsep
        ref += '  <0.0, 0.0, 0.0>, 1.0' + lsep
        ref += '  texture {' + lsep
        ref += '    pigment {' + lsep
        ref += '      radial color_map {' + lsep
        ref += '        [0.0 color rgb <1.0, 0.4, 0.2>]' + lsep
        ref += '        [1.0 color rgb <1.0, 0.4, 0.2>]' + lsep
        ref += '        [0.66 color rgb <0.4, 1.0, 0.2>]' + lsep
        ref += '        [0.33 color rgb <0.2, 0.4, 1.0>]' + lsep
        ref += '      }' + lsep
        ref += '      frequency 8' + lsep
        ref += '    }' + lsep
        ref += '    finish {' + lsep
        ref += '      specular 0.6' + lsep
        ref += '    }' + lsep
        ref += '  }' + lsep
        ref += '}' + lsep

        fix = SceneFile('test.pov')
        fix.append(Version(3.6))
        fix.append(Include('pov/tests/fixture/colors.inc'))
        fix.append(
            GlobalSettings(assumed_gamma=1.0)
        )

        # @TODO: Read from Config
        image_width = 800
        # @TODO: Read from Config
        image_height = 600

        fix.append(
            Camera(
                location=Vector(0.0, 0.5, -4.0),
                direction=1.5 * z,
                right=x * image_width / image_height,
                look_at=Vector(0.0, 0.0, 0.0)
            )
        )

        fix.append(
            SkySphere(
                Pigment(
                    ColorMap(
                        {0.0: Color(rgb=Vector(0.6, 0.7, 1.0)),
                         0.7: Color(rgb=Vector(0.0, 0.1, 0.8))}
                    ),
                    gradient=y
                )
            ),
            LightSource(
                (0.0, 0.0, 0.0),
                Color(rgb=Vector(1.0, 1.0, 1.0)),
                translate=Vector(-30.0, 30.0, -30.0)
            )
        )

        fix.append(
            Plane(
                y, -1,
                Pigment(
                    Color(rgb=Vector(0.7, 0.5, 0.3))
                )
            ),
            Sphere(
                Vector(0.0, 0.0, 0.0),
                1.0,
                Texture(
                    Pigment(
                        radial=ColorMap({
                            0.00: Color(rgb=Vector(1.0, 0.4, 0.2)),
                            0.33: Color(rgb=Vector(0.2, 0.4, 1.0)),
                            0.66: Color(rgb=Vector(0.4, 1.0, 0.2)),
                            1.00: Color(rgb=Vector(1.0, 0.4, 0.2))
                        }),
                        frequency=8
                    ),
                    Finish(
                        specular=0.6
                    )
                )
            )
        )

        # ----------------------------------------------------
        msg = '\n' + ''.join(difflib.ndiff(
            ref.splitlines(1),
            str(fix).splitlines(1)
        ))

        self.assertEqual(ref, str(fix), msg)

    # @unittest.skip
    def test_checkered_floor_example(self):
        """Test examples/checkered_floor.pov."""
        lsep = os.linesep

        ref = '#version 3.6;' + lsep
        ref += '#include "pov/tests/fixture/colors.inc"' + lsep
        ref += 'global_settings {' + lsep
        ref += '  assumed_gamma 1.0' + lsep
        ref += '  max_trace_level 5' + lsep
        ref += '}' + lsep
        ref += 'camera {' + lsep
        ref += '  location <0.0, 0.5, -4.0>' + lsep
        ref += '  look_at <0.0, 0.0, 0.0>' + lsep
        ref += '  right <1.33333333333, 0.0, 0.0>' + lsep
        ref += '  direction <0.0, 0.0, 1.5>' + lsep
        ref += '}' + lsep
        ref += 'sky_sphere {' + lsep
        ref += '  pigment {' + lsep
        ref += '    color_map {' + lsep
        ref += '      [0.0 color rgb <0.6, 0.7, 1.0>]' + lsep
        ref += '      [0.7 color rgb <0.0, 0.1, 0.8>]' + lsep
        ref += '    }' + lsep
        ref += '    gradient <0.0, 1.0, 0.0>' + lsep
        ref += '  }' + lsep
        ref += '}' + lsep
        ref += 'light_source {' + lsep
        ref += '  <0, 0, 0>' + lsep
        ref += '  color rgb <1, 1, 1>' + lsep
        ref += '  translate <-30, 30, -30>' + lsep
        ref += '}' + lsep
        ref += 'plane {' + lsep
        ref += '  <0.0, 1.0, 0.0>, -1' + lsep
        ref += '  texture {' + lsep
        ref += '    pigment {' + lsep
        ref += '      checker' + lsep
        ref += '      color rgb <1, 1, 1>' + lsep
        ref += '      color rgbft <0, 0, 1, 0, 0>' + lsep
        ref += '      scale 0.5' + lsep
        ref += '    }' + lsep
        ref += '    finish {' + lsep
        ref += '      ambient 0.1' + lsep
        ref += '      diffuse 0.8' + lsep
        ref += '    }' + lsep
        ref += '  }' + lsep
        ref += '}' + lsep
        ref += 'sphere {' + lsep
        ref += '  <0, 0, 0>, 1' + lsep
        ref += '  texture {' + lsep
        ref += '    pigment {' + lsep
        ref += '      color rgb <0.8, 0.8, 1.0>' + lsep
        ref += '    }' + lsep
        ref += '    finish {' + lsep
        ref += '      conserve_energy' + lsep
        ref += '      reflection {' + lsep
        ref += '        metallic' + lsep
        ref += '        0.8' + lsep
        ref += '      }' + lsep
        ref += '      diffuse 0.3' + lsep
        ref += '      ambient 0.0' + lsep
        ref += '      specular 0.6' + lsep
        ref += '    }' + lsep
        ref += '  }' + lsep
        ref += '}' + lsep

        fix = SceneFile('test.pov')
        fix.append(Version(3.6))
        fix.append(Include('pov/tests/fixture/colors.inc'))
        fix.append(
            GlobalSettings(
                assumed_gamma=1.0,
                max_trace_level=5
            )
        )

        # @TODO: Read from Config
        image_width = 800
        # @TODO: Read from Config
        image_height = 600

        fix.append(
            Camera(
                location=Vector(0.0, 0.5, -4.0),
                direction=1.5 * z,
                right=x * image_width / image_height,
                look_at=Vector(0.0, 0.0, 0.0)
            ),
            SkySphere(
                Pigment(
                    ColorMap({
                        0.0: Color(rgb=Vector(0.6, 0.7, 1.0)),
                        0.7: Color(rgb=Vector(0.0, 0.1, 0.8))
                    }),
                    gradient=y
                )
            ),
            LightSource(
                Vector(0, 0, 0),
                Color(rgb=Vector(1, 1, 1)),
                Translate(Vector(-30, 30, -30))
            )
        )

        fix.append(
            Plane(
                y, -1,
                Texture(
                    Pigment(
                        Color(rgb=Vector(1, 1, 1)),
                        Color(blue=1),
                        checker=True,
                        scale=0.5
                    ),
                    Finish(
                        diffuse=0.8,
                        ambient=0.1
                    )
                )
            ),
            Sphere(
                (0, 0, 0), 1,
                Texture(
                    Pigment(
                        Color(rgb=Vector(0.8, 0.8, 1.0))
                    ),
                    Finish(
                        Reflection(
                            0.8,
                            metallic=True
                        ),
                        diffuse=0.3,
                        ambient=0.0,
                        specular=0.6,
                        conserve_energy=True
                    )
                )
            )
        )

        # ----------------------------------------------------
        msg = '\n' + ''.join(difflib.ndiff(
            ref.splitlines(1),
            str(fix).splitlines(1)
        ))

        self.assertEqual(ref, str(fix), msg)

    # @unittest.skip
    def test_image_map_example(self):
        """@TODO: Apidoc."""
        ref = os.linesep.join([
            '#version 3.6;',
            '#include "pov/tests/fixture/colors.inc"',
            'global_settings {',
            '  assumed_gamma 1.0',
            '}',
            'camera {',
            '  location <0.0, 0.0, -4.0>',
            '  look_at <0.0, 0.0, 0.0>',
            '  right <1.33333333333, 0.0, 0.0>',
            '  direction <0.0, 0.0, 2.0>',
            '}',
            'sky_sphere {',
            '  pigment {',
            '    color_map {',
            '      [0.0 color rgbft <0, 0, 0.6, 0, 0>]',
            '      [1.0 color rgb <1, 1, 1>]',
            '    }',
            '    gradient <0.0, 1.0, 0.0>',
            '  }',
            '}',
            'light_source {',
            '  <0, 0, 0>',
            '  color rgb <1, 1, 1>',
            '  translate <-30, 30, -30>',
            '}',
            'plane {',
            '  <0.0, 1.0, 0.0>, -1',
            '  texture {',
            '    pigment {',
            '      checker',
            '      color rgb <1, 1, 1>',
            '      color rgbft <0, 0, 1, 0, 0>',
            '      scale 0.5',
            '    }',
            '    finish {',
            '      reflection 0.2',
            '    }',
            '  }',
            '}',
            'plane {',
            '  <0.0, 0.0, 1.0>, -1',
            '  texture {',
            '    pigment {',
            '      image_map {',
            '        png "test.png"',
            '        filter 0 0.8',
            '        filter 1 0.8',
            '        once',
            '        interpolate 2',
            '      }',
            '      translate <-0.5, -0.5, -0.0>',
            '      scale 2',
            '    }',
            '    finish {',
            '      ambient 0.3',
            '    }',
            '  }',
            '}',
            ''
        ])

        fix = SceneFile('test.pov')
        fix.append(Version(3.6))
        fix.append(Include('pov/tests/fixture/colors.inc'))
        fix.append(
            GlobalSettings(
                assumed_gamma=1.0,
            )
        )

        # @TODO: Read from Config
        image_width = 800
        # @TODO: Read from Config
        image_height = 600

        fix.append(
            Camera(
                location=Vector(0.0, 0.0, -4.0),
                direction=2 * z,
                right=x * image_width / image_height,
                look_at=Vector(0.0, 0.0, 0.0)
            ),
            SkySphere(
                Pigment(
                    ColorMap({
                        0.0: Color(blue=0.6),
                        1.0: Color(rgb=Vector(1, 1, 1))
                    }),
                    gradient=y
                )
            ),
            LightSource(
                Vector(0, 0, 0),
                Color(rgb=Vector(1, 1, 1)),
                Translate(Vector(-30, 30, -30))
            )
        )

        fix.append(
            Plane(
                y, -1,
                Texture(
                    Pigment(
                        Color(rgb=Vector(1, 1, 1)),
                        Color(blue=1),
                        checker=True,
                        scale=0.5
                    ),
                    Finish(
                        reflection=0.2
                    )
                )
            ),
            Plane(
                z, -1,
                Texture(
                    Pigment(
                        ImageMap(
                            'png', 'test.png',
                            Filter(0, 0.8),
                            Filter(1, 0.8),
                            interpolate=2,
                            once=True,
                        ),
                        Translate(-0.5 * (x + y)),
                        scale=2
                    ),
                    Finish(
                        ambient=0.3
                    )
                )
            )
        )

        # ----------------------------------------------------
        msg = '\n' + ''.join(difflib.ndiff(
            ref.splitlines(1),
            str(fix).splitlines(1)
        ))

        self.assertEqual(ref, str(fix), msg)
