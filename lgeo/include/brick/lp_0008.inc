/*******************************************************************************/
/*                                                                             */
/* LGEO Libray Include File     (C) Chaot!X@weird.cologne.de (Lutz Uhlmann)    */
/*                                                                             */
/* 19980725 Lutz Uhlmann                                                       */
/* 20020114 Lars C. Hassing   Added missing texture                            */
/*                                                                             */
/* This file is in no way related to the LEGO(tm) Group.                       */
/* It is provided for private non-commercial use only.                         */
/*                                                                             */
/* lp_0008: Classic Smiley Grin Pattern for lg_3626                            */
/*                                                                             */ 
/*******************************************************************************/
#ifdef(lg_3626p01)
#else
#declare lg_angle=atan2(2.25*LG_PLATE_HEIGHT, 6*LG_BRICK_WIDTH-2*LG_CORNER_SPACE)
#declare lg_3626p01 =
intersection {
 union {
  cylinder {
   <0.3, 0, -0.42>,
   <0.6, 0, -0.42>,
   0.06
   rotate <0, 0, 17>
  }
  cylinder {
   <0.3, 0, -0.42>,
   <0.6, 0, -0.42>,
   0.06
   rotate <0, 0, -17>
  }
  difference {
   cylinder {
    <0, 0, -0.25>,
    <0.6, 0, -0.25>,
    0.45
   }
   union {
    cylinder {
     <0, 0, -0.25>,
     <0.6, 0, -0.25>,
     0.39
    }
    box {
     <0, 0, 0.6>,
     <0.6, 0.6, -0.6>
     rotate <20, 0, 0>
     translate <0, 0, -0.25>
    }
    box {
     <0, 0, 0.6>,
     <0.6, -0.6, -0.6>
     rotate <-20, 0, 0>
     translate <0, 0, -0.25>
    }
   }
  }
  cylinder {
   <0, 0, -0.42>,
   <0.6, 0, -0.42>,
   0.03
   rotate <20, 0, 0>
   translate <0, 0, -0.25>
  }
  cylinder {
   <0, 0, -0.42>,
   <0.6, 0, -0.42>,
   0.03
   rotate <-20, 0, 0>
   translate <0, 0, -0.25>
  }
 }
 difference {
  cylinder {
   <0, 0, 0>,
   <0, 0, -LG_BRICK_HEIGHT>,
   0.51+0.001
  }
  cylinder {
   <0, 0, 0.01>,
   <0, 0, -LG_BRICK_HEIGHT-0.01>,
   0.51-0.001
  }
 }
 texture { lg_black }
}

#end
