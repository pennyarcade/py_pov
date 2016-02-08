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

from lgeo.include.common.lg_defs import LG_CORNER_SPACE, LGBW
from lgeo.include.common.lg_defs import LGPH, LG_WALL_WIDTH
from lgeo.include.common.lg_defs import LG_PLATE_INNER_HEIGHT, LG_E
from lgeo.include.common.lg_defs import LG_KNOB_INNER_RADIUS


def solid(length=2, width=1):
    """@Todo: Docstring."""
    return Union(
        Sphere(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE + 0.04),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE + 0.04),
            Vector(
                (length * LGBW - LG_CORNER_SPACE),
                LG_CORNER_SPACE,
                LG_CORNER_SPACE + 0.04
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                (length * LGBW - LG_CORNER_SPACE),
                LG_CORNER_SPACE,
                LG_CORNER_SPACE + 0.04
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                LG_CORNER_SPACE,
                LG_CORNER_SPACE + 0.04
            ),
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                LG_CORNER_SPACE,
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                LG_CORNER_SPACE,
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                LG_CORNER_SPACE,
                (LGPH - LG_CORNER_SPACE)
            ),
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE + 0.04),
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE + 0.04),
            Vector(
                LG_CORNER_SPACE,
                ((width * LGBW) - LG_CORNER_SPACE),
                LG_CORNER_SPACE + 0.04
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                ((width * LGBW) - LG_CORNER_SPACE),
                LG_CORNER_SPACE + 0.04
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                ((width * LGBW) - LG_CORNER_SPACE),
                LG_CORNER_SPACE + 0.04
            ),
            Vector(
                LG_CORNER_SPACE,
                ((width * LGBW) - LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                ((width * LGBW) - LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                LG_CORNER_SPACE,
                LG_CORNER_SPACE + 0.04
            ),
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                ((width * LGBW) - LG_CORNER_SPACE),
                LG_CORNER_SPACE + 0.04
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                ((width * LGBW) - LG_CORNER_SPACE),
                LG_CORNER_SPACE + 0.04
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                ((width * LGBW) - LG_CORNER_SPACE),
                LG_CORNER_SPACE + 0.04
            ),
            Vector(
                LG_CORNER_SPACE,
                ((width * LGBW) - LG_CORNER_SPACE),
                LG_CORNER_SPACE + 0.04
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                ((width * LGBW) - LG_CORNER_SPACE),
                LG_CORNER_SPACE + 0.04
            ),
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                ((width * LGBW) - LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                ((width * LGBW) - LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                ((width * LGBW) - LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            Vector(
                LG_CORNER_SPACE,
                ((width * LGBW) - LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                (LG_WALL_WIDTH - LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            Vector(
                LG_CORNER_SPACE,
                (LG_WALL_WIDTH - LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                (2 * LG_WALL_WIDTH + LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            Vector(
                LG_CORNER_SPACE,
                (2 * LG_WALL_WIDTH + LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                (3 * LG_WALL_WIDTH - LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            Vector(
                LG_CORNER_SPACE,
                (3 * LG_WALL_WIDTH - LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                ((length * LGBW) - LG_CORNER_SPACE),
                (4 * LG_WALL_WIDTH + LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            Vector(
                LG_CORNER_SPACE,
                (4 * LG_WALL_WIDTH + LG_CORNER_SPACE),
                (LGPH - LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                5 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                5 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                LG_WALL_WIDTH - LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_WALL_WIDTH - LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LGPH - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                LG_WALL_WIDTH - LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                LG_WALL_WIDTH - LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            Vector(
                length * LGBW - LG_CORNER_SPACE,
                4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Difference(
            Union(
                Box(
                    Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, 0.04),
                    Vector(
                        length * LGBW - LG_CORNER_SPACE,
                        width * LGBW - LG_CORNER_SPACE,
                        LGPH
                    )
                ),
                Box(
                    Vector(0, LG_CORNER_SPACE, LG_CORNER_SPACE + 0.04),
                    Vector(
                        length * LGBW,
                        width * LGBW - LG_CORNER_SPACE,
                        LGPH - LG_CORNER_SPACE
                    )
                ),
                Box(
                    Vector(LG_CORNER_SPACE, 0, LG_CORNER_SPACE + 0.04),
                    Vector(
                        length * LGBW - LG_CORNER_SPACE,
                        width * LGBW,
                        LGPH - LG_CORNER_SPACE
                    )
                ),
                Box(
                    Vector(0.04, 0.04, 0),
                    Vector(
                        (length * LGBW - 0.04),
                        (width * LGBW - 0.04),
                        0.04 + LG_E
                    )
                )
            ),
            Union(
                Box(
                    Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_CORNER_SPACE),
                    Vector(
                        length * LGBW - LG_WALL_WIDTH,
                        width * LGBW - LG_WALL_WIDTH,
                        LG_PLATE_INNER_HEIGHT + LG_E
                    )
                ),
                Box(
                    Vector(
                        -LG_E,
                        LG_WALL_WIDTH - LG_CORNER_SPACE,
                        LGPH + LG_E
                    ),
                    Vector(
                        LG_CORNER_SPACE,
                        2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                        LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
                    )
                ),
                Box(
                    Vector(
                        length * LGBW + LG_E,
                        LG_WALL_WIDTH - LG_CORNER_SPACE,
                        LGPH + LG_E
                    ),
                    Vector(
                        length * LGBW - LG_CORNER_SPACE,
                        2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                        LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
                    )
                ),
                Box(
                    Vector(
                        0,
                        LG_WALL_WIDTH - LG_CORNER_SPACE,
                        LGPH + LG_E
                    ),
                    Vector(
                        length * LGBW,
                        2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                        LGPH - LG_CORNER_SPACE
                    )
                ),
                Box(
                    Vector(0, LG_WALL_WIDTH, LGPH),
                    Vector(
                        length * LGBW,
                        2 * LG_WALL_WIDTH,
                        LG_PLATE_INNER_HEIGHT
                    )
                ),
                Box(
                    Vector(
                        -LG_E,
                        3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                        LGPH + LG_E
                    ),
                    Vector(
                        LG_CORNER_SPACE,
                        4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                        LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
                    )
                ),
                Box(
                    Vector(
                        length * LGBW + LG_E,
                        3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                        LGPH + LG_E
                    ),
                    Vector(
                        length * LGBW - LG_CORNER_SPACE,
                        4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                        LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE
                    )
                ),
                Box(
                    Vector(
                        0,
                        3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
                        LGPH + LG_E
                    ),
                    Vector(
                        length * LGBW,
                        4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
                        LGPH - LG_CORNER_SPACE
                    )
                ),
                Box(
                    Vector(
                        0,
                        3 * LG_WALL_WIDTH,
                        LGPH
                    ),
                    Vector(
                        length * LGBW,
                        4 * LG_WALL_WIDTH,
                        LG_PLATE_INNER_HEIGHT
                    )
                )
            )
        ),
        Difference(
            Cylinder(
                Vector(
                    LGBW,
                    LGBW / 2,
                    LG_PLATE_INNER_HEIGHT + LG_E
                ),
                Vector(LGBW, LGBW / 2, 0),
                (LG_KNOB_INNER_RADIUS)
            ),
            Union(
                Box(
                    Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_E),
                    Vector(
                        length * LGBW - LG_WALL_WIDTH,
                        2 * LG_WALL_WIDTH,
                        LGPH
                    )
                ),
                Box(
                    Vector(LG_WALL_WIDTH, 3 * LG_WALL_WIDTH, -LG_E),
                    Vector(
                        length * LGBW - LG_WALL_WIDTH,
                        4 * LG_WALL_WIDTH,
                        LGPH
                    )
                ),
            ),
        ),
        Translate(
            Vector(-LGBW, -0.5 * LGBW, -LGPH)
        ),
        Rotate(Vector(0, 0, 90))
    )

# #declare lg_2412b_clear =
# Merge(
#  Sphere(
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
#     LG_CORNER_SPACE + 0.04), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
#     LG_CORNER_SPACE + 0.04),
#   Vector((length * LGBW - LG_CORNER_SPACE),
#    LG_CORNER_SPACE, LG_CORNER_SPACE + 0.04),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector((length * LGBW - LG_CORNER_SPACE),
#     LG_CORNER_SPACE, LG_CORNER_SPACE + 0.04), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     LG_CORNER_SPACE, LG_CORNER_SPACE + 0.04),
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     LG_CORNER_SPACE, (LGPH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     LG_CORNER_SPACE, (LGPH - LG_CORNER_SPACE)),
# LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     LG_CORNER_SPACE, (LGPH - LG_CORNER_SPACE)),
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
#     (LGPH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
#     (LGPH - LG_CORNER_SPACE)), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
#     LG_CORNER_SPACE + 0.04),
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
#     (LGPH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
#     LG_CORNER_SPACE + 0.04),
#   Vector(LG_CORNER_SPACE, ((width * LGBW) - LG_CORNER_SPACE),
#     LG_CORNER_SPACE + 0.04),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(LG_CORNER_SPACE, ((width * LGBW) - LG_CORNER_SPACE),
#     LG_CORNER_SPACE + 0.04), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, ((width * LGBW) - LG_CORNER_SPACE),
#     LG_CORNER_SPACE + 0.04),
#   Vector(LG_CORNER_SPACE, ((width * LGBW) - LG_CORNER_SPACE),
#     (LGPH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(LG_CORNER_SPACE, ((width * LGBW) - LG_CORNER_SPACE),
#     (LGPH - LG_CORNER_SPACE)), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     LG_CORNER_SPACE, LG_CORNER_SPACE + 0.04),
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     ((width * LGBW) - LG_CORNER_SPACE), LG_CORNER_SPACE + 0.04),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     ((width * LGBW) - LG_CORNER_SPACE),
#     LG_CORNER_SPACE + 0.04), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     ((width * LGBW) - LG_CORNER_SPACE),
#     LG_CORNER_SPACE + 0.04),
#   Vector(LG_CORNER_SPACE, ((width * LGBW) - LG_CORNER_SPACE),
#     LG_CORNER_SPACE + 0.04),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     ((width * LGBW) - LG_CORNER_SPACE), LG_CORNER_SPACE + 0.04),
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     ((width * LGBW) - LG_CORNER_SPACE),
#     (LGPH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     ((width * LGBW) - LG_CORNER_SPACE),
#     (LGPH - LG_CORNER_SPACE)), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     ((width * LGBW) - LG_CORNER_SPACE),
#     (LGPH - LG_CORNER_SPACE)),
#   Vector(LG_CORNER_SPACE, ((width * LGBW) - LG_CORNER_SPACE),
#     (LGPH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     (LG_WALL_WIDTH - LG_CORNER_SPACE),
#     (LGPH - LG_CORNER_SPACE)),
#   Vector(LG_CORNER_SPACE, (LG_WALL_WIDTH - LG_CORNER_SPACE),
#     (LGPH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     (2 * LG_WALL_WIDTH + LG_CORNER_SPACE),
#     (LGPH - LG_CORNER_SPACE)),
#   Vector(LG_CORNER_SPACE, (2 * LG_WALL_WIDTH + LG_CORNER_SPACE),
#     (LGPH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     (3 * LG_WALL_WIDTH - LG_CORNER_SPACE),
#     LGPH - LG_CORNER_SPACE)),
#   Vector(LG_CORNER_SPACE, (3 * LG_WALL_WIDTH - LG_CORNER_SPACE),
#     (LGPH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(((length * LGBW) - LG_CORNER_SPACE),
#     (4 * LG_WALL_WIDTH + LG_CORNER_SPACE),
#     (LGPH - LG_CORNER_SPACE)),
#   Vector(LG_CORNER_SPACE, (4 * LG_WALL_WIDTH + LG_CORNER_SPACE),
#     (LGPH - LG_CORNER_SPACE)),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE),
#   Vector(LG_CORNER_SPACE, LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, 2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE),
#   Vector(LG_CORNER_SPACE, 3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, 4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE),
#   Vector(LG_CORNER_SPACE, 5 * LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(length * LGBW - LG_CORNER_SPACE, LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE),
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     LG_WALL_WIDTH - LG_CORNER_SPACE, LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     2 * LG_WALL_WIDTH + LG_CORNER_SPACE, LGPH - LG_CORNER_SPACE),
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     3 * LG_WALL_WIDTH - LG_CORNER_SPACE, LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     4 * LG_WALL_WIDTH + LG_CORNER_SPACE, LGPH - LG_CORNER_SPACE),
#   Vector(length * LGBW - LG_CORNER_SPACE,
#    5 * LG_WALL_WIDTH - LG_CORNER_SPACE, LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   Vector(LG_CORNER_SPACE, LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     LG_WALL_WIDTH - LG_CORNER_SPACE, LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, 2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   Vector(LG_CORNER_SPACE, 2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     2 * LG_WALL_WIDTH + LG_CORNER_SPACE, LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, 3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   Vector(LG_CORNER_SPACE, 3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     3 * LG_WALL_WIDTH - LG_CORNER_SPACE, LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, 4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   Vector(LG_CORNER_SPACE, 4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     4 * LG_WALL_WIDTH + LG_CORNER_SPACE, LGPH - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(LG_CORNER_SPACE, LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE), LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     LG_WALL_WIDTH - LG_CORNER_SPACE, LGPH - LG_CORNER_SPACE),
# LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(LG_CORNER_SPACE, 2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE), LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE), LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(LG_CORNER_SPACE, 3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE), LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE), LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(LG_CORNER_SPACE, 4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE), LG_CORNER_SPACE
#  ),
#  Sphere(
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LGPH - LG_CORNER_SPACE), LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   Vector(LG_CORNER_SPACE, 2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   Vector(length * LGBW - LG_CORNER_SPACE,
#     4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(LG_CORNER_SPACE, 3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   Vector(LG_CORNER_SPACE, 4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#     LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Difference(
#   Merge(
#    Box(
#     Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, 0.04),
#     Vector(length * LGBW - LG_CORNER_SPACE,
#         width * LGBW - LG_CORNER_SPACE, LGPH)
#    ),
#    Box(
#     Vector(0, LG_CORNER_SPACE, LG_CORNER_SPACE + 0.04),
#     Vector(length * LGBW,
#         width * LGBW - LG_CORNER_SPACE,
#         LGPH - LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(LG_CORNER_SPACE, 0, LG_CORNER_SPACE + 0.04),
#     Vector(length * LGBW - LG_CORNER_SPACE,
#         width * LGBW, LGPH - LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(0.04, 0.04, 0),
#     Vector((length * LGBW - 0.04),
#         (width * LGBW - 0.04), 0.04 + LG_E)
#    ),
#   ),
#   Union(
#    Box(
#     Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_CORNER_SPACE),
#     Vector(length * LGBW - LG_WALL_WIDTH,
#         width * LGBW - LG_WALL_WIDTH,
#         LG_PLATE_INNER_HEIGHT + LG_E)
#    ),
#    Box(
#     Vector(-LG_E, LG_WALL_WIDTH - LG_CORNER_SPACE, LGPH + LG_E),
#     Vector(LG_CORNER_SPACE,
#         2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#         LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(length * LGBW + LG_E,
#         LG_WALL_WIDTH - LG_CORNER_SPACE, LGPH + LG_E),
#     Vector(length * LGBW - LG_CORNER_SPACE,
#         2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#         LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(0, LG_WALL_WIDTH - LG_CORNER_SPACE, LGPH + LG_E),
#     Vector(length * LGBW,
#         2 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#         LGPH - LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(0, LG_WALL_WIDTH, LGPH),
#     Vector(length * LGBW, 2 * LG_WALL_WIDTH, LG_PLATE_INNER_HEIGHT)
#    ),
#    Box(
#     Vector(-LG_E, 3 * LG_WALL_WIDTH - LG_CORNER_SPACE, LGPH + LG_E),
#     Vector(LG_CORNER_SPACE, 4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#         LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(length * LGBW + LG_E, 3 * LG_WALL_WIDTH - LG_CORNER_SPACE,
#         LGPH + LG_E),
#     Vector(length * LGBW - LG_CORNER_SPACE,
#         4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#         LG_PLATE_INNER_HEIGHT - LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(0, 3 * LG_WALL_WIDTH - LG_CORNER_SPACE, LGPH + LG_E),
#     Vector(length * LGBW,
#         4 * LG_WALL_WIDTH + LG_CORNER_SPACE,
#         LGPH - LG_CORNER_SPACE)
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
