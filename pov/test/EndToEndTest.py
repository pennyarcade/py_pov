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
#import copy
from logging import *

from pov.basic import *
from pov.language_directive import *
from pov.global_settings import *
from pov.texture import *


@unittest.skip
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
        ref += "camera{ location  <0.0 , 1.0 ,-3.0>" + le
        ref += "        look_at   <0.0 , 1.0 , 0.0>" + le
        ref += "        right x*image_width/image_height" + le
        ref += "        angle 75 }" + le
        ref += "light_source{<1500,3000,-2500> color White}" + le
        ref += "plane{ <0,1,0>,1 hollow" + le
        ref += "       texture{" + le
        ref += "         pigment{ bozo turbulence 0.92" + le
        ref += "           color_map{" + le
        ref += "                 [0.00 rgb<0.05,0.15,0.45>]" + le
        ref += "                 [0.50 rgb<0.05,0.15,0.45>]" + le
        ref += "                 [0.70 rgb<1,1,1>        ]" + le
        ref += "                 [0.85 rgb<0.2,0.2,0.2>  ]" + le
        ref += "                 [1.00 rgb<0.5,0.5,0.5>  ]" + le
        ref += "                       }" + le
        ref += "           scale<1,1,1.5>*2.5" + le
        ref += "           translate<0,0,0>" + le
        ref += "           }" + le
        ref += "         finish {ambient 1 diffuse 0}" + le
        ref += "        }" + le
        ref += "       scale 10000}" + le
        ref += "fog { fog_type   2" + le
        ref += "      distance   50" + le
        ref += "      color      rgb<1,1,1>*0.8" + le
        ref += "      fog_offset 0.1" + le
        ref += "      fog_alt    1.5" + le
        ref += "      turbulence 1.8" + le
        ref += "    }" + le
        ref += "plane{ <0,1,0>, 0" + le
        ref += "       texture{" + le
        ref += "          pigment{ color rgb<0.22,0.45,0>}" + le
        ref += "          normal { bumps 0.75 scale 0.015 }" + le
        ref += "          finish { phong 0.1 }" + le
        ref += "       }" + le
        ref += "     }" + le
        ref += "sphere{ <0,0,0>, 0.75" + le
        ref += "        translate<0.85,1.1,0>" + le
        ref += "        texture{" + le
        ref += "          pigment{ color rgb<0.9,0.55,0>}" + le
        ref += "          finish { phong 1 }" + le
        ref += "        }" + le
        ref += "      }" + le

        fix = SceneFile('test.pov')
        fix.append(Version(3.6))
        fix.append(
            GlobalSettings(
                AssumedGamma(1.0)
            )
        )
        fix.append(
            Default(
                Finish(
                    Ambient(0.1),
                    Diffuse(0.9)
                )
            )
        )

        msg = '\n' + ''.join(difflib.ndiff(
            ref.splitlines(1),
            str(fix).splitlines(1)
        ))

        self.assertEqual(ref, str(fix), msg)
