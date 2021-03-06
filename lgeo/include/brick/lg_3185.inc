/*******************************************************************************/
/*                                                                             */
/* LGEO Libray Include File     (C) Chaot!X@weird.cologne.de (Lutz Uhlmann)    */
/*                                                                             */
/* 19970927 Lutz Uhlmann                                                       */
/* 20041126 Lars C. Hassing   Corrected name of clear part                     */
/*                                                                             */
/* This file is in no way related to the LEGO(tm) Group.                       */
/* It is provided for private non-commercial use only.                         */
/*                                                                             */
/* lg_3185: Fence 1 x 4 x 2                                                    */
/*                                                                             */ 
/*******************************************************************************/
#ifdef(lg_3185)
#else
#declare lg_3185 =
union {
 #declare MIR = 0
 #while (MIR < 2)
  union {
   sphere {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   box {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_BRICK_HEIGHT>,
    <LG_BRICK_WIDTH/2-LG_WALL_WIDTH, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>
   }
   box {
    <LG_BRICK_WIDTH/2, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_WALL_WIDTH, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   #if (MIR = 1)
    matrix <-1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0>
   #end
  }
  #declare MIR = MIR + 1
 #end
 cylinder {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 object {
  lg_plate_column
  translate <0, -LG_BRICK_WIDTH, -2*LG_BRICK_HEIGHT>
 }
 object {
  lg_plate_column
  translate <0, 0, -2*LG_BRICK_HEIGHT>
 }
 object {
  lg_plate_column
  translate <0, LG_BRICK_WIDTH, -2*LG_BRICK_HEIGHT>
 }
 box {
  <LG_BRICK_WIDTH/6, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH>
 }
 box {
  <LG_BRICK_WIDTH/6, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE-LG_E>
 }
 box {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_TOP_HEIGHT>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE-LG_E>
 }
 box {
  <LG_BRICK_WIDTH/6, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE-LG_E>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE-LG_E>
 }
 box {
  <LG_BRICK_WIDTH/6, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE-LG_E>
 }
 box {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE+LG_E>
 }
 box {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE+LG_E>
 }
 intersection {
  box {
   <LG_BRICK_WIDTH/6+LG_E, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
   <-LG_BRICK_WIDTH/6-LG_E, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>
  }
  union {
   #declare GRID = -1.5
   #while (GRID < 2)
    #declare MIR = -45
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
     #declare MIR = MIR + 90
    #end
    #declare GRID = GRID + 1
   #end
  }
 }
}

#declare lg_3185_clear =
merge {
 #declare MIR = 0
 #while (MIR < 2)
  merge {
   sphere {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   sphere {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   cylinder {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
    LG_CORNER_SPACE
   }
   box {
    <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -2*LG_BRICK_HEIGHT>,
    <LG_BRICK_WIDTH/2-LG_WALL_WIDTH, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_BRICK_HEIGHT+LG_CORNER_SPACE+LG_E>
   }
   box {
    <LG_BRICK_WIDTH/2, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
    <LG_BRICK_WIDTH/2-LG_WALL_WIDTH, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -2*LG_BRICK_HEIGHT+LG_CORNER_SPACE>
   }
   #if (MIR = 1)
    matrix <-1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0>
   #end
  }
  #declare MIR = MIR + 1
 #end
 cylinder {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 cylinder {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  LG_CORNER_SPACE
 }
 object {
  lg_plate_column_clear
  translate <0, -LG_BRICK_WIDTH, -2*LG_BRICK_HEIGHT>
 }
 object {
  lg_plate_column_clear
  translate <0, 0, -2*LG_BRICK_HEIGHT>
 }
 object {
  lg_plate_column_clear
  translate <0, LG_BRICK_WIDTH, -2*LG_BRICK_HEIGHT>
 }
 box {
  <LG_BRICK_WIDTH/6, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, 0>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH>
 }
 box {
  <LG_BRICK_WIDTH/6, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE-LG_E>
 }
 box {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_TOP_HEIGHT>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE-LG_E>
 }
 box {
  <LG_BRICK_WIDTH/6, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE-LG_E>
 }
 box {
  <LG_BRICK_WIDTH/6-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE-LG_E>
 }
 box {
  <LG_BRICK_WIDTH/6, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/6, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE-LG_E>
 }
 box {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE+LG_E>
 }
 box {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH, -5*LG_PLATE_HEIGHT-LG_CORNER_SPACE>
 }
 box {
  <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_CORNER_SPACE, -6*LG_PLATE_HEIGHT>,
  <-LG_BRICK_WIDTH/2+LG_CORNER_SPACE, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH, -6*LG_PLATE_HEIGHT+LG_CORNER_SPACE+LG_E>
 }
 intersection {
  box {
   <LG_BRICK_WIDTH/6+LG_E, 2*LG_BRICK_WIDTH-LG_WALL_WIDTH+LG_CORNER_SPACE, -LG_WALL_WIDTH+LG_CORNER_SPACE>,
   <-LG_BRICK_WIDTH/6-LG_E, -2*LG_BRICK_WIDTH+LG_WALL_WIDTH-LG_CORNER_SPACE, -5*LG_PLATE_HEIGHT+LG_WALL_WIDTH-LG_CORNER_SPACE>
  }
  merge {
   #declare GRID = -1.5
   #while (GRID < 2)
    #declare MIR = -45
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
     #declare MIR = MIR + 90
    #end
    #declare GRID = GRID + 1
   #end
  }
 }
}

#end
