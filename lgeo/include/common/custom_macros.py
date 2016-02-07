"""
Persistence of Vision Ray Tracer Scene Description File.

File: custom_macros.inc
Vers: 3.6
Desc: include file with macros to simplify placing of bricks
Link: -
Date: 04/2013
Auth: Chocokiko


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

# #Only load once
# ifdef(custom_macros)
#    #already loaded
# else
# declare custom_macros = 1;

# **************************************************************************
# Includes
# **************************************************************************
# ==== Standard POV-Ray Includes ====
# include "colors.inc"     # Standard Color definitions
# #include "textures.inc"   # Standard Texture definitions
# #include "functions.inc"  # internal functions usable in user defined
#                           # functions

# ==== Additional Includes ====
# Don't have all of the following included at once, it'll cost memory
# and time to parse!
# --- general include files ---
# #include "arrays.inc"     # macros for manipulating arrays
# #include "chars.inc"      # A complete library of character objects,
# by Ken Maeno
# #include "consts.inc"     # Various constants and alias definitions
# #include "debug.inc"      # contains various macros for
# debugging scene files
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
# include "lg_color.inc"
# from lgeo.include.common.lg_defs import *

# ==== LGEO fixed parts ====

# ==== LGEO parts ====

# ==== Py Pov ====
from pov.basic.Vector import Vector

from pov.other.Object import Object

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate

from pov.texture.Texture import Texture


# ***************************************************************************
# Macros
# ***************************************************************************


def UnchangedBrick(brick, texture):
    """Create Brick + Texture Object"""
    return Object(
        brick,
        Texture(texture)
    )


def StdBrick(brick, texture, tx, ty, tz, rx, ry, rz):
    """Create rotated + translated Brick object"""
    return Object(
        brick,
        texture,
        Rotate(Vector(rx, ry, rz)),
        Translate(Vector(tx, ty, tz))
    )
