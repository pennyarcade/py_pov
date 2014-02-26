'''****************************************************************************/
*                                                                             */
* LGEO Libray Include File     (C) lgeo@digitalbricks.org (Lutz Uhlmann)      */
*                                                                             */
* 19970801 Lutz Uhlmann                                                       */
* 20080102 Lutz Uhlmann fixed stud orientation                                */
*                                                                             */
* This file is in no way related to the LEGO(tm) Group.                       */
* It is provided for private non-commercial use only.                         */
*                                                                             */
* lg_3788: Car Mudguard 2 x 4                                                 */
*                                                                             */
*****************************************************************************'''

from lgeo.include.common.lg_defs import *
from lgeo.include.common.brick_subparts import *

from pov.basic.Vector import Vector

from pov.csg.Union import Union

from pov.finite_solid.Box import Box

from pov.object_modifier.Translate import Translate
from pov.object_modifier.Rotate import Rotate

from pov.other.Object import Object


lg_angle = atan2(0.44, 0.38)*180/pi


def solid():
    mainpart= Union()

    ROT = 0
    while (ROT < 2):
        rotpart = Union(
            Sphere(
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Sphere(
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Sphere(
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Sphere(
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Sphere(
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Sphere(
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Sphere(
                Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Sphere(
                Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(-0.3-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -0.2+LG_CORNER_SPACE),
                Vector(0.3+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -0.2+LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Cylinder(
                Vector(0, 0, 0),
                Vector(0.38/cos(lg_angle*pi/180), 0, 0),
                LG_CORNER_SPACE,
                Rotate(Vector(0, -lg_angle, 0)),
                Translate(Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE))
            ),
            Cylinder(
                Vector(0, 0, 0),
                Vector(-0.38/cos(lg_angle*pi/180), 0, 0),
                LG_CORNER_SPACE,
                Rotate(Vector(0, lg_angle, 0)),
                Translate(Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE))
            ),
            Difference(
                Union(
                    Box(
                        Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0),
                        Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT)
                    ),
                    Box(
                        Vector(LG_BRICK_WIDTH, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
                        Vector(-LG_BRICK_WIDTH, LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE)
                    ),
                    Box(
                        Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH, -LG_CORNER_SPACE),
                        Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE)
                    )
                ),
                Union(
                    Object(
                        lg_knob_inner_space,
                        Translate(Vector(LG_BRICK_WIDTH/2, 1.5*LG_BRICK_WIDTH, -LG_TOP_HEIGHT))
                    ),
                    Object(
                        lg_knob_inner_space,
                        Translate(Vector(-LG_BRICK_WIDTH/2, 1.5*LG_BRICK_WIDTH, -LG_TOP_HEIGHT))
                    ),
                    Box(
                        Vector(LG_BRICK_WIDTH-0.12, 2*LG_BRICK_WIDTH-0.12, -LG_TOP_HEIGHT),
                        Vector(-LG_BRICK_WIDTH+0.12, LG_BRICK_WIDTH-LG_E, -2*LG_PLATE_HEIGHT-LG_E)
                    ),
                    Box(
                        Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-0.12, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                        Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT-LG_E)
                    ),
                    Box(
                        Vector(-LG_CORNER_SPACE, -LG_WALL_WIDTH, 0),
                        Vector(0.38/cos(lg_angle*pi/180), LG_CORNER_SPACE+LG_E, -0.5),
                        Rotate(Vector(0, -lg_angle, 0)),
                        Translate(Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE))
                    ),
                    Box(
                        Vector(LG_CORNER_SPACE, -LG_WALL_WIDTH, 0),
                        Vector(-0.38/cos(lg_angle*pi/180), LG_CORNER_SPACE+LG_E, -0.5),
                        Rotate(Vector(0, lg_angle, 0)),
                        Translate(Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE))
                    ),
                    Box(
                        Vector(-0.3-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH, -0.2+LG_CORNER_SPACE),
                        Vector(0.3+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH+LG_E, -2*LG_PLATE_HEIGHT-LG_E)
                    )
                )
            ),
            Difference(
                Box(
                    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+0.13, -LG_CORNER_SPACE),
                    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_WALL_WIDTH, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE)
                ),
                Union(
                    Box(
                        Vector(LG_BRICK_WIDTH, 0.2, 0),
                        Vector(-LG_BRICK_WIDTH, 0, -0.4/cos(18.00416161)),
                        Rotate(Vector(-18.00416161, 0, 0)),
                        Translate(Vector(0, LG_BRICK_WIDTH+0.13, -0.2))
                    ),
                    Box(
                        Vector(LG_BRICK_WIDTH, LG_BRICK_WIDTH, 0),
                        Vector(-LG_BRICK_WIDTH, LG_BRICK_WIDTH-0.2, -LG_PLATE_HEIGHT-LG_E)
                    ),
                ),
            ),
            Box(
                Vector(LG_BRICK_WIDTH, LG_BRICK_WIDTH+0.1, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
                Vector(LG_BRICK_WIDTH-0.12+LG_E, -LG_BRICK_WIDTH-0.1, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE)
            ),
            Box(
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+0.1, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
                Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, -LG_BRICK_WIDTH-0.1, -2*LG_PLATE_HEIGHT)
            ),
            Box(
                Vector(LG_BRICK_WIDTH-0.12, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
                Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE+LG_E, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT)
            ),
            Box(
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT),
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_WALL_WIDTH, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE+LG_E)
            ),
            Box(
                Vector(LG_BRICK_WIDTH-LG_WALL_WIDTH, LG_BRICK_WIDTH/2+0.04, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                Vector(LG_BRICK_WIDTH-0.1, LG_BRICK_WIDTH/2-0.04, -LG_PLATE_HEIGHT-LG_CORNER_SPACE)
            ),
            Box(
                Vector(-LG_BRICK_WIDTH+LG_WALL_WIDTH, LG_BRICK_WIDTH/2+0.04, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
                Vector(-LG_BRICK_WIDTH+0.1, LG_BRICK_WIDTH/2-0.04, -LG_PLATE_HEIGHT-LG_CORNER_SPACE)
            ),
            Box(
                Vector(0, -0.12+LG_CORNER_SPACE, -LG_CORNER_SPACE),
                Vector(0.38/cos(lg_angle*pi/180), 0, LG_E),
                Rotate(Vector(0, -lg_angle, 0)),
                Translate(Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE))
            ),
            Box(
                Vector(0, -0.12+LG_CORNER_SPACE, -LG_CORNER_SPACE),
                Vector(-0.38/cos(lg_angle*pi/180), 0, LG_E),
                Rotate(Vector(0, lg_angle, 0)),
                Translate(Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE))
            ),
            Box(
                Vector(-0.3-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-0.12, -0.2+LG_CORNER_SPACE),
                Vector(0.3+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -0.2)
            ),
            Box(
                Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT),
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-0.12e0, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE)
            ),
            Box(
                Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT),
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-0.12e0, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE)
            ),
            Object(
                lg_knob(),
                Rotate(Vector(0, 0, 90+180*ROT)),
                Translate(Vector(LG_BRICK_WIDTH/2, LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT))
            ),
            Object(
                lg_knob(),
                Rotate(Vector(0, 0, 90+180*ROT)),
                Translate(Vector(-LG_BRICK_WIDTH/2, LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT))
            ),
            Object(
                lg_knob(),
                Rotate(Vector(0, 0, 90+180*ROT)),
                Translate(Vector(LG_BRICK_WIDTH/2, 3*LG_BRICK_WIDTH/2, 0))
            ),
            Object(
                lg_knob(),
                Rotate(Vector(0, 0, 90+180*ROT)),
                Translate(Vector(-LG_BRICK_WIDTH/2, 3*LG_BRICK_WIDTH/2, 0))
            )
        )

        if (ROT == 1):
            rotpart.append(
                Rotate(Vector(0, 0, 180))
            )

        mainpart.append(rotpart)
        ROT = ROT + 1
    #end

    mainpart.append(
        Difference(
            Box(
                Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT),
                Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_TOP_HEIGHT)
            ),
            Union(
                Object(
                    lg_knob_inner_space,
                    Translate(Vector(LG_BRICK_WIDTH/2, LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT-LG_TOP_HEIGHT))
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(Vector(-LG_BRICK_WIDTH/2, LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT-LG_TOP_HEIGHT))
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(Vector(-LG_BRICK_WIDTH/2, -LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT-LG_TOP_HEIGHT))
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(Vector(LG_BRICK_WIDTH/2, -LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT-LG_TOP_HEIGHT))
                )
            )
        ),
        Object(
            lg_plate_cylinder,
            Translate(Vector(0, 0, -2*LG_PLATE_HEIGHT))
        )
    )

    return mainpart

