"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970623 Lutz Uhlmann

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_3069b: Tile 1 x 2 with groove
"""

from lgeo.include.common.lg_defs import LGCS, LGBW, LGPH, LG_E
from lgeo.include.common.lg_defs import LGWW, LG_PLATE_INNER_HEIGHT

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate


def solid(length=2, width=1):
    """return lg_3069b: Tile 1 x 2 with groove."""
    return Union(
        Sphere(
            Vector(LGCS, LGCS, LGCS + 0.04),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGCS, LGCS + 0.04),
            Vector(length * LGBW - LGCS, LGCS, LGCS + 0.04),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, LGCS, LGCS + 0.04), 
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGCS, LGCS + 0.04),
            Vector(length * LGBW - LGCS, LGCS, LGPH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, LGCS, LGPH - LGCS), 
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGCS, LGPH - LGCS),
            Vector(LGCS, LGCS, LGPH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGCS, LGCS, LGPH - LGCS), 
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGCS, LGCS + 0.04),
            Vector(LGCS, LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGCS, LGCS + 0.04),
            Vector(LGCS, width * LGBW - LGCS, LGCS + 0.04),
            LGCS
        ),
        Sphere(
            Vector(LGCS, width * LGBW - LGCS, LGCS + 0.04), 
            LGCS
        ),
        Cylinder(
            Vector(LGCS, width * LGBW - LGCS, LGCS + 0.04),
            Vector(LGCS, width * LGBW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGCS, width * LGBW - LGCS, LGPH - LGCS), 
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGCS, LGPH - LGCS),
            Vector(LGCS, width * LGBW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGCS, LGCS + 0.04),
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGCS + 0.04),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGCS + 0.04),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGCS + 0.04),
            Vector(LGCS, width * LGBW - LGCS, LGCS + 0.04),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGCS + 0.04),
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGPH - LGCS),
            Vector(LGCS, width * LGBW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGCS, LGPH - LGCS),
            Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Difference(
            Union(
                Box(
                    Vector(LGCS, LGCS, 0.04),
                    Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGPH)
                ),
                Box(
                    Vector(LGCS, 0, LGCS + 0.04),
                    Vector(length * LGBW - LGCS, width * LGBW, LGPH - LGCS)
                ),
                Box(
                    Vector(0, LGCS, LGCS + 0.04),
                    Vector(length * LGBW, width * LGBW - LGCS, LGPH - LGCS)
                ),
                Box(
                    Vector(0.04, 0.04, 0),
                    Vector(length * LGBW - 0.04, width * LGBW - 0.04, 0.04 + LG_E)
                ),
            ),
            Box(
                Vector(LGWW, LGWW, -LGCS),
                Vector(length * LGBW - LGWW, width * LGBW - LGWW, LG_PLATE_INNER_HEIGHT)
            ),
        ),
        Translate(Vector(-LGBW, -0.5 * LGBW, -LGPH)),
        Rotate(Vector(0, 0, 90))
    )

# #declare lg_3069b_clear =
# merge {
#  Sphere(
#   Vector(LGCS, LGCS, LGCS + 0.04), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS, LGCS + 0.04),
#   Vector(length * LGBW - LGCS, LGCS, LGCS + 0.04),
#   LGCS
#  ),
#  Sphere(
#   Vector(length * LGBW - LGCS, LGCS, LGCS + 0.04), LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS, LGCS, LGCS + 0.04),
#   Vector(length * LGBW - LGCS, LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(length * LGBW - LGCS, LGCS, LGPH - LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS, LGCS, LGPH - LGCS),
#   Vector(LGCS, LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(LGCS, LGCS, LGPH - LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS, LGCS + 0.04),
#   Vector(LGCS, LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS, LGCS + 0.04),
#   Vector(LGCS, width * LGBW - LGCS, LGCS + 0.04),
#   LGCS
#  ),
#  Sphere(
#   Vector(LGCS, width * LGBW - LGCS, LGCS + 0.04), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, width * LGBW - LGCS, LGCS + 0.04),
#   Vector(LGCS, width * LGBW - LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(LGCS, width * LGBW - LGCS, LGPH - LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS, LGPH - LGCS),
#   Vector(LGCS, width * LGBW - LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS, LGCS, LGCS + 0.04),
#   Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGCS + 0.04),
#   LGCS
#  ),
#  Sphere(
#   Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGCS + 0.04),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGCS + 0.04),
#   Vector(LGCS, width * LGBW - LGCS, LGCS + 0.04),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGCS + 0.04),
#   Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGPH - LGCS),
#   Vector(LGCS, width * LGBW - LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS, LGCS, LGPH - LGCS),
#   Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Difference(
#   merge {
#    Box(
#     Vector(LGCS, LGCS, 0.04),
#     Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGPH)
#    ),
#    Box(
#     Vector(LGCS, 0, LGCS + 0.04),
#     Vector(length * LGBW - LGCS, width * LGBW, LGPH - LGCS)
#    ),
#    Box(
#     Vector(0, LGCS, LGCS + 0.04),
#     Vector(length * LGBW, width * LGBW - LGCS, LGPH - LGCS)
#    ),
#    Box(
#     Vector(0.04, 0.04, 0),
#     Vector((length * LGBW-0.04), (width * LGBW-0.04), 0.04+LG_E)
#    ),
#   ),
#   Box(
#    Vector(LG_WALL_width, LG_WALL_width, -LGCS),
#    Vector(
#        length * LGBW - LG_WALL_width,
#        width * LGBW - LG_WALL_width,
#        LG_PLATE_INNER_HEIGHT
#    )
#   ),
#  ),
#  Translate(Vector(-LGBW, -0.5*LGBW, -LGPH)
#  Rotate(Vector(0, 0, 90)
# ),

# #end
