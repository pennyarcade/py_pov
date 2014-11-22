# coding=UTF-8
"""***************************************************************************
    Persistence of Vision Ray Tracer Scene Description File
    File: 10036-1_car.pov
    Vers: 3.6
    Desc: Lego Set "Pizza To Go" Subpart: house
    Link: www.peeron.com/inv/sets/10036-1
    Date: 04/2013
    Auth: Chocokiko
**************************************************************************"""

'''**************************************************************************
    Parts List
    ----------

    3659    White   Arch 1 x 4 (Pic)
    3865    OldGray Baseplate 8 x 16 (Pic)
    3005    White   Brick 1 x 1 (Pic)
    4070    Black   Brick 1 x 1 with Headlight (Pic)
    3004    White   Brick 1 x 2 (Pic)
    3622    White   Brick 1 x 3 (Pic)
    3010    White   Brick 1 x 4 (Pic)
    3009    White   Brick 1 x 6 (Pic)
    3008    White   Brick 1 x 8
    3003    Yellow  Brick 2 x 2 (Pic)
    2357    White   Brick 2 x 2 Corner (Pic)
    3001    White   Brick 2 x 4 (Pic)
    4589    Black   Cone 1 x 1 (Pic)
    3192    Black   Door 1 x 3 x 3 Right
    3024    Red Plate 1 x 1 (Pic)
    4085c   Red Plate 1 x 1 with Clip Vertical - Type 3 (Pic)
    3023    Red Plate 1 x 2 (Pic)
    3023    OldGray Plate 1 x 2 (Pic)
    3623    Red Plate 1 x 3 (Pic)
    3710    White   Plate 1 x 4 (Pic)
    3460    Red Plate 1 x 8
    3022    Red Plate 2 x 2 (Pic)
    3022    White   Plate 2 x 2 (Pic)
    2420    Red Plate 2 x 2 Corner (Pic)
    3021    Red Plate 2 x 3 (Pic)
    3020    White   Plate 2 x 4 (Pic)
    3795    Red Plate 2 x 6 (Pic)
    4515    Red Slope Brick 10 6 x 8 (Pic)
    3675    Red Slope Brick 33 3 x 3 Double Convex (Pic)
    3665    White   Slope Brick 45 2 x 1 Inverted (Pic)
    3660    White   Slope Brick 45 2 x 2 Inverted (Pic)
    821407  White   Sticker Sheet Town Pizzeria Pizza Logos (Pic)   821407
    69c01   White   Tap 1 x 2 Assembly with Gray Spout (Pic)
    2412b   Red Tile 1 x 2 Grille with Groove (Pic)
    2412b   Yellow  Tile 1 x 2 Grille with Groove (Pic)
    4150p02 Yellow  Tile 2 x 2 Round with Pizza Pattern (Pic)
    3068b   Black   Tile 2 x 2 with Groove (Pic)
***************************************************************************'''


'''***************************************************************************
LGEO Disclaimer
Well, it is possible but not recommended. LGEO uses a different coordinate
system and scaling than LDRAW, so it may be pretty hard to build a model by
placing the parts by hand. In LGEO, for historic reasons Y axis is the depth
axis, and Z is the up axis, where also Z has switched sign to LDRAW Y axis.
Sorry for that, but my understanding of coordinate to this time was a flat
standard XY coordinate system with a third Z axis coming out of the plane.
Scaling is to real measurements, where 1 POV-Ray unit is 10mm. So 0.8 is 20
LDU (width of a LEGO brick) and 0.96 is 24 LDU (height of a LEGO brick).
***************************************************************************'''

# Only load once
# #ifndef(set_10036_1_car)
# #declare set_10036_1_car = 1;

'''***************************************************************************
Includes
***************************************************************************'''
# ==== Standard POV-Ray Includes ====
# include "colors.inc"      # Standard Color definitions
# #include "textures.inc"   # Standard Texture definitions
# #include "functions.inc"  
#   internal functions usable in user defined functions

# ==== Additional Includes ====
# Don't have all of the following included at once, it'll cost memory and time
# to parse!
# --- general include files ---
# #include "arrays.inc"     # macros for manipulating arrays
# #include "chars.inc"      # A complete library of character objects,
                            # by Ken Maeno
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
# #include "strings.inc"    # macros for generating and 
                            # manipulating text strings
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
# #include "woods.inc"      # Great wooden textures created 
                            # by Dan Farmer and Paul Novak

# ==== LGEO Colors and Definitions ====
# include "lg_color.inc"
# include "lg_defs.inc"

# ==== LGEO fixed parts ====

