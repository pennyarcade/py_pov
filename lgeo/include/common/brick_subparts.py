"""
Persistence of Vision Ray Tracer Scene Description File
File: custom_macros.inc
Vers: 3.6
Desc: include file with macros to simplify placing of bricks
Link: -
Date: 04/2013
Auth: Chocokiko
"""

# ****************************************************************************
# LGEO Disclaimer
# Well, it is possible but not recommended. LGEO uses a different coordinate
# system and scaling than LDRAW, so it may be pretty hard to build a model by
# placing the parts by hand. In LGEO, for historic reasons Y axis is the depth
# axis, and Z is the up axis, where also Z has switched sign to LDRAW Y axis.
# Sorry for that, but my understanding of coordinate to this time was a flat
# standard XY coordinate system with a third Z axis coming out of the plane.
# Scaling is to real measurements, where 1 POV-Ray unit is 10mm. So 0.8 is 20
# LDU (width of a LEGO brick) and 0.96 is 24 LDU (height of a LEGO brick).
# ****************************************************************************

from pov.basic.Vector import Vector

from pov.csg.Union import Union

from pov.finite_solid.Box import Box

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from pov.other.Object import Object

from lgeo.include.common.lg_defs import LG_WALL_WIDTH, LG_BRICK_WIDTH
from lgeo.include.common.lg_defs import LG_PLATE_INNER_HEIGHT, LG_CORNER_SPACE
from lgeo.include.common.lg_defs import LG_BRICK_INNER_HEIGHT
from lgeo.include.common.lg_defs import lg_knob_inner_space, lg_knob
from lgeo.include.common.lg_defs import LG_BRICK_HEIGHT, lg_brick_column

# **************************************************************************
# LGEO Standard Brick common subparts
# **************************************************************************


def get_knob_inner_space(length=1, width=1):
    """@Todo: DocString."""
    result = Union(
        Box(
            Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_CORNER_SPACE),
            Vector(
                length * LG_BRICK_WIDTH-LG_WALL_WIDTH,
                width * LG_BRICK_WIDTH-LG_WALL_WIDTH,
                LG_PLATE_INNER_HEIGHT
            )
        )
    )

    ks_x = 0
    while ks_x < length:
        ks_y = 0
        while ks_y < width:
            result.append(
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            (ks_x + 0.5) * LG_BRICK_WIDTH,
                            (ks_y + 0.5) * LG_BRICK_WIDTH,
                            LG_BRICK_INNER_HEIGHT
                        )
                    )
                )
            )
            ks_y = ks_y + 1
        ks_x = ks_x + 1

    return result


def get_knob_objects(length=1, width=1, height=LG_BRICK_HEIGHT):
    """@Todo: DocString."""
    result = Union()

    knob_x = 0
    while knob_x < length:
        knob_y = 0
        while knob_y < width:
            result.append(
                Object(
                    lg_knob(),
                    Rotate(Vector(0, 0, -90)),
                    Translate(
                        Vector(
                            (0.5 + knob_x) * LG_BRICK_WIDTH,
                            (0.5 + knob_y) * LG_BRICK_WIDTH,
                            height
                        )
                    ),
                )
            )
            knob_y = knob_y + 1
        knob_x = knob_x + 1

    return result


def get_brick_coloumn(length=1):
    """@Todo: DocString."""
    result = Union()

    col_x = 1
    while col_x < length:
        result.append(
            Object(
                lg_brick_column,
                Translate(
                    Vector(
                        col_x * LG_BRICK_WIDTH,
                        0.5 * LG_BRICK_WIDTH,
                        0
                    )
                ),
            )
        )
        col_x = col_x + 1

    return result
