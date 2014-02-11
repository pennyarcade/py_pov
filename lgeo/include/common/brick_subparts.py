'''*****************************************************************************
 Persistence of Vision Ray Tracer Scene Description File
 File: custom_macros.inc
 Vers: 3.6
 Desc: include file with macros to simplify placing of bricks
 Link: -
 Date: 04/2013
 Auth: Chocokiko
**************************************************************************'''

'''*****************************************************************************
LGEO Disclaimer
Well, it is possible but not recommended. LGEO uses a different coordinate
system and scaling than LDRAW, so it may be pretty hard to build a model by
placing the parts by hand. In LGEO, for historic reasons Y axis is the depth
axis, and Z is the up axis, where also Z has switched sign to LDRAW Y axis.
Sorry for that, but my understanding of coordinate to this time was a flat
standard XY coordinate system with a third Z axis coming out of the plane.
Scaling is to real measurements, where 1 POV-Ray unit is 10mm. So 0.8 is 20 LDU
(width of a LEGO brick) and 0.96 is 24 LDU (height of a LEGO brick).
*****************************************************************************'''

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from pov.other.Object import Object

from lgeo.include.common.lg_defs import *

'''*****************************************************************************
LGEO Standard Brick common subparts
*****************************************************************************'''


def get_knob_inner_space(LENGTH=1, WIDTH=1):
    return Union(
        Box(
            Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_CORNER_SPACE),
            Vector(LENGTH*LG_BRICK_WIDTH-LG_WALL_WIDTH, WIDTH*LG_BRICK_WIDTH-LG_WALL_WIDTH, LG_PLATE_INNER_HEIGHT)
        )
    )
