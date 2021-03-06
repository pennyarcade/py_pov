/*******************************************************************************/
/*                                                                             */
/* LGEO Libray Include File     (C) lgeo@digitalbricks.org (Lutz Uhlmann)      */
/*                                                                             */
/* 19980319 Lutz Uhlmann                                                       */
/* 20071101 Lutz Uhlmann fixed stud orientation                                */
/*                                                                             */
/* This file is in no way related to the LEGO(tm) Group.                       */
/* It is provided for private non-commercial use only.                         */
/*                                                                             */
/* lg_6070: Windscreen 2 x 5 x 1 & 2/3                                         */
/*                                                                             */ 
/*******************************************************************************/
#ifdef(lg_6070)
#else
#declare lg_angle=atan2(5*LG_PLATE_HEIGHT-0.24, 2*LG_BRICK_WIDTH);
#declare lg_6070 =
union {
 #declare MIR = 0;
 #while (MIR < 2)
  union {
   sphere {
    <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.24-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.24-LG_CORNER_SPACE>,
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   box {
    <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE-LG_E, -LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_WALL_WIDTH, -LG_PLATE_HEIGHT>
   }
   difference {
    union {
     cylinder {
      <0, LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>,
      <2*LG_BRICK_WIDTH/cos(lg_angle), LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>,
      LG_CORNER_SPACE
     }
     cylinder {
      <0, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+2*LG_CORNER_SPACE>,
      <2*LG_BRICK_WIDTH/cos(lg_angle), LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+2*LG_CORNER_SPACE>,
      LG_CORNER_SPACE
     }
     box {
      <0, LG_BRICK_WIDTH, 0>,
      <2*LG_BRICK_WIDTH/cos(lg_angle), LG_BRICK_WIDTH-LG_CORNER_SPACE-LG_E, -LG_PLATE_HEIGHT+2*LG_CORNER_SPACE>
     }
     box {
      <0, LG_BRICK_WIDTH-LG_WALL_WIDTH, 0>,
      <2*LG_BRICK_WIDTH/cos(lg_angle), LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>
     }
     rotate <0, lg_angle*180/pi, 0>
     translate <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0, -LG_CORNER_SPACE>
    }
    box {
     <3.5*LG_BRICK_WIDTH, LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
     <4.5*LG_BRICK_WIDTH, LG_BRICK_WIDTH/2, -5.5*LG_PLATE_HEIGHT>
    }
   }
   cylinder {
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   torus {
    0.08-LG_CORNER_SPACE,
    LG_CORNER_SPACE
    translate <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.08>
   }
   cylinder {
    <3.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.08>,
    <3.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -3*LG_PLATE_HEIGHT>,
    LG_CORNER_SPACE
   }
   box {
    <3.5*LG_BRICK_WIDTH+LG_CORNER_SPACE+LG_E, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.08>,
    <3.5*LG_BRICK_WIDTH, LG_BRICK_WIDTH-LG_WALL_WIDTH, -3*LG_PLATE_HEIGHT>
   }
   box {
    <3.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH, -5*LG_PLATE_HEIGHT+0.08>,
    <3.8*LG_BRICK_WIDTH, LG_BRICK_WIDTH-LG_WALL_WIDTH, -3*LG_PLATE_HEIGHT>
   }
   box {
    <3.75*LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH, -4.5*LG_PLATE_HEIGHT>,
    <4.25*LG_BRICK_WIDTH, LG_BRICK_WIDTH-LG_WALL_WIDTH, -4*LG_PLATE_HEIGHT>
   }
   box {
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE+LG_E>,
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT>
   }
   box {
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH, -5*LG_PLATE_HEIGHT+0.24-LG_CORNER_SPACE>
   }
   cylinder {
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.08>,
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+0.08>,
    0.08
   }
   cylinder {
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_CORNER_SPACE-LG_E, -5*LG_PLATE_HEIGHT+0.08>,
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH, -5*LG_PLATE_HEIGHT+0.08>,
    0.08-LG_CORNER_SPACE
   }
   #if (MIR = 1)
    matrix <1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0>
   #end
  }
  #declare MIR = MIR + 1;
 #end
 cylinder {
  <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.24-LG_CORNER_SPACE>,
  <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.24-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 object {
  lg_plate_column
  translate <0, 0, -LG_PLATE_HEIGHT>
 }
 box {
  <LG_BRICK_WIDTH/2, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <LG_BRICK_WIDTH/2-LG_WALL_WIDTH, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT>
 }
 box {
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE+LG_E, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>
 }
 box {
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_WALL_WIDTH, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT>
 }
 difference {
  box {
   <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>,
   <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_TOP_HEIGHT>
  }
  union {
   object {
    lg_knob_inner_space
    translate <0, LG_BRICK_WIDTH/2, -LG_TOP_HEIGHT>
   } 
   object {
    lg_knob_inner_space
    translate <0, -LG_BRICK_WIDTH/2, -LG_TOP_HEIGHT>
   } 
  }
 }
 box {
  <4.5*LG_BRICK_WIDTH, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <4.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.24-LG_CORNER_SPACE>
 }
 box {
  <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE+LG_E>,
  <4.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT>
 }
 box {
  <0, LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_CORNER_SPACE>,
  <2*LG_BRICK_WIDTH/cos(lg_angle), -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_TOP_HEIGHT+LG_CORNER_SPACE>
  rotate <0, lg_angle*180/pi, 0>
  translate <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0, -LG_CORNER_SPACE>
 }
 object {
  lg_knob
  rotate <0, 0, 90>
  translate <0, LG_BRICK_WIDTH/2, 0>
 }
 object {
  lg_knob
  rotate <0, 0, 90>
  translate <0, -LG_BRICK_WIDTH/2, 0>
 }
}

#declare lg_6070_clear =
merge {
 #declare MIR = 0;
 #while (MIR < 2)
  merge {
   sphere {
    <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.24-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.24-LG_CORNER_SPACE>,
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   object {
    lg_knob_clear
    translate <0, LG_BRICK_WIDTH/2, 0>
   }
   box {
    <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE-LG_E, -LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_WALL_WIDTH, -LG_PLATE_HEIGHT>
   }
   difference {
    merge {
     cylinder {
      <0, LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>,
      <2*LG_BRICK_WIDTH/cos(lg_angle), LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>,
      LG_CORNER_SPACE
     }
     cylinder {
      <0, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+2*LG_CORNER_SPACE>,
      <2*LG_BRICK_WIDTH/cos(lg_angle), LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+2*LG_CORNER_SPACE>,
      LG_CORNER_SPACE
     }
     box {
      <0, LG_BRICK_WIDTH, 0>,
      <2*LG_BRICK_WIDTH/cos(lg_angle), LG_BRICK_WIDTH-LG_CORNER_SPACE-LG_E, -LG_PLATE_HEIGHT+2*LG_CORNER_SPACE>
     }
     box {
      <0, LG_BRICK_WIDTH-LG_WALL_WIDTH, 0>,
      <2*LG_BRICK_WIDTH/cos(lg_angle), LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>
     }
     rotate <0, lg_angle*180/pi, 0>
     translate <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0, -LG_CORNER_SPACE>
    }
    box {
     <3.5*LG_BRICK_WIDTH, LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
     <4.5*LG_BRICK_WIDTH, LG_BRICK_WIDTH/2, -5.5*LG_PLATE_HEIGHT>
    }
   }
   cylinder {
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   torus {
    0.08-LG_CORNER_SPACE,
    LG_CORNER_SPACE
    translate <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.08>
   }
   cylinder {
    <3.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.08>,
    <3.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -3*LG_PLATE_HEIGHT>,
    LG_CORNER_SPACE
   }
   box {
    <3.5*LG_BRICK_WIDTH+LG_CORNER_SPACE+LG_E, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.08>,
    <3.5*LG_BRICK_WIDTH, LG_BRICK_WIDTH-LG_WALL_WIDTH, -3*LG_PLATE_HEIGHT>
   }
   box {
    <3.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH, -5*LG_PLATE_HEIGHT+0.08>,
    <3.8*LG_BRICK_WIDTH, LG_BRICK_WIDTH-LG_WALL_WIDTH, -3*LG_PLATE_HEIGHT>
   }
   box {
    <3.75*LG_BRICK_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH, -4.5*LG_PLATE_HEIGHT>,
    <4.25*LG_BRICK_WIDTH, LG_BRICK_WIDTH-LG_WALL_WIDTH, -4*LG_PLATE_HEIGHT>
   }
   box {
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE+LG_E>,
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT>
   }
   box {
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH, -5*LG_PLATE_HEIGHT+0.24-LG_CORNER_SPACE>
   }
   cylinder {
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.08>,
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+0.08>,
    0.08
   }
   cylinder {
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH-LG_CORNER_SPACE-LG_E, -5*LG_PLATE_HEIGHT+0.08>,
    <3.5*LG_BRICK_WIDTH+0.08, LG_BRICK_WIDTH, -5*LG_PLATE_HEIGHT+0.08>,
    0.08-LG_CORNER_SPACE
   }
   #if (MIR = 1)
    matrix <1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0>
   #end
  }
  #declare MIR = MIR + 1;
 #end
 cylinder {
  <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.24-LG_CORNER_SPACE>,
  <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.24-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 object {
  lg_plate_column_clear
  translate <0, 0, -LG_PLATE_HEIGHT>
 }
 box {
  <LG_BRICK_WIDTH/2, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <LG_BRICK_WIDTH/2-LG_WALL_WIDTH, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT>
 }
 box {
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE+LG_E, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>
 }
 box {
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_WALL_WIDTH, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_PLATE_HEIGHT>
 }
 difference {
  box {
   <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>,
   <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_TOP_HEIGHT>
  }
  union {
   object {
    lg_knob_inner_space_clear
    translate <0, LG_BRICK_WIDTH/2, -LG_TOP_HEIGHT>
   } 
   object {
    lg_knob_inner_space_clear
    translate <0, -LG_BRICK_WIDTH/2, -LG_TOP_HEIGHT>
   } 
  }
 }
 box {
  <4.5*LG_BRICK_WIDTH, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <4.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+0.24-LG_CORNER_SPACE>
 }
 box {
  <4.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE+LG_E>,
  <4.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT>
 }
 box {
  <0, LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_CORNER_SPACE>,
  <2*LG_BRICK_WIDTH/cos(lg_angle), -LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_TOP_HEIGHT+LG_CORNER_SPACE>
  rotate <0, lg_angle*180/pi, 0>
  translate <2.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0, -LG_CORNER_SPACE>
 }
 object {
  lg_knob_clear
  rotate <0, 0, 90>
  translate <0, LG_BRICK_WIDTH/2, 0>
 }
 object {
  lg_knob_clear
  rotate <0, 0, 90>
  translate <0, -LG_BRICK_WIDTH/2, 0>
 }
}

#end
