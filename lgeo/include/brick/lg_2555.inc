/*******************************************************************************/
/*                                                                             */
/* LGEO Libray Include File     (C) lgeo@digitalbricks.org (Lutz Uhlmann)      */
/*                                                                             */
/* 19970921 Lutz Uhlmann                                                       */
/*                                                                             */
/* This file is in no way related to the LEGO(tm) Group.                       */
/* It is provided for private non-commercial use only.                         */
/*                                                                             */
/* lg_2555: Tile 1 x 1 with Clip                                               */
/*                                                                             */ 
/*******************************************************************************/
#ifdef(lg_2555)
#else
#declare lg_angle1 = atan2(0.08, 0.42);
#declare lg_angle2 = asin((0.13+LG_CORNER_SPACE)/(0.16+LG_CORNER_SPACE));
#declare lg_2555 =
union {
 #declare ROT = 0;
 #while (ROT < 2)
  union {
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0, LG_KNOB_INNER_RADIUS+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
    rotate <lg_angle2*180/pi, 0, 0>
    translate <0, 0, 0.24>
   }
   sphere {
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0, LG_KNOB_INNER_RADIUS+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
    rotate <lg_angle2*180/pi, 0, 0>
    translate <0, 0, 0.24>
   }
   cylinder {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.24+(LG_WALL_WIDTH+LG_CORNER_SPACE)*cos(lg_angle2)>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.24+(LG_WALL_WIDTH+LG_CORNER_SPACE)*cos(lg_angle2)>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.24+(LG_WALL_WIDTH+LG_CORNER_SPACE)*cos(lg_angle2)>,
    LG_CORNER_SPACE
   }
   cylinder {
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.24+(LG_WALL_WIDTH+LG_CORNER_SPACE)*cos(lg_angle2)>,
    LG_CORNER_SPACE
   }
   intersection {
    torus {
     LG_KNOB_INNER_RADIUS+LG_CORNER_SPACE,
     LG_CORNER_SPACE
     rotate <0, 0, 90>
    }
    union {
     box {
      <LG_CORNER_SPACE+LG_E, 0, 2*LG_WALL_WIDTH>,
      <-LG_CORNER_SPACE-LG_E, 2*LG_WALL_WIDTH, -2*LG_WALL_WIDTH>
      rotate <-lg_angle2*180/pi, 0, 0>
     }
     box {
      <LG_CORNER_SPACE+LG_E, 0, 2*LG_WALL_WIDTH>,
      <-LG_CORNER_SPACE-LG_E, -2*LG_WALL_WIDTH, -2*LG_WALL_WIDTH>
      rotate <lg_angle2*180/pi, 0, 0>
     }
    }
    translate <LG_WALL_WIDTH-LG_CORNER_SPACE, 0, 0.24>
   }
   box {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_CORNER_SPACE, 0>
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_E, 0.08/sin(lg_angle1)>
    rotate <lg_angle1*180/pi, 0, 0>
    translate <0, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>
   }
   box {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE-LG_E>
   }
   box {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13, 0.42-LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE+LG_E, 0.24+(LG_WALL_WIDTH+LG_CORNER_SPACE)*cos(lg_angle2)>
   }
   #if (ROT = 1)
    rotate <0, 0, 180>
   #end
  }
  #declare ROT = ROT + 1;
 #end
 difference {
  union {
   box {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 0>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_PLATE_HEIGHT>
   }
   box {
    <LG_BRICK_WIDTH/2, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2, -LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>
   }
  }
  box {
   <LG_BRICK_WIDTH/2-LG_WALL_WIDTH, LG_BRICK_WIDTH/2-LG_WALL_WIDTH, -LG_TOP_HEIGHT>,
   <-LG_BRICK_WIDTH/2+LG_WALL_WIDTH, -LG_BRICK_WIDTH/2+LG_WALL_WIDTH, -LG_PLATE_HEIGHT-LG_E>
  }
 }
 difference {
  box {
   <LG_WALL_WIDTH, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_E>,
   <-LG_WALL_WIDTH, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>
  }
  union {
   difference {
    box {
     <LG_WALL_WIDTH+LG_E, 0.13+LG_CORNER_SPACE, 0.42>,
     <-LG_WALL_WIDTH-LG_E, -0.13-LG_CORNER_SPACE, 0.241>
    }
    union {
     box {
      <LG_WALL_WIDTH, 0, 2*LG_WALL_WIDTH>,
      <-LG_WALL_WIDTH, 2*LG_WALL_WIDTH, -2*LG_WALL_WIDTH>
      rotate <-lg_angle2*180/pi, 0, 0>
     }
     box {
      <LG_WALL_WIDTH, 0, 2*LG_WALL_WIDTH>,
      <-LG_WALL_WIDTH, -2*LG_WALL_WIDTH, -2*LG_WALL_WIDTH>
      rotate <lg_angle2*180/pi, 0, 0>
     }
     translate <0, 0, 0.24>
    }
   }
   box {
    <LG_WALL_WIDTH+LG_E, LG_WALL_WIDTH, 0>
    <-LG_WALL_WIDTH-LG_E, 0, 0.08/sin(lg_angle1)>
    rotate <lg_angle1*180/pi, 0, 0>
    translate <0, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>
   }
   box {
    <LG_WALL_WIDTH+LG_E, LG_WALL_WIDTH, 0>
    <-LG_WALL_WIDTH-LG_E, 0, 0.08/sin(lg_angle1)>
    rotate <lg_angle1*180/pi, 0, 0>
    translate <0, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>
    rotate <0, 0, 180>
   }
   cylinder {
    <LG_WALL_WIDTH, 0, 0.24>,
    <-LG_WALL_WIDTH, 0, 0.24>,
    LG_KNOB_INNER_RADIUS
   }
   cylinder {
    <LG_WALL_WIDTH+LG_E, 0, 0.24>,
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0, 0.24>,
    LG_KNOB_INNER_RADIUS+LG_CORNER_SPACE
   }
   cylinder {
    <-LG_WALL_WIDTH-LG_E, 0, 0.24>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0, 0.24>,
    LG_KNOB_INNER_RADIUS+LG_CORNER_SPACE
   }
  }
 }
}

