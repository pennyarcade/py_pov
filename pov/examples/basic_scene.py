'''
// Persistence of Vision Ray Tracer Scene Description File
// File: ?.pov
// Vers: 3.6
// Desc: Basic Scene Example
// Date: mm/dd/yy
// Auth: ?
//

#version 3.6;

#include "colors.inc"

global_settings {
  assumed_gamma 1.0
}

// ----------------------------------------

camera {
  location  <0.0, 0.5, -4.0>
  direction 1.5*z
  right     x*image_width/image_height
  look_at   <0.0, 0.0,  0.0>
}

sky_sphere {
  pigment {
    gradient y
    color_map {
      [0.0 rgb <0.6,0.7,1.0>]
      [0.7 rgb <0.0,0.1,0.8>]
    }
  }
}

light_source {
  <0, 0, 0>            // light's position (translated below)
  color rgb <1, 1, 1>  // light's color
  translate <-30, 30, -30>
}

// ----------------------------------------

plane {
  y, -1
  pigment { color rgb <0.7,0.5,0.3> }
}

sphere {
  0.0, 1
  texture {
    pigment {
      radial
      frequency 8
      color_map {
        [0.00 color rgb <1.0,0.4,0.2> ]
        [0.33 color rgb <0.2,0.4,1.0> ]
        [0.66 color rgb <0.4,1.0,0.2> ]
        [1.00 color rgb <1.0,0.4,0.2> ]
      }
    }
    finish{
      specular 0.6
    }
  }
}
'''

from logging import *

from pov.atmeff.SkySphere import SkySphere
from pov.basic.SceneFile import SceneFile
from pov.basic.Vector import *
from pov.basic.Color import Color
from pov.global_settings.GlobalSettings import GlobalSettings
from pov.finite_solid.Sphere import Sphere
from pov.infinite_solid.Plane import Plane
from pov.language_directive.Version import Version
from pov.language_directive.Include import Include
from pov.other.Camera import Camera
from pov.other.LightSource import LightSource
from pov.texture.Finish import Finish
from pov.texture.Texture import Texture
from pov.texture.Pigment import Pigment
from pov.texture.ColorMap import ColorMap


fix = SceneFile('test.pov')
fix.append(Version(3.6))
fix.append(Include('colors.inc'))
fix.append(
    GlobalSettings(assumed_gamma=1.0)
)

#@TODO: Read from Config
image_width = 800
#@TODO: Read from Config
image_height = 600

fix.append(
    Camera(
        location=Vector(0.0, 0.5, -4.0),
        direction=1.5 * z,
        right=x*image_width/image_height,
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

print str(fix)