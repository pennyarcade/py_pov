"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970623 Lutz Uhlmann
20071225 Lutz Uhlmann fixed stud orientation

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_3021: Plate 2 x 3
"""

from lgeo.include.common.brick_subparts import standard_plate


def solid():
    """Return lg_3021: Plate 2 x 3."""
    return standard_plate(2, 3)







# #declare lg_3021_clear =
# merge (
#  Sphere(
#   Vector(LGCS, LGCS, LGCS), LGCS
#  )
# Cylinder(
#   Vector(LGCS, LGCS, LGCS),
#   Vector((length*LGBW-LGCS), LGCS, LGCS),
#   LGCS
#  )
#  Sphere(
#   Vector((length*LGBW-LGCS), LGCS, LGCS), LGCS
#  )
# Cylinder(
#   Vector(((length*LGBW)-LGCS), LGCS, LGCS),
#   Vector(((length*LGBW)-LGCS), LGCS, (LGPH-LGCS)),
#   LGCS
#  )
#  Sphere(
#   Vector(((length*LGBW)-LGCS), LGCS, (LGPH-LGCS)), LGCS
#  )
# Cylinder(
#   Vector(((length*LGBW)-LGCS), LGCS, (LGPH-LGCS)),
#   Vector(LGCS, LGCS, (LGPH-LGCS)),
#   LGCS
#  )
#  Sphere(
#   Vector(LGCS, LGCS, (LGPH-LGCS)), LGCS
#  )
# Cylinder(
#   Vector(LGCS, LGCS, LGCS),
#   Vector(LGCS, LGCS, (LGPH-LGCS)),
#   LGCS
#  )
# Cylinder(
#   Vector(LGCS, LGCS, LGCS),
#   Vector(LGCS, ((width*LGBW)-LGCS), LGCS),
#   LGCS
#  )
#  Sphere(
#   Vector(LGCS, ((width*LGBW)-LGCS), LGCS), LGCS
#  )
# Cylinder(
#   Vector(LGCS, ((width*LGBW)-LGCS), LGCS),
#   Vector(LGCS, ((width*LGBW)-LGCS), (LGPH-LGCS)),
#   LGCS
#  )
#  Sphere(
#   Vector(LGCS, ((width*LGBW)-LGCS), (LGPH-LGCS)), LGCS
#  )
# Cylinder(
#   Vector(LGCS, LGCS, (LGPH-LGCS)),
#   Vector(LGCS, ((width*LGBW)-LGCS), (LGPH-LGCS)),
#   LGCS
#  )
# Cylinder(
#   Vector(((length*LGBW)-LGCS), LGCS, LGCS),
#   Vector(((length*LGBW)-LGCS), ((width*LGBW)-LGCS), LGCS),
#   LGCS
#  )
#  Sphere(
#   Vector(((length*LGBW)-LGCS), ((width*LGBW)-LGCS), LGCS), LGCS
#  )
# Cylinder(
#   Vector(((length*LGBW)-LGCS), ((width*LGBW)-LGCS), LGCS),
#   Vector(LGCS, ((width*LGBW)-LGCS), LGCS),
#   LGCS
#  )
# Cylinder(
#   Vector(((length*LGBW)-LGCS), ((width*LGBW)-LGCS), LGCS),
#   Vector(((length*LGBW)-LGCS), ((width*LGBW)-LGCS), (LGPH-LGCS)),
#   LGCS
#  )
#  Sphere(
#   Vector(((length*LGBW)-LGCS), ((width*LGBW)-LGCS), (LGPH-LGCS)), LGCS
#  )
# Cylinder(
#   Vector(((length*LGBW)-LGCS), ((width*LGBW)-LGCS), (LGPH-LGCS)),
#   Vector(LGCS, ((width*LGBW)-LGCS), (LGPH-LGCS)),
#   LGCS
#  )
# Cylinder(
#   Vector(((length*LGBW)-LGCS), LGCS, (LGPH-LGCS)),
#   Vector(((length*LGBW)-LGCS), ((width*LGBW)-LGCS), (LGPH-LGCS)),
#   LGCS
#  )
# Difference(
#   merge (
#    box (
#     Vector(LGCS, LGCS, 0),
#     Vector(length*LGBW-LGCS, width*LGBW-LGCS, LGPH)
#    )
#    box (
#     Vector(0, LGCS, LGCS),
#     Vector(length*LGBW, width*LGBW-LGCS, LGPH-LGCS)
#    )
#    box (
#     Vector(LGCS, 0, LGCS),
#     Vector(length*LGBW-LGCS, width*LGBW, LGPH-LGCS)
#    )
#   )
#   merge (
#    box (
#     Vector(LG_WALL_WIDTH, LG_WALL_WIDTH, -LGCS),
#     Vector(length*LGBW-LG_WALL_WIDTH, width*LGBW-LG_WALL_WIDTH, LG_PLATE_INNER_HEIGHT)
#    )
#    #declare KS_X = 0;
#    #while (KS_X Vector( length)
#     #declare KS_Y = 0;
#     #while (KS_Y Vector( width)
#      object (
#       lg_knob_inner_space_clear
#       translate Vector((KS_X+0.5)*LGBW, (KS_Y+0.5)*LGBW, LG_PLATE_INNER_HEIGHT)
#      )
#      #declare KS_Y = KS_Y + 1;
#      #end
#     #declare KS_X = KS_X + 1;
#    #end
#   )
#  )
#  #declare CYL_X = 1;
#  #while (CYL_X Vector( length)
#   object (
#    get_lg_cylinder(Union, LG_PLATE_INNER_HEIGHT)_clear
#    translate Vector(CYL_X*LGBW, LGBW, 0)
#   )
#   #declare CYL_X = CYL_X + 1;
#  #end
#  #declare KNOB_X = 0;
#  #while (KNOB_X Vector( length)
#   #declare KNOB_Y = 0;
#   #while (KNOB_Y Vector( width)
#    object (
#     lg_knob_clear
#     rotate Vector(0, 0, -90)
#     translate Vector((0.5+KNOB_X)*LGBW, (0.5+KNOB_Y)*LGBW, LGPH)
#    )
#    #declare KNOB_Y = KNOB_Y + 1;
#   #end
#   #declare KNOB_X = KNOB_X + 1;
#  #end
#  translate Vector(-length/2*LGBW, -LGBW, -LGPH)
#  rotate Vector(0, 0, 90)
# )

# #end
