/*******************************************************************************/
/*                                                                             */
/* LGEO Libray Include File     (C) Chaot!X@weird.cologne.de (Lutz Uhlmann)    */
/*                                                                             */
/* 19971011 Lutz Uhlmann                                                       */
/* 20050118 Lars C. Hassing   Fixed identifier in ifdef                        */
/*                                                                             */
/* This file is in no way related to the LEGO(tm) Group.                       */
/* It is provided for private non-commercial use only.                         */
/*                                                                             */
/* lp_0001: Red Stripes Pattern for lg_3297                                    */
/*                                                                             */ 
/*******************************************************************************/
#ifdef(lg_3297p01)
#else
#declare lg_angle1=65.32484819
#declare lg_3297p01 =
union {
 box {
  <LG_CORNER_SPACE+0.001, 0.99, -0.04>,
  <LG_CORNER_SPACE-0.001, 1.41, -2*LG_BRICK_WIDTH/sin(pi*lg_angle1/180)+0.04>
 }
 box {
  <LG_CORNER_SPACE+0.001, 0.19, -0.04>,
  <LG_CORNER_SPACE-0.001, 0.61, -2*LG_BRICK_WIDTH/sin(pi*lg_angle1/180)+0.04>
 }
 box {
  <LG_CORNER_SPACE+0.001, -0.19, -0.04>,
  <LG_CORNER_SPACE-0.001, -0.61, -2*LG_BRICK_WIDTH/sin(pi*lg_angle1/180)+0.04>
 }
 box {
  <LG_CORNER_SPACE+0.001, -0.99, -0.04>,
  <LG_CORNER_SPACE-0.001, -1.41, -2*LG_BRICK_WIDTH/sin(pi*lg_angle1/180)+0.04>
 }
 rotate <0, -lg_angle1, 0>
 translate <LG_BRICK_WIDTH/2-LG_CORNER_SPACE, 0, -LG_CORNER_SPACE>
 texture { lg_red normal { bumps 0.3 scale 0.02 } }
}

#end
