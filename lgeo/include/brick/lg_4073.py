"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19980315 Lutz Uhlmann

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_4073: Plate 1 x 1 Round
"""

from pov.basic.Vector import Vector

from pov.csg.Merge import Merge
from pov.csg.Difference import Difference

from pov.other.Object import Object

from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere
from pov.finite_solid.Torus import Torus

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from lgeo.include.common.lg_defs import LGCS, LGBW, LG_TOP_HEIGHT
from lgeo.include.common.lg_defs import LGPH, LG_WALL_WIDTH
from lgeo.include.common.lg_defs import LG_PLATE_INNER_HEIGHT, LG_E
from lgeo.include.common.lg_defs import LG_KNOB_INNER_RADIUS, LG_KNOB_CLEAR
from lgeo.include.common.lg_defs import LG_KNOB_INNER_SPACE, LG_CYLINDER_RADIUS
from lgeo.include.common.lg_defs import LG_KNOB_RADIUS, LG_PLATE_COLUMN
from lgeo.include.common.lg_defs import LG_KNOB_INNER_SPACE_CLEAR

# #ifdef(lg_4073)
# #else
# #declare lg_4073 =
# union {
#  Object(
#   lg_knob
#   Translate( Vector(0,0, LGPH),
#  ),
#  union {
#   Difference(
#    Cylinder(
#     Vector(0, 0, LG_PLATE_INNER_HEIGHT+LG_E),
#     Vector(0, 0, LGCS),
#     (LG_CYLINDER_RADIUS)
#    ),
#    Cylinder(
#     Vector(0, 0, LG_PLATE_INNER_HEIGHT+2*LG_E),
#     Vector(0, 0, 0),
#     (LG_KNOB_RADIUS)
#    ),
#   ),
#   Difference(
#    Cylinder(
#     Vector(0, 0, LGCS + LG_E),
#     Vector(0, 0, 0),
#     (LG_CYLINDER_RADIUS - LGCS)
#    ),
#    Cylinder(
#     Vector(0, 0, LG_PLATE_INNER_HEIGHT),
#     Vector(0, 0, -0.1),
#     LG_KNOB_RADIUS + LGCS
#    ),
#   ),
#   Torus(
#    (LG_CYLINDER_RADIUS - LGCS),
#    LGCS
#    Rotate(Vector(90, 0, 0),
#    Translate( Vector(0, 0, LGCS),
#   ),
#   Torus(
#    (LG_KNOB_RADIUS + LGCS),
#    LGCS
#    Rotate(Vector(90, 0, 0),
#    Translate( Vector(0, 0, LGCS),
#   ),
#  ),
#  Difference(
#   union {
#    Cylinder(
#     Vector(0, 0, LG_PLATE_INNER_HEIGHT+LGCS),
#     Vector(0, 0, LGPH-LGCS),
#     LGBW/2
#    ),
#    Cylinder(
#     Vector(0, 0, LG_PLATE_INNER_HEIGHT),
#     Vector(0, 0, LGPH),
#     LGBW/2-LGCS
#    ),
#   ),
#   Object(
#    lg_knob_inner_space
#    Translate( Vector(0,0, LG_PLATE_INNER_HEIGHT),
#   ),
#  ),
#  Torus(
#   (LGBW/2-LGCS),
#   LGCS
#   Rotate(Vector(90, 0, 0),
#   Translate( Vector(0, 0, LGPH-LGCS),
#  ),
#  Torus(
#   (LGBW/2-LGCS),
#   LGCS
#   Rotate(Vector(90, 0, 0),
#   Translate( Vector(0, 0, LG_PLATE_INNER_HEIGHT+LGCS),
#  ),
#  Translate( Vector(0, 0, -LGPH),
# ),

def clear():
    """Return lg_4073: Plate 1 x 1 Round."""
    return Merge(
        Object(
            LG_KNOB_CLEAR,
            Translate(Vector(0,0, LGPH)),
        ),
        Merge(
            Difference(
                Cylinder(
                    Vector(0, 0, LG_PLATE_INNER_HEIGHT + LG_E),
                    Vector(0, 0, LGCS),
                    LG_CYLINDER_RADIUS
                ),
                Cylinder(
                    Vector(0, 0, LG_PLATE_INNER_HEIGHT + 2 * LG_E),
                    Vector(0, 0, 0),
                    LG_KNOB_RADIUS
                ),
            ),
            Difference(
                Cylinder(
                    Vector(0, 0, LGCS + LG_E),
                    Vector(0, 0, 0),
                    LG_CYLINDER_RADIUS - LGCS
                ),
                Cylinder(
                    Vector(0, 0, LG_PLATE_INNER_HEIGHT),
                    Vector(0, 0, -0.1),
                    LG_KNOB_RADIUS + LGCS
                ),
            ),
            Torus(
                LG_CYLINDER_RADIUS - LGCS,
                LGCS,
                Rotate(Vector(90, 0, 0)),
                Translate(Vector(0, 0, LGCS)),
            ),
            Torus(
                LG_KNOB_RADIUS + LGCS,
                LGCS,
                Rotate(Vector(90, 0, 0)),
                Translate(Vector(0, 0, LGCS)),
            ),
        ),
        Difference(
            Merge(
              Cylinder(
                  Vector(0, 0, LG_PLATE_INNER_HEIGHT + LGCS),
                  Vector(0, 0, LGPH - LGCS),
                  LGBW / 2
              ),
              Cylinder(
                  Vector(0, 0, LG_PLATE_INNER_HEIGHT),
                  Vector(0, 0, LGPH),
                  LGBW / 2 - LGCS
              ),
            ),
            Object(
              LG_KNOB_INNER_SPACE_CLEAR,
              Translate(Vector(0, 0, LG_PLATE_INNER_HEIGHT)),
            ),
        ),
        Torus(
            LGBW / 2 - LGCS,
            LGCS,
            Rotate(Vector(90, 0, 0)),
            Translate(Vector(0, 0, LGPH - LGCS)),
        ),
        Torus(
            LGBW / 2 - LGCS,
            LGCS,
            Rotate(Vector(90, 0, 0)),
            Translate(Vector(0, 0, LG_PLATE_INNER_HEIGHT + LGCS)),
        ),
        Translate(Vector(0, 0, -LGPH)),
    )
