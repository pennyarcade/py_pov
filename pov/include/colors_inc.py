# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

Original Source:
    Persistence of Vision Ray Tracer version 3.5 Include File
    File: colors.inc
    Last updated: 2001.7.21
    Description: This file contains pre-defined
                 colors and color-manipulation macros.

"""

from logging import debug
from pov.basic.Color import Color
from pov.basic.Vector import Vector
from pov.language_directive.Version import Version

Version(3.5)

debug("including colors.inc\n")

# Persistence of Vision Raytracer Version 3.5
# Many pre-defined colors for use in scene files.

# COLORS:
RED = Color(rgb=Vector(1, 0, 0))
# GREEN = Color(rgb=Vector(0, 1, 0))
# BLUE = Color(rgb=Vector(0, 0, 1))
# YELLOW = Color(rgb=Vector(1, 1, 0))
# CYAN = Color(rgb=Vector(0, 1, 1))
# MAGENTA = Color(rgb=Vector(1, 0, 1))
# CLEAR = Color(rgbf=Vector(1, 1, 1, 1))
# WHITE = Color(rgb=Vector(1, 1, 1))
# BLACK = Color(rgb=Vector(0, 0, 0))

# These grays are useful for fine-tuning lighting color values
# and for other areas where subtle variations of grays are needed.

# PERCENTAGE GRAYS:
# GRAY05 = WHITE * 0.05
# GRAY10 = WHITE * 0.10
# GRAY15 = WHITE * 0.15
# GRAY20 = WHITE * 0.20
# GRAY25 = WHITE * 0.25
# GRAY30 = WHITE * 0.30
# GRAY35 = WHITE * 0.35
# GRAY40 = WHITE * 0.40
# GRAY45 = WHITE * 0.45
# GRAY50 = WHITE * 0.50
# GRAY55 = WHITE * 0.55
# GRAY60 = WHITE * 0.60
# GRAY65 = WHITE * 0.65
# GRAY70 = WHITE * 0.70
# GRAY75 = WHITE * 0.75
# GRAY80 = WHITE * 0.80
# GRAY85 = WHITE * 0.85
# GRAY90 = WHITE * 0.90
# GRAY95 = WHITE * 0.95

# OTHER GRAYS
# DIMGREY = Color(red=0.329412, green=0.329412, blue=0.329412)
# DIMGRAY = DIMGREY
# GRAY = Color(red=0.752941, green=0.752941, blue=0.752941)
# GREY = GRAY
# LIGHTGRAY = Color(red=0.658824, green=0.658824, blue=0.658824)
# LIGHTGREY = LIGHTGRAY
# VLIGHTGRAY = Color(red=0.80, green=0.80, blue=0.80)
# VLIGHTGREY = VLIGHTGRAY

# AQUAMARINE = Color(red=0.439216, green=0.858824, blue=0.576471)
# BLUEVIOLET = Color(red=0.62352, green=0.372549, blue=0.623529)
# BROWN = Color(red=0.647059, green=0.164706, blue=0.164706)
# CADETBLUE = Color(red=0.372549, green=0.623529, blue=0.623529)
# CORAL = Color(red=1.0, green=0.498039, blue=0.0)
# CORNFLOWERBLUE = Color(red=0.258824, green=0.258824, blue=0.435294)
# DARKGREEN = Color(red=0.184314, green=0.309804, blue=0.184314)
# DARKOLIVEGREEN = Color(red=0.309804, green=0.309804, blue=0.184314)
# DARKORCHID = Color(red=0.6, green=0.196078, blue=0.8)
# DARKSLATEBLUE = Color(red=0.119608, green=0.137255, blue=0.556863)
# DARKSLATEGRAY = Color(red=0.184314, green=0.309804, blue=0.309804)
# DARKSLATEGREY = Color(red=0.184314, green=0.309804, blue=0.309804)
# DARKTURQUOISE = Color(red=0.439216, green=0.576471, blue=0.858824)
# FIREBRICK = Color(red=0.556863, green=0.137255, blue=0.137255)
# FORESTGREEN = Color(red=0.137255, green=0.556863, blue=0.137255)
# GOLD = Color(red=0.8, green=0.498039, blue=0.196078)
# GOLDENROD = Color(red=0.858824, green=0.858824, blue=0.439216)
# GREENYELLOW = Color(red=0.576471, green=0.858824, blue=0.439216)
# INDIANRED = Color(red=0.309804, green=0.184314, blue=0.184314)
# KHAKI = Color(red=0.623529, green=0.623529, blue=0.372549)
# LIGHTBLUE = Color(red=0.74902, green=0.847059, blue=0.847059)
# LIGHTSTEELBLUE = Color(red=0.560784, green=0.560784, blue=0.737255)
# LIMEGREEN = Color(red=0.196078, green=0.8, blue=0.196078)
# MAROON = Color(red=0.556863, green=0.137255, blue=0.419608)
# MEDIUMAQUAMARINE = Color(red=0.196078, green=0.8, blue=0.6)
# MEDIUMBLUE = Color(red=0.196078, green=0.196078, blue=0.8)
# MEDIUMFORESTGREEN = Color(red=0.419608, green=0.556863, blue=0.137255)
# MEDIUMGOLDENROD = Color(red=0.917647, green=0.917647, blue=0.678431)
# MEDIUMORCHID = Color(red=0.576471, green=0.439216, blue=0.858824)
# MEDIUMSEAGREEN = Color(red=0.258824, green=0.435294, blue=0.258824)
# MEDIUMSLATEBLUE = Color(red=0.498039, blue=1.0)
# MEDIUMSPRINGGREEN = Color(red=0.498039, green=1.0)
# MEDIUMTURQUOISE = Color(red=0.439216, green=0.858824, blue=0.858824)
# MEDIUMVIOLETRED = Color(red=0.858824, green=0.439216, blue=0.576471)
# MIDNIGHTBLUE = Color(red=0.184314, green=0.184314, blue=0.309804)
# NAVY = Color(red=0.137255, green=0.137255, blue=0.556863)
# NAVYBLUE = Color(red=0.137255, green=0.137255, blue=0.556863)
# ORANGE = Color(red=1, green=0.5, blue=0.0)
# ORANGERED = Color(red=1.0, green=0.25)
# ORCHID = Color(red=0.858824, green=0.439216, blue=0.858824)
# PALEGREEN = Color(red=0.560784, green=0.737255, blue=0.560784)
# PINK = Color(red=0.737255, green=0.560784, blue=0.560784)
# PLUM = Color(red=0.917647, green=0.678431, blue=0.917647)
# SALMON = Color(red=0.435294, green=0.258824, blue=0.258824)
# SEAGREEN = Color(red=0.137255, green=0.556863, blue=0.419608)
# SIENNA = Color(red=0.556863, green=0.419608, blue=0.137255)
# SKYBLUE = Color(red=0.196078, green=0.6, blue=0.8)
# SLATEBLUE = Color(green=0.498039, blue=1.0)
# SPRINGGREEN = Color(green=1.0, blue=0.498039)
# STEELBLUE = Color(red=0.137255, green=0.419608, blue=0.556863)
# TAN = Color(red=0.858824, green=0.576471, blue=0.439216)
# THISTLE = Color(red=0.847059, green=0.74902, blue=0.847059)
# TURQUOISE = Color(red=0.678431, green=0.917647, blue=0.917647)
# VIOLET = Color(red=0.309804, green=0.184314, blue=0.309804)
# VIOLETRED = Color(red=0.8, green=0.196078, blue=0.6)
# WHEAT = Color(red=0.847059, green=0.847059, blue=0.74902)
# YELLOWGREEN = Color(red=0.6, green=0.8, blue=0.196078)
# SUMMERSKY = Color(red=0.22, green=0.69, blue=0.87)
# RICHBLUE = Color(red=0.35, green=0.35, blue=0.67)
# BRASS = Color(red=0.71, green=0.65, blue=0.26)
# COPPER = Color(red=0.72, green=0.45, blue=0.20)
# BRONZE = Color(red=0.55, green=0.47, blue=0.14)
# BRONZE2 = Color(red=0.65, green=0.49, blue=0.24)
# SILVER = Color(red=0.90, green=0.91, blue=0.98)
# BRIGHTGOLD = Color(red=0.85, green=0.85, blue=0.10)
# OLDGOLD = Color(red=0.81, green=0.71, blue=0.23)
# FELDSPAR = Color(red=0.82, green=0.57, blue=0.46)
# QUARTZ = Color(red=0.85, green=0.85, blue=0.95)
# MICA = Color(BLACK)  # needed in textures.inc
# NEONPINK = Color(red=1.00, green=0.43, blue=0.78)
# DARKPURPLE = Color(red=0.53, green=0.12, blue=0.47)
# NEONBLUE = Color(red=0.30, green=0.30, blue=1.00)
# COOLCOPPER = Color(red=0.85, green=0.53, blue=0.10)
# MANDARINORANGE = Color(red=0.89, green=0.47, blue=0.20)
# LIGHTWOOD = Color(red=0.91, green=0.76, blue=0.65)
# MEDIUMWOOD = Color(red=0.65, green=0.50, blue=0.39)
# DARKWOOD = Color(red=0.52, green=0.37, blue=0.26)
# SPICYPINK = Color(red=1.00, green=0.11, blue=0.68)
# SEMISWEETCHOC = Color(red=0.42, green=0.26, blue=0.15)
# BAKERSCHOC = Color(red=0.36, green=0.20, blue=0.09)
# FLESH = Color(red=0.96, green=0.80, blue=0.69)
# NEWTAN = Color(red=0.92, green=0.78, blue=0.62)
# NEWMIDNIGHTBLUE = Color(red=0.00, green=0.00, blue=0.61)
# VERYDARKBROWN = Color(red=0.35, green=0.16, blue=0.14)
# DARKBROWN = Color(red=0.36, green=0.25, blue=0.20)
# DARKTAN = Color(red=0.59, green=0.41, blue=0.31)
# GREENCOPPER = Color(red=0.32, green=0.49, blue=0.46)
# DKGREENCOPPER = Color(red=0.29, green=0.46, blue=0.43)
# DUSTYROSE = Color(red=0.52, green=0.39, blue=0.39)
# HUNTERSGREEN = Color(red=0.13, green=0.37, blue=0.31)
# SCARLET = Color(red=0.55, green=0.09, blue=0.09)

# MED_PURPLE = Color(red=0.73, green=0.16, blue=0.96)
# LIGHT_PURPLE = Color(red=0.87, green=0.58, blue=0.98)
# VERY_LIGHT_PURPLE = Color(red=0.94, green=0.81, blue=0.99)


# Color manipulation macros

def ch2rgb(hue):
    """
    Take Hue value as input, returns RGB vector.

    @todo: Apidoc
    @Todo: Param Syntax checks
    """
    hue %= 360
    if hue < 0:
        hue += 360
    if hue in range(120):
        red = (120 - hue) / 60
        green = (hue - 0) / 60
        blue = 0
    elif hue in range(120, 240):
        red = 0
        green = (240 - hue) / 60
        blue = (hue - 120) / 60
    elif hue in range(240, 360):
        red = (hue - 240) / 60
        green = 0
        blue = (360 - hue) / 60

    return Vector(min(red, 1), min(green, 1), min(blue, 1))


def crgb2h(rgb, maximum, span):
    """
    Take rgb vector, maximum component, and span as input, returns Hue value.

    @Todo: Param Syntax checks
    """
    red = rgb.red
    green = rgb.green
    blue = rgb.blue
    if span > 0:
        val_t1 = 0
        val_t2 = 0
        val_t3 = 0
        if red == maximum & green != maximum:
            val_t1 = 0 + (green - blue) / span
        if green == maximum & blue != maximum:
            val_t2 = 2 + (blue - red) / span
        if blue == maximum & red != maximum:
            val_t3 = 4 + (red - green) / span
        return (val_t1 + val_t2 + val_t3) * 60
    return 0


# def chsl2rgb(vector):
#     """
#     Convert a color in HSL color space to a color in RGB color space.