# ==== LGEO parts ====
# include "lg_3659" # White   Arch 1 x 4
# include "lg_3865" # OldGray Baseplate 8 x 16
# include "lg_3005" # White   Brick 1 x 1
# include "lg_4070" # Black   Brick 1 x 1 with Headlight
# include "lg_3004" # White   Brick 1 x 2
# include "lg_3622" # White   Brick 1 x 3
# include "lg_3010" # White   Brick 1 x 4
# include "lg_3009" # White   Brick 1 x 6
# include "lg_3008" # White   Brick 1 x 8
# include "lg_2357" # White   Brick 2 x 2 Corner
# include "lg_3001" # White   Brick 2 x 4
# include "lg_3192" # Black   Door 1 x 3 x 3 Right
# include "lg_4589" # Black   Cone 1 x 1
# include "lg_4085c"# Red     Plate 1 x 1 with Clip Vertical - Type 3
# include "lg_3023" # OldGray Plate 1 x 2
# include "lg_3623" # Red     Plate 1 x 3
# include "lg_3710" # White   Plate 1 x 4
# include "lg_3460" # Red     Plate 1 x 8
# include "lg_3022" # Red     Plate 2 x 2
# include "lg_2420" # Red     Plate 2 x 2 Corner
# include "lg_3020" # White   Plate 2 x 4
# include "lg_3795" # Red     Plate 2 x 6
# include "lg_4515" # Red     Slope Brick 10 6 x 8
# include "lg_3675" # Red     Slope Brick 33 3 x 3 Double Convex
# include "lg_3665" # White   Slope Brick 45 2 x 1 Inverted
# include "lg_3660" # White   Slope Brick 45 2 x 2 Inverted
# 821407  White   Sticker Sheet Town Pizzeria Pizza Logos MISSING
# include "lg_69c01" # White   Tap 1 x 2 Assembly with Gray Spout MISSING
# include "lg_2412b" # Yellow  Tile 1 x 2 Grille with Groove
# include "lg_3068b" # Black   Tile 2 x 2 with Groove

# ==== Custom Includes ====
# include "custom_macros.inc"

'''**************************************************************************
Objects (Step 1)
**************************************************************************'''

# 3865    OldGray Baseplate 8 x 16 (Pic)
# declare set_10036_1_house_base=
#   StdBrick(lg_3865, lg_grey, 0, 0, 0, -90, 0, 0)
# declare set_10036_1_house_base_ox= 0;
# declare set_10036_1_house_base_oy= 0;
# declare set_10036_1_house_base_oz= 0;

