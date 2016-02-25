"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970623 Lutz Uhlmann
20071226 Lutz Uhlmann fixed stud orientation

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_3020: Plate 2 x 4
"""

from lgeo.include.common.brick_subparts import standard_plate


def solid():
    """Return lg_3020: Plate 2 x 4."""
    return standard_plate(2, 4)


# #declare lg_3020_clear =
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
#   <((LENGTH*LGBW)-LGCS), LGCS, (LGPH-LGCS)>,
#   LGCS
#  }
#  sphere {
#   <((LENGTH*LGBW)-LGCS), LGCS, (LGPH-LGCS)>, LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS), LGCS, (LGPH-LGCS)>,
#   <LGCS, LGCS, (LGPH-LGCS)>,
#   LGCS
#  }
#  sphere {
#   <LGCS, LGCS, (LGPH-LGCS)>, LGCS
#  }
#  cylinder {
#   <LGCS, LGCS, LGCS>,
#   <LGCS, LGCS, (LGPH-LGCS)>,
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
#   <LGCS, ((WIDTH*LGBW)-LGCS), (LGPH-LGCS)>,
#   LGCS
#  }
#  sphere {
#   <LGCS, ((WIDTH*LGBW)-LGCS), (LGPH-LGCS)>, LGCS
#  }
#  cylinder {
#   <LGCS, LGCS, (LGPH-LGCS)>,
#   <LGCS, ((WIDTH*LGBW)-LGCS), (LGPH-LGCS)>,
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
#   <((LENGTH*LGBW)-LGCS), ((WIDTH*LGBW)-LGCS), (LGPH-LGCS)>,
#   LGCS
#  }
#  sphere {
#   <((LENGTH*LGBW)-LGCS), ((WIDTH*LGBW)-LGCS), (LGPH-LGCS)>, LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS), ((WIDTH*LGBW)-LGCS), (LGPH-LGCS)>,
#   <LGCS, ((WIDTH*LGBW)-LGCS), (LGPH-LGCS)>,
#   LGCS
#  }
#  cylinder {
#   <((LENGTH*LGBW)-LGCS), LGCS, (LGPH-LGCS)>,
#   <((LENGTH*LGBW)-LGCS), ((WIDTH*LGBW)-LGCS), (LGPH-LGCS)>,
#   LGCS
#  }
#  difference {
#   merge {
#    box {
#     <LGCS, LGCS, 0>,
#     <LENGTH*LGBW-LGCS, WIDTH*LGBW-LGCS, LGPH>
#    }
#    box {
#     <0, LGCS, LGCS>,
#     <LENGTH*LGBW, WIDTH*LGBW-LGCS, LGPH-LGCS>
#    }
#    box {
#     <LGCS, 0, LGCS>,
#     <LENGTH*LGBW-LGCS, WIDTH*LGBW, LGPH-LGCS>
#    }
#   }
#   merge {
#    box {
#     <LG_WALL_WIDTH, LG_WALL_WIDTH, -LGCS>,
#     <LENGTH*LGBW-LG_WALL_WIDTH, WIDTH*LGBW-LG_WALL_WIDTH,
#     LG_PLATE_INNER_HEIGHT>
#    }
#    #declare KS_X = 0;
#    #while (KS_X < LENGTH)
#     #declare KS_Y = 0;
#     #while (KS_Y < WIDTH)
#      object {
#       lg_knob_inner_space_clear
#       translate <(KS_X+0.5)*LGBW, (KS_Y+0.5)*LGBW, LG_PLATE_INNER_HEIGHT>
#      }
#      #declare KS_Y = KS_Y + 1;
#      #end
#     #declare KS_X = KS_X + 1;
#    #end
#   }
#  }
#  #declare CYL_X = 1;
#  #while (CYL_X < LENGTH)
#   object {
#    lg_plate_cylinder_clear
#    translate <CYL_X*LGBW, LGBW, 0>
#   }
#   #declare CYL_X = CYL_X + 1;
#  #end
#  #declare KNOB_X = 0;
#  #while (KNOB_X < LENGTH)
#   #declare KNOB_Y = 0;
#   #while (KNOB_Y < WIDTH)
#    object {
#     lg_knob_clear
#     rotate <0, 0, -90>
#     translate <(0.5+KNOB_X)*LGBW, (0.5+KNOB_Y)*LGBW, LGPH>
#    }
#    #declare KNOB_Y = KNOB_Y + 1;
#   #end
#   #declare KNOB_X = KNOB_X + 1;
#  #end
#  translate <-LENGTH/2*LGBW, -LGBW, -LGPH>
#  rotate <0, 0, 90>
# }

# #end