'''
#declare lg_3788_clear =
merge {
 #declare ROT = 0;
 #while (ROT < 2)
  merge {
   Sphere(
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Sphere(
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Sphere(
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Sphere(
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Sphere(
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Sphere(
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Sphere(
    Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Sphere(
    Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE),
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(-0.3-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -0.2+LG_CORNER_SPACE),
    Vector(0.3+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -0.2+LG_CORNER_SPACE),
    LG_CORNER_SPACE
   }
   Cylinder(
    Vector(0, 0, 0),
    Vector(0.38/cos(lg_angle*pi/180), 0, 0),
    LG_CORNER_SPACE
    Rotate(Vector(0, -lg_angle, 0>
    Translate(Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
   }
   Cylinder(
    Vector(0, 0, 0),
    Vector(-0.38/cos(lg_angle*pi/180), 0, 0),
    LG_CORNER_SPACE
    Rotate(Vector(0, lg_angle, 0>
    Translate(Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
   }
   Difference(
    merge {
     Box(
      Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0),
      Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT>
     ),
     Box(
      Vector(LG_BRICK_WIDTH, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE),
      Vector(-LG_BRICK_WIDTH, LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
     ),
     Box(
      Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH, -LG_CORNER_SPACE),
      Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
     ),
    ),
    Union(
     Object(
      lg_knob_inner_space_clear
      Translate(Vector(LG_BRICK_WIDTH/2, 1.5*LG_BRICK_WIDTH, -LG_TOP_HEIGHT>
     ),
     Object(
      lg_knob_inner_space_clear
      Translate(Vector(-LG_BRICK_WIDTH/2, 1.5*LG_BRICK_WIDTH, -LG_TOP_HEIGHT>
     ),
     Box(
      Vector(LG_BRICK_WIDTH-0.12, 2*LG_BRICK_WIDTH-0.12, -LG_TOP_HEIGHT),
      Vector(-LG_BRICK_WIDTH+0.12, LG_BRICK_WIDTH-LG_E, -2*LG_PLATE_HEIGHT-LG_E>
     ),
     Box(
      Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-0.12, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
      Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT-LG_E>
     ),
     Box(
      Vector(-LG_CORNER_SPACE, -LG_WALL_WIDTH, 0>
      Vector(0.38/cos(lg_angle*pi/180), LG_CORNER_SPACE+LG_E, -0.5>
      Rotate(Vector(0, -lg_angle, 0>
      Translate(Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
     ),
     Box(
      Vector(LG_CORNER_SPACE, -LG_WALL_WIDTH, 0>
      Vector(-0.38/cos(lg_angle*pi/180), LG_CORNER_SPACE+LG_E, -0.5>
      Rotate(Vector(0, lg_angle, 0>
      Translate(Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
     ),
     Box(
      Vector(-0.3-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH, -0.2+LG_CORNER_SPACE),
      Vector(0.3+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH+LG_E, -2*LG_PLATE_HEIGHT-LG_E>
     ),
    ),
   }
   Difference(
    Box(
     Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+0.13, -LG_CORNER_SPACE),
     Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_WALL_WIDTH, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
    ),
    Union(
     Box(
      Vector(LG_BRICK_WIDTH, 0.2, 0),
      Vector(-LG_BRICK_WIDTH, 0, -0.4/cos(18.00416161)>
      Rotate(Vector(-18.00416161, 0, 0>
      Translate(Vector(0, LG_BRICK_WIDTH+0.13, -0.2>
     ),
     Box(
      Vector(LG_BRICK_WIDTH, LG_BRICK_WIDTH, 0),
      Vector(-LG_BRICK_WIDTH, LG_BRICK_WIDTH-0.2, -LG_PLATE_HEIGHT-LG_E>
     ),
    ),
   }
   Box(
    Vector(LG_BRICK_WIDTH, LG_BRICK_WIDTH+0.1, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
    Vector(LG_BRICK_WIDTH-0.12+LG_E, -LG_BRICK_WIDTH-0.1, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
   }
   Box(
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+0.1, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
    Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, -LG_BRICK_WIDTH-0.1, -2*LG_PLATE_HEIGHT>
   }
   Box(
    Vector(LG_BRICK_WIDTH-0.12, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_CORNER_SPACE),
    Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE+LG_E, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT>
   }
   Box(
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT),
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_WALL_WIDTH, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE+LG_E>
   }
   Box(
    Vector(LG_BRICK_WIDTH-LG_WALL_WIDTH, LG_BRICK_WIDTH/2+0.04, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    Vector(LG_BRICK_WIDTH-0.1, LG_BRICK_WIDTH/2-0.04, -LG_PLATE_HEIGHT-LG_CORNER_SPACE>
   }
   Box(
    Vector(-LG_BRICK_WIDTH+LG_WALL_WIDTH, LG_BRICK_WIDTH/2+0.04, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE),
    Vector(-LG_BRICK_WIDTH+0.1, LG_BRICK_WIDTH/2-0.04, -LG_PLATE_HEIGHT-LG_CORNER_SPACE>
   }
   Box(
    Vector(0, -0.12+LG_CORNER_SPACE, -LG_CORNER_SPACE>
    Vector(0.38/cos(lg_angle*pi/180), 0, LG_E>
    Rotate(Vector(0, -lg_angle, 0>
    Translate(Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
   }
   Box(
    Vector(0, -0.12+LG_CORNER_SPACE, -LG_CORNER_SPACE>
    Vector(-0.38/cos(lg_angle*pi/180), 0, LG_E>
    Rotate(Vector(0, lg_angle, 0>
    Translate(Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
   }
   Box(
    Vector(-0.3-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-0.12, -0.2+LG_CORNER_SPACE),
    Vector(0.3+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -0.2>
   }
   Box(
    Vector(LG_BRICK_WIDTH-0.12+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT),
    Vector(LG_BRICK_WIDTH-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-0.12E, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
   }
   Box(
    Vector(-LG_BRICK_WIDTH+0.12-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_PLATE_HEIGHT),
    Vector(-LG_BRICK_WIDTH+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-0.12E, -2*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
   }
   Object(
    lg_knob_clear
    Rotate(Vector(0, 0, 90+180*ROT>
    Translate(Vector(LG_BRICK_WIDTH/2, LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT>
   }
   Object(
    lg_knob_clear
    Rotate(Vector(0, 0, 90+180*ROT>
    Translate(Vector(-LG_BRICK_WIDTH/2, LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT>
   }
   Object(
    lg_knob_clear
    Rotate(Vector(0, 0, 90+180*ROT>
    Translate(Vector(LG_BRICK_WIDTH/2, 3*LG_BRICK_WIDTH/2, 0>
   }
   Object(
    lg_knob_clear
    Rotate(Vector(0, 0, 90+180*ROT>
    Translate(Vector(-LG_BRICK_WIDTH/2, 3*LG_BRICK_WIDTH/2, 0>
   }
   #if (ROT = 1)
    Rotate(Vector(0, 0, 180>
   #end
  }
  #declare ROT = ROT +1;
 #end
 Difference(
  Box(
   <LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT),
   <-LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT-LG_TOP_HEIGHT>
  }
  Union(
   Object(
    lg_knob_inner_space_clear
    Translate(Vector(LG_BRICK_WIDTH/2, LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT-LG_TOP_HEIGHT>
   }
   Object(
    lg_knob_inner_space_clear
    Translate(Vector(-LG_BRICK_WIDTH/2, LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT-LG_TOP_HEIGHT>
   }
   Object(
    lg_knob_inner_space_clear
    Translate(Vector(-LG_BRICK_WIDTH/2, -LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT-LG_TOP_HEIGHT>
   }
   Object(
    lg_knob_inner_space_clear
    Translate(Vector(LG_BRICK_WIDTH/2, -LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT-LG_TOP_HEIGHT>
   }
  }
 }
 Object(
  lg_plate_cylinder_clear
  Translate(Vector(0, 0, -2*LG_PLATE_HEIGHT>
 }
}

#end
'''
