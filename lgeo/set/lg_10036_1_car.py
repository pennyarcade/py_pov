# coding=UTF-8
"""
Persistence of Vision Ray Tracer Scene Description File.

File: 10036-1_car.pov
Vers: 3.6
Desc: Lego Set "Pizza To Go" Subpart: car
Link: www.peeron.com/inv/sets/10036-1
Date: 04/2013
Auth: Chocokiko

Parts List
----------

2348b TrBlue  Glass for Hinge Car Roof 4 x 4 Sunroof with Ridges
2349    White   Hinge Car Roof 4 x 4 Sunroof
2357    White   Brick 2 x 2 Corner
2412b   Red     Tile 1 x 2 Grille with Groove
2412b   White   Tile 1 x 2 Grille with Groove
2436    White   Bracket 1 x 2 - 1 x 4
2441    Red Car Base 7 x 4 x 2/3
3003    Yellow  Brick 2 x 2
3004    White   Brick 1 x 2
3010    White   Brick 1 x 4
3020    White   Plate 2 x 4
3021    Red     Plate 2 x 3
3022    White   Plate 2 x 2
3024    White   Plate 1 x 1
3069b   Black   Tile 1 x 2 with Groove
3641    Black   Tyre
3710    White   Plate 1 x 4
3788    White   Car Mudguard 2 x 4
3823    TrLtBlu Windscreen 2 x 4 x 2
3829c01 OldGray Car Steering Stand and Wheel (Complete)
3853    White   Window 1 x 4 x 3
3856    White   Window 1 x 2 x 3 Shutter
4073    TrYello Plate 1 x 1 Round 1 Extra
4085c   White   Plate 1 x 1 with Clip Vertical - Type 3
4624    White   Wheel Centre Small
4625    White   Hinge Tile 1 x 4
4865    Black   Panel 1 x 2 x 1
821407  White   Sticker Sheet Town Pizzeria Pizza Logos


LGEO Disclaimer
Well, it is possible but not recommended. LGEO uses a different coordinate
system and scaling than LDRAW, so it may be pretty hard to build a model by
placing the parts by hand. In LGEO, for historic reasons Y axis is the depth
axis, and Z is the up axis, where also Z has switched sign to LDRAW Y axis.
Sorry for that, but my understanding of coordinate to this time was a flat
standard XY coordinate system with a third Z axis coming out of the plane.
Scaling is to real measurements, where 1 POV-Ray unit is 10mm. So 0.8 is 20
LDU (width of a LEGO brick) and 0.96 is 24 LDU (height of a LEGO brick).
"""

# Only load once
# ifndef(set_10036_1_car)
# declare set_10036_1_car = 1;

# ---
# Includes
# ---
# ==== Py Pov Includes ====
from pov.csg.Union import Union
from pov.other.Comment import Comment

# ==== Standard POV-Ray Includes ====
# include "colors.inc"     # Standard Color definitions

# #include "textures.inc"   # Standard Texture definitions
# #include "functions.inc"  # internal func. usable in user defined functions

# ==== Additional Includes ====
# Don't have all of the following included at once, it'll cost memory and time
# to parse!
# --- general include files ---
# #include "arrays.inc"     # macros for manipulating arrays
# #include "chars.inc"      # A library of character objects, by Ken Maeno
# #include "consts.inc"     # Various constants and alias definitions
# #include "debug.inc"      # contains various macros for debugging scene files
# #include "logo.inc"       # The official POV-Ray Logo in various forms
# #include "math.inc"       # general math functions and macros
# #include "rad_def.inc"    # Some common radiosity settings
# #include "rand.inc"       # macros for generating random numbers
# #include "shapes.inc"     # macros for generating various shapes
# #include "shapes2.inc"    # some not built in basic shapes
# #include "shapesq.inc"    # Pre-defined quartic shapes
# #include "skies.inc"      # Ready defined sky spheres
# #include "strings.inc"    # macros for generating and manipulating text
# #include "sunpos.inc"     # macro for sun position on a given date,
# time, and location on earth
# #include "transforms.inc" # transformation macros

