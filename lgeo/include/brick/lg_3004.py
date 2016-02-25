"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970623 Lutz Uhlmann
20071225 Lutz Uhlmann fixed stud orientation

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_3004: Brick 1 x 2
"""

from lgeo.include.common.brick_subparts import standard_plate

from lgeo.include.common.lg_defs import LGBH, LG_BRICK_INNER_HEIGHT


def solid(length=1, width=2, height=LGBH, innerheight=LG_BRICK_INNER_HEIGHT):
    """
    return lg_3004: Brick 1 x 2.

    @Todo: fix plate column
    """
    return standard_plate(length, width, height, innerheight)


# #ifdef(lg_3004)
# #else
# #declare LENGTH = 2;
# #declare WIDTH = 1;
# #declare lg_3004 =
# union {
#  sphere {
#   <LGCS, LGCS, LGCS>, LGCS
#  }
#  cylinder {
#   <LGCS, LGCS, LGCS>,
#   <(LENGTH*LGBW-LGCS), LGCS,
#   LGCS>,
#   LGCS
#  }
#  sphere {
#   <(LENGTH*LGBW-LGCS), LGCS,
#   LGCS>, LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS),
#   LGCS, LGCS>,
#   <((LENGTH*LGBW)-LGCS),
#   LGCS, (LGBH-LGCS)>,
#   LGCS
#  }
#  sphere {
#   <((LENGTH*LGBW)-LGCS), LGCS,
#   (LGBH-LGCS)>, LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS),
#   LGCS, (LGBH-LGCS)>,
#   <LGCS, LGCS, (LGBH-LGCS)>,
#   LGCS
#  }
#  sphere {
#   <LGCS, LGCS, (LGBH-LGCS)>,
#   LGCS
#  }
#  cylinder {
#   <LGCS, LGCS, LGCS>,
#   <LGCS, LGCS, (LGBH-LGCS)>,
#    LGCS
#  }
#  cylinder {
#   <LGCS, LGCS, LGCS>,
#   <LGCS, ((WIDTH*LGBW)-LGCS),
#   LGCS>,
#   LGCS
#  }
#  sphere {
#   <LGCS, ((WIDTH*LGBW)-LGCS),
#   LGCS>, LGCS
#  }
#  cylinder {
#   <LGCS, ((WIDTH*LGBW)-LGCS),
#   LGCS>,
#   <LGCS, ((WIDTH*LGBW)-LGCS),
#   (LGBH-LGCS)>,
#   LGCS
#  }
#  sphere {
#   <LGCS, ((WIDTH*LGBW)-LGCS),
#   (LGBH-LGCS)>, LGCS
#  }
#  cylinder {
#   <LGCS, LGCS, (LGBH-LGCS)>,
#   <LGCS, ((WIDTH*LGBW)-LGCS),
#   (LGBH-LGCS)>,
#   LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS),
#   LGCS, LGCS>,
#   <((LENGTH*LGBW)-LGCS),
#   ((WIDTH*LGBW)-LGCS), LGCS>,
#   LGCS
#  }
#  sphere {
#   <((LENGTH*LGBW)-LGCS),
#   ((WIDTH*LGBW)-LGCS), LGCS>, LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS),
#   ((WIDTH*LGBW)-LGCS), LGCS>,
#   <LGCS, ((WIDTH*LGBW)-LGCS),
#   LGCS>,
#   LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS),
#   ((WIDTH*LGBW)-LGCS), LGCS>,
#   <((LENGTH*LGBW)-LGCS),
#   ((WIDTH*LGBW)-LGCS),
#   (LGBH-LGCS)>,
#   LGCS
#  }
#  sphere {
#   <((LENGTH*LGBW)-LGCS),
#   ((WIDTH*LGBW)-LGCS),
#   (LGBH-LGCS)>, LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS),
#   ((WIDTH*LGBW)-LGCS),
#   (LGBH-LGCS)>,
#   <LGCS, ((WIDTH*LGBW)-LGCS),
#   (LGBH-LGCS)>,
#   LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS),
#   LGCS, (LGBH-LGCS)>,
#   <((LENGTH*LGBW)-LGCS),
#   ((WIDTH*LGBW)-LGCS),
#   (LGBH-LGCS)>,
#   LGCS
#  }
#  difference {
#   union {
#    box {
#     <LGCS, LGCS, 0>,
#     <LENGTH*LGBW-LGCS,
#     WIDTH*LGBW-LGCS, LGBH>
#    }
#    box {
#     <0, LGCS, LGCS>,
#     <LENGTH*LGBW, WIDTH*LGBW-LGCS,
#     LGBH-LGCS>
#    }
#    box {
#     <LGCS, 0, LGCS>,
#     <LENGTH*LGBW-LGCS, WIDTH*LGBW,
#     LGBH-LGCS>
#    }
#   }
#   union {
#    box {
#     <LG_WALL_WIDTH, LG_WALL_WIDTH, -LGCS>,
#     <LENGTH*LGBW-LG_WALL_WIDTH,
#     IDTH*LGBW-LG_WALL_WIDTH,
#     LG_BRICK_INNER_HEIGHT>
#    }
#    #declare KS_X = 0;
#    #while (KS_X < LENGTH)
#     object {
#      lg_knob_inner_space
#      translate <(KS_X+0.5)*LGBW,
#      0.5*LGBW,
#       LG_BRICK_INNER_HEIGHT>
#     }
#     #declare KS_X = KS_X + 1;
#    #end
#   }
#  }
#  object {
#   lg_brick_column
#   translate <LGBW, 0.5*LGBW, 0>
#  }
#  #declare KNOB_X = 0;
#  #while (KNOB_X < LENGTH)
#   object {
#    lg_knob
#    rotate <0, 0, -90>
#    translate <(0.5+KNOB_X)*LGBW, 0.5*LGBW, LGBH>
#   }
#   #declare KNOB_X = KNOB_X + 1;
#  #end
#  translate <-LGBW,-LGBW/2,-LGBH>
#  rotate <0,0,90>
# }

# #declare lg_3004_clear =
# merge {
#  sphere {
#   <LGCS, LGCS, LGCS>, LGCS
#  }
#  cylinder {
#   <LGCS, LGCS, LGCS>,
#   <(LENGTH*LGBW-LGCS), LGCS, LGCS>,
#   LGCS
#  }
#  sphere {
#   <(LENGTH*LGBW-LGCS), LGCS, LGCS>, LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS), LGCS, LGCS>,
#   <((LENGTH*LGBW)-LGCS), LGCS, (LGBH-LGCS)>,
#   LGCS
#  }
#  sphere {
#   <((LENGTH*LGBW)-LGCS), LGCS, (LGBH-LGCS)>, LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS), LGCS, (LGBH-LGCS)>,
#   <LGCS, LGCS, (LGBH-LGCS)>,
#   LGCS
#  }
#  sphere {
#   <LGCS, LGCS, (LGBH-LGCS)>, LGCS
#  }
#  cylinder {
#   <LGCS, LGCS, LGCS>,
#   <LGCS, LGCS, (LGBH-LGCS)>,
#   LGCS
#  }
#  cylinder {
#   <LGCS, LGCS, LGCS>,
#   <LGCS, ((WIDTH*LGBW)-LGCS), LGCS>,
#   LGCS
#  }
#  sphere {
#   <LGCS, ((WIDTH*LGBW)-LGCS), LGCS>, LGCS
#  }
#  cylinder {
#   <LGCS, ((WIDTH*LGBW)-LGCS), LGCS>,
#   <LGCS, ((WIDTH*LGBW)-LGCS), (LGBH-LGCS)>,
#   LGCS
#  }
#  sphere {
#   <LGCS, ((WIDTH*LGBW)-LGCS), (LGBH-LGCS)>, LGCS
#  }
#  cylinder {
#   <LGCS, LGCS, (LGBH-LGCS)>,
#   <LGCS, ((WIDTH*LGBW)-LGCS), (LGBH-LGCS)>,
#   LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS), LGCS, LGCS>,
#   <((LENGTH*LGBW)-LGCS), ((WIDTH*LGBW)-LGCS), LGCS>,
#   LGCS
#  }
#  sphere {
#   <((LENGTH*LGBW)-LGCS), ((WIDTH*LGBW)-LGCS), LGCS>, LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS), ((WIDTH*LGBW)-LGCS), LGCS>,
#   <LGCS, ((WIDTH*LGBW)-LGCS), LGCS>,
#   LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS), ((WIDTH*LGBW)-LGCS), LGCS>,
#   <((LENGTH*LGBW)-LGCS), ((WIDTH*LGBW)-LGCS), (LGBH-LGCS)>,
#   LGCS
#  }
#  sphere {
#   <((LENGTH*LGBW)-LGCS), ((WIDTH*LGBW)-LGCS), (LGBH-LGCS)>, LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS), ((WIDTH*LGBW)-LGCS), (LGBH-LGCS)>,
#   <LGCS, ((WIDTH*LGBW)-LGCS), (LGBH-LGCS)>,
#   LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS), LGCS, (LGBH-LGCS)>,
#   <((LENGTH*LGBW)-LGCS), ((WIDTH*LGBW)-LGCS), (LGBH-LGCS)>,
#   LGCS
#  }
#  difference {
#   merge {
#    box {
#     <LGCS, LGCS, 0>,
#     <LENGTH*LGBW-LGCS, WIDTH*LGBW-LGCS, LGBH>
#    }
#    box {
#     <0, LGCS, LGCS>,
#     <LENGTH*LGBW, WIDTH*LGBW-LGCS, LGBH-LGCS>
#    }
#    box {
#     <LGCS, 0, LGCS>,
#     <LENGTH*LGBW-LGCS, WIDTH*LGBW, LGBH-LGCS>
#    }
#   }
#   merge {
#    box {
#     <LG_WALL_WIDTH, LG_WALL_WIDTH, -LGCS>,
#     <LENGTH*LGBW-LG_WALL_WIDTH, WIDTH*LGBW-LG_WALL_WIDTH,
#     LG_BRICK_INNER_HEIGHT>
#    }
#    #declare KS_X = 0;
#    #while (KS_X < LENGTH)
#     object {
#      lg_knob_inner_space_clear
#      translate <(KS_X+0.5)*LGBW, 0.5*LGBW, LG_BRICK_INNER_HEIGHT>
#     }
#     #declare KS_X = KS_X + 1;
#    #end
#   }
#  }
#  object {
#   lg_brick_column_clear
#   translate <LGBW, 0.5*LGBW, 0>
#  }
#  #declare KNOB_X = 0;
#  #while (KNOB_X < LENGTH)
#   object {
#    lg_knob_clear
#    rotate <0, 0, -90>
#    translate <(0.5+KNOB_X)*LGBW, 0.5*LGBW, LGBH>
#   }
#   #declare KNOB_X = KNOB_X + 1;
#  #end
#  translate <-LGBW,-LGBW/2,-LGBH>
#  rotate <0,0,90>
# }

# #end