#     Input:  < Hue, Saturation, Lightness, Filter, Transmit >
#     Output: < Red, Green, Blue, Filter, Transmit >

#     @Todo: Param Syntax checks
#     @todo: support this?
#     """
#     incolor = Color(vector)
#     hue = (incolor.red)
#     saturation = (incolor.green)
#     lightness = (incolor.blue)
#     sat_rgb = ch2rgb(hue)
#     col = 2 * saturation * sat_rgb + (1 - saturation) * Vector(1, 1, 1)
#     if lightness < 0.5:
#         rgb = lightness * col
#     else:
#         rgb = (1 - lightness) * col + (2 * lightness - 1) * Vector(1, 1, 1)
#     return Color(
#         rgb.red, rgb.green, rgb.blue, incolor.filter, incolor.transmit
#     )


# def crgb2hsl(incolor):
#     """
#     Convert a color in RGB color space to a color in HSL color space.

#     Input:  < Red, Green, Blue, Filter, Transmit >
#     Output: < Hue, Saturation, Lightness, Filter, Transmit >

#     @Todo: Param Syntax checks
#     @todo: support this?
#     """
#     red = (incolor.red)
#     green = (incolor.green)
#     blue = (incolor.blue)
#     minimum = min(red, min(green, blue))
#     maximum = max(red, max(green, blue))
#     span = maximum - minimum
#     lightness = (minimum + maximum) / 2
#     saturation = 0
#     if lightness != 0 & lightness != 1:
#         if lightness < 0.5:
#             saturation = span / (lightness * 2)
#         else:
#             saturation = span / (2 - lightness * 2)
#     hue = crgb2h(Vector(red, green, blue), maximum, span)
#     return Vector(hue, saturation, lightness, incolor.filter, incolor.transmit)