# --- textures ---
# #include "finish.inc"     # Some basic finishes
# #include "glass.inc"      # Glass textures/interiors
# #include "golds.inc"      # Gold textures
# #include "metals.inc"     # Metallic pigments, finishes, and textures
# #include "stones.inc"     # Binding include-file for STONES1 and STONES2
# #include "stones1.inc"    # Great stone-textures created by Mike Miller
# #include "stones2.inc"    # More, done by Dan Farmer and Paul Novak
# #include "woodmaps.inc"   # Basic wooden colormaps
# #include "woods.inc"      # Great wooden textures created by
# Dan Farmer and Paul Novak


# ==== LGEO Colors and Definitions ====
from lgeo.include.common.lg_color import LG_RED, LG_WHITE, LG_YELLOW
from lgeo.include.common.lg_defs import LGPH, LGBW

# ==== LGEO fixed parts ====

# ==== LGEO parts ====
# include "lg_2348b.inc"
# include "lg_2349.inc"
# include "lg_2357.inc"
from lgeo.include.brick import lg_2412b
# include "lg_2436.inc"
from lgeo.include.brick import lg_2441
from lgeo.include.brick import lg_3003
# include "lg_3004.inc"
from lgeo.include.brick import lg_3010
# include "lg_3020.inc"
from lgeo.include.brick import lg_3021
from lgeo.include.brick import lg_3022
from lgeo.include.brick import lg_3024
# include "lg_3069b.inc"
# include "lg_3641.inc"
from lgeo.include.brick import lg_3788
# include "lg_3823.inc"
# include "lg_3829c01.inc"
# include "lg_3853.inc"
# include "lg_3856.inc"
# include "lg_4073.inc"
from lgeo.include.brick import lg_4085c
# include "lg_4624.inc"
# include "lg_4625.inc"
# include "lg_4865.inc"
# # 821407 Missing

# ==== Custom Includes ====
from lgeo.include.common.custom_macros import std_brick