set_10036_1_house_nonmoving = Union (
    # 3001    White   Brick 2 x 4 (Pic)
    # StdBrick(lg_3001, lg_white, -2*LGBW, 3*LGPH, 6*LGBW, -90, 90, 0)
    # StdBrick(lg_3001, lg_white, -2*LGBW, 3*LGPH, 4*LGBW, -90, 90, 0)

    '''*******************************************************************
    Objects (Step 2)
    *******************************************************************'''
    # 3004    White   Brick 1 x 2
    # StdBrick(lg_3004, lg_white, -3*LGBW, 3*LGPH, -4.5*LGBW, -90, 90, 0)
    # StdBrick(lg_3004, lg_white,  1*LGBW, 3*LGPH, -4.5*LGBW, -90, 90, 0)
    # 3622    White   Brick 1 x 3
    # StdBrick(lg_3622, lg_white, 0.5*LGBW, 3*LGPH, 2.5*LGBW, -90, 90, 0)
    # 3009    White   Brick 1 x 6
    # StdBrick(lg_3009, lg_white, 1.5*LGBW, 3*LGPH, -1*LGBW, -90, 0, 0)
    # 3068b   Black   Tile 2 x 2 with Groove
    # StdBrick(lg_3068b, lg_black, -2*LGBW, 4*LGPH, 5*LGBW, -90, 0, 0)

    '''*******************************************************************
    Objects (Step 3)
    *******************************************************************'''
    # 3010    White   Brick 1 x 4
    # StdBrick(lg_3010, lg_white, -2*LGBW, 6*LGPH, 6.5*LGBW, -90, 90, 0)
    # StdBrick(lg_3010, lg_white, -0.5*LGBW, 6*LGPH, 4*LGBW, -90, 00, 0)
    # StdBrick(lg_3010, lg_white, 1.5*LGBW, 6*LGPH, -1*LGBW, -90, 0, 0)
    # 3004    White   Brick 1 x 2
    # StdBrick(lg_3004, lg_white, -2*LGBW, 6*LGPH, 3.5*LGBW, -90, 90, 0)
    # 2357    White   Brick 2 x 2 Corner
    # StdBrick(lg_2357, lg_white, 1.5*LGBW, 6*LGPH, 2.5*LGBW, -90, -90, 0)
    # StdBrick(lg_2357, lg_white, 1.5*LGBW, 6*LGPH, -4.5*LGBW, -90, 0, 0)
    # 3660    White   Slope Brick 45 2 x 2 Inverted
    # StdBrick(lg_3660, lg_white, -3*LGBW, 6*LGPH, -4.5*LGBW, -90, -90, 0)

    '''*******************************************************************
    Objects (Step 4)
    *******************************************************************'''
    # 3005    White   Brick 1 x 1
    # StdBrick(lg_3005, lg_white, -3.5*LGBW, 9*LGPH, 6.5*LGBW, -90, 0, 0)
    # 3022    Red     Plate 2 x 2
    # StdBrick(lg_3022, lg_red, -2*LGBW, 7*LGPH, 3*LGBW, -90, 0, 0)
    # 3023    OldGray Plate 1 x 2
    # StdBrick(lg_3023, lg_grey, -2*LGBW, 7*LGPH, 6.5*LGBW, -90, 90, 0)

    '''*******************************************************************
    Objects (Step 5)
    *******************************************************************'''
    # 3020    White   Plate 2 x 4
    # StdBrick(lg_3020, lg_white, -2*LGBW, 8*LGPH, 5*LGBW, -90, 0, 0)
    # 3795    Red     Plate 2 x 6
    # StdBrick(lg_3795, lg_red, 1*LGBW, 7*LGPH, -1*LGBW, -90, 0, 0)
    # 69c01   White   Tap 1 x 2 Assembly with Gray Spout MISSING
    # StdBrick(lg_69c01, lg_white, -3*LGBW, 5.6*LGPH, -3.5*LGBW, -90, -90, 0)

    '''*******************************************************************
    Objects (Step 6)
    *******************************************************************'''
    # 2357    White   Brick 2 x 2 Corner
    # StdBrick(lg_3004, lg_white,  1*LGBW, 9*LGPH, -4.5*LGBW, -90, -90, 0)
    # StdBrick(lg_3004, lg_white, -3*LGBW, 9*LGPH, -4.5*LGBW, -90, -90, 0)
    # 3622    White   Brick 1 x 3
    # StdBrick(lg_3622, lg_white, 0.5*LGBW, 9*LGPH, 2.5*LGBW, -90, 90, 0)
    # 3010    White   Brick 1 x 4
    # StdBrick(lg_3010, lg_white, -0.5*LGBW, 9*LGPH, 5*LGBW, -90, 0, 0)
    # 3068b   Black   Tile 2 x 2 with Groove
    # StdBrick(lg_3068b, lg_black, -2*LGBW, 9*LGPH, 5*LGBW, -90, 0, 0)
    # 3023    OldGray Plate 1 x 2
    # StdBrick(lg_3023, lg_grey, -2*LGBW, 9*LGPH, 6.5*LGBW, -90, 90, 0)
    # StdBrick(lg_3023, lg_grey, -2*LGBW, 9*LGPH, 3.5*LGBW, -90, 90, 0)

    '''*******************************************************************
    Objects (Step 7)
    *******************************************************************'''
    # 3004    White   Brick 1 x 2
    # StdBrick(lg_3004, lg_white,  1*LGBW, 12*LGPH, -4.5*LGBW, -90, -90, 0)
    # StdBrick(lg_3004, lg_white, -3*LGBW, 12*LGPH, -4.5*LGBW, -90, -90, 0)
    # StdBrick(lg_3004, lg_white, -2*LGBW, 12*LGPH,  3.5*LGBW, -90, 90, 0)
    # 3005    White   Brick 1 x 1
    # StdBrick(lg_3005, lg_white, 1.5*LGBW, 12*LGPH, 2.5*LGBW, -90, 0, 0)
    # 2357    White   Brick 2 x 2 Corner
    # StdBrick(lg_2357, lg_white, -0.5*LGBW, 12*LGPH, 2.5*LGBW, -90, 90, 0)
    # 3010    White   Brick 1 x 4
    # StdBrick(lg_3010, lg_white, -2*LGBW, 12*LGPH,  6.5*LGBW, -90, 90, 0)
    # 4070    Black   Brick 1 x 1 with Headlight
    # StdBrick(lg_4070, lg_black, -0.5*LGBW, 12*LGPH, 4.5*LGBW, -90, 0, 0)
    # StdBrick(lg_4070, lg_black, -0.5*LGBW, 12*LGPH, 5.5*LGBW, -90, 0, 0)

    '''*******************************************************************
    Objects (Step 8)
    *******************************************************************'''
    # 3004    White   Brick 1 x 2
    # StdBrick(lg_3004, lg_white,  1*LGBW, 15*LGPH, -4.5*LGBW, -90, -90, 0)
    # StdBrick(lg_3004, lg_white, -3*LGBW, 15*LGPH, -4.5*LGBW, -90, -90, 0)
    # 3001    White   Brick 2 x 4
    # StdBrick(lg_3001, lg_white, -1*LGBW, 15*LGPH, 5*LGBW, -90, 0, 0)
    # StdBrick(lg_3001, lg_white, -3*LGBW, 15*LGPH, 5*LGBW, -90, 0, 0)
    # 3622    White   Brick 1 x 3
    # StdBrick(lg_3622, lg_white, 0.5*LGBW, 15*LGPH, 2.5*LGBW, -90, 90, 0)

    '''*******************************************************************
    Objects (Step 9)
    *******************************************************************'''
    # 3023    Red Plate 1 x 2
    # StdBrick(lg_3023, lg_red, -0.5*LGBW, 16*LGPH, 5*LGBW, -90, 0, 0)
    # StdBrick(lg_3023, lg_red, -2*LGBW, 16*LGPH, 3.5*LGBW, -90, 90, 0)
    # 4085c   Red     Plate 1 x 1 with Clip Vertical - Type 3
    # StdBrick(lg_4085c, lg_red, -3.5*LGBW, 16*LGPH, -4.5*LGBW, -90, 180, 0)
    # 3623    Red     Plate 1 x 3
    # StdBrick(lg_3623, lg_red, -3.5*LGBW, 16*LGPH, 4.5*LGBW, -90, 0, 0)
    # 3710    Red     Plate 1 x 4
    # StdBrick(lg_3710, lg_red, -2*LGBW, 16*LGPH, 6.5*LGBW, -90, 90, 0)
    # StdBrick(lg_3710, lg_red, -1*LGBW, 16*LGPH, -4.5*LGBW, -90, 90, 0)
    # 3460    Red     Plate 1 x 8
    # StdBrick(lg_3460, lg_red, 1.5*LGBW, 16*LGPH, -1*LGBW, -90, 0, 0)
    # 2420    Red     Plate 2 x 2 Corner
    # StdBrick(lg_2420, lg_red, -0.5*LGBW, 16*LGPH, 2.5*LGBW, -90, 90, 0)
    # 2412b   Yellow  Tile 1 x 2 Grille with Groove
    # StdBrick(lg_2412b, lg_yellow, 0.2*LGBW, 10.8*LGPH, 5*LGBW, 90, 0, 90)

    '''*******************************************************************
    Objects (Step 10)
    *******************************************************************'''
    # 3005    Red   Brick 1 x 1
    # StdBrick(lg_3005, lg_red, -2.5*LGBW, 17*LGPH, -4.5*LGBW, -90, 0, 0)
    # 3665    White   Slope Brick 45 2 x 1 Inverted
    # StdBrick(lg_3665, lg_white, -3.5*LGBW, 19*LGPH, -4.5*LGBW, -90, -90, 0)
    # StdBrick(lg_3665, lg_white, -3.5*LGBW, 19*LGPH, 3.5*LGBW, -90, 90, 0)
    # 3622    White   Brick 1 x 3
    # StdBrick(lg_3622, lg_white, -3.5*LGBW, 19*LGPH, 5.5*LGBW, -90, 0, 0)
    # 3010    White   Brick 1 x 4
    # StdBrick(lg_3010, lg_white, -0.5*LGBW, 19*LGPH, 5*LGBW, -90, 0, 0)
    # 3004    White   Brick 1 x 2
    # StdBrick(lg_3004, lg_white,  -2*LGBW, 19*LGPH, 3.5*LGBW, -90, 90, 0)
    # StdBrick(lg_3004, lg_white,  -2*LGBW, 19*LGPH, 6.5*LGBW, -90, 90, 0)

    '''*******************************************************************
    Objects (Step 11)
    *******************************************************************'''
    # 3010    White   Brick 1 x 4
    # StdBrick(lg_3010, lg_white,  -2*LGBW, 22*LGPH, 3.5*LGBW, -90, 90, 0)
    # StdBrick(lg_3010, lg_white,  -2*LGBW, 22*LGPH, 6.5*LGBW, -90, 90, 0)
    # 3004    White   Brick 1 x 2
    # StdBrick(lg_3004, lg_white, -3.5*LGBW, 22*LGPH, 5*LGBW, -90, 0, 0)
    # 2412b   Red     Tile 1 x 2 Grille with Groove
    # StdBrick(lg_2412b, lg_red,  -0.5*LGBW, 20*LGPH, 5*LGBW, -90, 0, 0)
    # 4515    Red     Slope Brick 10 6 x 8
    # StdBrick(lg_4515, lg_red, 0*LGBW, 19*LGPH, -1*LGBW, -90, 0, 0)

    '''*******************************************************************
    Objects (Step 12)
    *******************************************************************'''
    # 3010    White   Brick 1 x 4
    # StdBrick(lg_3010, lg_white, -3.5*LGBW, 25*LGPH, 5*LGBW, -90, 0, 0)
    # 3622    White   Brick 1 x 3
    # StdBrick(lg_3622, lg_white,  -1.5*LGBW, 25*LGPH, 3.5*LGBW, -90, 90, 0)
    # StdBrick(lg_3622, lg_white,  -1.5*LGBW, 25*LGPH, 6.5*LGBW, -90, 90, 0)

    '''*******************************************************************
    Objects (Step 13)
    *******************************************************************'''
    # 3008    White   Brick 1 x 8
    # StdBrick(lg_3008, lg_white, -3.5*LGBW, 22*LGPH, -1*LGBW, -90, 0, 0)
    # StdBrick(lg_3008, lg_white, -3.5*LGBW, 25*LGPH, -1*LGBW, -90, 0, 0)
    # 3460    Red Plate 1 x 8
    # StdBrick(lg_3460, lg_red, -3.5*LGBW, 26*LGPH, -1*LGBW, -90, 0, 0)
    # 3622    White   Brick 1 x 3
    # StdBrick(lg_3622, lg_white,  -2.5*LGBW, 28*LGPH, 3.5*LGBW, -90, 90, 0)
    # StdBrick(lg_3622, lg_white,  -2.5*LGBW, 28*LGPH, 6.5*LGBW, -90, 90, 0)
    # 3004    White   Brick 1 x 2
    # StdBrick(lg_3004, lg_white, -3.5*LGBW, 28*LGPH, 5*LGBW, -90, 0, 0)
    # 3659    White   Arch 1 x 4 (Pic)
    # StdBrick(lg_3659, lg_white, -0.5*LGBW, 28*LGPH, 5*LGBW, -90, 0, 0)

    '''*******************************************************************
    Objects (Step 14)
    *******************************************************************'''
    # 3675    Red     Slope Brick 33 3 x 3 Double Convex
    # StdBrick(lg_3675, lg_red, -0.5*LGBW, 31*LGPH, 5*LGBW, -90, 0, 0)
    # StdBrick(lg_3675_slope, lg_red, -0.5*LGBW, 31*LGPH, 5*LGBW, -90, 0, 0)
    # StdBrick(lg_3675, lg_red, -0.5*LGBW, 31*LGPH, 4*LGBW, -90, 90, 0)
    # StdBrick(lg_3675_slope, lg_red, -0.5*LGBW, 31*LGPH, 4*LGBW, -90, 90, 0)
    # StdBrick(lg_3675, lg_red, -1.5*LGBW, 31*LGPH, 4*LGBW, -90, 180, 0)
    # StdBrick(lg_3675_slope, lg_red, -1.5*LGBW, 31*LGPH, 4*LGBW, -90, 180, 0)
    # StdBrick(lg_3675, lg_red, -1.5*LGBW, 31*LGPH, 5*LGBW, -90, -90, 0)
    # StdBrick(lg_3675_slope, lg_red, -1.5*LGBW, 31*LGPH, 5*LGBW, -90, -90, 0)
    # 4589    Black   Cone 1 x 1
    # StdBrick(lg_4589, lg_black, -1.5*LGBW, 34*LGPH, 4*LGBW, -90, 0, 0)
)
# declare set_10036_1_house_nonmoving_ox= 0;
# declare set_10036_1_house_nonmoving_oy= 0;
# declare set_10036_1_house_nonmoving_oz= 0;


# 3192 Black   Door 1 x 3 x 3 Right
# declare set_10036_1_house_oven_door=
#     # StdBrick(lg_3192, lg_black, -3.5*LGBW, 12*LGPH, 3.5*LGBW, -90, 90, 0)
# declare set_10036_1_house_oven_door_ox= -3.5*LGBW;
# declare set_10036_1_house_oven_door_oy=   12*LGPH;
# declare set_10036_1_house_oven_door_oz=  3.5*LGBW;