#declare lg_2555_clear =
merge {
 #declare ROT = 0;
 #while (ROT < 2)
  merge {
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0, LG_KNOB_INNER_RADIUS+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
    rotate <lg_angle2*180/pi, 0, 0>
    translate <0, 0, 0.24>
   }
   sphere {
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0, LG_KNOB_INNER_RADIUS+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
    rotate <lg_angle2*180/pi, 0, 0>
    translate <0, 0, 0.24>
   }
   cylinder {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.24+(LG_WALL_WIDTH+LG_CORNER_SPACE)*cos(lg_angle2)>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.24+(LG_WALL_WIDTH+LG_CORNER_SPACE)*cos(lg_angle2)>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.24+(LG_WALL_WIDTH+LG_CORNER_SPACE)*cos(lg_angle2)>,
    LG_CORNER_SPACE
   }
   cylinder {
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.24+(LG_WALL_WIDTH+LG_CORNER_SPACE)*cos(lg_angle2)>,
    LG_CORNER_SPACE
   }
   intersection {
    torus {
     LG_KNOB_INNER_RADIUS+LG_CORNER_SPACE,
     LG_CORNER_SPACE
     rotate <0, 0, 90>
    }
    union {
     box {
      <LG_CORNER_SPACE+LG_E, 0, 2*LG_WALL_WIDTH>,
      <-LG_CORNER_SPACE-LG_E, 2*LG_WALL_WIDTH, -2*LG_WALL_WIDTH>
      rotate <-lg_angle2*180/pi, 0, 0>
     }
     box {
      <LG_CORNER_SPACE+LG_E, 0, 2*LG_WALL_WIDTH>,
      <-LG_CORNER_SPACE-LG_E, -2*LG_WALL_WIDTH, -2*LG_WALL_WIDTH>
      rotate <lg_angle2*180/pi, 0, 0>
     }
    }
    translate <LG_WALL_WIDTH-LG_CORNER_SPACE, 0, 0.24>
   }
   box {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_CORNER_SPACE, 0>
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_E, 0.08/sin(lg_angle1)>
    rotate <lg_angle1*180/pi, 0, 0>
    translate <0, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>
   }
   box {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-0.08-LG_CORNER_SPACE, 0.42>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE-LG_E>
   }
   box {
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0.13, 0.42-LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0.13+LG_CORNER_SPACE+LG_E, 0.24+(LG_WALL_WIDTH+LG_CORNER_SPACE)*cos(lg_angle2)>
   }
   #if (ROT = 1)
    rotate <0, 0, 180>
   #end
  }
  #declare ROT = ROT + 1;
 #end
 difference {
  merge {
   box {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 0>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_PLATE_HEIGHT>
   }
   box {
    <LG_BRICK_WIDTH/2, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH/2, -LG_CORNER_SPACE>,
    <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH/2, -LG_PLATE_HEIGHT+LG_CORNER_SPACE>
   }
  }
  box {
   <LG_BRICK_WIDTH/2-LG_WALL_WIDTH, LG_BRICK_WIDTH/2-LG_WALL_WIDTH, -LG_TOP_HEIGHT>,
   <-LG_BRICK_WIDTH/2+LG_WALL_WIDTH, -LG_BRICK_WIDTH/2+LG_WALL_WIDTH, -LG_PLATE_HEIGHT-LG_E>
  }
 }
 difference {
  box {
   <LG_WALL_WIDTH, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_E>,
   <-LG_WALL_WIDTH, -LG_BRICK_WIDTH/2+LG_CORNER_SPACE, 0.42-LG_CORNER_SPACE>
  }
  union {
   difference {
    box {
     <LG_WALL_WIDTH+LG_E, 0.13+LG_CORNER_SPACE, 0.42>,
     <-LG_WALL_WIDTH-LG_E, -0.13-LG_CORNER_SPACE, 0.241>
    }
    union {
     box {
      <LG_WALL_WIDTH, 0, 2*LG_WALL_WIDTH>,
      <-LG_WALL_WIDTH, 2*LG_WALL_WIDTH, -2*LG_WALL_WIDTH>
      rotate <-lg_angle2*180/pi, 0, 0>
     }
     box {
      <LG_WALL_WIDTH, 0, 2*LG_WALL_WIDTH>,
      <-LG_WALL_WIDTH, -2*LG_WALL_WIDTH, -2*LG_WALL_WIDTH>
      rotate <lg_angle2*180/pi, 0, 0>
     }
     translate <0, 0, 0.24>
    }
   }
   box {
    <LG_WALL_WIDTH+LG_E, LG_WALL_WIDTH, 0>
    <-LG_WALL_WIDTH-LG_E, 0, 0.08/sin(lg_angle1)>
    rotate <lg_angle1*180/pi, 0, 0>
    translate <0, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>
   }
   box {
    <LG_WALL_WIDTH+LG_E, LG_WALL_WIDTH, 0>
    <-LG_WALL_WIDTH-LG_E, 0, 0.08/sin(lg_angle1)>
    rotate <lg_angle1*180/pi, 0, 0>
    translate <0, LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -LG_CORNER_SPACE>
    rotate <0, 0, 180>
   }
   cylinder {
    <LG_WALL_WIDTH, 0, 0.24>,
    <-LG_WALL_WIDTH, 0, 0.24>,
    LG_KNOB_INNER_RADIUS
   }
   cylinder {
    <LG_WALL_WIDTH+LG_E, 0, 0.24>,
    <LG_WALL_WIDTH-LG_CORNER_SPACE, 0, 0.24>,
    LG_KNOB_INNER_RADIUS+LG_CORNER_SPACE
   }
   cylinder {
    <-LG_WALL_WIDTH-LG_E, 0, 0.24>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE, 0, 0.24>,
    LG_KNOB_INNER_RADIUS+LG_CORNER_SPACE
   }
  }
 }
}

#end