# declare set_10036_1_car_nonmoving= union {
def nonmoving(ox=0, oy=0, oz=0, rx=0, ry=0, rz=0):
    """
    docstring for lg_10036_car.

    # Offset X
    #self.ox = ox
    # Offset Y
    #self.oy = oy
    # Offset Z
    #self.oz = oz
    # Rotation X
    #self.rx = rx
    # Rotation Y
    #self.ry = ry
    # Rotation Z
    #self.rz = rz
    """
    part = Union(
        Comment("""
        # *******************************************************************
        # Objects (Step 1)
        # *******************************************************************
        """),
        Comment('**** Start 2441 Red Car Base 7 x 4 x 2/3 ****'),
        std_brick(
            lg_2441.solid(),
            LG_RED,
            0, 3 * LGPH, 0,
            -90, 0, 0),
        Comment('**** End 2441 Red Car Base 7 x 4 x 2/3 ****'),
        Comment("""
        # *******************************************************************
        # Objects (Step 2)
        # *******************************************************************
        """),
        Comment('**** Start 3022 White Plate 2 x 2 ****'),
        std_brick(
            lg_3022.solid(),
            LG_WHITE,
            2.5 * LGBW, 4 * LGPH, 0,
            -90, 0, 0
        ),
        Comment('**** End 3022 White Plate 2 x 2 ****'),
        Comment('**** Start 2412b White Tile 1 x 2 Grille with Groove ****'),
        std_brick(
            lg_2412b.solid(),
            LG_WHITE,
            0.5 * LGBW, 3 * LGPH, -1.5 * LGBW,
            -90, 90, 0
        ),
        Comment('**** End 2412b White Tile 1 x 2 Grille with Groove ****'),
        Comment('**** Start 2412b White Tile 1 x 2 Grille with Groove ****'),
        std_brick(
            lg_2412b.solid(),
            LG_WHITE,
            0.5 * LGBW, 3 * LGPH, 1.5 * LGBW,
            -90, 90, 0
        ),
        Comment('**** End 2412b White Tile 1 x 2 Grille with Groove ****'),
        Comment("""
        ********************************************************************
        * Objects (Step 3)
        ********************************************************************
        """),
        Comment('**** Start 3022 White Plate 2 x 2 ****'),
        std_brick(
            lg_3022.solid(),
            LG_WHITE,
            -2.5 * LGBW, 4 * LGPH, 0,
            -90, 0, 0
        ),
        Comment('**** End 3022 White Plate 2 x 2 ****'),
        Comment('**** Start 3010 White Brick 1 x 4 ****'),
        std_brick(
            lg_3010.solid(),
            LG_WHITE,
            -1 * LGBW, 5 * LGPH, 0,
            -90, 0, 0
        ),
        Comment('**** End 3010 White Brick 1 x 4 ****'),
        Comment("""
        ********************************************************************
        * Objects (Step 4)
        ********************************************************************
        """),
        Comment('**** Start 3003 Yellow Brick 2 x 2 ****'),
        std_brick(
            lg_3003.solid(),
            LG_YELLOW,
            0.5 * LGBW, 5 * LGPH, 0,
            -90, 0, 0
        ),
        Comment('**** End 3003 Yellow Brick 2 x 2 ****'),
        Comment('**** 3788    White   Car Mudguard 2 x 4 ****'),
        std_brick(
            lg_3788.solid(),
            LG_WHITE,
            2.5 * LGBW, 6 * LGPH, 0,
            -90, 0, 0
        ),
        Comment('**** 3788    White   Car Mudguard 2 x 4 ****'),
        Comment("""
        ********************************************************************
        * Objects (Step 5)
        ********************************************************************
        """),
        Comment('**** 3788    White   Car Mudguard 2 x 4 ****'),
        std_brick(
            lg_3788.solid(),
            LG_WHITE,
            -2.5 * LGBW, 6 * LGPH, 0,
            -90, 0, 0
        ),
        Comment('**** 3788    White   Car Mudguard 2 x 4 ****'),
        Comment('**** 3021  Red   Plate 2 x 3 ****'),
        std_brick(
            lg_3021.solid(),
            LG_RED,
            -1.5 * LGBW, 6 * LGPH, 0,
            -90, 0, 0
        ),
        Comment('**** 3021 Red Plate 2 x 3 ****'),
        Comment('**** 3024 White Plate 1 x 1 ****'),
        std_brick(
            lg_3024.solid(),
            LG_WHITE,
            -1.5 * LGBW, 6 * LGPH, -2 * LGBW,
            -90, 0, 0
        ),
        Comment('**** 3024 White Plate 1 x 1 ****'),
        Comment(
            '**** 4085c White Plate 1 x 1 with Clip Vertical - Type 3 ****'
        ),
        std_brick(
            lg_4085c.solid(),
            LG_WHITE,
            -1 * LGBW, 6 * LGPH, 1.5 * LGBW,
            -90, 0, 0
        ),
        Comment(
            '**** 4085c White Plate 1 x 1 with Clip Vertical - Type 3 ****'
        ),
        Comment("""
        ********************************************************************
        * Objects (Step 6)
        ********************************************************************
        """),


    )

    return part

#        Comment('****  ****'),
#        std_brick(
#
#        ),
#        Comment('****  ****'),

# 2436  White Bracket 1 x 2 - 1 x 4
# std_brick(lg_2436 ,  lg_white,  3*LGBW, 6*LGPH,  0*LGBW,  -90, 0, 0)
# 3020  White Plate 2 x 4
# std_brick(lg_3020 ,  lg_white, -1.5*LGBW, 7*LGPH,  0*LGBW,  -90, 0, 0)

# Objects (Step 7)

# 4073  TrYello Plate 1 x 1 Round
# std_brick(lg_4073 , lg_clear_yellow, 4.1*LGBW, 5*LGPH, -1.5*LGBW, 0, 90, 0)
# std_brick(lg_4073 , lg_clear_yellow, 4.1*LGBW, 5*LGPH,  1.5*LGBW, 0, 90, 0)
# 2412b Red   Tile 1 x 2 Grille with Groove
# std_brick(lg_2412b, lg_red ,  4.0*LGBW, 4.7*LGPH, 0*LGBW, -90, 0,  -90)
# 3069b Black Tile 1 x 2 with Groove
# std_brick(lg_3069b, lg_black ,   -2*LGBW, 8*LGPH, 0*LGBW, -90,  180, 0)
# 4865  Black Panel 1 x 2 x 1
# std_brick(lg_4865 ,  lg_black,   -1*LGBW,  10*LGPH, 0*LGBW, -90,  180, 0)

