'''****************************************************************************/
*                                                                             */
* LGEO Libray Include File     (C) lgeo@digitalbricks.org (Lutz Uhlmann)      */
*                                                                             */
* 19970623 Lutz Uhlmann                                                       */
* 20071225 Lutz Uhlmann fixed stud orientation                                */
*                                                                             */
* This file is in no way related to the LEGO(tm) Group.                       */
* It is provided for private non-commercial use only.                         */
*                                                                             */
* lg_3003: Brick 2 x 2                                                        */
*                                                                             */
*****************************************************************************'''

from lgeo.include.common.brick_subparts import *
from lgeo.include.common.lg_defs import *

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from pov.other.Object import Object


def solid(LENGTH=2, WIDTH=2):
    knobs_inner = get_knob_inner_space(LENGTH, WIDTH)

    KS_X = 0
    while (KS_X < LENGTH):
        KS_Y = 0
        while (KS_Y < WIDTH):
            knobs_inner.append(
                Object(
                    lg_knob_inner_space,
                    Translate(Vector((KS_X+0.5)*LG_BRICK_WIDTH, (KS_Y+0.5)*LG_BRICK_WIDTH, LG_BRICK_INNER_HEIGHT))
                )
            )
            KS_Y = KS_Y + 1
        KS_X = KS_X + 1

    result = Union(
        Sphere(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
            Vector((LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector((LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE),
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE),
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
            Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
            Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
            LG_CORNER_SPACE
        ),
        Difference(
            Union(
                Box(
                    Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, 0),
                    Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_HEIGHT),
                ),
                Box(
                    Vector(0, 0, LG_CORNER_SPACE),
                    Vector(LENGTH*LG_BRICK_WIDTH, WIDTH*LG_BRICK_WIDTH, LG_BRICK_HEIGHT-LG_CORNER_SPACE),
                )
            ),
            knobs_inner,
        ),
        Object(
            lg_brick_cylinder,
            Translate(Vector(LG_BRICK_WIDTH, LG_BRICK_WIDTH, 0)),
        )
    )

    KNOB_X = 0
    while (KNOB_X < LENGTH):
        KNOB_Y = 0
        while (KNOB_Y < WIDTH):
            result.append(
                Object(
                    lg_knob(),
                    Rotate(Vector(0, 0, -90)),
                    Translate(Vector((0.5+KNOB_X)*LG_BRICK_WIDTH, (0.5+KNOB_Y)*LG_BRICK_WIDTH, LG_BRICK_HEIGHT)),
                )
            )
            KNOB_Y = KNOB_Y + 1
        KNOB_X = KNOB_X + 1

    result.append(
        Translate(Vector(-LG_BRICK_WIDTH, -LG_BRICK_WIDTH, -LG_BRICK_HEIGHT)),
        Rotate(Vector(0, 0, 90))
    )

    return result

'''
#declare lg_3003_clear =
Union(
 Sphere(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector((LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector((LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Difference(
  Union(
   Box(
    Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, 0),
    Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_HEIGHT),
   ),
   Box(
    Vector(0, 0, LG_CORNER_SPACE),
    Vector(LENGTH*LG_BRICK_WIDTH, WIDTH*LG_BRICK_WIDTH, LG_BRICK_HEIGHT-LG_CORNER_SPACE),
   ),
  ),
  Union(
   Box(
    Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_CORNER_SPACE),
    Vector(LENGTH*LG_BRICK_WIDTH-LG_WALL_WIDTH, WIDTH*LG_BRICK_WIDTH-LG_WALL_WIDTH, LG_BRICK_INNER_HEIGHT),
   ),
   #declare KS_X = 0;
   #while (KS_X Vector( LENGTH)
    #declare KS_Y = 0;
    #while (KS_Y Vector( WIDTH)
     Object(
      lg_knob_inner_space_clear
      Translate(Vector((KS_X+0.5)*LG_BRICK_WIDTH, (KS_Y+0.5)*LG_BRICK_WIDTH, LG_BRICK_INNER_HEIGHT),
     ),
     #declare KS_Y = KS_Y + 1;
     #end
    #declare KS_X = KS_X + 1;
   #end
  ),
 ),
 Object(
  lg_brick_cylinder_clear
  Translate(Vector(LG_BRICK_WIDTH, LG_BRICK_WIDTH, 0),
 ),
 #declare KNOB_X = 0;
 #while (KNOB_X Vector( LENGTH)
  #declare KNOB_Y = 0;
  #while (KNOB_Y Vector( WIDTH)
   Object(
    lg_knob_clear
    Rotate(Vector(0, 0, -90),
    Translate(Vector((0.5+KNOB_X)*LG_BRICK_WIDTH, (0.5+KNOB_Y)*LG_BRICK_WIDTH, LG_BRICK_HEIGHT),
   ),
   #declare KNOB_Y = KNOB_Y + 1;
  #end
  #declare KNOB_X = KNOB_X + 1;
 #end
 Translate(Vector(-LG_BRICK_WIDTH,-LG_BRICK_WIDTH,-LG_BRICK_HEIGHT),
 Rotate(Vector(0,0,90),
),

#end
'''