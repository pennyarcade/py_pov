"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970815 Lutz Uhlmann

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_2357: Brick 2 x 2 Corner
"""

from math import sqrt

from lgeo.include.common.lg_defs import LGCS, LGBW, LG_E, LGBH, lg_knob
from lgeo.include.common.lg_defs import LG_WALL_WIDTH, LG_BRICK_INNER_HEIGHT
from lgeo.include.common.lg_defs import LG_BRICK_COLUMN
from lgeo.include.common.lg_defs import LG_KNOB_INNER_SPACE, LG_CYLINDER_RADIUS

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
    """return lg_4865: Panel 1 x 2 x 1."""
    result = Union(
        Sphere(
            Vector(LGCS, LGCS, LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGCS, LGCS),
            Vector((length * LGBW) - LGCS, LGCS, LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, LGCS, LGCS), LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGCS, LGCS),
            Vector(length * LGBW - LGCS, LGCS, LGBH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, LGCS, LGBH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGCS, LGBH - LGCS),
            Vector(LGCS, LGCS, LGBH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGCS, LGCS, (LGBH - LGCS)), LGCS
        ),
        Cylinder(
            Vector(LGCS, LGCS, LGCS),
            Vector(LGCS, LGCS, (LGBH - LGCS)),
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
            Vector(LGCS, width * LGBW - LGCS, LGBH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGCS, width * LGBW - LGCS, LGBH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGCS, LGBH - LGCS),
            Vector(LGCS, width * LGBW - LGCS, LGBH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGCS, LGCS),
            Vector(length * LGBW - LGCS, LGBW - LGCS, LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, LGBW - LGCS, LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, (width - 1) * LGBW - LGCS, LGCS),
            Vector(LGBW - LGCS, LGBW - LGCS, LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGBW - LGCS, LGCS),
            Vector(length * LGBW - LGCS, LGBW - LGCS, LGBH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, LGBW - LGCS, LGBH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGBW - LGCS, LGBH - LGCS),
            Vector(LGBW - LGCS, LGBW - LGCS, LGBH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGCS, LGBH - LGCS),
            Vector(length * LGBW - LGCS, LGBW - LGCS, LGBH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGBW - LGCS, width * LGBW - LGCS, LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGBW - LGCS, width * LGBW - LGCS, LGBH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW - LGCS, width * LGBW - LGCS, LGCS),
            Vector(LGBW - LGCS, width * LGBW - LGCS, LGBH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW - LGCS, width * LGBW - LGCS, LGCS),
            Vector(LGCS, width * LGBW - LGCS, LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW - LGCS, width * LGBW - LGCS, LGBH - LGCS),
            Vector(LGCS, width * LGBW - LGCS, LGBH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW - LGCS, width * LGBW - LGCS, LGCS),
            Vector(LGBW - LGCS, LGBW - LGCS, LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW - LGCS, width * LGBW - LGCS, LGBH - LGCS),
            Vector(LGBW - LGCS, LGBW - LGCS, LGBH - LGCS),
            LGCS
        ),
        Difference(
            Union(
                Difference(
                    Box(
                        Vector(LGCS, LGCS, 0),
                        Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGBH)
                    ),
                    Box(
                        Vector(LGBW - LGCS, LGBW - LGCS, -LG_E),
                        Vector(length * LGBW, width * LGBW, LGBH + LG_E)
                    ),
                ),
                Difference(
                    Union(
                        Box(
                            Vector(0, LGCS, LGCS),
                            Vector(
                                length * LGBW, width * LGBW - LGCS, LGBH - LGCS
                            )
                        ),
                        Box(
                            Vector(LGCS, 0, LGCS),
                            Vector(
                                length * LGBW - LGCS, width * LGBW, LGBH - LGCS
                            )
                        ),
                    ),
                    Box(
                        Vector(LGBW, LGBH, 0),
                        Vector(length * LGBW + LG_E, width * LGBW + LG_E, LGBH)
                    )
                ),
                Union(
                    Difference(
                        Box(
                            Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_E),
                            Vector(
                                length * LGBW - LG_WALL_WIDTH,
                                width * LGBW - LG_WALL_WIDTH,
                                LG_BRICK_INNER_HEIGHT
                            )
                        ),
                        Box(
                            Vector(length / LGBW, width * LGBW, -LGCS),
                            Vector(
                                length / 2 * LGBW - LG_WALL_WIDTH,
                                width / 2 * LGBW - LG_WALL_WIDTH,
                                LG_BRICK_INNER_HEIGHT + LG_E
                            )
                        ),
                    ),
                    Box(
                        Vector(length * LGBW - LGCS, LGBW - LGCS, -LG_E),
                        Vector(length * LGBW + LG_E, LGBW + LG_E, LGBH + LG_E)
                    ),
                    Box(
                        Vector(LGBW - LGCS, width * LGBW - LGCS, -LG_E),
                        Vector(LGBW + LG_E, width * LGBW + LG_E, LGBH + LG_E)
                    ),
                    Object(
                        LG_KNOB_INNER_SPACE,
                        Translate(
                            Vector(
                                0.5 * LGBW, 0.5 * LGBW, LG_BRICK_INNER_HEIGHT
                            )
                        )
                    ),
                    Object(
                        LG_KNOB_INNER_SPACE,
                        Translate(
                            Vector(
                                0.5 * LGBW, 1.5 * LGBW, LG_BRICK_INNER_HEIGHT
                            )
                        )
                    ),
                    Object(
                        LG_KNOB_INNER_SPACE,
                        Translate(
                            Vector(
                                1.5 * LGBW, 0.5 * LGBW, LG_BRICK_INNER_HEIGHT
                            )
                        )
                    )
                )
            ),
            Box(
                Vector(
                    sqrt(2) * (LGBW + LG_CYLINDER_RADIUS) / 2,
                    -0.06,
                    LG_BRICK_INNER_HEIGHT
                ),
                Vector(sqrt(2) * LGBW, 0.06, 0),
                Rotate(Vector(0, 0, 45))
            ),
        ),
        Object(
            LG_BRICK_COLUMN,
            Translate(Vector(LGBW, 0.5 * LGBW, 0))
        ),
        Object(
            LG_BRICK_COLUMN,
            Translate(Vector(0.5 * LGBW, LGBW, 0))
        ),
        Object(
            lg_knob(),
            Translate(Vector(0.5 * LGBW, 0.5 * LGBW, LGBH))
        ),
        Object(
            lg_knob(),
            Translate(Vector(1.5 * LGBW, 0.5 * LGBW, LGBH))
        ),
        Object(
            lg_knob(),
            Translate(Vector(0.5 * LGBW, 1.5 * LGBW, LGBH)),
        ),
        Translate(Vector((-length / 2 + 0.5) * LGBW, -0.5 * LGBW, -LGBH)),
        Rotate(Vector(0, 0, 180))
    )

    return result


# #declare lg_2357_clear =
# merge {
#  Sphere(
#   Vector(LGCS, LGCS, LGCS), LGCS
#  )
#  Cylinder(
#   Vector(LGCS, LGCS, LGCS),
#   Vector((length * LGBH - LGCS), LGCS, LGCS),
#   LGCS
#  )
#  Sphere(
#   Vector((length * LGBH - LGCS), LGCS, LGCS), LGCS
#  )
#  Cylinder(
#   Vector(((length * LGBH) - LGCS), LGCS, LGCS),
#   Vector(((length * LGBH) - LGCS), LGCS, (LGBH - LGCS)),
#   LGCS
#  )
#  Sphere(
#   Vector(((length * LGBH) - LGCS), LGCS, (LGBH - LGCS)), LGCS
#  )
#  Cylinder(
#   Vector(((length * LGBH) - LGCS), LGCS, (LGBH - LGCS)),
#   Vector(LGCS, LGCS, (LGBH - LGCS)),
#   LGCS
#  )
#  Sphere(
#   Vector(LGCS, LGCS, (LGBH - LGCS)), LGCS
#  )
#  Cylinder(
#   Vector(LGCS, LGCS, LGCS),
#   Vector(LGCS, LGCS, (LGBH - LGCS)),
#   LGCS
#  )
#  Cylinder(
#   Vector(LGCS, LGCS, LGCS),
#   Vector(LGCS, ((width * LGBH) - LGCS), LGCS),
#   LGCS
#  )
#  Sphere(
#   Vector(LGCS, ((width * LGBH) - LGCS), LGCS), LGCS
#  )
#  Cylinder(
#   Vector(LGCS, ((width * LGBH) - LGCS), LGCS),
#   Vector(LGCS, ((width * LGBH) - LGCS), (LGBH - LGCS)),
#   LGCS
#  )
#  Sphere(
#   Vector(LGCS, ((width * LGBH) - LGCS), (LGBH - LGCS)), LGCS
#  )
#  Cylinder(
#   Vector(LGCS, LGCS, (LGBH - LGCS)),
#   Vector(LGCS, ((width * LGBH) - LGCS), (LGBH - LGCS)),
#   LGCS
#  )
#  Cylinder(
#   Vector(((length * LGBH) - LGCS), LGCS, LGCS),
#   Vector(((length * LGBH) - LGCS), (LGBH - LGCS), LGCS),
#   LGCS
#  )
#  Sphere(
#   Vector(((length * LGBH) - LGCS), (LGBH - LGCS), LGCS), LGCS
#  )
#  Cylinder(
#   Vector(((length * LGBH) - LGCS), (((width-1)*LGBH) - LGCS), LGCS),
#   Vector((LGBH - LGCS), (LGBH - LGCS), LGCS),
#   LGCS
#  )
#  Cylinder(
#   Vector(((length * LGBH) - LGCS), (LGBH - LGCS), LGCS),
#   Vector(((length * LGBH) - LGCS), (LGBH - LGCS), (LGBH - LGCS)),
#   LGCS
#  )
#  Sphere(
#   Vector(((length * LGBH) - LGCS), (LGBH - LGCS), (LGBH - LGCS)), LGCS
#  )
#  Cylinder(
#   Vector(((length * LGBH) - LGCS), (LGBH - LGCS), (LGBH - LGCS)),
#   Vector((LGBH - LGCS), (LGBH - LGCS), (LGBH - LGCS)),
#   LGCS
#  )
#  Cylinder(
#   Vector(((length * LGBH) - LGCS), LGCS, (LGBH - LGCS)),
#   Vector(((length * LGBH) - LGCS), (LGBH - LGCS), (LGBH - LGCS)),
#   LGCS
#  )
#  Sphere(
#   Vector((LGBH - LGCS), ((width * LGBH) - LGCS), LGCS), LGCS
#  )
#  Sphere(
#   Vector((LGBH - LGCS), ((width * LGBH) - LGCS), (LGBH - LGCS)), LGCS
#  )
#  Cylinder(
#   Vector((LGBH - LGCS), ((width * LGBH) - LGCS), LGCS),
#   Vector((LGBH - LGCS), ((width * LGBH) - LGCS), (LGBH - LGCS)),
#   LGCS
#  )
#  Cylinder(
#   Vector((LGBH - LGCS), ((width * LGBH) - LGCS), LGCS),
#   Vector(LGCS, ((width * LGBH) - LGCS), LGCS),
#   LGCS
#  )
#  Cylinder(
#   Vector((LGBH - LGCS), ((width * LGBH) - LGCS), (LGBH - LGCS)),
#   Vector(LGCS, ((width * LGBH) - LGCS), (LGBH - LGCS)),
#   LGCS
#  )
#  Cylinder(
#   Vector((LGBH - LGCS), ((width * LGBH) - LGCS), LGCS),
#   Vector((LGBH - LGCS), (LGBH - LGCS), LGCS),
#   LGCS
#  )
#  Cylinder(
#   Vector((LGBH - LGCS), ((width * LGBH) - LGCS), (LGBH - LGCS)),
#   Vector((LGBH - LGCS), (LGBH - LGCS), (LGBH - LGCS)),
#   LGCS
#  )
#  Difference(
#   merge {
#    Difference(
#     Box(
#      Vector(LGCS, LGCS, 0),
#      Vector(length * LGBH - LGCS, width * LGBH - LGCS, LGBH)
#     )
#     Box(
#      Vector(LGBH - LGCS, LGBH - LGCS, -LG_E),
#      Vector(length * LGBH, width * LGBH, LGBH + LG_E)
#     )
#    )
#    Difference(
#     merge {
#      Box(
#       Vector(0, LGCS, LGCS),
#       Vector(length * LGBH, width * LGBH - LGCS, LGBH - LGCS)
#      )
#      Box(
#       Vector(LGCS, 0, LGCS),
#       Vector(length * LGBH - LGCS, width * LGBH, LGBH - LGCS)
#      )
#     )
#     Box(
#      Vector(LGBH, LGBH, 0),
#      Vector(length * LGBH + LG_E, width * LGBH + LG_E, LGBH)
#     )
#    )
#   )
#   merge {
#    Difference(
#     Box(
#      Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_E),
#      Vector(length * LGBH - LG_WALL_WIDTH,
# width * LGBH - LG_WALL_WIDTH, LG_BRICK_INNER_HEIGHT)
#     )
#     Box(
#      Vector(length/LGBH, width * LGBH, -LGCS),
#      Vector(length / 2 * LGBH - LG_WALL_WIDTH,
# width / 2 * LGBH - LG_WALL_WIDTH, LG_BRICK_INNER_HEIGHT + LG_E)
#     )
#    )
#    Box(
#     Vector(length * LGBH - LGCS, LGBH - LGCS, -LG_E),
#     Vector(length * LGBH + LG_E, LGBH + LG_E, LGBH + LG_E)
#    )
#    Box(
#     Vector(LGBH - LGCS, width * LGBH - LGCS, -LG_E),
#     Vector(LGBH + LG_E, width * LGBH + LG_E, LGBH + LG_E)
#    )
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(0.5*LGBH, 0.5*LGBH, LG_BRICK_INNER_HEIGHT)
#    )
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(0.5*LGBH, 1.5*LGBH, LG_BRICK_INNER_HEIGHT)
#    )
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(1.5*LGBH, 0.5*LGBH, LG_BRICK_INNER_HEIGHT)
#    )
#   )
#  )
#  Box(
#   Vector(sqrt(2)*(LGBH + LG_CYLINDER_RADIUS)/2, -0.06, LG_BRICK_INNER_HEIGHT),
#   Vector(sqrt(2)*LGBH, 0.06, 0)
#   Rotate(Vector(0, 0, 45)
#  )
#  Object(
#   lg_brick_column_clear
#   Translate(Vector(LGBH, 0.5*LGBH, 0)
#  )
#  Object(
#   lg_brick_column_clear
#   Translate(Vector(0.5*LGBH, LGBH, 0)
#  )
#  Object(
#   lg_knob_clear
#   Translate(Vector(0.5*LGBH, 0.5*LGBH, LGBH)
#  )
#  Object(
#   lg_knob_clear
#   Translate(Vector(1.5*LGBH, 0.5*LGBH, LGBH)
#  )
#  Object(
#   lg_knob_clear
#   Translate(Vector(0.5*LGBH, 1.5*LGBH, LGBH)
#  )
#  Translate(Vector(-0.5*LGBH, -0.5*LGBH, -LGBH)
#  Rotate(Vector(0, 0, 180)
# )

# #end