# Objects (Step 8)


# # 3004  White Brick 1 x 2
# std_brick(lg_3004 ,  lg_white, -1.5*LGBW,  10*LGPH, -1.5*LGBW,  -90,  90, 0)
# std_brick(lg_3004 ,  lg_white, -1.5*LGBW,  10*LGPH,  1.5*LGBW,  -90,  90, 0)


# Objects (Step 9)

# # 3020  White Plate 2 x 4
# std_brick(lg_3020 ,  lg_white, -1.5*LGBW,  11*LGPH,  0*LGBW,  -90, 0, 0)
# # 2357  White Brick 2 x 2 Corner
# std_brick(lg_2357 ,  lg_white,  3*LGBW, 9*LGPH, -1.5*LGBW,  -90, 0, 0)
# std_brick(lg_2357 ,  lg_white,  3*LGBW, 9*LGPH,  1.5*LGBW,  -90, -90, 0)

# Objects (Step 10)


# # 3069b Black Tile 1 x 2 with Groove
# std_brick(lg_3069b,  lg_black,  -2*LGBW,  12*LGPH,  0*LGBW,  -90, 180, 0)
# # 4865  Black Panel 1 x 2 x 1
# std_brick(lg_4865 ,  lg_black,  -1*LGBW,  14*LGPH,  0*LGBW,  -90, 180, 0)
# # 3823  TrLtBlu Windscreen 2 x 4 x 2
# std_brick(lg_3823, lg_clear_cyan,  2*LGBW,  15*LGPH,  0*LGBW,  -90, 0, 0)


# Objects (Step 11)

# # 3853  White Window 1 x 4 x 3
# std_brick(lg_3853, lg_white,  -3*LGBW,  15*LGPH,  0*LGBW,  -90,  180, 0)
# # 3004  White Brick 1 x 2
# std_brick(lg_3004, lg_white,  -1.5*LGBW,  14*LGPH, -1.5*LGBW,  -90,  90,  0)
# std_brick(lg_3004, lg_white,  -1.5*LGBW,  14*LGPH,  1.5*LGBW,  -90,  90,  0)
# # 3010  White Plate 1 x 4
# std_brick(lg_3010, lg_white,  -2*LGBW,  15*LGPH,  0*LGBW,  -90, 0,  0)


# Objects (Step 12)

# # 4625  White Hinge Tile 1 x 4
# std_brick(lg_4625, lg_white,  -1*LGBW,  15*LGPH,  0*LGBW,  -90, 0, 0)


# Objects (Step 13)

# # 3020  White Plate 2 x 4
# std_brick(lg_3020, lg_white,  -2.5*LGBW,  16*LGPH,  0*LGBW,  -90, 0, 0)
# # 4865  Black Panel 1 x 2 x 1
# std_brick(lg_4865, lg_white,   2*LGBW,  19*LGPH,  0*LGBW,  -90, 180, 0)
# # TODO: Add Pizza design...

#  split_union on
# }

# 3829c01 OldGray Car Steering Stand and Wheel (Complete)
# declare set_10036_1_car_steering_wheel_ox= 2*LGBW;
# declare set_10036_1_car_steering_wheel_oy= 6*LGPH;
# declare set_10036_1_car_steering_wheel_oz= 0;
# declare set_10036_1_car_steering_wheel =
# std_brick(lg_3829c01, lg_grey,  2*LGBW, 6*LGPH,  0*LGBW,  -90, 0,  0)

