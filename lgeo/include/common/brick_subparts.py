'''***************************************************************************
 Persistence of Vision Ray Tracer Scene Description File
 File: custom_macros.inc
 Vers: 3.6
 Desc: include file with macros to simplify placing of bricks
 Link: -
 Date: 04/2013
 Auth: Chocokiko
**************************************************************************'''

'''**************************************************************************
LGEO Disclaimer
Well, it is possible but not recommended. LGEO uses a different coordinate
system and scaling than LDRAW, so it may be pretty hard to build a model by
placing the parts by hand. In LGEO, for historic reasons Y axis is the depth
axis, and Z is the up axis, where also Z has switched sign to LDRAW Y axis.
Sorry for that, but my understanding of coordinate to this time was a flat
standard XY coordinate system with a third Z axis coming out of the plane.
Scaling is to real measurements, where 1 POV-Ray unit is 10mm. So 0.8 is 20
LDU (width of a LEGO brick) and 0.96 is 24 LDU (height of a LEGO brick).
***************************************************************************'''

from pov.basic.Vector import Vector

from pov.csg.Union import Union

from pov.finite_solid.Box import Box

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from pov.other.Object import Object

from lgeo.include.common.lg_defs import LG_WALL_WIDTH, LG_BRICK_WIDTH
from lgeo.include.common.lg_defs import LG_PLATE_INNER_HEIGHT, LG_CORNER_SPACE
from lgeo.include.common.lg_defs import LG_BRICK_INNER_HEIGHT

'''**************************************************************************
LGEO Standard Brick common subparts
**************************************************************************'''


def get_knob_inner_space(length=1, width=1):
    result = Union(
        Box(
            Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_CORNER_SPACE),
            Vector(
                length*LG_BRICK_WIDTH-LG_WALL_WIDTH,
                width*LG_BRICK_WIDTH-LG_WALL_WIDTH,
                LG_PLATE_INNER_HEIGHT
            )
        )
    )

    KS_X = 0
    while (KS_X < length):
        KS_Y = 0
        while (KS_Y < width):
            result.append(
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            (KS_X+0.5)*LG_BRICK_WIDTH,
                            (KS_Y+0.5)*LG_BRICK_WIDTH,
                            LG_BRICK_INNER_HEIGHT
                        )
                    )
                )
            )
            KS_Y = KS_Y + 1
        KS_X = KS_X + 1

    return result


def get_knob_objects(length=1, width=1, height=LG_BRICK_HEIGHT):
    result = Union()

    KNOB_X = 0
    while (KNOB_X < length):
        KNOB_Y = 0
        while (KNOB_Y < width):
            result.append(
                Object(
                    lg_knob(),
                    Rotate(Vector(0, 0, -90)),
                    Translate(
                        Vector(
                            (0.5+KNOB_X)*LG_BRICK_WIDTH,
                            (0.5+KNOB_Y)*LG_BRICK_WIDTH,
                            height
                        )
                    ),
                )
            )
            KNOB_Y = KNOB_Y + 1
        KNOB_X = KNOB_X + 1

    return result


def get_brick_coloumn(length=1):
    result = Union()

    COL_X = 1
    while (COL_X < length):
        result.append(
            Object(
                lg_brick_column,
                Translate(
                    Vector(
                        COL_X*LG_BRICK_WIDTH,
                        0.5*LG_BRICK_WIDTH,
                        0
                    )
                ),
            )
        )
        COL_X = COL_X + 1

    return result
