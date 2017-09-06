"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970623 Lutz Uhlmann
20071226 Lutz Uhlmann fixed stud orientation

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_3710: Brick 1 x 4

"""

from lgeo.include.common.brick_subparts import get_knob_inner_space
from lgeo.include.common.brick_subparts import get_knob_objects
from lgeo.include.common.lg_defs import LGCS, LGBW, LGPH

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

# from pov.other.Object import Object


# FIXME: refactor into general function for brick bars
def solid(length=4, width=1):
    """return lg_3710: Brick 1 x 4."""
    return Union(
        Sphere(
            Vector(LGCS, LGCS, LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGCS, LGCS),
            Vector(
                length * LGBW - LGCS,
                LGCS,
                LGCS
            ),
            LGCS
        ),
        Sphere(
            Vector(
                length * LGBW - LGCS,
                LGCS,
                LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(
                length * LGBW - LGCS,
                LGCS,
                LGCS
            ),
            Vector(
                length * LGBW - LGCS,
                LGCS,
                LGPH - LGCS
            ),
            LGCS
        ),
        Sphere(
            Vector(
                length * LGBW - LGCS,
                LGCS,
                LGPH - LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(
                length * LGBW - LGCS,
                LGCS,
                LGPH - LGCS
            ),
            Vector(
                LGCS,
                LGCS,
                LGPH - LGCS
            ),
            LGCS
        ),
        Sphere(
            Vector(
                LGCS,
                LGCS,
                LGPH - LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(
                LGCS,
                LGCS,
                LGCS
            ),
            Vector(
                LGCS,
                LGCS,
                LGPH - LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(
                LGCS,
                LGCS,
                LGCS
            ),
            Vector(
                LGCS,
                width * LGBW - LGCS,
                LGCS
            ),
            LGCS
        ),
        Sphere(
            Vector(
                LGCS,
                width * LGBW - LGCS,
                LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(
                LGCS,
                width * LGBW - LGCS,
                LGCS
            ),
            Vector(
                LGCS,
                width * LGBW - LGCS,
                LGPH - LGCS
            ),
            LGCS
        ),
        Sphere(
            Vector(
                LGCS,
                width * LGBW - LGCS,
                LGPH - LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(
                LGCS,
                LGCS,
                LGPH - LGCS
            ),
            Vector(
                LGCS,
                width * LGBW - LGCS,
                LGPH - LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(
                length * LGBW - LGCS,
                LGCS,
                LGCS
            ),
            Vector(
                length * LGBW - LGCS,
                width * LGBW - LGCS,
                LGCS
            ),
            LGCS
        ),
        Sphere(
            Vector(
                length * LGBW - LGCS,
                width * LGBW - LGCS,
                LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(
                length * LGBW - LGCS,
                width * LGBW - LGCS,
                LGCS
            ),
            Vector(
                LGCS,
                width * LGBW - LGCS,
                LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(
                length * LGBW - LGCS,
                width * LGBW - LGCS,
                LGCS
            ),
            Vector(
                length * LGBW - LGCS,
                width * LGBW - LGCS,
                LGPH - LGCS
            ),
            LGCS
        ),
        Sphere(
            Vector(
                length * LGBW - LGCS,
                width * LGBW - LGCS,
                LGPH - LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(
                length * LGBW - LGCS,
                width * LGBW - LGCS,
                LGPH - LGCS
            ),
            Vector(
                LGCS,
                width * LGBW - LGCS,
                LGPH - LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(
                length * LGBW - LGCS,
                LGCS,
                LGPH - LGCS
            ),
            Vector(
                length * LGBW - LGCS,
                width * LGBW - LGCS,
                LGPH - LGCS
            ),
            LGCS
        ),
        Difference(
            Union(
                Box(
                    Vector(LGCS, LGCS, 0),
                    Vector(
                        length * LGBW - LGCS,
                        width * LGBW - LGCS,
                        LGPH
                    ),
                ),
                Box(
                    Vector(0, LGCS, LGCS),
                    Vector(
                        length * LGBW,
                        width * LGBW - LGCS,
                        LGPH - LGCS
                    ),
                ),
                Box(
                    Vector(LGCS, 0, LGCS),
                    Vector(
                        length * LGBW - LGCS,
                        width * LGBW,
                        LGPH - LGCS
                    ),
                ),
            ),
            get_knob_inner_space(length, width)
        ),
        # LG_PLATE_COLUMN,
        get_knob_objects(length, width, LGPH),
        Translate(
            Vector(
                -length / 2 * LGBW,
                -LGBW / 2,
                -LGPH
            )
        ),
        Rotate(Vector(0, 0, 90))
    )


# #declare lg_3010_clear =
# Merge(
#  Sphere(
#   Vector(LGCS, LGCS,
#     LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS, LGCS),
#   Vector((length * LGBW - LGCS),
#     LGCS, LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector((length * LGBW - LGCS),
#     LGCS, LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS),
#     LGCS, LGCS),
#   Vector(((length * LGBW)-LGCS),
#     LGCS, (LGPH - LGCS)),
#   LGCS
#  ),
#  Sphere(
#   Vector(((length * LGBW)-LGCS),
#     LGCS, (LGPH - LGCS)), LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS),
#     LGCS, (LGPH - LGCS)),
#   Vector(LGCS, LGCS, (LGPH - LGCS)),
#   LGCS
#  ),
#  Sphere(
#   Vector(LGCS, LGCS,
#     (LGPH - LGCS)), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS,
#     LGCS),
#   Vector(LGCS, LGCS,
#     (LGPH - LGCS)),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS, LGCS),
#   Vector(LGCS,
#     ((width * LGBW)-LGCS), LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     LGCS),
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     (LGPH - LGCS)),
#   LGCS
#  ),
#  Sphere(
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     (LGPH - LGCS)), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS,
#     (LGPH - LGCS)),
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     (LGPH - LGCS)),
#   LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS),
#     LGCS, LGCS),
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS), LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS), LGCS),
# LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS), LGCS),
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS), LGCS),
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS),
#     (LGPH - LGCS)),
#   LGCS
#  ),
#  Sphere(
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS),
#     (LGPH - LGCS)), LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS),
#     (LGPH - LGCS)),
#   Vector(LGCS,
#     ((width * LGBW)-LGCS),
#     (LGPH - LGCS)),
#   LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS),
#     LGCS, (LGPH - LGCS)),
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS),
#     (LGPH - LGCS)),
#   LGCS
#  ),
#  Difference(
#   Merge(
#    Box(
#     Vector(LGCS, LGCS, 0),
#     Vector(length * LGBW - LGCS,
#       width * LGBW - LGCS, LGPH),
#    ),
#    Box(
#     Vector(0, LGCS, LGCS),
#     Vector(length * LGBW,
#       width * LGBW - LGCS,
#       LGPH - LGCS),
#    ),
#    Box(
#     Vector(LGCS, 0, LGCS),
#     Vector(length * LGBW - LGCS,
#       width * LGBW, LGPH - LGCS),
#    ),
#   ),
#   Merge(
#    Box(
#     Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LGCS),
#     Vector(length * LGBW - LG_WALL_WIDTH,
#       width * LGBW - LG_WALL_WIDTH, LG_BRICK_INNER_HEIGHT),
#    ),
#    #declare KS_X = 0;
#    #while (KS_X Vector( length)
#     Object(
#      lg_knob()_inner_space_clear
#      Translate(Vector((KS_X+0.5)*LGBW,
#       0.5*LGBW, LG_BRICK_INNER_HEIGHT),
#     ),
#     #declare KS_X = KS_X + 1;
#    #end
#   ),
#  ),
#  #declare COL_X = 1;
#  #while (COL_X Vector( length)
#   Object(
#    lg_brick_column_clear
#    Translate(Vector(COL_X*LGBW, 0.5*LGBW, 0),
#   ),
#   #declare COL_X = COL_X + 1;
#  #end
#  #declare KNOB_X = 0;
#  #while (KNOB_X Vector( length)
#   Object(
#    lg_knob()_clear
#    Rotate(Vector(0, 0, -90),
#    Translate(Vector((0.5+KNOB_X)*LGBW,
#     0.5*LGBW, LGPH),
#   ),
#   #declare KNOB_X = KNOB_X + 1;
#  #end
#  Translate(Vector(-length/2*LGBW,
#   -LGBW/2,-LGPH),
#  Rotate(Vector(0,0,90),
# ),
