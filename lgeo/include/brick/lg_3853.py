"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970623 Lutz Uhlmann
20080105 Lutz Uhlmann fixed stud orientation

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_3853: lg_3853: Window 1 x 4 x 3
"""

from lgeo.include.common.lg_defs import LGBW, LGCS, LG_PLATE_INNER_HEIGHT
from lgeo.include.common.lg_defs import LGBH, LGPH, LG_PLATE_COLUMN
from lgeo.include.common.lg_defs import LG_TOP_HEIGHT, LG_E, LGWW
from lgeo.include.common.lg_defs import LG_KNOB_HEIGHT, LG_KNOB_CORNER_SPACE, LG_KNOB_RADIUS
from lgeo.include.common.lg_defs import lg_tech_knob_logo

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference
from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere
from pov.finite_solid.Torus import Torus
from pov.object_modifier.Translate import Translate
from pov.object_modifier.Rotate import Rotate
from pov.other.Object import Object


LENGTH = 1
WIDTH = 4
HEIGHT = 3


def solid():
    """LG 3853 Solid brick."""
    mainpart = Union()

    for rot in (0, 1):
        rotpart = Union(
            Sphere(
                Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGCS),
                LGCS
            ),
            Sphere(
                Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGCS),
                LGCS
            ),
            Cylinder(
                Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -LGCS),
                Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -LGCS),
                LGCS
            ),
            Cylinder(
                Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGCS),
                Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGCS),
                LGCS
            ),
            Cylinder(
                Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGCS),
                Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGCS),
                LGCS
            ),
            Cylinder(
                Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -LGCS),
                Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGCS),
                LGCS
            ),
            Cylinder(
                Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -LGCS),
                Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGCS),
                LGCS
            )
        )

        if rot == 1:
            rotpart.append(
                Rotate(Vector(0, 0, 180))
            )
        mainpart.append(rotpart)

    mainpart.append(
        Sphere(
            Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGCS), LGCS
        ),
        Sphere(
            Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -LGCS), LGCS
        ),
        Cylinder(
            Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -LGCS),
            Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGCS),
            Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGCS),
            LGCS
        ),
        Cylinder(
            Vector(0.06 - LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH + 0.1 - LGCS),
            Vector(0.06 - LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH + 0.1 - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(-0.06 + LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH + 0.1 - LGCS),
            Vector(-0.06 + LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH + 0.1 - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -LGWW + LGCS),
            Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -LGWW + LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH - LGCS),
            Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -LGWW + LGCS),
            Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -LGWW + LGCS),
            Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -LGWW + LGCS),
            Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -LGWW + LGCS),
            Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH - LGCS),
            LGCS
        ),
        Cylinder(
            Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -LGWW + LGCS),
            Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -LGWW + LGCS),
            LGCS
        ),
        Cylinder(
            Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH - LGCS),
            Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH - LGCS),
            LGCS
        ),
        Box(
            Vector(0.06 - LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH + 0.1),
            Vector(-0.06 + LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH)
        ),
        Box(
            Vector(0.06, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH + 0.1 - LGCS),
            Vector(-0.06, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH)
        )
    )

    for BOX_X in range(-2, 1, 1):
        BOX_X += 0.5
        mainpart.append(
            Box(
                Vector(LENGTH / 2 * LGBW - LGWW, BOX_X * LGBW + 0.03, -HEIGHT * LGBH + LGCS),
                Vector(
                    LENGTH / 2 * LGBW - LG_TOP_HEIGHT + LG_E,
                    BOX_X * LGBW - 0.03,
                    -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT + LG_E
                )
            ),
            Box(
                Vector(-LENGTH / 2 * LGBW + LGWW, BOX_X * LGBW + 0.03, -HEIGHT * LGBH + LGCS),
                Vector(
                    -LENGTH / 2 * LGBW + LG_TOP_HEIGHT - LG_E,
                    BOX_X * LGBW - 0.03,
                    -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT + LG_E
                )
            )
        )

    mainpart.append(
        Box(
            Vector(0.03, WIDTH / 2 * LGBW - LGWW, -HEIGHT * LGBH + LGCS),
            Vector(-0.03, WIDTH / 2 * LGBW - LG_TOP_HEIGHT + LG_E, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT + LG_E)
        ),
        Box(
            Vector(0.03, -WIDTH / 2 * LGBW + LGWW, -HEIGHT * LGBH + LGCS),
            Vector(-0.03, -WIDTH / 2 * LGBW + LG_TOP_HEIGHT - LG_E, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT + LG_E)
        ),
        Difference(
            Union(
                Box(
                    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, 0),
                    Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGWW)
                ),
                Box(
                    Vector(LENGTH / 2 * LGBW, WIDTH / 2 * LGBW - LGCS, -LGCS),
                    Vector(-LENGTH / 2 * LGBW, -WIDTH / 2 * LGBW + LGCS, -LGWW + LGCS)
                ),
                Box(
                    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW, -LGCS),
                    Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW, -LGWW + LGCS)
                ),
                Union(
                    Cylinder(
                        Vector(0, 0, LG_KNOB_HEIGHT - LG_KNOB_CORNER_SPACE),
                        Vector(0, 0, -LG_E),
                        (LG_KNOB_RADIUS)
                    ),
                    Cylinder(
                        Vector(0, 0, LG_KNOB_HEIGHT),
                        Vector(0, 0, -LG_E),
                        (LG_KNOB_RADIUS - LG_KNOB_CORNER_SPACE)
                    ),
                    Torus(
                        LG_KNOB_RADIUS - LG_KNOB_CORNER_SPACE,
                        LG_KNOB_CORNER_SPACE,
                        Rotate(Vector(90, 0, 0)),
                        Translate(Vector(0, 0, (LG_KNOB_HEIGHT - LG_KNOB_CORNER_SPACE)))
                    ),
                    # FIXME: refactor into knob?
                    #if (lg_quality ) 2)
                    #  Object(lego_logo_text scale 0.75 rotate Vector(0, 0, 90) translate Vector(0,0,LG_KNOB_HEIGHT) ),
                    #end
                    Translate(Vector(-LGBW / 2, 1.5 * LGBW, 0))
                ),
                Object(
                    lg_tech_knob_logo(),
                    Rotate(Vector(0, 0, 90)),
                    Translate(Vector(-LGBW / 2, 0.5 * LGBW, 0))
                ),
                Object(
                    lg_tech_knob_logo(),
                    Rotate(Vector(0, 0, 90)),
                    Translate(Vector(-LGBW / 2, -0.5 * LGBW, 0))
                ),
                Union(
                    Cylinder(
                        Vector(0, 0, LG_KNOB_HEIGHT - LG_KNOB_CORNER_SPACE),
                        Vector(0, 0, -LG_E),
                        LG_KNOB_RADIUS
                    ),
                    Cylinder(
                        Vector(0, 0, LG_KNOB_HEIGHT),
                        Vector(0, 0, -LG_E),
                        LG_KNOB_RADIUS - LG_KNOB_CORNER_SPACE
                    ),
                    Torus(
                        LG_KNOB_RADIUS - LG_KNOB_CORNER_SPACE,
                        LG_KNOB_CORNER_SPACE,
                        Rotate(Vector(90, 0, 0)),
                        Translate(Vector(0, 0, (LG_KNOB_HEIGHT - LG_KNOB_CORNER_SPACE)))
                    ),
                    # FIXME: refactor into knob?
                    #if (lg_quality ) 2)
                    # Object(lego_logo_text scale 0.75 rotate Vector(0, 0, 90) translate Vector(0,0,LG_KNOB_HEIGHT) ),
                    #end
                    Translate(Vector(-LGBW / 2, -1.5 * LGBW, 0))
                )
            ),
            Union(
                Cylinder(
                    Vector(
                        LENGTH / 2 * LGBW - LGWW - 0.08,
                        WIDTH / 2 * LGBW - LGWW - 0.08,
                        -LGWW - LG_E
                    ),
                    Vector(
                        LENGTH / 2 * LGBW - LGWW - 0.08,
                        WIDTH / 2 * LGBW - LGWW - 0.08,
                        LG_KNOB_HEIGHT + LG_E
                    ),
                    0.08
                ),
                Cylinder(
                    Vector(
                        -LENGTH / 2 * LGBW + LGWW + 0.08,
                        WIDTH / 2 * LGBW - LGWW - 0.08,
                        -LGWW - LG_E
                    ),
                    Vector(
                        -LENGTH / 2 * LGBW + LGWW + 0.08,
                        WIDTH / 2 * LGBW - LGWW - 0.08,
                        LG_KNOB_HEIGHT + LG_E
                    ),
                    0.08
                ),
                Cylinder(
                    Vector(
                        LENGTH / 2 * LGBW - LGWW - 0.08,
                        -WIDTH / 2 * LGBW + LGWW + 0.08,
                        -LGWW - LG_E
                    ),
                    Vector(
                        LENGTH / 2 * LGBW - LGWW - 0.08,
                        -WIDTH / 2 * LGBW + LGWW + 0.08,
                        LG_KNOB_HEIGHT + LG_E
                    ),
                    0.08
                ),
                Cylinder(
                    Vector(
                        -LENGTH / 2 * LGBW + LGWW + 0.08,
                        -WIDTH / 2 * LGBW + LGWW + 0.08,
                        -LGWW - LG_E
                    ),
                    Vector(
                        -LENGTH / 2 * LGBW + LGWW + 0.08,
                        -WIDTH / 2 * LGBW + LGWW + 0.08,
                        LG_KNOB_HEIGHT + LG_E
                    ),
                    0.08
                ),
            ),
        ),
        Difference(
            Union(
                Box(
                    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH),
                    Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH)
                ),
                Box(
                    Vector(LENGTH / 2 * LGBW, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGCS),
                    Vector(-LENGTH / 2 * LGBW, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGCS)
                ),
                Box(
                    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS),
                    Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGCS)
                ),
            ),
            Union(
                Box(
                    Vector(
                        LENGTH / 2 * LGBW - LG_TOP_HEIGHT,
                        WIDTH / 2 * LGBW - LG_TOP_HEIGHT,
                        -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT
                    ),
                    Vector(-LENGTH / 2 * LGBW + LG_TOP_HEIGHT, -WIDTH / 2 * LGBW + LG_TOP_HEIGHT, -HEIGHT * LGBH-LG_E)
                ),
                Cylinder(
                    Vector(
                        LENGTH / 2 * LGBW - LGWW - 0.08,
                        WIDTH / 2 * LGBW - LGWW - 0.08,
                        -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT - LG_E
                    ),
                    Vector(
                        LENGTH / 2 * LGBW - LGWW - 0.08,
                        WIDTH / 2 * LGBW - LGWW - 0.08,
                        -HEIGHT * LGBH + LGPH + LG_E
                    ),
                    0.08
                ),
                Cylinder(
                    Vector(
                        -LENGTH / 2 * LGBW + LGWW + 0.08,
                        WIDTH / 2 * LGBW - LGWW - 0.08,
                        -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT - LG_E
                    ),
                    Vector(
                        -LENGTH / 2 * LGBW + LGWW + 0.08,
                        WIDTH / 2 * LGBW - LGWW - 0.08,
                        -HEIGHT * LGBH + LGPH + LG_E
                    ),
                    0.08
                ),
                Cylinder(
                    Vector(
                        LENGTH / 2 * LGBW - LGWW - 0.08,
                        -WIDTH / 2 * LGBW + LGWW + 0.08,
                        -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT - LG_E
                    ),
                    Vector(
                        LENGTH / 2 * LGBW - LGWW - 0.08,
                        -WIDTH / 2 * LGBW + LGWW + 0.08,
                        -HEIGHT * LGBH + LGPH + LG_E
                    ),
                    0.08
                ),
                Cylinder(
                    Vector(
                        -LENGTH / 2 * LGBW + LGWW + 0.08,
                        -WIDTH / 2 * LGBW + LGWW + 0.08,
                        -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT - LG_E
                    ),
                    Vector(
                        -LENGTH / 2 * LGBW + LGWW + 0.08,
                        -WIDTH / 2 * LGBW + LGWW + 0.08,
                        -HEIGHT * LGBH + LGPH + LG_E
                    ),
                    0.08
                ),
            ),
        ),
        Difference(
            Union(
                Box(
                    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW, -LGWW + LGCS),
                    Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGWW, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT)
                ),
                Box(
                    Vector(-LENGTH / 2 * LGBW, WIDTH / 2 * LGBW - LGCS, -LGWW + LGCS),
                    Vector(LENGTH / 2 * LGBW, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT)
                ),
            ),
            Cylinder(
                Vector(LENGTH / 2 * LGBW - LGWW - 0.08, WIDTH / 2 * LGBW - LGWW + 0.04, -LGWW - (8 * LGPH - LGWW) / 2),
                Vector(LENGTH / 2 * LGBW - LGWW - 0.08, WIDTH / 2 * LGBW - LGWW - LG_E, -LGWW - (8 * LGPH - LGWW) / 2),
                0.09
            ),
        ),
        Difference(
            Union(
                Box(
                    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW, -LGWW + LGCS),
                    Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGWW, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT)
                ),
                Box(
                    Vector(-LENGTH / 2 * LGBW, -WIDTH / 2 * LGBW + LGCS, -LGWW + LGCS),
                    Vector(LENGTH / 2 * LGBW, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT)
                ),
            ),
            Cylinder(
                Vector(LENGTH / 2 * LGBW - LGWW - 0.08, -WIDTH / 2 * LGBW + LGWW - 0.04, -LGWW - (8 * LGPH-LGWW) / 2),
                Vector(LENGTH / 2 * LGBW - LGWW - 0.08, -WIDTH / 2 * LGBW + LGWW + LG_E, -LGWW - (8 * LGPH-LGWW) / 2),
                0.09
            ),
        ),
        Object(
            LG_PLATE_COLUMN,
            Translate(Vector(0, -LGBW, -HEIGHT * LGBH))
        ),
        Object(
            LG_PLATE_COLUMN,
            Translate(Vector(0, 0, -HEIGHT * LGBH))
        ),
        Object(
            LG_PLATE_COLUMN,
            Translate(Vector(0, LGBW, -HEIGHT * LGBH))
        ),
        Cylinder(
            Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -LGCS),
            Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
            LGCS
        ),
        Cylinder(
            Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -LGWW + LGCS),
            Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
            LGCS
        ),





    )

    return mainpart




'''
#declare lg_3853 =
Union(




 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  LGCS
 ),
 Difference(
  Union(
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -LGCS)
   ),
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -LGWW + LGCS)
   ),
  ),
  Box(
   Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18-LG_E, LG_E),
   Vector(LENGTH / 2 * LGBW - 0.2, WIDTH / 2 * LGBW + 0.18+LG_E, -LGWW - LG_E)
  ),
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
  LGCS
 ),
 Difference(
  Union(
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -LGCS)
   ),
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -LGWW + LGCS)
   ),
  ),
  Box(
   Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18+LG_E, LG_E),
   Vector(LENGTH / 2 * LGBW - 0.2, -WIDTH / 2 * LGBW - 0.18-LG_E, -LGWW - LG_E)
  ),
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Difference(
  Union(
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS)
   ),
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
  ),
  Box(
   Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18-LG_E, -HEIGHT * LGBH + LGPH + LG_E),
   Vector(LENGTH / 2 * LGBW - 0.2, WIDTH / 2 * LGBW + 0.18+LG_E, -HEIGHT * LGBH + LGPH-LGWW - LG_E)
  ),
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Difference(
  Union(
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS)
   ),
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
  ),
  Box(
   Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18+LG_E, -HEIGHT * LGBH + LGPH + LG_E),
   Vector(LENGTH / 2 * LGBW - 0.2, -WIDTH / 2 * LGBW - 0.18-LG_E, -HEIGHT * LGBH + LGPH-LGWW - LG_E)
  ),
 ),
 Difference(
  Union(
   Box(
    Vector(LENGTH / 2 * LGBW, WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - 0.18, -LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18, -LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - 0.18+LGCS, 0)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW, -LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18, -LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, 0)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW)
   ),
   Difference(
    Union(
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -LGWW + LGCS),
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -LGCS),
      0.18
     ),
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -LGWW),
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, 0),
      0.18-LGCS
     ),
    ),
    Box(
     Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18-LG_E, LG_E),
     Vector(LENGTH / 2 * LGBW - 0.2, WIDTH / 2 * LGBW + 0.18+LG_E, -LGWW - LG_E)
    ),
   ),
  ),
  Sphere(
   Vector(LENGTH / 2 * LGBW + 0.1, WIDTH / 2 * LGBW, -LGWW - 0.12+0.12*sin(25*pi/180)), 0.12
  ),
 ),
 Difference(
  Union(
   Box(
    Vector(LENGTH / 2 * LGBW, -WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + 0.18, -LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18, -LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + 0.18-LGCS, 0)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW, -LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18, -LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, 0)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW)
   ),
   Difference(
    Union(
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -LGWW + LGCS),
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -LGCS),
      0.18
     ),
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -LGWW),
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, 0),
      0.18-LGCS
     ),
    ),
    Box(
     Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18+LG_E, LG_E),
     Vector(LENGTH / 2 * LGBW - 0.2, -WIDTH / 2 * LGBW - 0.18-LG_E, -LGWW - LG_E)
    ),
   ),
  ),
  Sphere(
   Vector(LENGTH / 2 * LGBW + 0.1, -WIDTH / 2 * LGBW, -LGWW - 0.12+0.12*sin(25*pi/180)), 0.12
  ),
 ),
 Difference(
  Union(
   Box(
    Vector(LENGTH / 2 * LGBW, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - 0.18, -HEIGHT * LGBH + LGPH-LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW)
   ),
   Difference(
    Union(
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS),
      0.18
     ),
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGWW),
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH),
      0.18-LGCS
     ),
    ),
    Box(
     Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18-LG_E, -HEIGHT * LGBH + LGPH + LG_E),
     Vector(LENGTH / 2 * LGBW - 0.2, WIDTH / 2 * LGBW + 0.18+LG_E, -HEIGHT * LGBH + LGPH-LGWW - LG_E)
    ),
   ),
  ),
  Sphere(
   Vector(LENGTH / 2 * LGBW + 0.1, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH + 0.12-0.12*sin(25*pi/180)), 0.12
  ),
 ),
 Difference(
  Union(
   Box(
    Vector(LENGTH / 2 * LGBW, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + 0.18, -HEIGHT * LGBH + LGPH-LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW)
   ),
   Difference(
    Union(
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS),
      0.18
     ),
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGWW),
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH),
      0.18-LGCS
     ),
    ),
    Box(
     Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18+LG_E, -HEIGHT * LGBH + LGPH + LG_E),
     Vector(LENGTH / 2 * LGBW - 0.2, -WIDTH / 2 * LGBW - 0.18-LG_E, -HEIGHT * LGBH + LGPH-LGWW - LG_E)
    ),
   ),
  ),
  Sphere(
   Vector(LENGTH / 2 * LGBW + 0.1, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH + 0.12-0.12*sin(25*pi/180)), 0.12
  ),
 ),
),

#declare lg_3853_clear =
merge {
 #declare ROT = 0;
 #while (ROT Vector(2)
  merge {
   Sphere(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGCS), LGCS
   ),
   Sphere(
    Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGCS), LGCS
   ),
   Cylinder(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -LGCS),
    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -LGCS),
    LGCS
   ),
   Cylinder(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGCS),
    Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGCS),
    LGCS
   ),
   Cylinder(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGCS),
    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGCS),
    LGCS
   ),
   Cylinder(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -LGCS),
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGCS),
    LGCS
   ),
   Cylinder(
    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -LGCS),
    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGCS),
    LGCS
   ),
   #if (ROT=1)
    rotate Vector(0, 0, 180)
   #end
  ),
  #declare ROT = ROT + 1;
 #end
 Sphere(
  Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGCS), LGCS
 ),
 Sphere(
  Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -LGCS), LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -LGCS),
  Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGCS),
  Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(0.06 - LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH + 0.1 - LGCS),
  Vector(0.06 - LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH + 0.1 - LGCS),
  LGCS
 ),
 Cylinder(
  Vector(-0.06 + LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH + 0.1 - LGCS),
  Vector(-0.06 + LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH + 0.1 - LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -LGWW + LGCS),
  Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -LGWW + LGCS),
  Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -LGWW + LGCS),
  Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Box(
  Vector(0.06 - LGCS, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH + 0.1),
  Vector(-0.06 + LGCS, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH + 0.1)
 ),
 Box(
  Vector(0.06, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LGPH + 0.1 - LGCS),
  Vector(-0.06, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LGPH + 0.1 - LGCS)
 ),
 #declare BOX_X = -1.5;
 #while (BOX_X Vector(2)
  Box(
   Vector(LENGTH / 2 * LGBW - LGWW, BOX_X * LGBW + 0.03, -HEIGHT * LGBH + LGCS),
   Vector(LENGTH / 2 * LGBW - LG_TOP_HEIGHT + LG_E, BOX_X * LGBW - 0.03, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT + LG_E)
  ),
  Box(
   Vector(-LENGTH / 2 * LGBW + LGWW, BOX_X * LGBW + 0.03, -HEIGHT * LGBH + LGCS),
   Vector(-LENGTH / 2 * LGBW + LG_TOP_HEIGHT - LG_E, BOX_X * LGBW - 0.03, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT + LG_E)
  ),
  #declare BOX_X = BOX_X + 1;
 #end
 Box(
  Vector(0.03, WIDTH / 2 * LGBW - LGWW, -HEIGHT * LGBH + LGCS),
  Vector(-0.03, WIDTH / 2 * LGBW - LG_TOP_HEIGHT + LG_E, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT + LG_E)
 ),
 Box(
  Vector(0.03, -WIDTH / 2 * LGBW + LGWW, -HEIGHT * LGBH + LGCS),
  Vector(-0.03, -WIDTH / 2 * LGBW + LG_TOP_HEIGHT - LG_E, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT + LG_E)
 ),
 Difference(
  merge {
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, 0),
    Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGWW)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW, WIDTH / 2 * LGBW - LGCS, -LGCS),
    Vector(-LENGTH / 2 * LGBW, -WIDTH / 2 * LGBW + LGCS, -LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW, -LGCS),
    Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW, -LGWW + LGCS)
   ),
   merge {
    Cylinder(
     Vector(0, 0, LG_KNOB_HEIGHT - LG_KNOB_CORNER_SPACE),
     Vector(0, 0, -LG_E),
     (LG_KNOB_RADIUS)
    ),
    Cylinder(
     Vector(0, 0, LG_KNOB_HEIGHT),
     Vector(0, 0, -LG_E),
     (LG_KNOB_RADIUS - LG_KNOB_CORNER_SPACE)
    ),
    Torus(
     (LG_KNOB_RADIUS - LG_KNOB_CORNER_SPACE),
     (LG_KNOB_CORNER_SPACE)
     rotate Vector(90, 0, 0)
     translate Vector(0, 0, (LG_KNOB_HEIGHT - LG_KNOB_CORNER_SPACE))
    ),
    #if (lg_quality ) 2)
     Object(lego_logo_text scale 0.75 rotate Vector(0, 0, 90) translate Vector(0,0,LG_KNOB_HEIGHT) ),
    #end
    translate Vector(0, 1.5 * LGBW, 0)
   ),
   Object(
    lg_tech_knob_logo_clear
    rotate Vector(0, 0, 90)
    translate Vector(0, 0.5 * LGBW, 0)
   ),
   Object(
    lg_tech_knob_logo_clear
    rotate Vector(0, 0, 90)
    translate Vector(0, -0.5 * LGBW, 0)
   ),
   merge {
    Cylinder(
     Vector(0, 0, LG_KNOB_HEIGHT - LG_KNOB_CORNER_SPACE),
     Vector(0, 0, -LG_E),
     (LG_KNOB_RADIUS)
    ),
    Cylinder(
     Vector(0, 0, LG_KNOB_HEIGHT),
     Vector(0, 0, -LG_E),
     (LG_KNOB_RADIUS - LG_KNOB_CORNER_SPACE)
    ),
    Torus(
     (LG_KNOB_RADIUS - LG_KNOB_CORNER_SPACE),
     (LG_KNOB_CORNER_SPACE)
     rotate Vector(90, 0, 0)
     translate Vector(0, 0, (LG_KNOB_HEIGHT - LG_KNOB_CORNER_SPACE))
    ),
    #if (lg_quality ) 2)
     Object(lego_logo_text scale 0.75 rotate Vector(0, 0, 90) translate Vector(0,0,LG_KNOB_HEIGHT) ),
    #end
    translate Vector(0, -1.5 * LGBW, 0)
   ),
  ),
  merge {
   Cylinder(
    Vector(LENGTH / 2 * LGBW - LGWW - 0.08, WIDTH / 2 * LGBW - LGWW - 0.08, -LGWW - LG_E),
    Vector(LENGTH / 2 * LGBW - LGWW - 0.08, WIDTH / 2 * LGBW - LGWW - 0.08, LG_KNOB_HEIGHT + LG_E),
    0.08
   ),
   Cylinder(
    Vector(-LENGTH / 2 * LGBW + LGWW + 0.08, WIDTH / 2 * LGBW - LGWW - 0.08, -LGWW - LG_E),
    Vector(-LENGTH / 2 * LGBW + LGWW + 0.08, WIDTH / 2 * LGBW - LGWW - 0.08, LG_KNOB_HEIGHT + LG_E),
    0.08
   ),
   Cylinder(
    Vector(LENGTH / 2 * LGBW - LGWW - 0.08, -WIDTH / 2 * LGBW + LGWW + 0.08, -LGWW - LG_E),
    Vector(LENGTH / 2 * LGBW - LGWW - 0.08, -WIDTH / 2 * LGBW + LGWW + 0.08, LG_KNOB_HEIGHT + LG_E),
    0.08
   ),
   Cylinder(
    Vector(-LENGTH / 2 * LGBW + LGWW + 0.08, -WIDTH / 2 * LGBW + LGWW + 0.08, -LGWW - LG_E),
    Vector(-LENGTH / 2 * LGBW + LGWW + 0.08, -WIDTH / 2 * LGBW + LGWW + 0.08, LG_KNOB_HEIGHT + LG_E),
    0.08
   ),
  ),
 ),
 Difference(
  merge {
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH),
    Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGCS),
    Vector(-LENGTH / 2 * LGBW, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS),
    Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGCS)
   ),
  ),
  merge {
   Box(
    Vector(LENGTH / 2 * LGBW - LG_TOP_HEIGHT, WIDTH / 2 * LGBW - LG_TOP_HEIGHT, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT),
    Vector(-LENGTH / 2 * LGBW + LG_TOP_HEIGHT, -WIDTH / 2 * LGBW + LG_TOP_HEIGHT, -HEIGHT * LGBH-LG_E)
   ),
   Cylinder(
    Vector(LENGTH / 2 * LGBW - LGWW - 0.08, WIDTH / 2 * LGBW - LGWW - 0.08, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT - LG_E),
    Vector(LENGTH / 2 * LGBW - LGWW - 0.08, WIDTH / 2 * LGBW - LGWW - 0.08, -HEIGHT * LGBH + LGPH + LG_E),
    0.08
   ),
   Cylinder(
    Vector(-LENGTH / 2 * LGBW + LGWW + 0.08, WIDTH / 2 * LGBW - LGWW - 0.08, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT - LG_E),
    Vector(-LENGTH / 2 * LGBW + LGWW + 0.08, WIDTH / 2 * LGBW - LGWW - 0.08, -HEIGHT * LGBH + LGPH + LG_E),
    0.08
   ),
   Cylinder(
    Vector(LENGTH / 2 * LGBW - LGWW - 0.08, -WIDTH / 2 * LGBW + LGWW + 0.08, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT - LG_E),
    Vector(LENGTH / 2 * LGBW - LGWW - 0.08, -WIDTH / 2 * LGBW + LGWW + 0.08, -HEIGHT * LGBH + LGPH + LG_E),
    0.08
   ),
   Cylinder(
    Vector(-LENGTH / 2 * LGBW + LGWW + 0.08, -WIDTH / 2 * LGBW + LGWW + 0.08, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT - LG_E),
    Vector(-LENGTH / 2 * LGBW + LGWW + 0.08, -WIDTH / 2 * LGBW + LGWW + 0.08, -HEIGHT * LGBH + LGPH + LG_E),
    0.08
   ),
  ),
 ),
 Difference(
  merge {
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW, -LGWW + LGCS),
    Vector(-LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGWW, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT)
   ),
   Box(
    Vector(-LENGTH / 2 * LGBW, WIDTH / 2 * LGBW - LGCS, -LGWW + LGCS),
    Vector(LENGTH / 2 * LGBW, WIDTH / 2 * LGBW - LGWW + LGCS, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT)
   ),
  ),
  Cylinder(
   Vector(LENGTH / 2 * LGBW - LGWW - 0.08, WIDTH / 2 * LGBW - LGWW + 0.04, -LGWW - (8 * LGPH-LGWW) / 2),
   Vector(LENGTH / 2 * LGBW - LGWW - 0.08, WIDTH / 2 * LGBW - LGWW - LG_E, -LGWW - (8 * LGPH-LGWW) / 2),
   0.09
  ),
 ),
 Difference(
  merge {
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW, -LGWW + LGCS),
    Vector(-LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGWW, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT)
   ),
   Box(
    Vector(-LENGTH / 2 * LGBW, -WIDTH / 2 * LGBW + LGCS, -LGWW + LGCS),
    Vector(LENGTH / 2 * LGBW, -WIDTH / 2 * LGBW + LGWW - LGCS, -HEIGHT * LGBH + LG_PLATE_INNER_HEIGHT)
   ),
  ),
  Cylinder(
   Vector(LENGTH / 2 * LGBW - LGWW - 0.08, -WIDTH / 2 * LGBW + LGWW - 0.04, -LGWW - (8 * LGPH-LGWW) / 2),
   Vector(LENGTH / 2 * LGBW - LGWW - 0.08, -WIDTH / 2 * LGBW + LGWW + LG_E, -LGWW - (8 * LGPH-LGWW) / 2),
   0.09
  ),
 ),
 Object(
  lg_plate_column_clear
  translate Vector(0, -LGBW, -HEIGHT * LGBH)
 ),
 Object(
  lg_plate_column_clear
  translate Vector(0, 0, -HEIGHT * LGBH)
 ),
 Object(
  lg_plate_column_clear
  translate Vector(0, LGBW, -HEIGHT * LGBH)
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  LGCS
 ),
 Difference(
  merge {
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -LGCS)
   ),
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -LGWW + LGCS)
   ),
  ),
  Box(
   Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18-LG_E, LG_E),
   Vector(LENGTH / 2 * LGBW - 0.2, WIDTH / 2 * LGBW + 0.18+LG_E, -LGWW - LG_E)
  ),
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS),
  LGCS
 ),
 Difference(
  merge {
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -LGCS)
   ),
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -LGWW + LGCS)
   ),
  ),
  Box(
   Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18+LG_E, LG_E),
   Vector(LENGTH / 2 * LGBW - 0.2, -WIDTH / 2 * LGBW - 0.18-LG_E, -LGWW - LG_E)
  ),
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Difference(
  merge {
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS)
   ),
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
  ),
  Box(
   Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18-LG_E, -HEIGHT * LGBH + LGPH + LG_E),
   Vector(LENGTH / 2 * LGBW - 0.2, WIDTH / 2 * LGBW + 0.18+LG_E, -HEIGHT * LGBH + LGPH-LGWW - LG_E)
  ),
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Sphere(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
  LGCS
 ),
 Cylinder(
  Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS),
  LGCS
 ),
 Difference(
  merge {
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS)
   ),
   Torus(
    0.18-LGCS,
    LGCS
    rotate Vector(90,0,0)
    translate Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
  ),
  Box(
   Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18+LG_E, -HEIGHT * LGBH + LGPH + LG_E),
   Vector(LENGTH / 2 * LGBW - 0.2, -WIDTH / 2 * LGBW - 0.18-LG_E, -HEIGHT * LGBH + LGPH-LGWW - LG_E)
  ),
 ),
 Difference(
  merge {
   Box(
    Vector(LENGTH / 2 * LGBW, WIDTH / 2 * LGBW - 0.18+LGCS, -LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - 0.18, -LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18, -LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - 0.18+LGCS, 0)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW, -LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18, -LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, 0)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW)
   ),
   Difference(
    merge {
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -LGWW + LGCS),
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -LGCS),
      0.18
     ),
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -LGWW),
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, 0),
      0.18-LGCS
     ),
    ),
    Box(
     Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18-LG_E, LG_E),
     Vector(LENGTH / 2 * LGBW - 0.2, WIDTH / 2 * LGBW + 0.18+LG_E, -LGWW - LG_E)
    ),
   ),
  ),
  Sphere(
   Vector(LENGTH / 2 * LGBW + 0.1, WIDTH / 2 * LGBW, -LGWW - 0.12+0.12*sin(25*pi/180)), 0.12
  ),
 ),
 Difference(
  merge {
   Box(
    Vector(LENGTH / 2 * LGBW, -WIDTH / 2 * LGBW + 0.18-LGCS, -LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + 0.18, -LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18, -LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + 0.18-LGCS, 0)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -LGWW)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW, -LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18, -LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, 0)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18-LGCS, -LGWW)
   ),
   Difference(
    merge {
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -LGWW + LGCS),
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -LGCS),
      0.18
     ),
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -LGWW),
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, 0),
      0.18-LGCS
     ),
    ),
    Box(
     Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18+LG_E, LG_E),
     Vector(LENGTH / 2 * LGBW - 0.2, -WIDTH / 2 * LGBW - 0.18-LG_E, -LGWW - LG_E)
    ),
   ),
  ),
  Sphere(
   Vector(LENGTH / 2 * LGBW + 0.1, -WIDTH / 2 * LGBW, -LGWW - 0.12+0.12*sin(25*pi/180)), 0.12
  ),
 ),
 Difference(
  merge {
   Box(
    Vector(LENGTH / 2 * LGBW, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - 0.18, -HEIGHT * LGBH + LGPH-LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, WIDTH / 2 * LGBW - LGCS, -HEIGHT * LGBH + LGPH)
    Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW)
   ),
   Difference(
    merge {
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS),
      0.18
     ),
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGWW),
      Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH),
      0.18-LGCS
     ),
    ),
    Box(
     Vector(LENGTH / 2 * LGBW + 0.08, WIDTH / 2 * LGBW - 0.18-LG_E, -HEIGHT * LGBH + LGPH + LG_E),
     Vector(LENGTH / 2 * LGBW - 0.2, WIDTH / 2 * LGBW + 0.18+LG_E, -HEIGHT * LGBH + LGPH-LGWW - LG_E)
    ),
   ),
  ),
  Sphere(
   Vector(LENGTH / 2 * LGBW + 0.1, WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH + 0.12-0.12*sin(25*pi/180)), 0.12
  ),
 ),
 Difference(
  merge {
   Box(
    Vector(LENGTH / 2 * LGBW, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + 0.18, -HEIGHT * LGBH + LGPH-LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW + LGCS, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW - 0.18+LGCS, -HEIGHT * LGBH + LGPH-LGWW)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18, -HEIGHT * LGBH + LGPH-LGWW + LGCS)
   ),
   Box(
    Vector(LENGTH / 2 * LGBW - LGCS, -WIDTH / 2 * LGBW + LGCS, -HEIGHT * LGBH + LGPH)
    Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18-LGCS, -HEIGHT * LGBH + LGPH-LGWW)
   ),
   Difference(
    merge {
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGWW + LGCS),
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGCS),
      0.18
     ),
     Cylinder(
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH-LGWW),
      Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH),
      0.18-LGCS
     ),
    ),
    Box(
     Vector(LENGTH / 2 * LGBW + 0.08, -WIDTH / 2 * LGBW + 0.18+LG_E, -HEIGHT * LGBH + LGPH + LG_E),
     Vector(LENGTH / 2 * LGBW - 0.2, -WIDTH / 2 * LGBW - 0.18-LG_E, -HEIGHT * LGBH + LGPH-LGWW - LG_E)
    ),
   ),
  ),
  Sphere(
   Vector(LENGTH / 2 * LGBW + 0.1, -WIDTH / 2 * LGBW, -HEIGHT * LGBH + LGPH + 0.12-0.12*sin(25*pi/180)), 0.12
  ),
 ),
),

#end
'''
