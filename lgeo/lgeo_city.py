'''****************************************************************************
 Persistence of Vision Ray Tracer Scene Description File
 File: main.pov
 Vers: 3.6
 Desc: Main file for testing scenes
 Link:
 Date: 04/2013
 Auth: Chocokiko
*****************************************************************************'''


'''
//Only load once
#ifdef(main)
    //already loaded
#else
#declare main = 1;

/*******************************************************************************
Includes
*******************************************************************************/
'''

import sys
from logging import *

# ==== Standard POV-Ray Includes ====
from pov.include.colors_inc import *

'''
#include "colors.inc"     // Standard Color definitions
// #include "textures.inc"   // Standard Texture definitions
// #include "functions.inc"  // internal functions usable in user defined functions

// ==== Additional Includes ====
// Don't have all of the following included at once, it'll cost memory and time
// to parse!
// --- general include files ---
// #include "arrays.inc"     // macros for manipulating arrays
// #include "chars.inc"      // A complete library of character objects, by Ken Maeno
// #include "consts.inc"     // Various constants and alias definitions
// #include "debug.inc"      // contains various macros for debugging scene files
// #include "logo.inc"       // The official POV-Ray Logo in various forms
// #include "math.inc"       // general math functions and macros
// #include "rad_def.inc"    // Some common radiosity settings
// #include "rand.inc"       // macros for generating random numbers
// #include "shapes.inc"     // macros for generating various shapes
// #include "shapes2.inc"    // some not built in basic shapes
// #include "shapesq.inc"    // Pre-defined quartic shapes
// #include "skies.inc"      // Ready defined sky spheres
// #include "strings.inc"    // macros for generating and manipulating text strings
// #include "sunpos.inc"     // macro for sun position on a given date, time, and location on earth
// #include "transforms.inc" // transformation macros

// --- textures ---
// #include "finish.inc"     // Some basic finishes
// #include "glass.inc"      // Glass textures/interiors
// #include "golds.inc"      // Gold textures
// #include "metals.inc"     // Metallic pigments, finishes, and textures
// #include "stones.inc"     // Binding include-file for STONES1 and STONES2
// #include "stones1.inc"    // Great stone-textures created by Mike Miller
// #include "stones2.inc"    // More, done by Dan Farmer and Paul Novak
// #include "woodmaps.inc"   // Basic wooden colormaps
// #include "woods.inc"      // Great wooden textures created by Dan Farmer and Paul Novak
'''

# ==== LGEO Colors and Definitions ====
#include "lg_color.inc"
#include "lg_defs.inc"

# ==== LGEO fixed parts ====

# ==== LGEO parts ====

# ==== Object includes ====
#include "10036-1_car.pov"
#include "10036-1_house.pov"
#include "10036-1_main.pov"


fix = SceneFile('test.pov')
fix.append(Version(3.6))


'''
/*******************************************************************************
Settings --> After Includes to overwrite presets
*******************************************************************************/

global_settings {
  assumed_gamma 1.5
  ambient_light rgb <1, 1, 1>
}

// LGEO Settings
#declare lg_quality = 4;

// L3P Settings
#declare L3Version = 1.4;
#declare L3Quality = 4;  // Quality level, 0=BBox, 1=no refr, 2=normal, 3=studlogo, 4=stud2logo
#declare L3SW = 0.5;  // Width of seam between two bricks
#declare L3Studs = 1;  // 1=on 0=off
#declare L3Bumps = 0;  // 1=on 0=off

#declare L3Ambient = 0.4;
#declare L3Diffuse = 0.4;
#declare L3Ior     = 1.25;
#declare L3NormalBumps = normal { bumps 0.01 scale 20 }
#declare L3NormalSlope = normal { bumps 0.3 scale 0.5 }

#declare L3SWT = (L3SW ? L3SW : 0.001);  // At least a small seam when transparent


/*******************************************************************************
Camera
*******************************************************************************/

camera {
  location  <5, 12, 12>
  direction 1.5*z
  right     x*image_width/image_height
  look_at   <0.0, 5.0,  0.0>
}

/*******************************************************************************
Background
*******************************************************************************/

sky_sphere {
  pigment {
    gradient y
    color_map {
      [0.0 rgb <0.6,0.7,1.0>]
      [0.7 rgb <0.0,0.1,0.8>]
    }
  }
}

/*******************************************************************************
Light
*******************************************************************************/

//light_source {
//  <0, 0, 0>            // light's position (translated below)
//  color rgb <1, 1, 1>  // light's color
//  translate <-3000, 3000, -3000>
//}

light_source {
  <0, 0, 0>            // light's position (translated below)
  color rgb <1, 1, 1>  // light's color
  translate <300, 300, 300>
}


/*******************************************************************************
Ground plane
*******************************************************************************/
plane {
  y, -0.01
  pigment { color rgb <0.7,0.5,0.3> }
}

/*******************************************************************************
Objects
*******************************************************************************/
// Pizza to go / Car
/*
object {set_10036_1_car_nonmoving}
object {set_10036_1_car_steering_wheel}
object {set_10036_1_car_schutter_l}
object {set_10036_1_car_schutter_r}
object {set_10036_1_car_sunroof}
object {set_10036_1_car_sunroof_glass}
object {set_10036_1_car_wheel_fr}
object {set_10036_1_car_wheel_fl}
object {set_10036_1_car_wheel_rr}
object {set_10036_1_car_wheel_rl}
*/

/*
object {set_10036_1_house_base}
object {set_10036_1_house_nonmoving}
object {set_10036_1_house_oven_door}
*/

#end
'''


# print everything to stdout for now
print str(fix)




