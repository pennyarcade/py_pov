/*******************************************************************************/
/*                                                                             */
/* LGEO Libray Include File     (C) lgeo@digitalbricks.org (Lutz Uhlmann)      */
/*                                                                             */
/* 19980315 Lutz Uhlmann                                                       */
/*                                                                             */
/* This file is in no way related to the LEGO(tm) Group.                       */
/* It is provided for private non-commercial use only.                         */
/*                                                                             */
/* lg_3358: Gate 1 x 3 x 2                                                     */
/*                                                                             */ 
/*******************************************************************************/
#ifdef(lg_3358)
#else
#declare lg_3358 =
union {
 #declare MIR = 0;
 #while (MIR < 2)
  union {
   sphere {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, -LG_E>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, -LG_E>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   #if (MIR = 1)
    matrix <-1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0>
   #end
  }
  #declare MIR = MIR + 1;
 #end
 cylinder {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 box {
  <LG_BRICK_WIDTH/6, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, 0>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH>
 }
 box {
  <LG_BRICK_WIDTH/6, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
 }
 box {
  <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, LG_KNOB_HEIGHT>,
  <-LG_WALL_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE-LG_E>
 }
 box {
  <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180), -LG_E>,
  <-LG_WALL_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180), LG_KNOB_HEIGHT-LG_CORNER_SPACE>
 }
 box {
  <LG_WALL_WIDTH/2, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, -LG_E>,
  <-LG_WALL_WIDTH/2, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>
 }
 cylinder {
  <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
  <-LG_WALL_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
  <-LG_WALL_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 intersection {
  box {
   <LG_BRICK_WIDTH/6+LG_E, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
   <-LG_BRICK_WIDTH/6-LG_E, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>
  }
  union {
   #declare GRID = -2;
   #while (GRID < 0)
    #declare MIR = -45;
    #while (MIR < 90)
     union {
      cylinder {
       <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, LG_GRID_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH*sqrt(2)>,
       <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, LG_GRID_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH*sqrt(2)>,
       LG_CORNER_SPACE
      }
      cylinder {
       <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -LG_GRID_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH*sqrt(2)>,
       <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -LG_GRID_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH*sqrt(2)>,
       LG_CORNER_SPACE
      }
      cylinder {
       <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, LG_GRID_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH*sqrt(2)>,
       <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, LG_GRID_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH*sqrt(2)>,
       LG_CORNER_SPACE
      }
      cylinder {
       <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -LG_GRID_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH*sqrt(2)>,
       <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -LG_GRID_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH*sqrt(2)>,
       LG_CORNER_SPACE
      }
      box {
       <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, LG_GRID_WIDTH/2, LG_BRICK_WIDTH*sqrt(2)>,
       <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -LG_GRID_WIDTH/2, -LG_BRICK_WIDTH*sqrt(2)>
      }
      box {
       <LG_BRICK_WIDTH/6, LG_GRID_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH*sqrt(2)>,
       <-LG_BRICK_WIDTH/6, -LG_GRID_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH*sqrt(2)>
      }
      rotate <MIR, 0, 0>
      translate <0, GRID*LG_BRICK_WIDTH, -LG_BRICK_WIDTH>
     } 
     #declare MIR = MIR + 90;
    #end
    #declare GRID = GRID + 1;
   #end
  }
 }
 torus {
  LG_BRICK_WIDTH/2-LG_CORNER_SPACE,
  LG_CORNER_SPACE
  rotate <90, 0, 0>
  translate <0, 0, -LG_CORNER_SPACE>
 }
 torus {
  LG_BRICK_WIDTH/2-LG_CORNER_SPACE,
  LG_CORNER_SPACE
  rotate <90, 0, 0>
  translate <0, 0, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
 }
 difference {
  union {
   cylinder {
    <0, 0, -LG_CORNER_SPACE>,
    <0, 0, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_BRICK_WIDTH/2
   }
   cylinder {
    <0, 0, 0>,
    <0, 0, -5*LG_PLATE_HEIGHT>,
    LG_BRICK_WIDTH/2-LG_CORNER_SPACE
   }
  }
  cylinder {
   <0, 0, -LG_TOP_HEIGHT>,
   <0, 0, -5*LG_PLATE_HEIGHT-LG_E>,
   LG_KNOB_RADIUS
  }
 }
 object {
  lg_knob
 }
 rotate <0, 0, -90>
}

#declare lg_3358_clear =
merge {
 #declare MIR = 0;
 #while (MIR < 2)
  merge {
   sphere {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, -LG_E>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, -LG_E>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   #if (MIR = 1)
    matrix <-1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0>
   #end
  }
  #declare MIR = MIR + 1;
 #end
 cylinder {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 box {
  <LG_BRICK_WIDTH/6, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, 0>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH>
 }
 box {
  <LG_BRICK_WIDTH/6, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6, -0.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6, -2.5*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
 }
 box {
  <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, LG_KNOB_HEIGHT>,
  <-LG_WALL_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE-LG_E>
 }
 box {
  <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180), -LG_E>,
  <-LG_WALL_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180), LG_KNOB_HEIGHT-LG_CORNER_SPACE>
 }
 box {
  <LG_WALL_WIDTH/2, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, -LG_E>,
  <-LG_WALL_WIDTH/2, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>
 }
 cylinder {
  <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
  <-LG_WALL_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_KNOB_RADIUS*sin(69*pi/180)-LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_WALL_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
  <-LG_WALL_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH-LG_KNOB_RADIUS*sin(69*pi/180)+LG_CORNER_SPACE, LG_KNOB_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 intersection {
  box {
   <LG_BRICK_WIDTH/6+LG_E, -0.5*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
   <-LG_BRICK_WIDTH/6-LG_E, -2.5*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>
  }
  merge {
   #declare GRID = -2;
   #while (GRID < 0)
    #declare MIR = -45;
    #while (MIR < 90)
     merge {
      cylinder {
       <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, LG_GRID_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH*sqrt(2)>,
       <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, LG_GRID_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH*sqrt(2)>,
       LG_CORNER_SPACE
      }
      cylinder {
       <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -LG_GRID_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH*sqrt(2)>,
       <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -LG_GRID_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH*sqrt(2)>,
       LG_CORNER_SPACE
      }
      cylinder {
       <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, LG_GRID_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH*sqrt(2)>,
       <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, LG_GRID_WIDTH/2-LG_CORNER_SPACE, -LG_BRICK_WIDTH*sqrt(2)>,
       LG_CORNER_SPACE
      }
      cylinder {
       <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -LG_GRID_WIDTH/2+LG_CORNER_SPACE, LG_BRICK_WIDTH*sqrt(2)>,
       <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -LG_GRID_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH*sqrt(2)>,
       LG_CORNER_SPACE
      }
      box {
       <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, LG_GRID_WIDTH/2, LG_BRICK_WIDTH*sqrt(2)>,
       <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -LG_GRID_WIDTH/2, -LG_BRICK_WIDTH*sqrt(2)>
      }
      box {
       <LG_BRICK_WIDTH/6, LG_GRID_WIDTH/2-LG_CORNER_SPACE, LG_BRICK_WIDTH*sqrt(2)>,
       <-LG_BRICK_WIDTH/6, -LG_GRID_WIDTH/2+LG_CORNER_SPACE, -LG_BRICK_WIDTH*sqrt(2)>
      }
      rotate <MIR, 0, 0>
      translate <0, GRID*LG_BRICK_WIDTH, -LG_BRICK_WIDTH>
     } 
     #declare MIR = MIR + 90;
    #end
    #declare GRID = GRID + 1;
   #end
  }
 }
 torus {
  LG_BRICK_WIDTH/2-LG_CORNER_SPACE,
  LG_CORNER_SPACE
  rotate <90, 0, 0>
  translate <0, 0, -LG_CORNER_SPACE>
 }
 torus {
  LG_BRICK_WIDTH/2-LG_CORNER_SPACE,
  LG_CORNER_SPACE
  rotate <90, 0, 0>
  translate <0, 0, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>
 }
 difference {
  merge {
   cylinder {
    <0, 0, -LG_CORNER_SPACE>,
    <0, 0, -5*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_BRICK_WIDTH/2
   }
   cylinder {
    <0, 0, 0>,
    <0, 0, -5*LG_PLATE_HEIGHT>,
    LG_BRICK_WIDTH/2-LG_CORNER_SPACE
   }
  }
  cylinder {
   <0, 0, -LG_TOP_HEIGHT>,
   <0, 0, -5*LG_PLATE_HEIGHT-LG_E>,
   LG_KNOB_RADIUS
  }
 }
 object {
  lg_knob_clear
 }
 rotate <0, 0, -90>
}

#end
