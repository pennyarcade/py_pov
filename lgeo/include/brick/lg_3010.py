'''***************************************************************************
*                                                                            *
* LGEO Libray Include File     (C) lgeo@digitalbricks.org (Lutz Uhlmann)     *
*                                                                            *
* 19970623 Lutz Uhlmann                                                      *
* 20071226 Lutz Uhlmann fixed stud orientation                               *
*                                                                            *
* This file is in no way related to the LEGO(tm) Group.                      *
* It is provided for private non-commercial use only.                        *
*                                                                            *
* lg_3010: Brick 1 x 4                                                       *
*                                                                            *
***************************************************************************'''

from lgeo.include.common.brick_subparts import get_knob_inner_space
from lgeo.include.common.brick_subparts import get_brick_coloumn, get_knob_objects
from lgeo.include.common.lg_defs import LG_CORNER_SPACE, LG_BRICK_WIDTH
from lgeo.include.common.lg_defs import LG_BRICK_HEIGHT

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from pov.other.Object import Object


def solid(length=4, width=1):
    '''
        @Todo: DocString
    '''
    return Union(
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
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
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
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
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
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
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE
            ),
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Sphere(
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            Vector(
                LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            Vector(
                length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                LG_BRICK_HEIGHT-LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Difference(
            Union(
                Box(
                    Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, 0),
                    Vector(
                        length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                        width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                        LG_BRICK_HEIGHT
                    ),
                ),
                Box(
                    Vector(0, LG_CORNER_SPACE, LG_CORNER_SPACE),
                    Vector(
                        length*LG_BRICK_WIDTH,
                        width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                        LG_BRICK_HEIGHT-LG_CORNER_SPACE
                    ),
                ),
                Box(
                    Vector(LG_CORNER_SPACE, 0, LG_CORNER_SPACE),
                    Vector(
                        length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
                        width*LG_BRICK_WIDTH,
                        LG_BRICK_HEIGHT-LG_CORNER_SPACE
                    ),
                ),
            ),
            get_knob_inner_space(length, width)
        ),
        get_brick_coloumn(length),
        get_knob_objects(length, width),
        Translate(
            Vector(
                -length/2*LG_BRICK_WIDTH,
                -LG_BRICK_WIDTH/2,
                -LG_BRICK_HEIGHT
            )
        ),
        Rotate(Vector(0, 0, 90))
    )


# noqa
'''

#declare lg_3010_clear =
Merge(
 Sphere(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
    LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector((length*LG_BRICK_WIDTH-LG_CORNER_SPACE),
    LG_CORNER_SPACE, LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector((length*LG_BRICK_WIDTH-LG_CORNER_SPACE),
    LG_CORNER_SPACE, LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
    (LG_BRICK_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
    LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
    (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE,
    ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(LG_CORNER_SPACE, ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_BRICK_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(LG_CORNER_SPACE, LG_CORNER_SPACE,
    (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE, ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE, LG_CORNER_SPACE),
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
  Vector(LG_CORNER_SPACE, ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE), LG_CORNER_SPACE),
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Sphere(
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_BRICK_HEIGHT-LG_CORNER_SPACE)), LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  Vector(LG_CORNER_SPACE,
    ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Cylinder(
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    LG_CORNER_SPACE, (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  Vector(((length*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    ((width*LG_BRICK_WIDTH)-LG_CORNER_SPACE),
    (LG_BRICK_HEIGHT-LG_CORNER_SPACE)),
  LG_CORNER_SPACE
 ),
 Difference(
  Merge(
   Box(
    Vector(LG_CORNER_SPACE, LG_CORNER_SPACE, 0),
    Vector(length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
      width*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_HEIGHT),
   ),
   Box(
    Vector(0, LG_CORNER_SPACE, LG_CORNER_SPACE),
    Vector(length*LG_BRICK_WIDTH,
      width*LG_BRICK_WIDTH-LG_CORNER_SPACE,
      LG_BRICK_HEIGHT-LG_CORNER_SPACE),
   ),
   Box(
    Vector(LG_CORNER_SPACE, 0, LG_CORNER_SPACE),
    Vector(length*LG_BRICK_WIDTH-LG_CORNER_SPACE,
      width*LG_BRICK_WIDTH, LG_BRICK_HEIGHT-LG_CORNER_SPACE),
   ),
  ),
  Merge(
   Box(
    Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LG_CORNER_SPACE),
    Vector(length*LG_BRICK_WIDTH-LG_WALL_WIDTH,
      width*LG_BRICK_WIDTH-LG_WALL_WIDTH, LG_BRICK_INNER_HEIGHT),
   ),
   #declare KS_X = 0;
   #while (KS_X Vector( length)
    Object(
     lg_knob()_inner_space_clear
     Translate(Vector((KS_X+0.5)*LG_BRICK_WIDTH,
      0.5*LG_BRICK_WIDTH, LG_BRICK_INNER_HEIGHT),
    ),
    #declare KS_X = KS_X + 1;
   #end
  ),
 ),
 #declare COL_X = 1;
 #while (COL_X Vector( length)
  Object(
   lg_brick_column_clear
   Translate(Vector(COL_X*LG_BRICK_WIDTH, 0.5*LG_BRICK_WIDTH, 0),
  ),
  #declare COL_X = COL_X + 1;
 #end
 #declare KNOB_X = 0;
 #while (KNOB_X Vector( length)
  Object(
   lg_knob()_clear
   Rotate(Vector(0, 0, -90),
   Translate(Vector((0.5+KNOB_X)*LG_BRICK_WIDTH,
    0.5*LG_BRICK_WIDTH, LG_BRICK_HEIGHT),
  ),
  #declare KNOB_X = KNOB_X + 1;
 #end
 Translate(Vector(-length/2*LG_BRICK_WIDTH,
  -LG_BRICK_WIDTH/2,-LG_BRICK_HEIGHT),
 Rotate(Vector(0,0,90),
),

'''
