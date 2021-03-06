/*******************************************************************************/
/*                                                                             */
/* LGEO Libray Include File     (C) lgeo@digitalbricks.org (Lutz Uhlmann)      */
/*                                                                             */
/* 19980413 Lutz Uhlmann                                                       */
/* 20071118 Lutz Uhlmann fixed 45 degree section edges                         */
/* 20071123 Lutz Uhlmann fixed stud notches height to fit studs with logo      */
/* 20071201 Lutz Uhlmann fixed hollow stud logo and orientation                */
/*                                                                             */
/* This file is in no way related to the LEGO(tm) Group.                       */
/* It is provided for private non-commercial use only.                         */
/*                                                                             */
/* lg_2345: Castle Wall Corner 3 x 3 x 6                                       */
/*                                                                             */ 
/*******************************************************************************/
#ifdef(lg_2345)
#else
#declare lg_2345 =
union {
 #declare MIR = 0;
 #while (MIR < 2)
  union {
   sphere {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_E>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT+LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT+LG_CORNER_SPACE>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   box {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE-LG_E, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT+LG_CORNER_SPACE>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   box {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE-LG_E, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>,
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <0.5*LG_BRICK_WIDTH, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -17*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_BRICK_HEIGHT>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <LG_BRICK_WIDTH-0.06, 0.5*LG_BRICK_WIDTH-LG_E, -5*LG_BRICK_HEIGHT>,
    <LG_BRICK_WIDTH+0.06, 0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_BRICK_HEIGHT+LG_PLATE_INNER_HEIGHT+LG_E>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_E, LG_BRICK_WIDTH-0.06, -5*LG_BRICK_HEIGHT>,
    <0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, LG_BRICK_WIDTH+0.06, -5*LG_BRICK_HEIGHT+LG_PLATE_INNER_HEIGHT+LG_E>
   }
   difference {
    union {
     box {
      <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>,
      <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT>
     }
     box {
      <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>,
      <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>
     }
     box {
      <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
      <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>
     }
     box {
      <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT>,
      <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH, -14*LG_PLATE_HEIGHT-LG_TOP_HEIGHT>
     }
    }
    box {
     <0, 2*LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT-LG_E>,
     <LG_BRICK_WIDTH, -1.5*LG_BRICK_WIDTH, -14*LG_PLATE_HEIGHT+LG_E>
     rotate <0, 0, -45>
     translate <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 0>
    }
   }
   box {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE-LG_E, -LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH, -LG_BRICK_HEIGHT-LG_E>
   }
   object {
    lg_tech_knob_logo
    #if (MIR = 1)
     matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
    #end
    translate <0, LG_BRICK_WIDTH, -LG_BRICK_HEIGHT>
   }
   object {
    lg_tech_knob_logo
    #if (MIR = 1)
     matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
    #end
    translate <LG_BRICK_WIDTH, LG_BRICK_WIDTH, -LG_BRICK_HEIGHT>
   }
   #if (MIR = 1)
    matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
   #end
  }
  #declare MIR = MIR + 1;
 #end
 sphere {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 sphere {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -1.5*LG_BRICK_WIDTH+3*LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -1.5*LG_BRICK_WIDTH+LG_WALL_WIDTH/sin(pi/4)+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 sphere {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 sphere {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 object {
  lg_plate_cylinder 
  translate <-0.5*LG_BRICK_WIDTH, 0.5*LG_BRICK_WIDTH, -6*LG_BRICK_HEIGHT>
 }
 box {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT>,
  <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT-LG_TOP_HEIGHT>
 }
 difference {
  union {
   cylinder {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <-0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -1.5*LG_BRICK_WIDTH+3*LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   box {
    <0, 0, -6*LG_BRICK_HEIGHT>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE/sin(pi/4), -2*LG_BRICK_WIDTH/sin(pi/4), -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 0>
   }
   box {
    <0, 0, 0>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE/sin(pi/4), -2*LG_BRICK_WIDTH/sin(pi/4), -LG_CORNER_SPACE-LG_E>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 0>
   }
   box {
    <LG_CORNER_SPACE, 0, -LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE/sin(pi/4)-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH/sin(pi/4), -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 0>
   }
  }
  union {
   box {
    <1.5*LG_BRICK_WIDTH, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT-LG_E>,
    <LG_BRICK_WIDTH, LG_BRICK_WIDTH, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <-0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -1.5*LG_BRICK_WIDTH, -6*LG_BRICK_HEIGHT-LG_E>,
    <-LG_BRICK_WIDTH, -LG_BRICK_WIDTH, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <1.5*LG_BRICK_WIDTH, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_E>,
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, LG_BRICK_WIDTH, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
   }
   box {
    <-0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -1.5*LG_BRICK_WIDTH, LG_E>,
    <-LG_BRICK_WIDTH, -1.5*LG_BRICK_WIDTH+LG_WALL_WIDTH/sin(pi/4)+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
   }
   box {
    <0, 3*LG_CORNER_SPACE/sin(pi/4), LG_E>
    <-0.1, 0, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>
   }
   box {
    <0, 3*LG_CORNER_SPACE/sin(pi/4), -LG_E>
    <-0.1, 0, LG_BRICK_HEIGHT+LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>
   }
   box {
    <0.1, 3*LG_CORNER_SPACE/sin(pi/4), LG_E>
    <-0.1, 0, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>
   }
   box {
    <0.1, 3*LG_CORNER_SPACE/sin(pi/4), -LG_E>
    <-0.1, 0, LG_BRICK_HEIGHT+LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>
   }
   box {
    <0, 3*LG_CORNER_SPACE/sin(pi/4), LG_E>
    <-0.1, 0, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>
    matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
   }
   box {
    <0, 3*LG_CORNER_SPACE/sin(pi/4), -LG_E>
    <-0.1, 0, LG_BRICK_HEIGHT+LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>
    matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
   }
   box {
    <0.1, 3*LG_CORNER_SPACE/sin(pi/4), LG_E>
    <-0.1, 0, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>
    matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
   }
   box {
    <0.1, 3*LG_CORNER_SPACE/sin(pi/4), -LG_E>
    <-0.1, 0, LG_BRICK_HEIGHT+LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>
    matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
   }
   box {
    <LG_KNOB_RADIUS+LG_E, LG_KNOB_RADIUS+LG_E, -LG_E>,
    <-LG_KNOB_RADIUS-LG_E, -LG_KNOB_RADIUS-LG_E, LG_KNOB_HEIGHT+2*LG_E>
    rotate <0, 0, 45>
    translate <LG_BRICK_WIDTH, 0, -6*LG_BRICK_HEIGHT>
   }
   box {
    <LG_KNOB_RADIUS+LG_E, LG_KNOB_RADIUS+LG_E, -LG_E>,
    <-LG_KNOB_RADIUS-LG_E, -LG_KNOB_RADIUS-LG_E, LG_KNOB_HEIGHT+2*LG_E>
    rotate <0, 0, 45>
    translate <0, -LG_BRICK_WIDTH, -6*LG_BRICK_HEIGHT>
   }
  }
 }
 cylinder {
  <-LG_BRICK_WIDTH, LG_BRICK_WIDTH, -LG_BRICK_HEIGHT-LG_E>,
  <-LG_BRICK_WIDTH, LG_BRICK_WIDTH, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT-LG_WALL_WIDTH>,
  0.08
 }
 box {
  <-LG_WALL_WIDTH/2, -0.08, -LG_BRICK_HEIGHT-LG_E>,
  <-1.5*LG_BRICK_WIDTH/sin(pi/4), 0.08, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT-LG_WALL_WIDTH>
  rotate <0, 0, -45>
  translate <0.5*LG_BRICK_WIDTH, -0.5*LG_BRICK_WIDTH, 0>
 }
 difference {
  box {
   <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT>,
   <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT>
  }
  box {
   <0, LG_E, LG_E>,
   <2*LG_BRICK_WIDTH, -3*LG_BRICK_WIDTH, -LG_TOP_HEIGHT-LG_E>
   rotate <0, 0, -45>
   translate <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT>
  }
 }
 object {
  lg_tech_knob_logo
  translate <-LG_BRICK_WIDTH, LG_BRICK_WIDTH, -LG_BRICK_HEIGHT>
 }
}

#declare lg_2345_clear =
merge {
 #declare MIR = 0;
 #while (MIR < 2)
  merge {
   sphere {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_E>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT+LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT+LG_CORNER_SPACE>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   box {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE-LG_E, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT+LG_CORNER_SPACE>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   box {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE-LG_E, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>,
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <0.5*LG_BRICK_WIDTH, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -17*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_BRICK_HEIGHT>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <LG_BRICK_WIDTH-0.06, 0.5*LG_BRICK_WIDTH-LG_E, -5*LG_BRICK_HEIGHT>,
    <LG_BRICK_WIDTH+0.06, 0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_BRICK_HEIGHT+LG_PLATE_INNER_HEIGHT+LG_E>
   }
   box {
    <0.5*LG_BRICK_WIDTH-LG_E, LG_BRICK_WIDTH-0.06, -5*LG_BRICK_HEIGHT>,
    <0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, LG_BRICK_WIDTH+0.06, -5*LG_BRICK_HEIGHT+LG_PLATE_INNER_HEIGHT+LG_E>
   }
   difference {
    merge {
     box {
      <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>,
      <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_BRICK_HEIGHT>
     }
     box {
      <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>,
      <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>
     }
     box {
      <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
      <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -14*LG_PLATE_HEIGHT-LG_CORNER_SPACE>
     }
     box {
      <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -14*LG_PLATE_HEIGHT>,
      <0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH, -14*LG_PLATE_HEIGHT-LG_TOP_HEIGHT>
     }
    }
    box {
     <0, 2*LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT-LG_E>,
     <LG_BRICK_WIDTH, -1.5*LG_BRICK_WIDTH, -14*LG_PLATE_HEIGHT+LG_E>
     rotate <0, 0, -45>
     translate <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 0>
    }
   }
   box {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE-LG_E, -LG_CORNER_SPACE>,
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH, -LG_BRICK_HEIGHT-LG_E>
   }
   object {
    lg_tech_knob_logo_clear
    #if (MIR = 1)
     matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
    #end
    translate <0, LG_BRICK_WIDTH, -LG_BRICK_HEIGHT>
   }
   object {
    lg_tech_knob_logo_clear
    #if (MIR = 1)
     matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
    #end
    translate <LG_BRICK_WIDTH, LG_BRICK_WIDTH, -LG_BRICK_HEIGHT>
   }
   #if (MIR = 1)
    matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
   #end
  }
  #declare MIR = MIR + 1;
 #end
 sphere {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 sphere {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>,
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -1.5*LG_BRICK_WIDTH+3*LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -1.5*LG_BRICK_WIDTH+LG_WALL_WIDTH/sin(pi/4)+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 sphere {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 sphere {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 object {
  lg_plate_cylinder_clear
  translate <-0.5*LG_BRICK_WIDTH, 0.5*LG_BRICK_WIDTH, -6*LG_BRICK_HEIGHT>
 }
 box {
  <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT>,
  <0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -17*LG_PLATE_HEIGHT-LG_TOP_HEIGHT>
 }
 difference {
  merge {
   cylinder {
    <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    <-0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -1.5*LG_BRICK_WIDTH+3*LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   box {
    <0, 0, -6*LG_BRICK_HEIGHT>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE/sin(pi/4), -2*LG_BRICK_WIDTH/sin(pi/4), -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 0>
   }
   box {
    <0, 0, 0>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE/sin(pi/4), -2*LG_BRICK_WIDTH/sin(pi/4), -LG_CORNER_SPACE-LG_E>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 0>
   }
   box {
    <LG_CORNER_SPACE, 0, -LG_CORNER_SPACE>,
    <-LG_WALL_WIDTH+LG_CORNER_SPACE/sin(pi/4)-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH/sin(pi/4), -6*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, 0>
   }
  }
  union {
   box {
    <1.5*LG_BRICK_WIDTH, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT-LG_E>,
    <LG_BRICK_WIDTH, LG_BRICK_WIDTH, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <-0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -1.5*LG_BRICK_WIDTH, -6*LG_BRICK_HEIGHT-LG_E>,
    <-LG_BRICK_WIDTH, -LG_BRICK_WIDTH, -5*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   box {
    <1.5*LG_BRICK_WIDTH, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, LG_E>,
    <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, LG_BRICK_WIDTH, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
   }
   box {
    <-0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -1.5*LG_BRICK_WIDTH, LG_E>,
    <-LG_BRICK_WIDTH, -1.5*LG_BRICK_WIDTH+LG_WALL_WIDTH/sin(pi/4)+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
   }
   box {
    <0, 3*LG_CORNER_SPACE/sin(pi/4), LG_E>
    <-0.1, 0, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>
   }
   box {
    <0, 3*LG_CORNER_SPACE/sin(pi/4), -LG_E>
    <-0.1, 0, LG_BRICK_HEIGHT+LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>
   }
   box {
    <0.1, 3*LG_CORNER_SPACE/sin(pi/4), LG_E>
    <-0.1, 0, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>
   }
   box {
    <0.1, 3*LG_CORNER_SPACE/sin(pi/4), -LG_E>
    <-0.1, 0, LG_BRICK_HEIGHT+LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>
   }
   box {
    <0, 3*LG_CORNER_SPACE/sin(pi/4), LG_E>
    <-0.1, 0, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>
    matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
   }
   box {
    <0, 3*LG_CORNER_SPACE/sin(pi/4), -LG_E>
    <-0.1, 0, LG_BRICK_HEIGHT+LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-LG_WALL_WIDTH/sin(pi/4)-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>
    matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
   }
   box {
    <0.1, 3*LG_CORNER_SPACE/sin(pi/4), LG_E>
    <-0.1, 0, -LG_BRICK_HEIGHT-LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>
    matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
   }
   box {
    <0.1, 3*LG_CORNER_SPACE/sin(pi/4), -LG_E>
    <-0.1, 0, LG_BRICK_HEIGHT+LG_CORNER_SPACE>
    rotate <0, 0, -45>
    translate <1.5*LG_BRICK_WIDTH-3*LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_BRICK_HEIGHT>
    matrix <0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0>
   }
   box {
    <LG_KNOB_RADIUS+LG_E, LG_KNOB_RADIUS+LG_E, -LG_E>,
    <-LG_KNOB_RADIUS-LG_E, -LG_KNOB_RADIUS-LG_E, LG_KNOB_HEIGHT+2*LG_E>
    rotate <0, 0, 45>
    translate <LG_BRICK_WIDTH, 0, -6*LG_BRICK_HEIGHT>
   }
   box {
    <LG_KNOB_RADIUS+LG_E, LG_KNOB_RADIUS+LG_E, -LG_E>,
    <-LG_KNOB_RADIUS-LG_E, -LG_KNOB_RADIUS-LG_E, LG_KNOB_HEIGHT+2*LG_E>
    rotate <0, 0, 45>
    translate <0, -LG_BRICK_WIDTH, -6*LG_BRICK_HEIGHT>
   }
  }
 }
 cylinder {
  <-LG_BRICK_WIDTH, LG_BRICK_WIDTH, -LG_BRICK_HEIGHT-LG_E>,
  <-LG_BRICK_WIDTH, LG_BRICK_WIDTH, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT-LG_WALL_WIDTH>,
  0.08
 }
 box {
  <-LG_WALL_WIDTH/2, -0.08, -LG_BRICK_HEIGHT-LG_E>,
  <-1.5*LG_BRICK_WIDTH/sin(pi/4), 0.08, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT-LG_WALL_WIDTH>
  rotate <0, 0, -45>
  translate <0.5*LG_BRICK_WIDTH, -0.5*LG_BRICK_WIDTH, 0>
 }
 difference {
  box {
   <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_BRICK_HEIGHT>,
   <-1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -1.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT-LG_TOP_HEIGHT>
  }
  box {
   <0, LG_E, LG_E>,
   <2*LG_BRICK_WIDTH, -3*LG_BRICK_WIDTH, -LG_TOP_HEIGHT-LG_E>
   rotate <0, 0, -45>
   translate <1.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_BRICK_HEIGHT>
  }
 }
 object {
  lg_tech_knob_logo_clear
  translate <-LG_BRICK_WIDTH, LG_BRICK_WIDTH, -LG_BRICK_HEIGHT>
 }
}

#end
