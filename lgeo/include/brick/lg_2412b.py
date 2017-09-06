"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

@Todo: Put some information here that makes sense
19980319 Lutz Uhlmann
20071101 Lutz Uhlmann moved from lg_2412 to lg_2412b

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_2412b: Tile 1 x 2 Grille with Groove
"""

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from lgeo.include.common.lg_defs import LGCS, LGBW
from lgeo.include.common.lg_defs import LGPH, LGWW
from lgeo.include.common.lg_defs import LG_PLATE_INNER_HEIGHT, LG_E
from lgeo.include.common.lg_defs import LG_KNOB_INNER_RADIUS


def solid(length=2, width=1):
    """@Todo: Docstring."""
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
            Vector(length * LGBW - LGCS, LGWW - LGCS, LGPH - LGCS),
            Vector(LGCS, LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, 2 * LGWW + LGCS, LGPH - LGCS),
            Vector(LGCS, 2 * LGWW + LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, 3 * LGWW - LGCS, LGPH - LGCS),
            Vector(LGCS, 3 * LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, 4 * LGWW + LGCS, LGPH - LGCS),
            Vector(LGCS, 4 * LGWW + LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGCS, LGPH - LGCS),
            Vector(LGCS, LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, 2 * LGWW + LGCS, LGPH - LGCS),
            Vector(LGCS, 3 * LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, 4 * LGWW + LGCS, LGPH - LGCS),
            Vector(LGCS, 5 * LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGCS, LGPH - LGCS),
            Vector(length * LGBW - LGCS, LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, 2 * LGWW + LGCS, LGPH - LGCS),
            Vector(length * LGBW - LGCS, 3 * LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, 4 * LGWW + LGCS, LGPH - LGCS),
            Vector(length * LGBW - LGCS, 5 * LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGWW - LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            Vector(LGCS, LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGWW - LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            Vector(length * LGBW - LGCS, LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, 2 * LGWW + LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            Vector(LGCS, 2 * LGWW + LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, 2 * LGWW + LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            Vector(length * LGBW - LGCS, 2 * LGWW + LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, 3 * LGWW - LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            Vector(LGCS, 3 * LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, 3 * LGWW - LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            Vector(length * LGBW - LGCS, 3 * LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, 4 * LGWW + LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            Vector(LGCS, 4 * LGWW + LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, 4 * LGWW + LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            Vector(length * LGBW - LGCS, 4 * LGWW + LGCS, LGPH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGCS, LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGCS, 2 * LGWW + LGCS, LGPH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, 2 * LGWW + LGCS, LGPH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGCS, 3 * LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, 3 * LGWW - LGCS, LGPH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGCS, 4 * LGWW + LGCS, LGPH - LGCS),
            LGCS
        ),
        Sphere(
            Vector(length * LGBW - LGCS, 4 * LGWW + LGCS, LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, LGWW - LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            Vector(length * LGBW - LGCS, 2 * LGWW + LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, LGWW - LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            Vector(LGCS, 2 * LGWW + LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(length * LGBW - LGCS, 3 * LGWW - LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            Vector(length * LGBW - LGCS, 4 * LGWW + LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGCS, 3 * LGWW - LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            Vector(LGCS, 4 * LGWW + LGCS, LG_PLATE_INNER_HEIGHT - LGCS),
            LGCS
        ),
        Difference(
            Union(
                Box(
                    Vector(LGCS, LGCS, 0.04),
                    Vector(length * LGBW - LGCS, width * LGBW - LGCS, LGPH)
                ),
                Box(
                    Vector(0, LGCS, LGCS + 0.04),
                    Vector(length * LGBW, width * LGBW - LGCS, LGPH - LGCS)
                ),
                Box(
                    Vector(LGCS, 0, LGCS + 0.04),
                    Vector(length * LGBW - LGCS, width * LGBW, LGPH - LGCS)
                ),
                Box(
                    Vector(0.04, 0.04, 0),
                    Vector(length * LGBW - 0.04, width * LGBW - 0.04, 0.04 + LG_E)
                )
            ),
            Union(
                Box(
                    Vector(LGWW, LGWW, -LGCS),
                    Vector(length * LGBW - LGWW, width * LGBW - LGWW, LG_PLATE_INNER_HEIGHT + LG_E)
                ),
                Box(
                    Vector(-LG_E, LGWW - LGCS, LGPH + LG_E),
                    Vector(LGCS, 2 * LGWW + LGCS, LG_PLATE_INNER_HEIGHT - LGCS)
                ),
                Box(
                    Vector(length * LGBW + LG_E, LGWW - LGCS, LGPH + LG_E),
                    Vector(length * LGBW - LGCS, 2 * LGWW + LGCS, LG_PLATE_INNER_HEIGHT - LGCS)
                ),
                Box(
                    Vector(0, LGWW - LGCS, LGPH + LG_E),
                    Vector(length * LGBW, 2 * LGWW + LGCS, LGPH - LGCS)
                ),
                Box(
                    Vector(0, LGWW, LGPH),
                    Vector(length * LGBW, 2 * LGWW, LG_PLATE_INNER_HEIGHT)
                ),
                Box(
                    Vector(-LG_E, 3 * LGWW - LGCS, LGPH + LG_E),
                    Vector(LGCS, 4 * LGWW + LGCS, LG_PLATE_INNER_HEIGHT - LGCS)
                ),
                Box(
                    Vector(length * LGBW + LG_E, 3 * LGWW - LGCS, LGPH + LG_E),
                    Vector(length * LGBW - LGCS, 4 * LGWW + LGCS, LG_PLATE_INNER_HEIGHT - LGCS)
                ),
                Box(
                    Vector(0, 3 * LGWW - LGCS, LGPH + LG_E),
                    Vector(length * LGBW, 4 * LGWW + LGCS, LGPH - LGCS)
                ),
                Box(
                    Vector(0, 3 * LGWW, LGPH),
                    Vector(length * LGBW, 4 * LGWW, LG_PLATE_INNER_HEIGHT)
                )
            )
        ),
        Difference(
            Cylinder(
                Vector(LGBW, LGBW / 2, LG_PLATE_INNER_HEIGHT + LG_E),
                Vector(LGBW, LGBW / 2, 0),
                LG_KNOB_INNER_RADIUS
            ),
            Union(
                Box(
                    Vector(LGWW, LGWW, -LG_E),
                    Vector(length * LGBW - LGWW, 2 * LGWW, LGPH)
                ),
                Box(
                    Vector(LGWW, 3 * LGWW, -LG_E),
                    Vector(length * LGBW - LGWW, 4 * LGWW, LGPH)
                ),
            ),
        ),
        Translate(Vector(-LGBW, -0.5 * LGBW, -LGPH)),
        Rotate(Vector(0, 0, 90))
    )

# #declare lg_2412b_clear =
# Merge(
#  Sphere(
#   Vector(LGCS, LGCS,
#     LGCS + 0.04), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS,
#     LGCS + 0.04),
#   Vector(length * LGBW - LGCS,
#    LGCS, LGCS + 0.04),
#   LGCS
#  ),
#  Sphere(
#   Vector(length * LGBW - LGCS,
#     LGCS, LGCS + 0.04), LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     LGCS, LGCS + 0.04),
#   Vector(length * LGBW - LGCS,
#     LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(length * LGBW - LGCS,
#     LGCS, LGPH - LGCS),
# LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     LGCS, LGPH - LGCS),
#   Vector(LGCS, LGCS,
#     LGPH - LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(LGCS, LGCS,
#     LGPH - LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS,
#     LGCS + 0.04),
#   Vector(LGCS, LGCS,
#     LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS,
#     LGCS + 0.04),
#   Vector(LGCS, width * LGBW - LGCS,
#     LGCS + 0.04),
#   LGCS
#  ),
#  Sphere(
#   Vector(LGCS, width * LGBW - LGCS,
#     LGCS + 0.04), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, width * LGBW - LGCS,
#     LGCS + 0.04),
#   Vector(LGCS, width * LGBW - LGCS,
#     LGPH - LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(LGCS, width * LGBW - LGCS,
#     LGPH - LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     LGCS, LGCS + 0.04),
#   Vector(length * LGBW - LGCS,
#     width * LGBW - LGCS, LGCS + 0.04),
#   LGCS
#  ),
#  Sphere(
#   Vector(length * LGBW - LGCS,
#     width * LGBW - LGCS,
#     LGCS + 0.04), LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     width * LGBW - LGCS,
#     LGCS + 0.04),
#   Vector(LGCS, width * LGBW - LGCS,
#     LGCS + 0.04),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     width * LGBW - LGCS, LGCS + 0.04),
#   Vector(length * LGBW - LGCS,
#     width * LGBW - LGCS,
#     LGPH - LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(length * LGBW - LGCS,
#     width * LGBW - LGCS,
#     LGPH - LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     width * LGBW - LGCS,
#     LGPH - LGCS),
#   Vector(LGCS, width * LGBW - LGCS,
#     LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     (LG_WALL_WIDTH - LGCS),
#     LGPH - LGCS),
#   Vector(LGCS, (LG_WALL_WIDTH - LGCS),
#     LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     (2 * LG_WALL_WIDTH + LGCS),
#     LGPH - LGCS),
#   Vector(LGCS, (2 * LG_WALL_WIDTH + LGCS),
#     LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     (3 * LG_WALL_WIDTH - LGCS),
#     LGPH - LGCS)),
#   Vector(LGCS, (3 * LG_WALL_WIDTH - LGCS),
#     LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     (4 * LG_WALL_WIDTH + LGCS),
#     LGPH - LGCS),
#   Vector(LGCS, (4 * LG_WALL_WIDTH + LGCS),
#     LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS,
#     LGPH - LGCS),
#   Vector(LGCS, LG_WALL_WIDTH - LGCS,
#     LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, 2 * LG_WALL_WIDTH + LGCS,
#     LGPH - LGCS),
#   Vector(LGCS, 3 * LG_WALL_WIDTH - LGCS,
#     LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, 4 * LG_WALL_WIDTH + LGCS,
#     LGPH - LGCS),
#   Vector(LGCS, 5 * LG_WALL_WIDTH - LGCS,
#     LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS, LGCS,
#     LGPH - LGCS),
#   Vector(length * LGBW - LGCS,
#     LG_WALL_WIDTH - LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     2 * LG_WALL_WIDTH + LGCS, LGPH - LGCS),
#   Vector(length * LGBW - LGCS,
#     3 * LG_WALL_WIDTH - LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     4 * LG_WALL_WIDTH + LGCS, LGPH - LGCS),
#   Vector(length * LGBW - LGCS,
#    5 * LG_WALL_WIDTH - LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LG_WALL_WIDTH - LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   Vector(LGCS, LG_WALL_WIDTH - LGCS,
#     LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     LG_WALL_WIDTH - LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   Vector(length * LGBW - LGCS,
#     LG_WALL_WIDTH - LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, 2 * LG_WALL_WIDTH + LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   Vector(LGCS, 2 * LG_WALL_WIDTH + LGCS,
#     LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     2 * LG_WALL_WIDTH + LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   Vector(length * LGBW - LGCS,
#     2 * LG_WALL_WIDTH + LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, 3 * LG_WALL_WIDTH - LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   Vector(LGCS, 3 * LG_WALL_WIDTH - LGCS,
#     LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     3 * LG_WALL_WIDTH - LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   Vector(length * LGBW - LGCS,
#     3 * LG_WALL_WIDTH - LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, 4 * LG_WALL_WIDTH + LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   Vector(LGCS, 4 * LG_WALL_WIDTH + LGCS,
#     LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     4 * LG_WALL_WIDTH + LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   Vector(length * LGBW - LGCS,
#     4 * LG_WALL_WIDTH + LGCS, LGPH - LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(LGCS, LG_WALL_WIDTH - LGCS,
#     LGPH - LGCS), LGCS
#  ),
#  Sphere(
#   Vector(length * LGBW - LGCS,
#     LG_WALL_WIDTH - LGCS, LGPH - LGCS),
# LGCS
#  ),
#  Sphere(
#   Vector(LGCS, 2 * LG_WALL_WIDTH + LGCS,
#     LGPH - LGCS), LGCS
#  ),
#  Sphere(
#   Vector(length * LGBW - LGCS,
#     2 * LG_WALL_WIDTH + LGCS,
#     LGPH - LGCS), LGCS
#  ),
#  Sphere(
#   Vector(LGCS, 3 * LG_WALL_WIDTH - LGCS,
#     LGPH - LGCS), LGCS
#  ),
#  Sphere(
#   Vector(length * LGBW - LGCS,
#     3 * LG_WALL_WIDTH - LGCS,
#     LGPH - LGCS), LGCS
#  ),
#  Sphere(
#   Vector(LGCS, 4 * LG_WALL_WIDTH + LGCS,
#     LGPH - LGCS), LGCS
#  ),
#  Sphere(
#   Vector(length * LGBW - LGCS,
#     4 * LG_WALL_WIDTH + LGCS,
#     LGPH - LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     LG_WALL_WIDTH - LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   Vector(length * LGBW - LGCS,
#     2 * LG_WALL_WIDTH + LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LG_WALL_WIDTH - LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   Vector(LGCS, 2 * LG_WALL_WIDTH + LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length * LGBW - LGCS,
#     3 * LG_WALL_WIDTH - LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   Vector(length * LGBW - LGCS,
#     4 * LG_WALL_WIDTH + LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, 3 * LG_WALL_WIDTH - LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   Vector(LGCS, 4 * LG_WALL_WIDTH + LGCS,
#     LG_PLATE_INNER_HEIGHT - LGCS),
#   LGCS
#  ),
#  Difference(
#   Merge(
#    Box(
#     Vector(LGCS, LGCS, 0.04),
#     Vector(length * LGBW - LGCS,
#         width * LGBW - LGCS, LGPH)
#    ),
#    Box(
#     Vector(0, LGCS, LGCS + 0.04),
#     Vector(length * LGBW,
#         width * LGBW - LGCS,
#         LGPH - LGCS)
#    ),
#    Box(
#     Vector(LGCS, 0, LGCS + 0.04),
#     Vector(length * LGBW - LGCS,
#         width * LGBW, LGPH - LGCS)
#    ),
#    Box(
#     Vector(0.04, 0.04, 0),
#     Vector((length * LGBW - 0.04),
#         (width * LGBW - 0.04), 0.04 + LG_E)
#    ),
#   ),
#   Union(
#    Box(
#     Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LGCS),
#     Vector(length * LGBW - LG_WALL_WIDTH,
#         width * LGBW - LG_WALL_WIDTH,
#         LG_PLATE_INNER_HEIGHT + LG_E)
#    ),
#    Box(
#     Vector(-LG_E, LG_WALL_WIDTH - LGCS, LGPH + LG_E),
#     Vector(LGCS,
#         2 * LG_WALL_WIDTH + LGCS,
#         LG_PLATE_INNER_HEIGHT - LGCS)
#    ),
#    Box(
#     Vector(length * LGBW + LG_E,
#         LG_WALL_WIDTH - LGCS, LGPH + LG_E),
#     Vector(length * LGBW - LGCS,
#         2 * LG_WALL_WIDTH + LGCS,
#         LG_PLATE_INNER_HEIGHT - LGCS)
#    ),
#    Box(
#     Vector(0, LG_WALL_WIDTH - LGCS, LGPH + LG_E),
#     Vector(length * LGBW,
#         2 * LG_WALL_WIDTH + LGCS,
#         LGPH - LGCS)
#    ),
#    Box(
#     Vector(0, LG_WALL_WIDTH, LGPH),
#     Vector(length * LGBW, 2 * LG_WALL_WIDTH, LG_PLATE_INNER_HEIGHT)
#    ),
#    Box(
#     Vector(-LG_E, 3 * LG_WALL_WIDTH - LGCS, LGPH + LG_E),
#     Vector(LGCS, 4 * LG_WALL_WIDTH + LGCS,
#         LG_PLATE_INNER_HEIGHT - LGCS)
#    ),
#    Box(
#     Vector(length * LGBW + LG_E, 3 * LG_WALL_WIDTH - LGCS,
#         LGPH + LG_E),
#     Vector(length * LGBW - LGCS,
#         4 * LG_WALL_WIDTH + LGCS,
#         LG_PLATE_INNER_HEIGHT - LGCS)
#    ),
#    Box(
#     Vector(0, 3 * LG_WALL_WIDTH - LGCS, LGPH + LG_E),
#     Vector(length * LGBW,
#         4 * LG_WALL_WIDTH + LGCS,
#         LGPH - LGCS)
#    ),
#    Box(
#     Vector(0, 3 * LG_WALL_WIDTH, LGPH),
#     Vector(length * LGBW,
#         4 * LG_WALL_WIDTH, LG_PLATE_INNER_HEIGHT)
#    ),
#   ),
#  ),
#  Difference(
#   Cylinder(
#    Vector(LGBW, LGBW / 2, LG_PLATE_INNER_HEIGHT + LG_E),
#    Vector(LGBW, LGBW / 2, 0),
#    (LG_KNOB_INNER_RADIUS)
#   ),
#   Union(
#    Box(
#     Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_E),
#     Vector(length * LGBW - LG_WALL_WIDTH,
#         2 * LG_WALL_WIDTH, LGPH)
#    ),
#    Box(
#     Vector(LG_WALL_WIDTH, 3 * LG_WALL_WIDTH, -LG_E),
#     Vector(length * LGBW - LG_WALL_WIDTH,
#         4 * LG_WALL_WIDTH, LGPH)
#    ),
#   ),
#  ),
#  Translate(Vector(-LGBW, -0.5 * LGBW, -LGPH)),
#  Rotate(Vector(0, 0, 90))
# ),
