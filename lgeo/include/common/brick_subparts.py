"""
Persistence of Vision Ray Tracer Scene Description File.

File: custom_macros.inc
Vers: 3.6
Desc: include file with macros to simplify placing of bricks
Link: -
Date: 04/2013
Auth: Chocokiko

LGEO Disclaimer
Well, it is possible but not recommended. LGEO uses a different coordinate
system and scaling than LDRAW, so it may be pretty hard to build a model by
placing the parts by hand. In LGEO, for historic reasons Y axis is the depth
axis, and Z is the up axis, where also Z has switched sign to LDRAW Y axis.
Sorry for that, but my understanding of coordinate to this time was a flat
standard XY coordinate system with a third Z axis coming out of the plane.
Scaling is to real measurements, where 1 POV-Ray unit is 10mm. So 0.8 is 20
LDU (width of a LEGO brick) and 0.96 is 24 LDU (height of a LEGO brick).

"""

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference

from pov.finite_solid.Sphere import Sphere
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Box import Box

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from pov.other.Object import Object

from lgeo.include.common.lg_defs import LG_WALL_WIDTH, LGBW, LGPH
from lgeo.include.common.lg_defs import LG_PLATE_INNER_HEIGHT, LGCS
from lgeo.include.common.lg_defs import LG_BRICK_INNER_HEIGHT
from lgeo.include.common.lg_defs import lg_knob_inner_space, lg_knob
from lgeo.include.common.lg_defs import LGBH, lg_brick_column
from lgeo.include.common.lg_defs import get_lg_cylinder

# **************************************************************************
# LGEO Standard Brick common subparts
# **************************************************************************


def get_knob_inner_space(length=1, width=1, height=LG_BRICK_INNER_HEIGHT):
    """@Todo: DocString."""
    result = Union(
        Box(
            Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LGCS),
            Vector(
                length * LGBW - LG_WALL_WIDTH,
                width * LGBW - LG_WALL_WIDTH,
                LG_PLATE_INNER_HEIGHT
            )
        )
    )

    for ks_x in range(0, length):
        for ks_y in range(0, width):
            result.append(
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            (ks_x + 0.5) * LGBW,
                            (ks_y + 0.5) * LGBW,
                            height
                        )
                    )
                )
            )

    return result


def get_knob_objects(length=1, width=1, height=LGBH):
    """@Todo: DocString."""
    result = Union()

    for knob_x in range(0, length):
        for knob_y in range(0, width):
            result.append(
                Object(
                    lg_knob(),
                    Rotate(Vector(0, 0, -90)),
                    Translate(
                        Vector(
                            (0.5 + knob_x) * LGBW,
                            (0.5 + knob_y) * LGBW,
                            height
                        )
                    ),
                )
            )

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
                        col_x * LGBW,
                        0.5 * LGBW,
                        0
                    )
                ),
            )
        )
        col_x = col_x + 1

    return result


def get_cylinder(
    length=1,
    width=1,
    cclass=Union,
    height=LG_PLATE_INNER_HEIGHT
):
    """Return Plate Cylinder"""
    result = cclass()

    for cyl_x in range(1, length):
        for cyl_y in range(1, width):
            result.append(
                Object(
                    get_lg_cylinder(cclass, height),
                    Translate(Vector(cyl_x * LGBW, cyl_y * LGBW, 0))
                )
            )

    return result


def standard_plate(
    length=1,
    width=1,
    height=LGPH,
    innerheight=LG_PLATE_INNER_HEIGHT
):
    """Standard plate brick"""
    return Union(
        Sphere(
            Vector(LGCS, LGCS, LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGCS, LGCS),
            Vector(length * LGBW - LGCS, LGCS, LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, LGCS, LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGCS, LGCS),
            Vector(length * LGBW - LGCS, LGCS, height - LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, LGCS, height - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGCS, height - LGCS),
            Vector(LGCS, LGCS, height - LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGCS, LGCS, height - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGCS, LGCS),
            Vector(LGCS, LGCS, height - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGCS, LGCS),
            Vector(LGCS, width * LGBW - LGCS, LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGCS, width * LGBW - LGCS, LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, width * LGBW - LGCS, LGCS),
            Vector(LGCS, width * LGBW - LGCS, height - LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGCS, width * LGBW - LGCS, height - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGCS, height - LGCS),
            Vector(LGCS, width * LGBW - LGCS, height - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGCS, LGCS),
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGCS),
            Vector(LGCS, width * LGBW - LGCS, LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGCS),
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, height - LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, height - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, height - LGCS),
            Vector(LGCS, width * LGBW - LGCS, height - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGCS, height - LGCS),
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, height - LGCS),
            LGCS
        ),
        Difference(
            Union(
                Box(
                    Vector(LGCS, LGCS, 0),
                    Vector(length * LGBW - LGCS, width * LGBW - LGCS, height)
                ),
                Box(
                    Vector(0, LGCS, LGCS),
                    Vector(length * LGBW, width * LGBW - LGCS, height - LGCS)
                ),
                Box(
                    Vector(LGCS, 0, LGCS),
                    Vector(length * LGBW - LGCS, width * LGBW, height - LGCS)
                ),
            ),
            get_knob_inner_space(length, width)
        ),
        get_cylinder(length, width, Union, innerheight),
        get_knob_objects(length, width, height),
        Translate(
            Vector(-length / 2 * LGBW, -LGBW, -height)
        ),
        Rotate(Vector(0, 0, 90))
    )
