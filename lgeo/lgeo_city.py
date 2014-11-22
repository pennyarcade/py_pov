'''****************************************************************************
 Persistence of Vision Ray Tracer Scene Description File
 File: main.pov
 Vers: 3.6
 Desc: Main file for testing scenes
 Link:
 Date: 04/2013
 Auth: Chocokiko
****************************************************************************'''

# Only load once
# ifdef(main)
#     already loaded
# else
# declare main = 1;

'''***************************************************************************
Includes
***************************************************************************'''
# ==== System Includes ====
# import sys
# import logging

# ==== py_pov Inchudes
from pov.atmeff.SkySphere import SkySphere

from pov.basic.SceneFile import SceneFile
from pov.basic.Color import Color
from pov.basic.Vector import Vector, x, y, z

from pov.global_settings.GlobalSettings import GlobalSettings

from pov.infinite_solid.Plane import Plane

from pov.language_directive.Version import Version

from pov.object_modifier.Translate import Translate

from pov.other.Camera import Camera
from pov.other.LightSource import LightSource
from pov.other.Object import Object

from pov.texture.ColorMap import ColorMap
from pov.texture.Normal import Normal
from pov.texture.Pigment import Pigment

from pov.texture.pattern.Gradient import Gradient


# ==== Standard POV-Ray Includes ====
# Standard Color definitions
from pov.include.colors_inc import *


# Standard Texture definitions
# #include "textures.inc"
# internal functions usable in user defined functions
# #include "functions.inc"

# ==== Additional Includes ====
# Don't have all of the following included at once, it'll cost memory and time
# to parse!
# --- general include files ---
# macros for manipulating arrays
# #include "arrays.inc"
# A complete library of character objects, by Ken Maeno
# #include "chars.inc"
# Various constants and alias definitions
# #include "consts.inc"
# contains various macros for debugging scene files
# #include "debug.inc"
# The official POV-Ray Logo in various forms
# #include "logo.inc"
# general math functions and macros
# #include "math.inc"
# Some common radiosity settings
# #include "rad_def.inc"
# macros for generating random numbers
# #include "rand.inc"
# #include "shapes.inc"     # macros for generating various shapes
# #include "shapes2.inc"    # some not built in basic shapes
# #include "shapesq.inc"    # Pre-defined quartic shapes
# #include "skies.inc"      # Ready defined sky spheres
# macros for generating and manipulating text strings
# #include "strings.inc"
# macro for sun position on a given date, time, and location on earth
# #include "sunpos.inc"
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
# Great wooden textures created by Dan Farmer and Paul Novak
# #include "woods.inc"


# ==== LGEO Colors and Definitions ====
# include "lg_color.inc"
# include "lg_defs.inc"

# ==== LGEO fixed parts ====

# ==== LGEO parts ====

# ==== Object includes ====
from lgeo.set import lg_10036_1_car
# include "10036-1_house.pov"
# include "10036-1_main.pov"


def main():

    fix = SceneFile('test.pov')
    fix.append(Version(3.6))

    '''***********************************************************************
    Settings --> After Includes to overwrite presets
    ***********************************************************************'''

    # @TODO: Read from Config
    image_width = 800
    # @TODO: Read from Config
    image_height = 600

    fix.append(
        GlobalSettings(
            assumed_gamma=1.5,
            ambient_light=Color(rgb=Vector(1, 1, 1))
        )
    )

    # LGEO Settings
    # TODO: Same as below
    lg_quality = 4

    # L3P Settings
    l3_version = 1.4
    # Quality level, 0=BBox, 1=no refr, 2=normal, 3=studlogo, 4=stud2logo
    l3_quality = lg_quality
    # Width of seam between two bricks
    L3SW = 0.5
    L3Studs = 1  # 1=on 0=off
    L3Bumps = 0  # 1=on 0=off

    L3Ambient = 0.4
    L3Diffuse = 0.4
    L3Ior = 1.25
    L3NormalBumps = Normal(
        bumps=0.01,
        scale=20
    )
    L3NormalSlope = Normal(
        bumps=0.3,
        scale=0.5
    )

    # At least a small seam when transparent
    if L3SW:
        L3SWT = L3SW
    else:
        L3SWT = 0.001

    '''***********************************************************************
    Camera
    ***********************************************************************'''
    fix.append(
        Camera(
            location=Vector(5, 12, 12),
            direction=1.5*z,
            right=x*image_width/image_height,
            look_at=(0.0, 5.0, 0.0)
        )
    )

    '''***********************************************************************
    Background
    ***********************************************************************'''
    fix.append(
        SkySphere(
            Pigment(
                Gradient(y),
                ColorMap({
                    0.00: Color(rgb=Vector(0.6, 0.7, 1.0)),
                    0.70: Color(rgb=Vector(0.0, 0.1, 0.8))
                }),
            )
        )
    )

    '''***********************************************************************
    Light
    ***********************************************************************'''
    fix.append(
        # LightSource(
        #  Vector(0, 0, 0)      # light's position (translated below)
        #  Color(rgb=(1, 1, 1)  # light's color
        #  Translate(
        #      Vector(-3000, 3000, -3000)
        #  )
        # )

        LightSource(
            Vector(0, 0, 0),             # light's position (translated below)
            Color(rgb=Vector(1, 1, 1)),  # light's color
            Translate(
                Vector(300, 300, 300)
            )
        )
    )

    '''***********************************************************************
    Ground plane
    ***********************************************************************'''
    fix.append(
        Plane(
            y, -0.01,
            Pigment(
                Color(rgb=Vector(0.7, 0.5, 0.3))
            )
        )
    )

    '''***********************************************************************
    Objects
    ***********************************************************************'''
    # Pizza to go / Car

    fix.append(
        Object(
            lg_10036_1_car.nonmoving()
        )

        # object {set_10036_1_car_steering_wheel}
        # object {set_10036_1_car_schutter_l}
        # object {set_10036_1_car_schutter_r}
        # object {set_10036_1_car_sunroof}
        # object {set_10036_1_car_sunroof_glass}
        # object {set_10036_1_car_wheel_fr}
        # object {set_10036_1_car_wheel_fl}
        # object {set_10036_1_car_wheel_rr}
        # object {set_10036_1_car_wheel_rl}

        # object {set_10036_1_house_base}
        # object {set_10036_1_house_nonmoving}
        # object {set_10036_1_house_oven_door}
    )

    return fix
