"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19990514 Lutz Uhlmann

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_4865: Panel 1 x 2 x 1
"""


from lgeo.include.common.lg_defs import LGCS, LGBW, LGPH, LG_E, LGBH
from lgeo.include.common.lg_defs import LGWW
from lgeo.include.common.lg_defs import LG_TOP_HEIGHT, LG_PLATE_COLUMN

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from pov.other.Object import Object


def solid(length=1, width=2, height=1):
    """return lg_4865: Panel 1 x 2 x 1."""
    result = Union(
    )

    for rot in range(0, 2):
        rotation = Rotate(Vector(0, 0, 0))
        translation = Translate(Vector(0, 0, 0))
        if rot == 1:
            rotation = Rotate(Vector(0, 0, 180))
            translation = Translate(Vector(-LGBW, 0, 0))

        result.append(
            Union(
                Sphere(
                    Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS, -height * LGBH + LGCS),
                    LGCS
                ),
                Sphere(
                    Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS, -height * LGBH + LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS, -height * LGBH + LGCS),
                    Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS, -height * LGBH + LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS, -height * LGBH + LGCS),
                    Vector(length / 2 * LGBW - LGCS, -width / 2 * LGBW + LGCS, -height * LGBH + LGCS),
                    LGCS
                ),
                rotation,
                translation
            ),
        )

    result.append(
        Union(
            Cylinder(
                Vector(-length / 2 * LGBW + LGWW - LGCS, width / 2 * LGBW - LGCS, -LGCS),
                Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS, -LGCS),
                LGCS
            ),
            Cylinder(
                Vector(-length / 2 * LGBW + LGWW - LGCS, -width / 2 * LGBW + LGCS, -LGCS),
                Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW + LGCS, -LGCS),
                LGCS
            ),
            Cylinder(
                Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS, -LGCS),
                Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW + LGCS, -LGCS),
                LGCS
            ),
            Cylinder(
                Vector(-length / 2 * LGBW + LGWW - LGCS, width / 2 * LGBW - LGCS, -LGCS),
                Vector(-length / 2 * LGBW + LGWW - LGCS, -width / 2 * LGBW + LGCS, -LGCS),
                LGCS
            ),
            Sphere(
                Vector(-length / 2 * LGBW + LGWW - LGCS, width / 2 * LGBW - LGCS, -LGCS),
                LGCS
            ),
            Sphere(
                Vector(-length / 2 * LGBW + LGWW - LGCS, -width / 2 * LGBW + LGCS, -LGCS),
                LGCS
            ),
            Sphere(
                Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS, -LGCS),
                LGCS
            ),
            Sphere(
                Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW + LGCS, -LGCS),
                LGCS
            ),
            Cylinder(
                Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS, -LGCS),
                Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS, -height * LGBH + LGCS),
                LGCS
            ),
            Cylinder(
                Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW + LGCS, -LGCS),
                Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW + LGCS, -height * LGBH + LGCS),
                LGCS
            ),
            Cylinder(
                Vector(-length / 2 * LGBW + LGWW - LGCS, -width / 2 * LGBW + LGCS, -LGCS),
                Vector(-length / 2 * LGBW + LGWW - LGCS, width / 2 * LGBW - LGCS, -LGCS),
                LGCS
            ),
            Cylinder(
                Vector(-length / 2 * LGBW - LGCS + LGWW, width / 2 * LGBW - LGCS, -(height * 3 - 1) * LGPH - LGCS),
                Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS, -(height * 3 - 1) * LGPH - LGCS),
                LGCS
            ),
            Cylinder(
                Vector(-length / 2 * LGBW - LGCS + LGWW, -width / 2 * LGBW + LGCS, -(height * 3 - 1) * LGPH - LGCS),
                Vector(length / 2 * LGBW - LGCS, -width / 2 * LGBW + LGCS, -(height * 3 - 1) * LGPH - LGCS),
                LGCS
            ),
            Cylinder(
                Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS, -(height * 3 - 1) * LGPH - LGCS),
                Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS, -height * LGBH + LGCS),
                LGCS
            ),
            Cylinder(
                Vector(length / 2 * LGBW - LGCS, -width / 2 * LGBW + LGCS, -(height * 3 - 1) * LGPH - LGCS),
                Vector(length / 2 * LGBW - LGCS, -width / 2 * LGBW + LGCS, -height * LGBH + LGCS),
                LGCS
            ),
            Cylinder(
                Vector(length / 2 * LGBW - LGCS, -width / 2 * LGBW + LGCS, -(height * 3 - 1) * LGPH - LGCS),
                Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS, -(height * 3 - 1) * LGPH - LGCS),
                LGCS
            ),
            Cylinder(
                Vector(-length / 2 * LGBW - LGCS + LGWW, width / 2 * LGBW - LGCS, -LGCS),
                Vector(-length / 2 * LGBW - LGCS + LGWW, width / 2 * LGBW - LGCS, -(height * 3 - 1) * LGPH - LGCS),
                LGCS
            ),
            Cylinder(
                Vector(-length / 2 * LGBW - LGCS + LGWW, -width / 2 * LGBW + LGCS, -LGCS),
                Vector(-length / 2 * LGBW - LGCS + LGWW, -width / 2 * LGBW + LGCS, -(height * 3 - 1) * LGPH - LGCS),
                LGCS
            ),
            Sphere(
                Vector(length / 2 * LGBW - LGCS, -width / 2 * LGBW + LGCS, -(height * 3 - 1) * LGPH - LGCS),
                LGCS
            ),
            Sphere(
                Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS, -(height * 3 - 1) * LGPH - LGCS),
                LGCS
            ),
            Difference(
                Union(
                    Box(
                        Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS, -height * LGBH + LGPH),
                        Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW + LGCS, -height * LGBH),
                    ),
                    Box(
                        Vector(length / 2 * LGBW, width / 2 * LGBW - LGCS, -height * LGBH + LGPH - LGCS),
                        Vector(-length / 2 * LGBW, -width / 2 * LGBW + LGCS, -height * LGBH + LGCS),
                    ),
                    Box(
                        Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW, -height * LGBH + LGPH - LGCS),
                        Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW, -height * LGBH + LGCS)
                    ),
                ),
                Box(
                    Vector(length / 2 * LGBW - LGWW, width / 2 * LGBW - LGWW, -height * LGBH + LGPH - LG_TOP_HEIGHT),
                    Vector(-length / 2 * LGBW + LGWW, -width / 2 * LGBW + LGWW, -height * LGBH - LG_E)
                ),
            ),
            Box(
                Vector(-length / 2 * LGBW, width / 2 * LGBW - LGCS, -LGCS),
                Vector(-length / 2 * LGBW + LGWW, -width / 2 * LGBW + LGCS, -height * LGBH + LGCS)
            ),
            Box(
                Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW, -LGCS),
                Vector(-length / 2 * LGBW + LGWW - LGCS, -width / 2 * LGBW, -height * LGBH + LGCS)
            ),
            Box(
                Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS, -2 * LGCS),
                Vector(-length / 2 * LGBW + LGWW - LGCS, -width / 2 * LGBW + LGCS, 0)
            ),
            Object(
                LG_PLATE_COLUMN,
                Translate(Vector(-LGBW / 2, 0, -height * LGBH))
            ),
        )
    )

    return result


# #declare lg_4865_clear =
# merge {
#  #declare ROT = 0;
#  #while (ROT Vector( 2)
#   merge {
#    Sphere(
#     Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS,
# -height * LGBH + LGCS), LGCS
#    ),
#    Sphere(
#     Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS,
# -height * LGBH + LGCS), LGCS
#    ),
#    Cylinder(
#     Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS,
# -height * LGBH + LGCS),
#     Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS,
# -height * LGBH + LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS,
# -height * LGBH + LGCS),
#     Vector(length / 2 * LGBW - LGCS, -width / 2 * LGBW + LGCS,
# -height * LGBH + LGCS),
#     LGCS
#    ),
#    #if (ROT=1)
#     rotate Vector(0, 0, 180)
#    #end
#   ),
#   #declare ROT = ROT + 1;
#  #end
#  Cylinder(
#   Vector(-length / 2 * LGBW + LG_WALL_WIDTH - LGCS,
# width / 2 * LGBW - LGCS, -LGCS),
#   Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length / 2 * LGBW + LG_WALL_WIDTH - LGCS,
# -width / 2 * LGBW + LGCS, -LGCS),
#   Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW + LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS, -LGCS),
#   Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW + LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length / 2 * LGBW + LG_WALL_WIDTH - LGCS,
# width / 2 * LGBW - LGCS, -LGCS),
#   Vector(-length / 2 * LGBW + LG_WALL_WIDTH - LGCS,
# -width / 2 * LGBW + LGCS, -LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(-length / 2 * LGBW + LG_WALL_WIDTH - LGCS,
# width / 2 * LGBW - LGCS, -LGCS), LGCS
#  ),
#  Sphere(
#   Vector(-length / 2 * LGBW + LG_WALL_WIDTH - LGCS,
# -width / 2 * LGBW + LGCS, -LGCS), LGCS
#  ),
#  Sphere(
#   Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS, -LGCS), LGCS
#  ),
#  Sphere(
#   Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW + LGCS, -LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS, -LGCS),
#   Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS,
# -height * LGBH + LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW + LGCS, -LGCS),
#   Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW + LGCS,
# -height * LGBH + LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length / 2 * LGBW + LG_WALL_WIDTH - LGCS,
# -width / 2 * LGBW + LGCS, -LGCS),
#   Vector(-length / 2 * LGBW + LG_WALL_WIDTH - LGCS,
# width / 2 * LGBW - LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length / 2 * LGBW - LGCS + LG_WALL_WIDTH,
# width / 2 * LGBW - LGCS, -(height * 3 - 1) * LGPH - LGCS),
#   Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS,
# -(height * 3 - 1) * LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length / 2 * LGBW - LGCS + LG_WALL_WIDTH,
# -width / 2 * LGBW + LGCS, -(height * 3 - 1) * LGPH - LGCS),
#   Vector(length / 2 * LGBW - LGCS, -width / 2 * LGBW + LGCS,
# -(height * 3 - 1) * LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS,
# -(height * 3 - 1) * LGPH - LGCS),
#   Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS,
# -height * LGBH + LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length / 2 * LGBW - LGCS, -width / 2 * LGBW + LGCS,
# -(height * 3 - 1) * LGPH - LGCS),
#   Vector(length / 2 * LGBW - LGCS, -width / 2 * LGBW + LGCS,
# -height * LGBH + LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length / 2 * LGBW - LGCS, -width / 2 * LGBW + LGCS,
# -(height * 3 - 1) * LGPH - LGCS),
#   Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS,
# -(height * 3 - 1) * LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length / 2 * LGBW - LGCS + LG_WALL_WIDTH,
# width / 2 * LGBW - LGCS, -LGCS),
#   Vector(-length / 2 * LGBW - LGCS + LG_WALL_WIDTH,
# width / 2 * LGBW - LGCS, -(height * 3 - 1) * LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length / 2 * LGBW - LGCS + LG_WALL_WIDTH,
# -width / 2 * LGBW + LGCS, -LGCS),
#   Vector(-length / 2 * LGBW - LGCS + LG_WALL_WIDTH,
# -width / 2 * LGBW + LGCS, -(height * 3 - 1) * LGPH - LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(length / 2 * LGBW - LGCS, -width / 2 * LGBW + LGCS,
# -(height * 3 - 1) * LGPH - LGCS),LGCS
#  ),
#  Sphere(
#   Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS,
# -(height * 3 - 1) * LGPH - LGCS),LGCS
#  ),
#  Difference(
#   merge {
#    Box(
#     Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW - LGCS,
# -height * LGBH + LGPH)
#     Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW + LGCS,
# -height * LGBH)
#    ),
#    Box(
#     Vector(length / 2 * LGBW, width / 2 * LGBW - LGCS,
# -height * LGBH + LGPH - LGCS)
#     Vector(-length / 2 * LGBW, -width / 2 * LGBW + LGCS,
# -height * LGBH + LGCS)
#    ),
#    Box(
#     Vector(length / 2 * LGBW - LGCS, width / 2 * LGBW,
# -height * LGBH + LGPH - LGCS)
#     Vector(-length / 2 * LGBW + LGCS, -width / 2 * LGBW,
# -height * LGBH + LGCS)
#    ),
#   ),
#   Box(
#    Vector(length / 2 * LGBW - LG_WALL_WIDTH,
# width / 2 * LGBW - LG_WALL_WIDTH, -height * LGBH + LGPH - LG_TOP_HEIGHT)
#    Vector(-length / 2 * LGBW + LG_WALL_WIDTH,
# -width / 2 * LGBW + LG_WALL_WIDTH, -height * LGBH - LG_E)
#   ),
#  ),
#  Box(
#   Vector(-length / 2 * LGBW, width / 2 * LGBW - LGCS, -LGCS)
#   Vector(-length / 2 * LGBW + LG_WALL_WIDTH, -width / 2 * LGBW + LGCS,
# -height * LGBH + LGCS)
#  ),
#  Box(
#   Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW, -LGCS)
#   Vector(-length / 2 * LGBW + LG_WALL_WIDTH - LGCS, -width / 2 * LGBW,
# -height * LGBH + LGCS)
#  ),
#  Box(
#   Vector(-length / 2 * LGBW + LGCS, width / 2 * LGBW - LGCS, -2*LGCS)
#   Vector(-length / 2 * LGBW + LG_WALL_WIDTH - LGCS,
# -width / 2 * LGBW + LGCS, 0)
#  ),
#  Object(
#   lg_plate_column_clear
#   Translate(Vector(0, 0, -height * LGBH)
#  ),
# ),

# #end
