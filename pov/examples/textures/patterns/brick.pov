// Persistence Of Vision raytracer version 3.5 sample file.
// Brick pattern example
//
// -w320 -h240
// -w800 -h600 +a0.3

global_settings { assumed_gamma 2.2 }

#include "colors.inc"

#declare T1=
 texture{
   pigment{
     brick
     scale 0.1
   }
 }

#declare T2=
 texture{
   pigment{White}
   normal{
     brick 0.6
     scale 0.1
   }
   finish{phong 0.8 phong_size 200}
 }

#include "pignorm.inc"
