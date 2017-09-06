"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970623 Lutz Uhlmann
20071225 Lutz Uhlmann fixed stud orientation

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_4085c: Plate 1 x 1 with Clip Vertical
"""

from math import acos, sin, pi

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference
from pov.csg.Intersection import Intersection

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere
from pov.finite_solid.Torus import Torus

from pov.object_modifier.Matrix import Matrix
from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from pov.other.Object import Object

from lgeo.include.common.lg_defs import LGBW, LGCS
from lgeo.include.common.lg_defs import LGPH, LG_E
from lgeo.include.common.lg_defs import LG_TOP_HEIGHT, LGWW
from lgeo.include.common.lg_defs import LG_KNOB_INNER_RADIUS, lg_knob
from lgeo.include.common.lg_defs import LG_KNOB_INNER_SPACE


LG_ANGLE = acos((0.13 + LGCS) / (0.16 + LGCS))


def solid():
    """lg_4085c: Plate 1 x 1 with Clip Vertical."""
    result = Union()

    for mir in range(0, 2):
        mirmatrix = Matrix(Vector(1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0))
        if mir == 1:
            mirmatrix = Matrix(Vector(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0))

        result.append(
            Union(
                Sphere(
                    Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGCS),
                    LGCS
                ),
                Sphere(
                    Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Sphere(
                    Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGCS),
                    LGCS
                ),
                Sphere(
                    Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGCS),
                    Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
                    Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGCS),
                    Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGCS),
                    Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(LGBW / 2 - LGCS, 0.2 - LGCS, -LGCS),
                    Vector(LGBW - LGWW, 0.2 - LGCS, -LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(LGBW / 2 - LGCS, 0.2 - LGCS, -LGPH + LGCS),
                    Vector(LGBW - LGWW, 0.2 - LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Sphere(
                    Vector(LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE), 0.13 + LGCS, -LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(LGBW + LGWW - LGCS, 0.13 + LGCS, -LGCS),
                    Vector(LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE), 0.13 + LGCS, -LGCS),
                    LGCS
                ),
                Sphere(
                    Vector(LGBW + LGWW - LGCS, 0.13 + LGCS, -LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(LGBW + LGWW - LGCS, 0.13 + LGCS, -LGCS),
                    Vector(LGBW + LGWW - LGCS, 2 * LGWW - LGCS, -LGCS),
                    LGCS
                ),
                Sphere(
                    Vector(LGBW + LGWW - LGCS, 2 * LGWW - LGCS, -LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(LGBW, 2 * LGWW - LGCS, -LGCS),
                    Vector(LGBW + LGWW - LGCS, 2 * LGWW - LGCS, -LGCS),
                    LGCS
                ),
                Sphere(
                    Vector(LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE), 0.13 + LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(LGBW + LGWW - LGCS, 0.13 + LGCS, -LGPH + LGCS),
                    Vector(LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE), 0.13 + LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Sphere(
                    Vector(LGBW + LGWW - LGCS, 0.13 + LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(LGBW + LGWW - LGCS, 0.13 + LGCS, -LGPH + LGCS),
                    Vector(LGBW + LGWW - LGCS, 2 * LGWW - LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Sphere(
                    Vector(LGBW + LGWW - LGCS, 2 * LGWW - LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(LGBW, 2 * LGWW - LGCS, -LGPH + LGCS),
                    Vector(LGBW + LGWW - LGCS, 2 * LGWW - LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE), 0.13 + LGCS, -LGCS),
                    Vector(LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE), 0.13 + LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(LGBW + LGWW - LGCS, 0.13 + LGCS, -LGCS),
                    Vector(LGBW + LGWW - LGCS, 0.13 + LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Cylinder(
                    Vector(LGBW + LGWW - LGCS, 2 * LGWW - LGCS, -LGCS),
                    Vector(LGBW + LGWW - LGCS, 2 * LGWW - LGCS, -LGPH + LGCS),
                    LGCS
                ),
                Box(
                    Vector(LGBW + LGWW, 0.13 + LGCS, -LGCS),
                    Vector(LGBW + LGWW - LGCS - LG_E, 2 * LGWW - LGCS, -LGPH + LGCS)
                ),
                Box(
                    Vector(LGBW, 2 * LGWW, -LGCS),
                    Vector(LGBW + LGWW - LGCS, 2 * LGWW - LGCS - LG_E, -LGPH + LGCS)
                ),
                Box(
                    Vector(LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE), 0.13 + LGCS + LG_E, -LGCS),
                    Vector(LGBW + LGWW - LGCS, 0.13, -LGPH + LGCS)
                ),
                Difference(
                    Box(
                        Vector(LGBW + LGWW - LGCS, 0.13, 0),
                        Vector(LGBW, 2 * LGWW - LGCS, -LGPH)
                    ),
                    Union(
                        Cylinder(
                            Vector(LGBW, 0, 0),
                            Vector(LGBW, 0, -LGPH),
                            LG_KNOB_INNER_RADIUS
                        ),
                        Cylinder(
                            Vector(LGBW, 0, -LGPH - LG_E),
                            Vector(LGBW, 0, -LGPH + LGCS),
                            LG_KNOB_INNER_RADIUS + LGCS
                        ),
                        Cylinder(
                            Vector(LGBW, 0, LG_E),
                            Vector(LGBW, 0, -LGCS),
                            LG_KNOB_INNER_RADIUS + LGCS
                        ),
                        Difference(
                            Box(
                                Vector(LGBW + LGWW, 0, LG_E),
                                Vector(LGBW - LG_E, 0.13 + LGCS, -LGPH - LG_E)
                            ),
                            Box(
                                Vector(0, 0.4, LG_E),
                                Vector(-0.4, -0.4, -LGPH - LG_E),
                                Rotate(Vector(0, 0, -LG_ANGLE * 180 / pi)),
                                Translate(Vector(LGBW, 0, 0))
                            ),
                        ),
                    ),
                ),
                mirmatrix
            )
        )

    result.append(
        Union(
            Cylinder(
                Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGCS),
                Vector(LGBW / 2 - LGCS, -LGBW / 2 + LGCS, -LGCS),
                LGCS
            ),
            Cylinder(
                Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
                Vector(LGBW / 2 - LGCS, -LGBW / 2 + LGCS, -LGPH + LGCS),
                LGCS
            ),
            Cylinder(
                Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGCS),
                Vector(-LGBW / 2 + LGCS, -LGBW / 2 + LGCS, -LGCS),
                LGCS
            ),
            Cylinder(
                Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
                Vector(-LGBW / 2 + LGCS, -LGBW / 2 + LGCS, -LGPH + LGCS),
                LGCS
            ),
            Difference(
                Union(
                    Box(
                        Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, 0),
                        Vector(-LGBW / 2 + LGCS, -LGBW / 2 + LGCS, -LGPH)
                    ),
                    Box(
                        Vector(LGBW / 2, LGBW / 2 - LGCS, -LGCS),
                        Vector(-LGBW / 2, -LGBW / 2 + LGCS, -LGPH + LGCS)
                    ),
                    Box(
                        Vector(LGBW / 2 - LGCS, LGBW / 2, -LGCS),
                        Vector(-LGBW / 2 + LGCS, -LGBW / 2, -LGPH + LGCS)
                    ),
                ),
                Union(
                    Box(
                        Vector(LGBW / 2 - LGWW, LGBW / 2 - LGWW, -LG_TOP_HEIGHT),
                        Vector(-LGBW / 2 + LGWW, -LGBW / 2 + LGWW, -LGPH - LG_E)
                    ),
                    Object(
                        LG_KNOB_INNER_SPACE,
                        Translate(Vector(0, 0, -LG_TOP_HEIGHT))
                    ),
                ),
            ),
            Object(
                lg_knob(),
                Rotate(Vector(0, 0, -90))
            ),
            Intersection(
                Union(
                    Torus(
                        0.32 - LGCS,
                        LGCS,
                        Rotate(Vector(90, 0, 0)),
                        Translate(Vector(LGBW, 0, -LGCS))
                    ),
                    Torus(
                        0.32 - LGCS,
                        LGCS,
                        Rotate(Vector(90, 0, 0)),
                        Translate(Vector(LGBW, 0, -LGPH + LGCS))
                    ),
                    Difference(
                        Union(
                            Cylinder(
                                Vector(LGBW, 0, 0),
                                Vector(LGBW, 0, -LGPH),
                                0.32 - LGCS
                            ),
                            Cylinder(
                                Vector(LGBW, 0, -LGCS),
                                Vector(LGBW, 0, -LGPH + LGCS),
                                0.32
                            ),
                        ),
                        Union(
                            Cylinder(
                                Vector(LGBW, 0, 0),
                                Vector(LGBW, 0, -LGPH),
                                LG_KNOB_INNER_RADIUS
                            ),
                            Cylinder(
                                Vector(LGBW, 0, -LGPH - LG_E),
                                Vector(LGBW, 0, -LGPH + LGCS),
                                LG_KNOB_INNER_RADIUS + LGCS
                            ),
                            Cylinder(
                                Vector(LGBW, 0, LG_E),
                                Vector(LGBW, 0, -LGCS),
                                LG_KNOB_INNER_RADIUS + LGCS
                            ),
                        ),
                    ),
                ),
                Box(
                    Vector(LGBW, 0.4, LG_E),
                    Vector(LGBW / 2, -0.4, -LGPH - LG_E)
                ),
            ),
            Intersection(
                Torus(
                    LG_KNOB_INNER_RADIUS + LGCS,
                    LGCS,
                    Rotate(Vector(90, 0, 0))
                ),
                Union(
                    Box(
                        Vector(0, 0.4, LGCS + LG_E),
                        Vector(-0.4, -0.4, -LGCS - LG_E),
                        Rotate(Vector(0, 0, LG_ANGLE * 180 / pi))
                    ),
                    Box(
                        Vector(0, 0.4, LGCS + LG_E),
                        Vector(-0.4, -0.4, -LGCS - LG_E),
                        Rotate(Vector(0, 0, -LG_ANGLE * 180 / pi))
                    ),
                ),
                Translate(Vector(LGBW, 0, -LGCS))
            ),
            Intersection(
                Torus(
                    LG_KNOB_INNER_RADIUS + LGCS,
                    LGCS,
                    Rotate(Vector(90, 0, 0))
                ),
                Union(
                    Box(
                        Vector(0, 0.4, LGCS + LG_E),
                        Vector(-0.4, -0.4, -LGCS - LG_E),
                        Rotate(Vector(0, 0, LG_ANGLE * 180 / pi))
                    ),
                    Box(
                        Vector(0, 0.4, LGCS + LG_E),
                        Vector(-0.4, -0.4, -LGCS - LG_E),
                        Rotate(Vector(0, 0, -LG_ANGLE * 180 / pi))
                    ),
                ),
                Translate(Vector(LGBW, 0, -LGPH + LGCS))
            ),
            Box(
                Vector(LGBW - LGWW - LGCS, 0.2 - LGCS, 0),
                Vector(LGBW / 2 - LGCS - LG_E, -0.2 + LGCS, -LGPH)
            ),
            Box(
                Vector(LGBW - LGWW, 0.2, -LGCS),
                Vector(LGBW / 2 - LGCS - LG_E, -0.2, -LGPH + LGCS)
            )
        )
    )

    return result


# #declare lg_4085c_clear =
# Merge(
#  #declare MIR = 0;
#  #while (MIR Vector( 2)
#   Merge(
#    Sphere(
#     Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGCS),
#     LGCS
#    ),
#    Sphere(
#     Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
#     LGCS
#    ),
#    Sphere(
#     Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGCS),
#     LGCS
#    ),
#    Sphere(
#     Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGCS),
#     Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
#     Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGCS),
#     Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGCS),
#     Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(LGBW / 2 - LGCS, 0.2 - LGCS, -LGCS),
#     Vector(LGBW - LG_WALL_WIDTH, 0.2 - LGCS, -LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(LGBW / 2 - LGCS, 0.2 - LGCS, -LGPH + LGCS),
#     Vector(LGBW - LG_WALL_WIDTH, 0.2 - LGCS, -LGPH + LGCS),
#     LGCS
#    ),
#    Sphere(
#     Vector(
#         LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE),
#         0.13 + LGCS,
#         -LGCS
#     ),
#     LGCS
#    ),
#    Cylinder(
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 0.13 + LGCS, -LGCS),
#     Vector(LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE),
#       0.13 + LGCS, -LGCS),
#     LGCS
#    ),
#    Sphere(
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 0.13 + LGCS, -LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 0.13 + LGCS, -LGCS),
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 2 * LG_WALL_WIDTH - LGCS, -LGCS),
#     LGCS
#    ),
#    Sphere(
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 2 * LG_WALL_WIDTH - LGCS, -LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(LGBW, 2 * LG_WALL_WIDTH - LGCS, -LGCS),
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 2 * LG_WALL_WIDTH - LGCS, -LGCS),
#     LGCS
#    ),
#    Sphere(
#     Vector(LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE),
#      0.13 + LGCS, -LGPH + LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 0.13 + LGCS, -LGPH + LGCS),
#     Vector(LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE),
#         0.13 + LGCS, -LGPH + LGCS),
#     LGCS
#    ),
#    Sphere(
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 0.13 + LGCS, -LGPH + LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 0.13 + LGCS, -LGPH + LGCS),
#     Vector(LGBW + LG_WALL_WIDTH - LGCS,
#     2 * LG_WALL_WIDTH - LGCS, -LGPH + LGCS),
#     LGCS
#    ),
#    Sphere(
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 2 * LG_WALL_WIDTH - LGCS,
#     -LGPH + LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(LGBW, 2 * LG_WALL_WIDTH - LGCS, -LGPH + LGCS),
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 2 * LG_WALL_WIDTH - LGCS,
#     -LGPH + LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE),
#     0.13 + LGCS, -LGCS),
#     Vector(LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE),
#     0.13 + LGCS, -LGPH + LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 0.13 + LGCS, -LGCS),
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 0.13 + LGCS, -LGPH + LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 2 * LG_WALL_WIDTH - LGCS, -LGCS),
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 2 * LG_WALL_WIDTH - LGCS,
#     -LGPH + LGCS),
#     LGCS
#    ),
#    Box(
#     Vector(LGBW + LG_WALL_WIDTH, 0.13 + LGCS, -LGCS),
#     Vector(LGBW + LG_WALL_WIDTH - LGCS - LG_E, 2 * LG_WALL_WIDTH - LGCS,
#     -LGPH + LGCS)
#    ),
#    Box(
#     Vector(LGBW, 2 * LG_WALL_WIDTH, -LGCS),
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 2 * LG_WALL_WIDTH - LGCS - LG_E,
#     -LGPH + LGCS)
#    ),
#    Box(
#     Vector(LGBW + (LG_KNOB_INNER_RADIUS + LGCS) * sin(LG_ANGLE),
#     0.13 + LGCS + LG_E, -LGCS),
#     Vector(LGBW + LG_WALL_WIDTH - LGCS, 0.13, -LGPH + LGCS)
#    ),
#    Difference(
#     Box(
#      Vector(LGBW + LG_WALL_WIDTH - LGCS, 0.13, 0),
#      Vector(LGBW, 2 * LG_WALL_WIDTH - LGCS, -LGPH)
#     ),
#     Union(
#      Cylinder(
#       Vector(LGBW, 0, 0),
#       Vector(LGBW, 0, -LGPH),
#       LG_KNOB_INNER_RADIUS
#      ),
#      Cylinder(
#       Vector(LGBW, 0, -LGPH - LG_E),
#       Vector(LGBW, 0, -LGPH + LGCS),
#       LG_KNOB_INNER_RADIUS + LGCS
#      ),
#      Cylinder(
#       Vector(LGBW, 0, LG_E),
#       Vector(LGBW, 0, -LGCS),
#       LG_KNOB_INNER_RADIUS + LGCS
#      ),
#      Difference(
#       Box(
#        Vector(LGBW + LG_WALL_WIDTH, 0, LG_E),
#        Vector(LGBW - LG_E, 0.13 + LGCS, -LGPH - LG_E)
#       ),
#       Box(
#        Vector(0, 0.4, LG_E),
#        Vector(-0.4, -0.4, -LGPH - LG_E)
#        rotate Vector(0, 0, -LG_ANGLE*180/pi)
#        translate Vector(LGBW, 0, 0)
#       ),
#      ),
#     ),
#    ),
#    #if (MIR = 1)
#     matrix Vector(1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0)
#    #end
#   ),
#   #declare MIR = MIR + 1;
#  #end
#  Cylinder(
#   Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGCS),
#   Vector(LGBW / 2 - LGCS, -LGBW / 2 + LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
#   Vector(LGBW / 2 - LGCS, -LGBW / 2 + LGCS, -LGPH + LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGCS),
#   Vector(-LGBW / 2 + LGCS, -LGBW / 2 + LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-LGBW / 2 + LGCS, LGBW / 2 - LGCS, -LGPH + LGCS),
#   Vector(-LGBW / 2 + LGCS, -LGBW / 2 + LGCS, -LGPH + LGCS),
#   LGCS
#  ),
#  Difference(
#   Merge(
#    Box(
#     Vector(LGBW / 2 - LGCS, LGBW / 2 - LGCS, 0),
#     Vector(-LGBW / 2 + LGCS, -LGBW / 2 + LGCS, -LGPH)
#    ),
#    Box(
#     Vector(LGBW / 2, LGBW / 2 - LGCS, -LGCS),
#     Vector(-LGBW / 2, -LGBW / 2 + LGCS, -LGPH + LGCS)
#    ),
#    Box(
#     Vector(LGBW / 2 - LGCS, LGBW / 2, -LGCS),
#     Vector(-LGBW / 2 + LGCS, -LGBW / 2, -LGPH + LGCS)
#    ),
#   ),
#   Union(
#    Box(
#     Vector(LGBW / 2 - LG_WALL_WIDTH, LGBW / 2 - LG_WALL_WIDTH,
#     -LG_TOP_HEIGHT),
#     Vector(-LGBW / 2 + LG_WALL_WIDTH, -LGBW / 2 + LG_WALL_WIDTH,
#     -LGPH - LG_E)
#    ),
#    Object(
#     LG_KNOB_INNER_SPACE
#     translate Vector(0, 0, -LG_TOP_HEIGHT)
#    ),
#   ),
#  ),
#  Object(
#   lg_knob_clear
#   rotate Vector(0, 0, -90)
#  ),
#  Intersection(
#   Merge(
#    Torus(
#     0.32 - LGCS,
#     LGCS
#     rotate Vector(90, 0, 0)
#     translate Vector(LGBW, 0, -LGCS)
#    ),
#    Torus(
#     0.32 - LGCS,
#     LGCS
#     rotate Vector(90, 0, 0)
#     translate Vector(LGBW, 0, -LGPH + LGCS)
#    ),
#    Difference(
#     Merge(
#      Cylinder(
#       Vector(LGBW, 0, 0),
#       Vector(LGBW, 0, -LGPH),
#       0.32 - LGCS
#      ),
#      Cylinder(
#       Vector(LGBW, 0, -LGCS),
#       Vector(LGBW, 0, -LGPH + LGCS),
#       0.32
#      ),
#     ),
#     Union(
#      Cylinder(
#       Vector(LGBW, 0, 0),
#       Vector(LGBW, 0, -LGPH),
#       LG_KNOB_INNER_RADIUS
#      ),
#      Cylinder(
#       Vector(LGBW, 0, -LGPH - LG_E),
#       Vector(LGBW, 0, -LGPH + LGCS),
#       LG_KNOB_INNER_RADIUS + LGCS
#      ),
#      Cylinder(
#       Vector(LGBW, 0, LG_E),
#       Vector(LGBW, 0, -LGCS),
#       LG_KNOB_INNER_RADIUS + LGCS
#      ),
#     ),
#    ),
#   ),
#   Box(
#    Vector(LGBW, 0.4, LG_E),
#    Vector(LGBW / 2, -0.4, -LGPH - LG_E)
#   ),
#  ),
#  Intersection(
#   Torus(
#    LG_KNOB_INNER_RADIUS + LGCS,
#    LGCS
#    rotate Vector(90, 0, 0)
#   ),
#   Union(
#    Box(
#     Vector(0, 0.4, LGCS + LG_E),
#     Vector(-0.4, -0.4, -LGCS - LG_E)
#     rotate Vector(0, 0, LG_ANGLE*180/pi)
#    ),
#    Box(
#     Vector(0, 0.4, LGCS + LG_E),
#     Vector(-0.4, -0.4, -LGCS - LG_E)
#     rotate Vector(0, 0, -LG_ANGLE*180/pi)
#    ),
#   ),
#   translate Vector(LGBW, 0, -LGCS)
#  ),
#  Intersection(
#   Torus(
#    LG_KNOB_INNER_RADIUS + LGCS,
#    LGCS
#    rotate Vector(90, 0, 0)
#   ),
#   Union(
#    Box(
#     Vector(0, 0.4, LGCS + LG_E),
#     Vector(-0.4, -0.4, -LGCS - LG_E)
#     rotate Vector(0, 0, LG_ANGLE*180/pi)
#    ),
#    Box(
#     Vector(0, 0.4, LGCS + LG_E),
#     Vector(-0.4, -0.4, -LGCS - LG_E)
#     rotate Vector(0, 0, -LG_ANGLE*180/pi)
#    ),
#   ),
#   translate Vector(LGBW, 0, -LGPH + LGCS)
#  ),
#  Box(
#   Vector(LGBW - LG_WALL_WIDTH - LGCS, 0.2 - LGCS, 0),
#   Vector(LGBW / 2 - LGCS - LG_E, -0.2+LGCS, -LGPH)
#  ),
#  Box(
#   Vector(LGBW - LG_WALL_WIDTH, 0.2, -LGCS),
#   Vector(LGBW / 2 - LGCS - LG_E, -0.2, -LGPH + LGCS)
#  ),
# ),

# #end
