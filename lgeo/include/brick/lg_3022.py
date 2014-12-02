'''****************************************************************************/
*                                                                             */
* LGEO Libray Include File     (C) lgeo@digitalbricks.org (Lutz Uhlmann)      */
*                                                                             */
* 19970623 Lutz Uhlmann                                                       */
* 20071226 Lutz Uhlmann fixed stud orientation                                */
*                                                                             */
* This file is in no way related to the LEGO(tm) Group.                       */
* It is provided for private non-commercial use only.                         */
*                                                                             */
* lg_3022: Plate 2 x 2                                                        */
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


def solid(LENGTH=2, WIDTH=2):
    return Union(
        Sphere(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
            Vector(
                LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_PLATE_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_PLATE_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_PLATE_HEIGHT-LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_PLATE_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_PLATE_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_PLATE_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_PLATE_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_PLATE_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_PLATE_HEIGHT-LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_PLATE_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                ((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
                ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
                LG_CORNER_SPACE
            ),
            Vector(
                ((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
                ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
                (LG_PLATE_HEIGHT-LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                ((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
                ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
                (LG_PLATE_HEIGHT-LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                ((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
                ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
                (LG_PLATE_HEIGHT-LG_CORNER_SPACE)
            ),
            Vector(
                LG_CORNER_SPACE,
                ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
                (LG_PLATE_HEIGHT-LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                ((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
                LG_CORNER_SPACE,
                (LG_PLATE_HEIGHT-LG_CORNER_SPACE)
            ),
            Vector(
                ((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
                ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
                (LG_PLATE_HEIGHT-LG_CORNER_SPACE)
            ),
            LG_CORNER_SPACE
        ),
        Difference(
            Union(
                Box(
                    Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, 0),
                    Vector(
                        LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                        WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                        LG_PLATE_HEIGHT
                    )
                ),
                Box(
                    Vector(0, LG_CORNER_SPACE, LG_CORNER_SPACE),
                    Vector(
                        LENGTH*LG_BRICK_WIDTH,
                        WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                        LG_PLATE_HEIGHT-LG_CORNER_SPACE
                    )
                ),
                Box(
                    Vector(LG_CORNER_SPACE, 0, LG_CORNER_SPACE),
                    Vector(
                        LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                        WIDTH*LG_BRICK_WIDTH,
                        LG_PLATE_HEIGHT-LG_CORNER_SPACE
                    )
                ),
            ),
            get_knob_inner_space(LENGTH, WIDTH)
        ),
        Object(
            lg_plate_cylinder,
            Translate(Vector(LG_BRICK_WIDTH, LG_BRICK_WIDTH, 0))
        ),
        get_knob_objects(LENGTH, WIDTH, LG_PLATE_HEIGHT),
        Translate(
            Vector(-LENGTH/2*LG_BRICK_WIDTH, -LG_BRICK_WIDTH, -LG_PLATE_HEIGHT)
        ),
        Rotate(Vector(0, 0, 90))
    )


# noqa
'''

#declare lg_3022_clear =
Merge(
 Sphere(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
    LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector((LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE),
    LG_CORNER_SPACE, LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector((LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE),
    LG_CORNER_SPACE, LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
    (LG_PLATE_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_PLATE_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_PLATE_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE, (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  Vector(((LENGTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((WIDTH*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_PLATE_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Difference(
  Merge(
   Box(
    Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, 0),
    Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
        WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_PLATE_HEIGHT)
   ),
   Box(
    Vector(0, LG_CORNER_SPACE, LG_CORNER_SPACE),
    Vector(LENGTH*LG_BRICK_WIDTH,
        WIDTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
        LG_PLATE_HEIGHT-LG_CORNER_SPACE)
   ),
   Box(
    Vector(LG_CORNER_SPACE, 0, LG_CORNER_SPACE),
    Vector(LENGTH*LG_BRICK_WIDTH-LG_CORNER_SPACE,
        WIDTH*LG_BRICK_WIDTH, LG_PLATE_HEIGHT-LG_CORNER_SPACE)
   ),
  ),
  Merge(
   Box(
    Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_CORNER_SPACE),
    Vector(LENGTH*LG_BRICK_WIDTH-LG_WALL_WIDTH,
        WIDTH*LG_BRICK_WIDTH-LG_WALL_WIDTH,
        LG_PLATE_INNER_HEIGHT)
   ),
   #declare KS_X = 0;
   #while (KS_X < LENGTH)
    #declare KS_Y = 0;
    #while (KS_Y < WIDTH)
     Object(
      lg_knob_inner_space_clear
      Translate(Vector((KS_X+0.5)*LG_BRICK_WIDTH,
        (KS_Y+0.5)*LG_BRICK_WIDTH, LG_PLATE_INNER_HEIGHT)
     ),
     #declare KS_Y = KS_Y + 1;
     #end
    #declare KS_X = KS_X + 1;
   #end
  ),
 ),
 Object(
  lg_plate_cylinder_clear
  Translate(Vector(LG_BRICK_WIDTH, LG_BRICK_WIDTH, 0)
 ),
 #declare KNOB_X = 0;
 #while (KNOB_X < LENGTH)
  #declare KNOB_Y = 0;
  #while (KNOB_Y < WIDTH)
   Object(
    lg_knob_clear
    Rotate(Vector(0, 0, -90)
    Translate(Vector((0.5+KNOB_X)*LG_BRICK_WIDTH,
        (0.5+KNOB_Y)*LG_BRICK_WIDTH, LG_PLATE_HEIGHT)
   ),
   #declare KNOB_Y = KNOB_Y + 1;
  #end
  #declare KNOB_X = KNOB_X + 1;
 #end
 Translate(Vector(-LENGTH/2*LG_BRICK_WIDTH,
    -LG_BRICK_WIDTH, -LG_PLATE_HEIGHT)
 Rotate(Vector(0, 0, 90)
),

#end
'''
