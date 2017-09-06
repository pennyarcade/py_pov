"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970623 Lutz Uhlmann
20071225 Lutz Uhlmann fixed stud orientation

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_3003: Brick 2 x 2
"""

from lgeo.include.common.brick_subparts import standard_plate

from lgeo.include.common.lg_defs import LGBH, LG_BRICK_INNER_HEIGHT


def solid(length=2, width=2, height=LGBH, innerheight=LG_BRICK_INNER_HEIGHT):
    """@Todo: DocString."""
    return standard_plate(length, width, height, innerheight)


# #declare lg_3003_clear =
# Merge(
#  Sphere(
#   Vector(LGCS, LGCS, LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS, LGCS),
#   Vector((length * LGBW - LGCS), LGCS,
#     LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector((length * LGBW - LGCS), LGCS,
#     LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS), LGCS,
#     LGCS),
#   Vector(((length * LGBW)-LGCS), LGCS,
#     (LGBH - LGCS)),
#   LGCS
#  ),
#  Sphere(
#   Vector(((length * LGBW)-LGCS), LGCS,
#     (LGBH - LGCS)), LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS), LGCS,
#     (LGBH - LGCS)),
#   Vector(LGCS, LGCS,
#     (LGBH - LGCS)),
#   LGCS
#  ),
#  Sphere(
#   Vector(LGCS, LGCS,
#     (LGBH - LGCS)),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS, LGCS),
#   Vector(LGCS, LGCS,
#     (LGBH - LGCS)),
#   LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS, LGCS),
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     LGCS),
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     (LGBH - LGCS)),
#   LGCS
#  ),
#  Sphere(
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     (LGBH - LGCS)), LGCS
#  ),
#  Cylinder(
#   Vector(LGCS, LGCS,
#     (LGBH - LGCS)),
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     (LGBH - LGCS)),
#   LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS), LGCS,
#     LGCS),
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS), LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS), LGCS),
# LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS), LGCS),
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS), LGCS),
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS),
#     (LGBH - LGCS)),
#   LGCS
#  ),
#  Sphere(
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS),
#     (LGBH - LGCS)), LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS),
#     (LGBH - LGCS)),
#   Vector(LGCS, ((width * LGBW)-LGCS),
#     (LGBH - LGCS)),
#   LGCS
#  ),
#  Cylinder(
#   Vector(((length * LGBW)-LGCS),
#     LGCS, (LGBH - LGCS)),
#   Vector(((length * LGBW)-LGCS),
#     ((width * LGBW)-LGCS),
#     (LGBH - LGCS)),
#   LGCS
#  ),
#  Difference(
#   Merge(
#    Box(
#     Vector(LGCS, LGCS, 0),
#     Vector(length * LGBW - LGCS,
#       width * LGBW - LGCS, LGBH),
#    ),
#    Box(
#     Vector(0, 0, LGCS),
#     Vector(length * LGBW, width * LGBW,
#       LGBH - LGCS),
#    ),
#   ),
#   Merge(
#    Box(
#     Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LGCS),
#     Vector(length * LGBW - LG_WALL_WIDTH,
#       width * LGBW - LG_WALL_WIDTH, LG_BRICK_INNER_HEIGHT),
#    ),
#    #declare KS_X = 0;
#    #while (KS_X Vector(length)
#     #declare KS_Y = 0;
#     #while (KS_Y Vector(width)
#      Object(
#       lg_knob_inner_space_clear
#       Translate(Vector((KS_X+0.5)*LGBW,
#         (KS_Y+0.5)*LGBW, LG_BRICK_INNER_HEIGHT),
#      ),
#      #declare KS_Y = KS_Y + 1;
#      #end
#     #declare KS_X = KS_X + 1;
#    #end
#   ),
#  ),
#  Object(
#   lg_brick_cylinder_clear
#   Translate(Vector(LGBW, LGBW, 0),
#  ),
#  #declare KNOB_X = 0;
#  #while (KNOB_X Vector(length)
#   #declare KNOB_Y = 0;
#   #while (KNOB_Y Vector(width)
#    Object(
#     lg_knob_clear
#     Rotate(Vector(0, 0, -90),
#     Translate(Vector((0.5+KNOB_X)*LGBW,
#       (0.5+KNOB_Y)*LGBW, LGBH),
#    ),
#    #declare KNOB_Y = KNOB_Y + 1;
#   #end
#   #declare KNOB_X = KNOB_X + 1;
#  #end
#  Translate(Vector(-LGBW,-LGBW,-LGBH),
#  Rotate(Vector(0,0,90),
# )