# def chsv2rgb(vector):
#     """
#     Convert a color in HSV color space to a color in RGB color space.

#     Input:  < Hue, Saturation, Value, Filter, Transmit >
#     Output: < Red, Green, Blue, Filter, Transmit >
#     """
#     hsvft = Color(vector)
#     hue = hsvft.red
#     saturation = hsvft.green
#     value = hsvft.blue
#     sat_rgb = ch2rgb(hue)
#     rgb = ((1 - saturation) * Color(
#         rgb=Vector(1, 1, 1)
#     ) + saturation * sat_rgb)
#     rgb *= value
#     return Color(
#         rgbft=Vector(
#             rgb.red, rgb.green, rgb.blue, hsvft.filter, hsvft.transmit
#         )
#     )


# def crgb2hsv(vector):
#     """
#     Convert a color in RGB color space to a color in HSV color space.

#     Input:  < Red, Green, Blue, Filter, Transmit >
#     Output: < Hue, Saturation, Value, Filter, Transmit >
#     """
#     incolor = Color(vector)
#     red = incolor.red
#     green = incolor.green
#     blue = incolor.blue
#     minimum = min(red, min(green, blue))
#     maximum = max(red, max(green, blue))
#     span = maximum - minimum
#     hue = crgb2h(Color(rgb=Vector(red, green, blue)), maximum, span)
#     saturation = 0
#     if maximum != 0:
#         saturation = span / maximum
#     return Color(
#         rgbft=Vector(
#             hue, saturation, maximum, incolor.filter, incolor.transmit
#         )
#     )