# # 3856  White Window 1 x 2 x 3 Shutter
# # declare set_10036_1_car_schutter_l=
# std_brick(lg_3856, lg_white, -3.65*LGBW,  15*LGPH, -2*LGBW,  -90, -90, 0)
# # declare set_10036_1_car_schutter_l_ox= -3.65*LGBW;
# # declare set_10036_1_car_schutter_l_oy= 15*LGPH;
# #
# # declare set_10036_1_car_schutter_l_oz= -2*LGBW;

# # declare set_10036_1_car_schutter_r=
# std_brick(lg_3856, lg_white, -3.65*LGBW,  15*LGPH,  2*LGBW,  -90,  90, 0)
# #declare set_10036_1_car_schutter_r_ox= -3.65*LGBW;
# #declare set_10036_1_car_schutter_r_oy= 15*LGPH;
# #declare set_10036_1_car_schutter_r_oz= 2*LGBW;

# # 2349  White Hinge Car Roof 4 x 4 Sunroof
# #declare set_10036_1_car_sunroof=
# std_brick(lg_2349, lg_white, 0.5*LGBW,  16*LGPH,  0*LGBW,  -90, 0, 0)
# #declare set_10036_1_car_sunroof_ox= 0.5*LGBW;
# #declare set_10036_1_car_sunroof_oy= 16*LGPH;
# #declare set_10036_1_car_sunroof_oz= 0;

# # 2348b TrBlue  Glass for Hinge Car Roof 4 x 4 Sunroof with Ridges
# #declare set_10036_1_car_sunroof_glass=
# std_brick(lg_2348b, lg_clear_cyan, 1.35*LGBW,15.5*LGPH, 0*LGBW,  -90, 0, 0)
# #declare set_10036_1_car_sunroof_glass_ox= 1.35*LGBW;
# #declare set_10036_1_car_sunroof_glass_oy= 15.5*LGPH;
# #declare set_10036_1_car_sunroof_glass_oz= 0;

# //4624  White Wheel Centre Small
# //3641  Black Tyre
# #declare set_10036_1_car_wheel_fr=
#   union {
#   UnchangedBrick(lg_4624, lg_white)
#   UnchangedBrick(lg_3641, lg_black)

#   rotate <-90, 90, 0>
#   translate <-2.5*LGBW, 2.5*LGPH, -2*LGBW>
#   }
# #declare set_10036_1_car_wheel_fr_ox= -2.5*LGBW;
# #declare set_10036_1_car_wheel_fr_oy=  2.5*LGPH;
# #declare set_10036_1_car_wheel_fr_ox= -2*LGBW;

# #declare set_10036_1_car_wheel_fl=
#   union {
#   UnchangedBrick(lg_4624, lg_white)
#   UnchangedBrick(lg_3641, lg_black)

#   rotate <-90, 90, 0>
#   translate <2.5*LGBW, 2.5*LGPH, -2*LGBW>
#   }
# #declare set_10036_1_car_wheel_fl_ox=  2.5*LGBW;
# #declare set_10036_1_car_wheel_fl_oy=  2.5*LGPH;
# #declare set_10036_1_car_wheel_fl_ox= -2*LGBW;

# #declare set_10036_1_car_wheel_rl =
#   union {
#   UnchangedBrick(lg_4624, lg_white)
#   UnchangedBrick(lg_3641, lg_black)

#   rotate <-90, -90, 0>
#   translate <-2.5*LGBW, 2.5*LGPH, 2*LGBW>
#   }
# #declare set_10036_1_car_wheel_rl_ox= -2.5*LGBW;
# #declare set_10036_1_car_wheel_rl_oy=  2.5*LGPH;
# #declare set_10036_1_car_wheel_rl_ox=  2*LGBW;


# #declare set_10036_1_car_wheel_rr=
#   union {
#   UnchangedBrick(lg_4624, lg_white)
#   UnchangedBrick(lg_3641, lg_black)

#   rotate <-90, -90, 0>
#   translate <2.5*LGBW, 2.5*LGPH, 2*LGBW>
#   }
# #declare set_10036_1_car_wheel_rr_ox=  2.5*LGBW;
# #declare set_10036_1_car_wheel_rr_oy=  2.5*LGPH;
# #declare set_10036_1_car_wheel_rr_ox=  2*LGBW;

# #end
