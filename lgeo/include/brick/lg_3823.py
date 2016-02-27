"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970913 Lutz Uhlmann
20080102 Lutz Uhlmann fixed hollow stud logo and orientation

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_3823: Windscreen 2 x 4 x 2

@Todo: Needs to be redone!!
"""

from math import atan2, cos, sin, pi

from lgeo.include.common.lg_defs import LGCS, LGBW, LGPH, LG_E, LGBH
from lgeo.include.common.lg_defs import LG_WALL_WIDTH, LG_PLATE_INNER_HEIGHT
from lgeo.include.common.lg_defs import LG_TOP_HEIGHT, LG_KNOB_INNER_RADIUS
from lgeo.include.common.lg_defs import lg_tech_knob_logo_clear

from pov.basic.Vector import Vector

from pov.csg.Merge import Merge
from pov.csg.Union import Union
from pov.csg.Intersection import Intersection
from pov.csg.Difference import Difference

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere
from pov.finite_solid.Torus import Torus

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate
from pov.object_modifier.Matrix import Matrix
from pov.object_modifier.Scale import Scale

from pov.other.Object import Object


LG_ANGLE = atan2(LGBW, 5 * LGPH) * 180 / pi

# #ifdef(lg_3823)
# #else
# #declare LG_ANGLE=atan2(LGBW, 5 * LGPH)*180/pi;
# #declare lg_3823 =
# Union(
#  #declare MIR = 0;
#  #while (MIR Vector( 2)
#   Union(
#    Cylinder(
#     Vector(0, 2 * LGBW - LGCS, -LGCS),
#     Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
#     LGCS
#    ),
#    Sphere(
#     Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
#     LGCS
#    ),
#    Sphere(
#     Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, -2 * LGBH + LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
#     Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, -2 * LGBH + LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
#     Vector(-LGBW / 2 + LGCS, 1.5 * LGBW + 0.12, -LGCS),
#     LGCS
#    ),
#    Intersection(
#     Torus(
#      LGBW / 2 - LGCS,
#      LGCS
#      Rotate(Vector(90, 0, 0)
#     ),
#     Box(
#      Vector(-LGBW / 2 - LG_E, -LGBW / 2 - LG_E, LGCS + LG_E),
#      Vector(0, 0, -LGCS - LG_E)
#     ),
#     Translate(Vector(0, 1.5 * LGBW + 0.12, -LGCS)
#    ),
#    Cylinder(
#     Vector(0, LGBW + 0.12 + LGCS, -LGCS),
#     Vector(LGBW / 2 - LG_WALL_WIDTH / 2 + LGCS, LGBW + 0.12 + LGCS, -LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(LGBW, 2 * LGBW - LGCS, -2 * LGBH + LGCS),
#     Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, -2 * LGBH + LGCS),
#     LGCS
#    ),
#    Intersection(
#     Difference(
#      Cylinder(
#       Vector(0, 0, 0),
#       Vector(0, 0, -5 * LGPH),
#       LGBW / 2
#      ),
#      Cylinder(
#       Vector(0, 0, LGCS + LG_E),
#       Vector(0, 0, -6*LGPH),
#       LGBW / 2 - LG_WALL_WIDTH
#      ),
#     ),
#     Box(
#      Vector(LGBW / 2 + LG_E, LGBW / 2 + LG_E, LGCS + LG_E),
#      Vector(0, 0, -2 * LGBH)
#     ),
#     Martix(Vector(1, 0, 2/LGBW*LGCS*sin(LG_ANGLE*pi/180),
#             0, 1, 0,
#             -1/2, 0, 1,
#             LGCS*(cos(LG_ANGLE*pi/180)-1), 3 * LGBW / 2, -LGCS)
#    ),
#    Intersection(
#     Torus(
#      LGBW / 2 - LGCS,
#      LGCS
#      Rotate(Vector(90, 0, 0)
#     ),
#     Box(
#      Vector(LGBW / 2 + LG_E, LGBW / 2 + LG_E, LGCS + LG_E),
#      Vector(0, 0, -LGCS - LG_E)
#     ),
#     Translate(Vector(0, 3 * LGBW / 2, -LGCS)
#    ),
#    Intersection(
#     Torus(
#      LGBW / 2 - LGCS,
#      LGCS
#      Rotate(Vector(90, 0, 0)
#     ),
#     Box(
#      Vector(LGBW / 2 + LG_E, LGBW / 2 + LG_E, LGCS + LG_E),
#      Vector(0, 0, -LGCS - LG_E)
#     ),
#     Translate(Vector(LGBW, 3 * LGBW / 2, -5 * LGPH - LGCS)
#    ),
#    Intersection(
#     Torus(
#      LGBW / 2 - LGCS,
#      LGCS
#      Rotate(Vector(90, 0, 0)
#     ),
#     Box(
#      Vector(LGBW / 2 + LG_E, LGBW / 2 + LG_E, LGCS + LG_E),
#      Vector(0, 0, -LGCS - LG_E)
#     ),
#     Translate(Vector(LGBW, 3 * LGBW / 2, -2 * LGBH + LGCS)
#    ),
#    Difference(
#     Union(
#      Cylinder(
#       Vector(LGBW / 2 + LGCS, LGBW + LGCS, -5 * LGPH - LGCS),
#       Vector(-LGCS, LGBW + LGCS, -5 * LGPH - LGCS),
#       LGCS
#      ),
#      Cylinder(
#       Vector(-LGBW / 2 + LGCS, 1.5 * LGBW - LGCS, -5 * LGPH - LGCS),
#       Vector(-LGBW / 2 + LGCS, 2 * LGBW - LG_WALL_WIDTH + LG_E,
#           -5 * LGPH - LGCS),
#       LGCS
#      ),
#      Cylinder(
#       Vector(LGBW / 2 + LGCS, LGBW + LGCS, -6 * LGPH +LGCS),
#       Vector(-LGCS, LGBW + LGCS, -6 * LGPH +LGCS),
#       LGCS
#      ),
#      Cylinder(
#       Vector(-LGBW / 2 + LGCS, 1.5 * LGBW - LGCS, -6 * LGPH +LGCS),
#       Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, -6 * LGPH +LGCS),
#       LGCS
#      ),
#      Box(
#       Vector(LGBW / 2 + LGCS + LG_E, LGBW + LGCS, -2 * LGBH),
#       Vector(-LGBW / 2, LGBW + LG_WALL_WIDTH, -2 * LGBH + LGCS + LG_E)
#      ),
#      Box(
#       Vector(-LGBW / 2 + LGCS, LGBW + LGCS, -2 * LGBH),
#       Vector(-LGBW / 2 + LG_WALL_WIDTH, 2 * LGBW - LGCS,
#      -2 * LGBH + LGCS + LG_E)
#      ),
#      Box(
#       Vector(LGBW + LGCS, 2 * LGBW - LGCS, -5 * LGPH),
#       Vector(-LGBW / 2 + LGCS, LGBW + LGCS,
#       -2 * LGBH + LG_PLATE_INNER_HEIGHT)
#      ),
#      Box(
#       Vector(LGBW / 2 + LGCS + LG_E, LGBW, -5 * LGPH - LGCS),
#       Vector(-LGBW / 2, LGBW + LG_WALL_WIDTH, -2 * LGBH + LGCS)
#      ),
#      Box(
#       Vector(-LGBW / 2, LGBW + LGCS, -5 * LGPH - LGCS),
#       Vector(-LGBW / 2 + LG_WALL_WIDTH, 2 * LGBW - LGCS, -2 * LGBH + LGCS)
#      ),
#     ),
#     Cylinder(
#      Vector(-LGBW / 2, LGBW, -2 * LGBH - LG_E),
#      Vector(-LGBW / 2, LGBW, -5 * LGPH + LG_E),
#      LGBW / 2
#     ),
#    ),
#    Cylinder(
#     Vector(LGBW / 2, 1.5 * LGBW, -5 * LGPH - LG_TOP_HEIGHT + LG_E),
#     Vector(LGBW / 2, 1.5 * LGBW, -2 * LGBH),
#     LG_KNOB_INNER_RADIUS
#    ),
#    Cylinder(
#     Vector(LGBW, LGBW, -5 * LGPH - LG_TOP_HEIGHT + LG_E),
#     Vector(LGBW, LGBW, -2 * LGBH),
#     LG_KNOB_INNER_RADIUS
#    ),
#    Intersection(
#     Difference(
#      Union(
#       Cylinder(
#        Vector(LGBW, 1.5 * LGBW, -5 * LGPH - LGCS),
#        Vector(LGBW, 1.5 * LGBW, -2 * LGBH + LGCS),
#        LGBW / 2
#       ),
#       Cylinder(
#        Vector(LGBW, 1.5 * LGBW, -5 * LGPH),
#        Vector(LGBW, 1.5 * LGBW, -2 * LGBH),
#        LGBW / 2 - LGCS
#       ),
#      ),
#      Cylinder(
#       Vector(LGBW, 1.5 * LGBW, -5 * LGPH - LG_TOP_HEIGHT),
#       Vector(LGBW, 1.5 * LGBW, -2 * LGBH - LG_E),
#       LGBW / 2 - LG_WALL_WIDTH
#      ),
#     ),
#     Box(
#      Vector(LGBW, 1.5 * LGBW, -5 * LGPH + LGCS),
#      Vector(1.5 * LGBW + LG_E, 2 * LGBW + LG_E, -2 * LGBH - LG_E)
#     ),
#    ),
#    Difference(
#     Union(
#      Box(
#       Vector(LGBW, 2 * LGBW, -2 * LGBH + LGCS),
#       Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS - LG_E, -LGCS)
#      ),
#      Box(
#       Vector(LGBW, 2 * LGBW - LG_WALL_WIDTH, -2 * LGBH),
#       Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, 0)
#      ),
#     ),
#     Box(
#      Vector(LGBW + LG_E, LGBW / 2 + LG_E, LGCS + LG_E),
#      Vector(0, 0, -2 * LGBH)
#      Martix(Vector(1, 0, 2/LGBW*LGCS*sin(LG_ANGLE*pi/180),
#              0, 1, 0,
#              -1/2, 0, 1,
#              LGCS*(cos(LG_ANGLE*pi/180)-1), 3 * LGBW / 2, -LGCS)
#     ),
#    ),
#    Box(
#     Vector(-LGBW / 2, 2 * LGBW - LGCS, -5 * LGPH - LGCS),
#     Vector(-LGBW / 2 + LGCS + LG_E, 2 * LGBW - LG_WALL_WIDTH, -LGCS)
#    ),
#    Intersection(
#     Union(
#      Cylinder(
#       Vector(0, 0, 0),
#       Vector(0, 0, -LGCS - LG_E),
#       LGBW / 2 - LGCS
#      ),
#      Cylinder(
#       Vector(0, 0, -LGCS),
#       Vector(0, 0, -LG_WALL_WIDTH),
#       LGBW / 2
#      ),
#     ),
#     Box(
#      Vector(-LGBW / 2 - LG_E, -LGBW / 2 - LG_E, LG_E),
#      Vector(0, 0, -LG_WALL_WIDTH - LG_E)
#     ),
#     Translate(Vector(0, 1.5 * LGBW + 0.12, 0)
#    ),
#    Intersection(
#     Union(
#      Cylinder(
#       Vector(0, 0, 0),
#       Vector(0, 0, -LGCS - LG_E),
#       LGBW / 2 - LGCS
#      ),
#      Cylinder(
#       Vector(0, 0, -LGCS),
#       Vector(0, 0, -LG_WALL_WIDTH),
#       LGBW / 2
#      ),
#     ),
#     Box(
#      Vector(LGBW / 2 - LG_E, LGBW / 2 - LG_E, LG_E),
#      Vector(0, 0, -LG_WALL_WIDTH - LG_E)
#     ),
#     Translate(Vector(0, 1.5 * LGBW, 0)
#    ),
#    Box(
#     Vector(LGBW / 2 - LGCS, LGBW + 0.12 + LGCS, 0),
#     Vector(0, 1.5 * LGBW, -LGCS - LG_E)
#    ),
#    Box(
#     Vector(LGBW / 2 - LGCS, LGBW + 0.12, -LGCS),
#     Vector(0, 1.5 * LGBW, -LG_WALL_WIDTH)
#    ),
#    Box(
#     Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, 0),
#     Vector(0, 1.5 * LGBW + 0.12, -LGCS - LG_E)
#    ),
#    Box(
#     Vector(-LGBW / 2, 2 * LGBW - LGCS, -LGCS),
#     Vector(0, 1.5 * LGBW + 0.12, -LG_WALL_WIDTH)
#    ),
#    Object(
#     lg_tech_knob_logo
#     Rotate(Vector(0, 0, 90)
#     Scale(Vector(1, 1-2*MIR, 1)
#     Translate(Vector(0, 1.5 * LGBW, 0)
#    ),
#    #if (MIR = 1)
#     Martix(Vector(1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0)
#    #end
#   ),
#   #declare MIR = MIR + 1;
#  #end
#  Cylinder(
#   Vector(3 * LGBW / 2 - LGCS, 3 * LGBW / 2, -5 * LGPH - LGCS),
#   Vector(3 * LGBW / 2 - LGCS, -3 * LGBW / 2, -5 * LGPH - LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(3 * LGBW / 2 - LGCS, 3 * LGBW / 2, -2 * LGBH + LGCS),
#   Vector(3 * LGBW / 2 - LGCS, -3 * LGBW / 2, -2 * LGBH + LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGBW / 2 - LGCS, 3 * LGBW / 2, -LGCS),
#   Vector(LGBW / 2 - LGCS, -3 * LGBW / 2, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGBW / 2 - LG_WALL_WIDTH / 2 + LGCS, LGBW + 0.12 + LGCS, -LGCS),
#   Vector(LGBW / 2 - LG_WALL_WIDTH / 2 + LGCS, -LGBW-0.12-LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGBW / 2 + LGCS, LGBW + LGCS, -2 * LGBH + LGCS),
#   Vector(LGBW / 2 + LGCS, -LGBW - LGCS, -2 * LGBH + LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGBW / 2 + LGCS, LGBW + LGCS, -5 * LGPH - LGCS),
#   Vector(LGBW / 2 + LGCS, -LGBW - LGCS, -5 * LGPH - LGCS),
#   LGCS
#  ),
#  Box(
#   Vector(LGBW / 2 + LGCS, LGBW + LG_WALL_WIDTH, -2 * LGBH),
#   Vector(LGBW / 2 + LG_WALL_WIDTH, -LGBW - LG_WALL_WIDTH,
#   -2 * LGBH + LGCS + LG_E)
#  ),
#  Box(
#   Vector(1.5 * LGBW - LGCS, 1.5 * LGBW, -2 * LGBH),
#   Vector(1.5 * LGBW - LG_WALL_WIDTH, -1.5 * LGBW, -2 * LGBH + LGCS + LG_E)
#  ),
#  Box(
#   Vector(LGBW / 2, LGBW + LG_WALL_WIDTH, -5 * LGPH - LGCS),
#   Vector(LGBW / 2 + LG_WALL_WIDTH, -LGBW - LG_WALL_WIDTH, -2 * LGBH + LGCS)
#  ),
#  Box(
#   Vector(1.5 * LGBW, 1.5 * LGBW, -5 * LGPH - LGCS),
#   Vector(1.5 * LGBW - LG_WALL_WIDTH, -1.5 * LGBW, -2 * LGBH + LGCS)
#  ),
#  Box(
#   Vector(1.5 * LGBW - LGCS, 1.5 * LGBW, -5 * LGPH),
#   Vector(LGBW / 2 + LGCS, -1.5 * LGBW, -2 * LGBH + LG_PLATE_INNER_HEIGHT)
#  ),
#  Difference(
#   Union(
#    Box(
#     Vector(LGBW / 2, 1.5 * LGBW, 0),
#     Vector(LGBW / 2 - LG_WALL_WIDTH, -1.5 * LGBW, -5 * LGPH)
#     Martix(Vector(1, 0, 2/LGBW*LGCS*sin(LG_ANGLE*pi/180),
#             0, 1, 0,
#             -1/2, 0, 1,
#             LGCS*(cos(LG_ANGLE*pi/180)-1), 0, -LGCS)
#    ),
#    Box(
#     Vector(LGBW / 2 - LGCS, 1.5 * LGBW, 0),
#     Vector(LGBW / 2 - LG_WALL_WIDTH, -1.5 * LGBW, -LG_WALL_WIDTH / 2)
#    ),
#   ),
#   Union(
#    Box(
#     Vector(LGBW / 2 - LG_WALL_WIDTH / 2, LGBW + 0.12 + LGCS, LG_E),
#     Vector(LG_WALL_WIDTH, -LGBW-0.12-LGCS, -LG_WALL_WIDTH - LG_E)
#    ),
#    Box(
#     Vector(LGBW / 2 - LG_WALL_WIDTH / 2 + LGCS, LGBW + 0.12 + LGCS, LG_E),
#     Vector(LG_WALL_WIDTH, -LGBW-0.12-LGCS, -LGCS)
#    ),
#   ),
#  ),
#  Cylinder(
#   Vector(LGBW, 0, -5 * LGPH - LG_TOP_HEIGHT + LG_E),
#   Vector(LGBW, 0, -2 * LGBH),
#   LG_KNOB_INNER_RADIUS
#  ),
# ),


def clear():
    """return lg_3823: Windscreen 2 x 4 x 2."""
    result = Merge(
    )

    for mir in range(0, 2):
        mirmatrix = Matrix(Vector(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        if mir == 1:
            mirmatrix = Matrix(Vector(1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0))

        result.append(
            Merge(
                Cylinder(
                    Vector(0, 2 * LGBW - LGCS, -LGCS),
                    Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
                    LGCS
                ),
                Sphere(
                    Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
                    LGCS
                ),
                Sphere(
                    Vector(
                        -LGBW / 2 + LGCS, 2 * LGBW - LGCS, -2 * LGBH + LGCS
                    ),
                    LGCS
                ),
                Cylinder(
                    Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
                    Vector(
                        -LGBW / 2 + LGCS, 2 * LGBW - LGCS, -2 * LGBH + LGCS
                    ),
                    LGCS
                ),
                Cylinder(
                    Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
                    Vector(-LGBW / 2 + LGCS, 1.5 * LGBW + 0.12, -LGCS),
                    LGCS
                ),
                Intersection(
                    Torus(
                        LGBW / 2 - LGCS,
                        LGCS,
                        Rotate(Vector(90, 0, 0))
                    ),
                    Box(
                        Vector(
                            -LGBW / 2 - LG_E, -LGBW / 2 - LG_E, LGCS + LG_E
                        ),
                        Vector(0, 0, -LGCS - LG_E)
                    ),
                    Translate(Vector(0, 1.5 * LGBW + 0.12, -LGCS))
                ),
                Cylinder(
                    Vector(0, LGBW + 0.12 + LGCS, -LGCS),
                    Vector(
                        LGBW / 2 - LG_WALL_WIDTH / 2 + LGCS,
                        LGBW + 0.12 + LGCS,
                        -LGCS
                    ),
                    LGCS
                ),
                Cylinder(
                    Vector(LGBW, 2 * LGBW - LGCS, -2 * LGBH + LGCS),
                    Vector(
                        -LGBW / 2 + LGCS, 2 * LGBW - LGCS, -2 * LGBH + LGCS
                    ),
                    LGCS
                ),
                Intersection(
                    Difference(
                        Cylinder(
                            Vector(0, 0, 0),
                            Vector(0, 0, -2.5 * LGPH),
                            # Vector(0, 0, -5 * LGPH),
                            LGBW / 2
                        ),
                        Cylinder(
                            Vector(0, 0, LGCS + LG_E),
                            Vector(0, 0, -3 * LGPH),
                            # Vector(0, 0, -6 * LGPH),
                            LGBW / 2 - LG_WALL_WIDTH
                        ),
                    ),
                    Box(
                        Vector(LGBW / 2 + LG_E, LGBW / 2 + LG_E, LGCS + LG_E),
                        Vector(0, 0, -2 * LGBH)
                    ),
                    Matrix(
                        Vector(
                            1, 0, 2 / LGBW * LGCS * sin(LG_ANGLE * pi / 180),
                            0, 1, 0,
                            -1 / 2, 0, 1,
                            LGCS * (cos(LG_ANGLE * pi / 180) - 1),
                            3 * LGBW / 2, -LGCS
                        )
                    )
                ),
                Intersection(
                    Difference(
                        Cylinder(
                            Vector(0, 0, -2.5 * LGPH),
                            Vector(0, 0, -5 * LGPH),
                            # Vector(0, 0, -5 * LGPH),
                            LGBW / 2
                        ),
                        Cylinder(
                            Vector(0, 0, -2.5 * LGPH),
                            Vector(0, 0, -5 * LGPH),
                            # Vector(0, 0, -6 * LGPH),
                            LGBW / 2 - LG_WALL_WIDTH
                        ),
                    ),
                    Box(
                        Vector(LGBW / 2 + LG_E, LGBW / 2 + LG_E, LGCS + LG_E),
                        Vector(0, 0, -2 * LGBH)
                    ),
                    Translate(Vector(1 * LGBW, 0 * LGBW, 0)),
                    Matrix(
                        Vector(
                            1, 0, 0,
                            # 2 / LGBW * LGCS * sin(LG_ANGLE * pi / 180),
                            0, 1, 0,
                            0, 0, 1,
                            0,  # LGCS * (cos(LG_ANGLE * pi / 180) -1),
                            3 * LGBW / 2, -LGCS
                        )
                    ),
                ),
                Intersection(
                    Torus(
                        LGBW / 2 - LGCS,
                        LGCS,
                        Rotate(Vector(90, 0, 0))
                    ),
                    Box(
                        Vector(LGBW / 2 + LG_E, LGBW / 2 + LG_E, LGCS + LG_E),
                        Vector(0, 0, -LGCS - LG_E)
                    ),
                    Translate(Vector(0, 3 * LGBW / 2, -LGCS))
                ),
                Intersection(
                    Torus(
                        LGBW / 2 - LGCS,
                        LGCS,
                        Rotate(Vector(90, 0, 0))
                    ),
                    Box(
                        Vector(LGBW / 2 + LG_E, LGBW / 2 + LG_E, LGCS + LG_E),
                        Vector(0, 0, -LGCS - LG_E)
                    ),
                    Translate(Vector(LGBW, 3 * LGBW / 2, -5 * LGPH - LGCS))
                ),
                Intersection(
                    Torus(
                        LGBW / 2 - LGCS,
                        LGCS,
                        Rotate(Vector(90, 0, 0))
                    ),
                    Box(
                        Vector(LGBW / 2 + LG_E, LGBW / 2 + LG_E, LGCS + LG_E),
                        Vector(0, 0, -LGCS - LG_E)
                    ),
                    Translate(Vector(LGBW, 3 * LGBW / 2, -2 * LGBH + LGCS))
                ),
                Difference(
                    Merge(
                        Cylinder(
                            Vector(
                                LGBW / 2 + LGCS, LGBW + LGCS, -5 * LGPH - LGCS
                            ),
                            Vector(-LGCS, LGBW + LGCS, -5 * LGPH - LGCS),
                            LGCS
                        ),
                        Cylinder(
                            Vector(
                                -LGBW / 2 + LGCS,
                                1.5 * LGBW - LGCS,
                                -5 * LGPH - LGCS
                            ),
                            Vector(
                                -LGBW / 2 + LGCS,
                                2 * LGBW - LG_WALL_WIDTH + LG_E,
                                -5 * LGPH - LGCS
                            ),
                            LGCS
                        ),
                        Cylinder(
                            Vector(
                                LGBW / 2 + LGCS, LGBW + LGCS, -6 * LGPH + LGCS
                            ),
                            Vector(-LGCS, LGBW + LGCS, -6 * LGPH + LGCS),
                            LGCS
                        ),
                        Cylinder(
                            Vector(
                                -LGBW / 2 + LGCS,
                                1.5 * LGBW - LGCS,
                                -6 * LGPH + LGCS
                            ),
                            Vector(
                                -LGBW / 2 + LGCS,
                                2 * LGBW - LGCS,
                                -6 * LGPH + LGCS
                            ),
                            LGCS
                        ),
                        Box(
                            Vector(
                                LGBW / 2 + LGCS + LG_E,
                                LGBW + LGCS,
                                -2 * LGBH
                            ),
                            Vector(
                                -LGBW / 2,
                                LGBW + LG_WALL_WIDTH,
                                -2 * LGBH + LGCS + LG_E
                            )
                        ),
                        Box(
                            Vector(-LGBW / 2 + LGCS, LGBW + LGCS, -2 * LGBH),
                            Vector(
                                -LGBW / 2 + LG_WALL_WIDTH,
                                2 * LGBW - LGCS,
                                -2 * LGBH + LGCS + LG_E
                            )
                        ),
                        Box(
                            Vector(LGBW + LGCS, 2 * LGBW - LGCS, -5 * LGPH),
                            Vector(
                                -LGBW / 2 + LGCS,
                                LGBW + LGCS,
                                -2 * LGBH + LG_PLATE_INNER_HEIGHT
                            )
                        ),
                        Box(
                            Vector(
                                LGBW / 2 + LGCS + LG_E, LGBW, -5 * LGPH - LGCS
                            ),
                            Vector(
                                -LGBW / 2,
                                LGBW + LG_WALL_WIDTH,
                                -2 * LGBH + LGCS
                            )
                        ),
                        Box(
                            Vector(-LGBW / 2, LGBW + LGCS, -5 * LGPH - LGCS),
                            Vector(
                                -LGBW / 2 + LG_WALL_WIDTH,
                                2 * LGBW - LGCS,
                                -2 * LGBH + LGCS
                            )
                        ),
                    ),
                    Cylinder(
                        Vector(-LGBW / 2, LGBW, -2 * LGBH - LG_E),
                        Vector(-LGBW / 2, LGBW, -5 * LGPH + LG_E),
                        LGBW / 2
                    ),
                ),
                Cylinder(
                    Vector(
                        LGBW / 2, 1.5 * LGBW, -5 * LGPH - LG_TOP_HEIGHT + LG_E
                    ),
                    Vector(LGBW / 2, 1.5 * LGBW, -2 * LGBH),
                    LG_KNOB_INNER_RADIUS
                ),
                Cylinder(
                    Vector(LGBW, LGBW, -5 * LGPH - LG_TOP_HEIGHT + LG_E),
                    Vector(LGBW, LGBW, -2 * LGBH),
                    LG_KNOB_INNER_RADIUS
                ),
                Intersection(
                    Difference(
                        Merge(
                            Cylinder(
                                Vector(LGBW, 1.5 * LGBW, -5 * LGPH - LGCS),
                                Vector(LGBW, 1.5 * LGBW, -2 * LGBH + LGCS),
                                LGBW / 2
                            ),
                            Cylinder(
                                Vector(LGBW, 1.5 * LGBW, -5 * LGPH),
                                Vector(LGBW, 1.5 * LGBW, -2 * LGBH),
                                LGBW / 2 - LGCS
                            ),
                        ),
                        Cylinder(
                            Vector(
                                LGBW, 1.5 * LGBW, -5 * LGPH - LG_TOP_HEIGHT
                            ),
                            Vector(LGBW, 1.5 * LGBW, -2 * LGBH - LG_E),
                            LGBW / 2 - LG_WALL_WIDTH
                        ),
                    ),
                    Box(
                        Vector(LGBW, 1.5 * LGBW, -5 * LGPH + LGCS),
                        Vector(
                            1.5 * LGBW + LG_E,
                            2 * LGBW + LG_E,
                            -2 * LGBH - LG_E
                        )
                    ),
                ),
                Difference(
                    Merge(
                        Box(
                            Vector(LGBW, 2 * LGBW, -2 * LGBH + LGCS),
                            Vector(
                                -LGBW / 2 + LGCS, 2 * LGBW - LGCS - LG_E, -LGCS
                            )
                        ),
                        Box(
                            Vector(LGBW, 2 * LGBW - LG_WALL_WIDTH, -2 * LGBH),
                            Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, 0)
                        ),
                    ),
                    Box(
                        Vector(LGBW + LG_E, LGBW / 2 + LG_E, LGCS + LG_E),
                        Vector(0, 0, -2 * LGBH),
                        Matrix(
                            Vector(
                                1, 0,
                                2 / LGBW * LGCS * sin(LG_ANGLE * pi / 180),
                                0, 1, 0,
                                -1 / 2, 0, 1,
                                LGCS * (cos(LG_ANGLE * pi / 180) - 1),
                                3 * LGBW / 2, -LGCS
                            )
                        )
                    ),
                ),
                Box(
                    Vector(-LGBW / 2, 2 * LGBW - LGCS, -5 * LGPH - LGCS),
                    Vector(
                        -LGBW / 2 + LGCS + LG_E,
                        2 * LGBW - LG_WALL_WIDTH,
                        -LGCS
                    )
                ),
                Intersection(
                    Merge(
                        Cylinder(
                            Vector(0, 0, 0),
                            Vector(0, 0, -LGCS - LG_E),
                            LGBW / 2 - LGCS
                        ),
                        Cylinder(
                            Vector(0, 0, -LGCS),
                            Vector(0, 0, -LG_WALL_WIDTH),
                            LGBW / 2
                        ),
                    ),
                    Box(
                        Vector(-LGBW / 2 - LG_E, -LGBW / 2 - LG_E, LG_E),
                        Vector(0, 0, -LG_WALL_WIDTH - LG_E)
                    ),
                    Translate(Vector(0, 1.5 * LGBW + 0.12, 0))
                ),
                Intersection(
                    Merge(
                        Cylinder(
                            Vector(0, 0, 0),
                            Vector(0, 0, -LGCS - LG_E),
                            LGBW / 2 - LGCS
                        ),
                        Cylinder(
                            Vector(0, 0, -LGCS),
                            Vector(0, 0, -LG_WALL_WIDTH),
                            LGBW / 2
                        ),
                    ),
                    Box(
                        Vector(LGBW / 2 - LG_E, LGBW / 2 - LG_E, LG_E),
                        Vector(0, 0, -LG_WALL_WIDTH - LG_E)
                    ),
                    Translate(Vector(0, 1.5 * LGBW, 0))
                ),
                Box(
                    Vector(LGBW / 2 - LGCS, LGBW + 0.12 + LGCS, 0),
                    Vector(0, 1.5 * LGBW, -LGCS - LG_E)
                ),
                Box(
                    Vector(LGBW / 2 - LGCS, LGBW + 0.12, -LGCS),
                    Vector(0, 1.5 * LGBW, -LG_WALL_WIDTH)
                ),
                Box(
                    Vector(-LGBW / 2 + LGCS, 2 * LGBW - LGCS, 0),
                    Vector(0, 1.5 * LGBW + 0.12, -LGCS - LG_E)
                ),
                Box(
                    Vector(-LGBW / 2, 2 * LGBW - LGCS, -LGCS),
                    Vector(0, 1.5 * LGBW + 0.12, -LG_WALL_WIDTH)
                ),
                Object(
                    lg_tech_knob_logo_clear(),
                    Rotate(Vector(0, 0, 90)),
                    Scale(Vector(1, 1 - 2 * mir, 1)),
                    Translate(Vector(0, 1.5 * LGBW, 0)),
                ),
                mirmatrix
            )
        )

    result.append(
        Merge(
            Cylinder(
                Vector(3 * LGBW / 2 - LGCS, 3 * LGBW / 2, -5 * LGPH - LGCS),
                Vector(3 * LGBW / 2 - LGCS, -3 * LGBW / 2, -5 * LGPH - LGCS),
                LGCS
            ),
            Cylinder(
                Vector(3 * LGBW / 2 - LGCS, 3 * LGBW / 2, -2 * LGBH + LGCS),
                Vector(3 * LGBW / 2 - LGCS, -3 * LGBW / 2, -2 * LGBH + LGCS),
                LGCS
            ),
            Cylinder(
                Vector(LGBW / 2 - LGCS, 3 * LGBW / 2, -LGCS),
                Vector(LGBW / 2 - LGCS, -3 * LGBW / 2, -LGCS),
                LGCS
            ),
            Cylinder(
                Vector(
                    LGBW / 2 - LG_WALL_WIDTH / 2 + LGCS,
                    LGBW + 0.12 + LGCS,
                    -LGCS
                ),
                Vector(
                    LGBW / 2 - LG_WALL_WIDTH / 2 + LGCS,
                    -LGBW - 0.12 - LGCS,
                    -LGCS
                ),
                LGCS
            ),
            Cylinder(
                Vector(LGBW / 2 + LGCS, LGBW + LGCS, -2 * LGBH + LGCS),
                Vector(LGBW / 2 + LGCS, -LGBW - LGCS, -2 * LGBH + LGCS),
                LGCS
            ),
            Cylinder(
                Vector(LGBW / 2 + LGCS, LGBW + LGCS, -5 * LGPH - LGCS),
                Vector(LGBW / 2 + LGCS, -LGBW - LGCS, -5 * LGPH - LGCS),
                LGCS
            ),
            Box(
                Vector(LGBW / 2 + LGCS, LGBW + LG_WALL_WIDTH, -2 * LGBH),
                Vector(
                    LGBW / 2 + LG_WALL_WIDTH,
                    -LGBW - LG_WALL_WIDTH,
                    -2 * LGBH + LGCS + LG_E
                )
            ),
            Box(
                Vector(1.5 * LGBW - LGCS, 1.5 * LGBW, -2 * LGBH),
                Vector(
                    1.5 * LGBW - LG_WALL_WIDTH,
                    -1.5 * LGBW,
                    -2 * LGBH + LGCS + LG_E
                )
            ),
            Box(
                Vector(LGBW / 2, LGBW + LG_WALL_WIDTH, -5 * LGPH - LGCS),
                Vector(
                    LGBW / 2 + LG_WALL_WIDTH,
                    -LGBW - LG_WALL_WIDTH,
                    -2 * LGBH + LGCS
                )
            ),
            Box(
                Vector(1.5 * LGBW, 1.5 * LGBW, -5 * LGPH - LGCS),
                Vector(
                    1.5 * LGBW - LG_WALL_WIDTH, -1.5 * LGBW, -2 * LGBH + LGCS
                )
            ),
            Box(
                Vector(1.5 * LGBW - LGCS, 1.5 * LGBW, -5 * LGPH),
                Vector(
                    LGBW / 2 + LGCS,
                    -1.5 * LGBW,
                    -2 * LGBH + LG_PLATE_INNER_HEIGHT
                )
            ),
            Difference(
                Merge(
                    Box(
                        Vector(LGBW / 2, 1.5 * LGBW, 0),
                        Vector(
                            LGBW / 2 - LG_WALL_WIDTH, -1.5 * LGBW, -2.5 * LGPH
                        ),
                        Matrix(
                            Vector(
                                1, 0,
                                2 / LGBW * LGCS * sin(LG_ANGLE * pi / 180),
                                0, 1, 0,
                                -1 / 2, 0, 1,
                                LGCS * (cos(LG_ANGLE * pi / 180) - 1),
                                0, -LGCS
                            )
                        )
                    ),
                    Box(
                        Vector(LGBW / 2 - LGCS, 1.5 * LGBW, 0),
                        Vector(
                            LGBW / 2 - LG_WALL_WIDTH,
                            -1.5 * LGBW,
                            -LG_WALL_WIDTH / 2
                        )
                    ),
                ),
                Union(
                    Box(
                        Vector(
                            LGBW / 2 - LG_WALL_WIDTH / 2,
                            LGBW + 0.12 + LGCS,
                            LG_E
                        ),
                        Vector(
                            LG_WALL_WIDTH,
                            -LGBW - 0.12 - LGCS,
                            -LG_WALL_WIDTH - LG_E
                        )
                    ),
                    Box(
                        Vector(
                            LGBW / 2 - LG_WALL_WIDTH / 2 + LGCS,
                            LGBW + 0.12 + LGCS,
                            LG_E
                        ),
                        Vector(LG_WALL_WIDTH, -LGBW - 0.12 - LGCS, -LGCS)
                    ),
                ),
            ),


            Difference(
                Merge(
                    Box(
                        Vector(LGBW / 2, 1.5 * LGBW, 0),
                        Vector(
                            LGBW / 2 - LG_WALL_WIDTH, -1.5 * LGBW, -2.5 * LGPH
                        ),
                        # Matrix(
                        #     Vector(
                        #           1, 0,
                        #           2 / LGBW * LGCS * sin(LG_ANGLE * pi / 180),
                        #           0, 1, 0,
                        #           -1 / 2, 0, 1,
                        #           LGCS * (cos(LG_ANGLE * pi / 180) - 1),
                        #           0, -LGCS
                        #     )
                        # )
                    ),
                    Box(
                        Vector(LGBW / 2 - LGCS, 1.5 * LGBW, 0),
                        Vector(
                            LGBW / 2 - LG_WALL_WIDTH,
                            -1.5 * LGBW,
                            -LG_WALL_WIDTH / 2
                        )
                    ),
                ),
                Union(
                    Box(
                        Vector(
                            LGBW / 2 - LG_WALL_WIDTH / 2,
                            LGBW + 0.12 + LGCS,
                            LG_E
                        ),
                        Vector(
                            LG_WALL_WIDTH,
                            -LGBW - 0.12 - LGCS,
                            -LG_WALL_WIDTH - LG_E
                        )
                    ),
                    Box(
                        Vector(
                            LGBW / 2 - LG_WALL_WIDTH / 2 + LGCS,
                            LGBW + 0.12 + LGCS,
                            LG_E
                        ),
                        Vector(LG_WALL_WIDTH, -LGBW - 0.12 - LGCS, -LGCS)
                    ),
                ),
                Translate(Vector(LGBW, 0, -2.5 * LGPH)),
            ),


            Cylinder(
                Vector(LGBW, 0, -5 * LGPH - LG_TOP_HEIGHT + LG_E),
                Vector(LGBW, 0, -2 * LGBH),
                LG_KNOB_INNER_RADIUS
            ),
        ),
        # Rotate(Vector(0, 0, -45))

    )

    return result
