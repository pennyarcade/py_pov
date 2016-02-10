"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970623 Lutz Uhlmann
20071225 Lutz Uhlmann fixed stud orientation

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_3003: Brick 2 x 2
"""

from lgeo.include.common.brick_subparts import get_knob_objects
from lgeo.include.common.brick_subparts import get_knob_inner_space
from lgeo.include.common.lg_defs import LG_CORNER_SPACE, lg_brick_cylinder
from lgeo.include.common.lg_defs import LGBW
from lgeo.include.common.lg_defs import LGBH

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from pov.other.Object import Object


def solid(length=2, width=2):
    """@Todo: DocString."""
    return Union(
        Sphere(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
            Vector(
                LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                width * LGBW - LG_CORNER_SPACE,
                LGBH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Difference(
            Union(
                Box(
                    Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, 0),
                    Vector(
                        length * LGBW - LG_CORNER_SPACE,
                        width * LGBW - LG_CORNER_SPACE,
                        LGBH
                    ),
                ),
                Box(
                    Vector(0, 0, LG_CORNER_SPACE),
                    Vector(
                        length * LGBW,
                        width * LGBW,
                        LGBH - LG_CORNER_SPACE
                    )
                )
            ),
            get_knob_inner_space(length, width)
        ),
        Object(
            lg_brick_cylinder,
            Translate(Vector(LGBW, LGBW, 0))
        ),
        get_knob_objects(length, width),
        Translate(Vector(-LGBW, -LGBW, -LGBH)),
        Rotate(Vector(0, 0, 90))
    )


# #declare lg_3003_clear =
# Merge(
#  Sphere(
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
#   Vector((length * LGBW - LG_CORNER_SPACE), LG_CORNER_SPACE,
#     LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector((length * LGBW - LG_CORNER_SPACE), LG_CORNER_SPACE,
#     LG_CORNER_SPACE), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LG_CORNER_SPACE), LG_CORNER_SPACE,
#     LG_CORNER_SPACE),
#   Vector(((length * LGBW)-LG_CORNER_SPACE), LG_CORNER_SPACE,
#     (LGBH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(((length * LGBW)-LG_CORNER_SPACE), LG_CORNER_SPACE,
#     (LGBH - LG_CORNER_SPACE)), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LG_CORNER_SPACE), LG_CORNER_SPACE,
#     (LGBH - LG_CORNER_SPACE)),
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
#     (LGBH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
#     (LGBH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
#     (LGBH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
#   Vector(LG_CORNER_SPACE, ((width * LGBW)-LG_CORNER_SPACE),
#     LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(LG_CORNER_SPACE, ((width * LGBW)-LG_CORNER_SPACE),
#     LG_CORNER_SPACE), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, ((width * LGBW)-LG_CORNER_SPACE),
#     LG_CORNER_SPACE),
#   Vector(LG_CORNER_SPACE, ((width * LGBW)-LG_CORNER_SPACE),
#     (LGBH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(LG_CORNER_SPACE, ((width * LGBW)-LG_CORNER_SPACE),
#     (LGBH - LG_CORNER_SPACE)), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
#     (LGBH - LG_CORNER_SPACE)),
#   Vector(LG_CORNER_SPACE, ((width * LGBW)-LG_CORNER_SPACE),
#     (LGBH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LG_CORNER_SPACE), LG_CORNER_SPACE,
#     LG_CORNER_SPACE),
#   Vector(((length * LGBW)-LG_CORNER_SPACE),
#     ((width * LGBW)-LG_CORNER_SPACE), LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(((length * LGBW)-LG_CORNER_SPACE),
#     ((width * LGBW)-LG_CORNER_SPACE), LG_CORNER_SPACE),
# LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LG_CORNER_SPACE),
#     ((width * LGBW)-LG_CORNER_SPACE), LG_CORNER_SPACE),
#   Vector(LG_CORNER_SPACE, ((width * LGBW)-LG_CORNER_SPACE),
#     LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LG_CORNER_SPACE),
#     ((width * LGBW)-LG_CORNER_SPACE), LG_CORNER_SPACE),
#   Vector(((length * LGBW)-LG_CORNER_SPACE),
#     ((width * LGBW)-LG_CORNER_SPACE),
#     (LGBH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(((length * LGBW)-LG_CORNER_SPACE),
#     ((width * LGBW)-LG_CORNER_SPACE),
#     (LGBH - LG_CORNER_SPACE)), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LG_CORNER_SPACE),
#     ((width * LGBW)-LG_CORNER_SPACE),
#     (LGBH - LG_CORNER_SPACE)),
#   Vector(LG_CORNER_SPACE, ((width * LGBW)-LG_CORNER_SPACE),
#     (LGBH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LG_CORNER_SPACE),
#     LG_CORNER_SPACE, (LGBH - LG_CORNER_SPACE)),
#   Vector(((length * LGBW)-LG_CORNER_SPACE),
#     ((width * LGBW)-LG_CORNER_SPACE),
#     (LGBH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Difference(
#   Merge(
#    Box(
#     Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, 0),
#     Vector(length * LGBW - LG_CORNER_SPACE,
#       width * LGBW - LG_CORNER_SPACE, LGBH),
#    ),
#    Box(
#     Vector(0, 0, LG_CORNER_SPACE),
#     Vector(length * LGBW, width * LGBW,
#       LGBH - LG_CORNER_SPACE),
#    ),
#   ),
#   Merge(
#    Box(
#     Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_CORNER_SPACE),
#     Vector(length * LGBW - LG_WALL_WIDTH,
#       width * LGBW - LG_WALL_WIDTH, LG_BRICK_INNER_HEIGHT),
#    ),
#    #declare KS_X = 0;
#    #while (KS_X Vector( length)
#     #declare KS_Y = 0;
#     #while (KS_Y Vector( width)
#      Object(
#       lg_knob_inner_space_clear
#       Translate(Vector((KS_X+0.5)*LGBW,
#         (KS_Y+0.5)*LGBW, LG_BRICK_INNER_HEIGHT),
#      ),
#      #declare KS_Y = KS_Y + 1;
#      #end
#     #declare KS_X = KS_X + 1;
#    #end
#   ),
#  ),
#  Object(
#   lg_brick_cylinder_clear
#   Translate(Vector(LGBW, LGBW, 0),
#  ),
#  #declare KNOB_X = 0;
#  #while (KNOB_X Vector( length)
#   #declare KNOB_Y = 0;
#   #while (KNOB_Y Vector( width)
#    Object(
#     lg_knob_clear
#     Rotate(Vector(0, 0, -90),
#     Translate(Vector((0.5+KNOB_X)*LGBW,
#       (0.5+KNOB_Y)*LGBW, LGBH),
#    ),
#    #declare KNOB_Y = KNOB_Y + 1;
#   #end
#   #declare KNOB_X = KNOB_X + 1;
#  #end
#  Translate(Vector(-LGBW,-LGBW,-LGBH),
#  Rotate(Vector(0,0,90),
# )
