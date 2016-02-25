"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

@Todo: Put some information here that makes sense
19970710 Lutz Uhlmann
20071125 Lutz Uhlmann fixed stud orientation
20080218 Lutz Uhlmann fixed hollow stud logo and orientation

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_2436: Bracket 1 x 2 - 1 x 4
"""

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference

from pov.other.Object import Object

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from lgeo.include.common.lg_defs import LGCS, LGBW, LG_TOP_HEIGHT
from lgeo.include.common.lg_defs import LGPH, LG_WALL_WIDTH
from lgeo.include.common.lg_defs import LG_E, lg_knob
from lgeo.include.common.lg_defs import LG_KNOB_INNER_SPACE, lg_tech_knob_logo
from lgeo.include.common.lg_defs import LG_KNOB_RADIUS, LG_PLATE_COLUMN


def solid():
    """@Todo: Docstring."""
    return Union(
        Sphere(
            Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGCS),
            LGCS
        ),
        Sphere(
            Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGCS),
            LGCS
        ),
        Sphere(
            Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGPH + LGCS),
            LGCS
        ),
        Sphere(
            Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGPH + LGCS),
            LGCS
        ),
        Cylinder(
            Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGCS),
            Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGCS),
            LGCS
        ),
        Cylinder(
            Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGPH + LGCS),
            Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGPH + LGCS),
            LGCS
        ),
        Cylinder(
            Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGCS),
            Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGPH + LGCS),
            LGCS
        ),
        Cylinder(
            Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGCS),
            Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGPH + LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LGCS, -LGBW + LGCS, -LGCS),
            Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LGCS, LGBW - LGCS, -LGCS),
            Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LGCS, -LGBW + LGCS, -LGPH + LGCS),
            Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGPH + LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LGCS, LGBW - LGCS, -LGPH + LGCS),
            Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGPH + LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGBW + LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGBW + LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGCS),
            LGCS
        ),
        Sphere(
            Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGCS),
            LGCS
        ),
        Sphere(
            Vector(
                LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGBW + LGCS
            ),
            LGCS
        ),
        Sphere(
            Vector(
                LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGBW + LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LGCS, -LGBW + LGCS, -LGCS),
            Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LGCS, LGBW - LGCS, -LGCS),
            Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGBW + LGCS),
            Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGBW + LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGCS),
            Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGCS),
            LGCS
        ),
        Cylinder(
            Vector(
                LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGBW + LGCS
            ),
            Vector(
                LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGBW + LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGBW + LGCS),
            Vector(
                LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGBW + LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGBW + LGCS),
            Vector(
                LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGBW + LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGCS),
            Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
            Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGCS),
            Vector(
                LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGBW + LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGCS),
            Vector(
                LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGBW + LGCS
            ),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGCS),
            Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGBW + LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
            Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGBW + LGCS),
            LGCS
        ),
        Difference(
            Union(
                Box(
                    Vector(LGBW / 2 + LGCS + LG_E, -LGBW + LGCS, 0),
                    Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGPH)
                ),
                Box(
                    Vector(LGBW / 2 + LGCS + LG_E, -LGBW, -LGCS),
                    Vector(-LGBW / 2 + LGCS, LGBW, -LGPH + LGCS)
                ),
                Box(
                    Vector(LGBW / 2 + LGCS + LG_E, -LGBW + LGCS, -LGCS),
                    Vector(-LGBW / 2, LGBW - LGCS, -LGPH + LGCS)
                ),
            ),
            Union(
                Box(
                    Vector(
                        LGBW / 2 + LG_E,
                        -LGBW + LG_WALL_WIDTH,
                        -LG_TOP_HEIGHT
                    ),
                    Vector(
                        -LGBW / 2 + LG_WALL_WIDTH,
                        LGBW - LG_WALL_WIDTH,
                        -LGPH - LG_E
                    )
                ),
                Object(
                    LG_KNOB_INNER_SPACE,
                    Translate(Vector(0, -LGBW / 2, -LG_TOP_HEIGHT))
                ),
                Object(
                    LG_KNOB_INNER_SPACE,
                    Translate(Vector(0, LGBW / 2, -LG_TOP_HEIGHT))
                ),
            ),
        ),
        Box(
            Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, 0),
            Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGBW)
        ),
        Box(
            Vector(LGBW / 2 + LGCS, 2 * LGBW, -LGCS),
            Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW, -LGBW + LGCS)
        ),
        Box(
            Vector(LGBW / 2, 2 * LGBW - LGCS, -LGCS),
            Vector(LGBW / 2 + LG_WALL_WIDTH, -2 * LGBW + LGCS, -LGBW + LGCS)
        ),
        Box(
            Vector(LG_KNOB_RADIUS, -LGBW / 2 + 0.06, -LGPH),
            Vector(LGBW / 2 + LG_E, -LGBW / 2 - 0.06, -LG_TOP_HEIGHT + LG_E)
        ),
        Box(
            Vector(LG_KNOB_RADIUS, LGBW / 2 + 0.06, -LGPH),
            Vector(LGBW / 2 + LG_E, LGBW / 2 - 0.06, -LG_TOP_HEIGHT + LG_E)
        ),
        Object(
            LG_PLATE_COLUMN,
            Translate(Vector(0, 0, -LGPH))
        ),
        Object(
            lg_knob(),
            Rotate(Vector(0, 0, 90)),
            Translate(Vector(0, -LGBW / 2, 0))
        ),
        Object(
            lg_knob(),
            Rotate(Vector(0, 0, 90)),
            Translate(Vector(0, LGBW / 2, 0))
        ),
        Object(
            lg_tech_knob_logo(),
            Rotate(Vector(0, 0, 90)),
            Rotate(Vector(0, 90, 0)),
            Translate(
                Vector(LGBW / 2 + LG_WALL_WIDTH, -3 * LGBW / 2, -LGBW / 2)
            )
        ),
        Object(
            lg_tech_knob_logo(),
            Rotate(Vector(0, 0, 90)),
            Rotate(Vector(0, 90, 0)),
            Translate(Vector(LGBW / 2 + LG_WALL_WIDTH, -LGBW / 2, -LGBW / 2))
        ),
        Object(
            lg_tech_knob_logo(),
            Rotate(Vector(0, 0, 90)),
            Rotate(Vector(0, 90, 0)),
            Translate(Vector(LGBW / 2 + LG_WALL_WIDTH, LGBW / 2, -LGBW / 2))
        ),
        Object(
            lg_tech_knob_logo(),
            Rotate(Vector(0, 0, 90)),
            Rotate(Vector(0, 90, 0)),
            Translate(
                Vector(LGBW / 2 + LG_WALL_WIDTH, 3 * LGBW / 2, -LGBW / 2)
            )
        ),
    )


"""
#declare lg_2436_clear =
merge {
 Sphere(
  Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGCS),
  LGCS
 ),
 Sphere(
  Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGCS),
  LGCS
 ),
 Sphere(
  Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGPH + LGCS),
  LGCS
 ),
 Sphere(
  Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGPH + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGCS),
  Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGPH + LGCS),
  Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGPH + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGCS),
  Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGPH + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGCS),
  Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGPH + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LGCS, -LGBW + LGCS, -LGCS),
  Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LGCS, LGBW - LGCS, -LGCS),
  Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LGCS, -LGBW + LGCS, -LGPH + LGCS),
  Vector(-LGBW / 2 + LGCS, -LGBW + LGCS, -LGPH + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LGCS, LGBW - LGCS, -LGPH + LGCS),
  Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGPH + LGCS),
  LGCS
 ),
 Sphere(
  Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
  LGCS
 ),
 Sphere(
  Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGCS),
  LGCS
 ),
 Sphere(
  Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGBW + LGCS),
  LGCS
 ),
 Sphere(
  Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGBW + LGCS),
  LGCS
 ),
 Sphere(
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGCS),
  LGCS
 ),
 Sphere(
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGCS),
  LGCS
 ),
 Sphere(
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGBW + LGCS),
  LGCS
 ),
 Sphere(
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGBW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LGCS, -LGBW + LGCS, -LGCS),
  Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LGCS, LGBW - LGCS, -LGCS),
  Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGBW + LGCS),
  Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGBW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGCS),
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGBW + LGCS),
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGBW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGBW + LGCS),
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGBW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGBW + LGCS),
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGBW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGCS),
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGCS),
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGBW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGCS),
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, 2 * LGBW - LGCS, -LGBW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGCS),
  Vector(LGBW / 2 + LGCS, -2 * LGBW + LGCS, -LGBW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGCS),
  Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, -LGBW + LGCS),
  LGCS
 ),
 Difference(
  merge {
   Box(
    Vector(LGBW / 2 + LGCS + LG_E, -LGBW + LGCS, 0),
    Vector(-LGBW / 2 + LGCS, LGBW - LGCS, -LGPH)
   ),
   Box(
    Vector(LGBW / 2 + LGCS + LG_E, -LGBW, -LGCS),
    Vector(-LGBW / 2 + LGCS, LGBW, -LGPH + LGCS)
   ),
   Box(
    Vector(LGBW / 2 + LGCS + LG_E, -LGBW + LGCS, -LGCS),
    Vector(-LGBW / 2, LGBW - LGCS, -LGPH + LGCS)
   ),
  ),
  merge {
   Box(
    Vector(LGBW / 2 + LG_E, -LGBW + LG_WALL_WIDTH, -LG_TOP_HEIGHT),
    Vector(-LGBW / 2 + LG_WALL_WIDTH, LGBW - LG_WALL_WIDTH, -LGPH - LG_E)
   ),
   Object(
    LG_KNOB_INNER_SPACE_clear
    Translate(Vector(0, -LGBW / 2, -LG_TOP_HEIGHT)
   ),
   Object(
    LG_KNOB_INNER_SPACE_clear
    Translate(Vector(0, LGBW / 2, -LG_TOP_HEIGHT)
   ),
  ),
 ),
 Box(
  Vector(LGBW / 2 + LGCS, 2 * LGBW - LGCS, 0),
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW + LGCS, -LGBW)
 ),
 Box(
  Vector(LGBW / 2 + LGCS, 2 * LGBW, -LGCS),
  Vector(LGBW / 2 + LG_WALL_WIDTH - LGCS, -2 * LGBW, -LGBW + LGCS)
 ),
 Box(
  Vector(LGBW / 2, 2 * LGBW - LGCS, -LGCS),
  Vector(LGBW / 2 + LG_WALL_WIDTH, -2 * LGBW + LGCS, -LGBW + LGCS)
 ),
 Box(
  Vector(LG_KNOB_RADIUS, -LGBW / 2+0.06, -LGPH),
  Vector(LGBW / 2 + LG_E, -LGBW / 2-0.06, -LG_TOP_HEIGHT + LG_E)
 ),
 Box(
  Vector(LG_KNOB_RADIUS, LGBW / 2+0.06, -LGPH),
  Vector(LGBW / 2 + LG_E, LGBW / 2-0.06, -LG_TOP_HEIGHT + LG_E)
 ),
 Object(
  LG_PLATE_COLUMN_clear
  Translate(Vector(0, 0, -LGPH)
 ),
 Object(
  lg_knob_clear
  Rotate(Vector(0, 0, 90)
  Translate(Vector(0, -LGBW / 2, 0)
 ),
 Object(
  lg_knob_clear
  Rotate(Vector(0, 0, 90)
  Translate(Vector(0, LGBW / 2, 0)
 ),
 Object(
  lg_tech_knob_logo_clear
  Rotate(Vector(0, 0, 90)
  Rotate(Vector(0, 90, 0)
  Translate(Vector(LGBW / 2 + LG_WALL_WIDTH, -3 * LGBW / 2, -LGBW / 2)
 ),
 Object(
  lg_tech_knob_logo_clear
  Rotate(Vector(0, 0, 90)
  Rotate(Vector(0, 90, 0)
  Translate(Vector(LGBW / 2 + LG_WALL_WIDTH, -LGBW / 2, -LGBW / 2)
 ),
 Object(
  lg_tech_knob_logo_clear
  Rotate(Vector(0, 0, 90)
  Rotate(Vector(0, 90, 0)
  Translate(Vector(LGBW / 2 + LG_WALL_WIDTH, LGBW / 2, -LGBW / 2)
 ),
 Object(
  lg_tech_knob_logo_clear
  Rotate(Vector(0, 0, 90)
  Rotate(Vector(0, 90, 0)
  Translate(Vector(LGBW / 2 + LG_WALL_WIDTH, 3 * LGBW / 2, -LGBW / 2)
 ),
),

#end
"""
