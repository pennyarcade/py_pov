# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

Original Source:
    Persistence of Vision Ray Tracer version 3.5 Include File
    File: colors.inc
    Last updated: 2001.7.21
    Description: This file contains pre-defined colors and color-manipulation macros.

"""

from logging import *
from pov.basic.Color import Color
from pov.basic.Vector import Vector
from pov.language_directive.Version import Version

Version(3.5)

debug("including colors.inc\n")

'''
    Persistence of Vision Raytracer Version 3.5
    Many pre-defined colors for use in scene files.
'''

# COLORS:
Red = Color(rgb=Vector(1, 0, 0))
Green = Color(rgb=Vector(0, 1, 0))
Blue = Color(rgb=Vector(0, 0, 1))
Yellow = Color(rgb=Vector(1, 1, 0))
Cyan = Color(rgb=Vector(0, 1, 1))
Magenta = Color(rgb=Vector(1, 0, 1))
Clear = Color(rgbf=Vector(1, 1, 1, 1))
White = Color(rgb=Vector(1, 1, 1))
Black = Color(rgb=Vector(0, 0, 0))

# These grays are useful for fine-tuning lighting color values
# and for other areas where subtle variations of grays are needed.

# PERCENTAGE GRAYS:
Gray05 = White * 0.05
Gray10 = White * 0.10
Gray15 = White * 0.15
Gray20 = White * 0.20
Gray25 = White * 0.25
Gray30 = White * 0.30
Gray35 = White * 0.35
Gray40 = White * 0.40
Gray45 = White * 0.45
Gray50 = White * 0.50
Gray55 = White * 0.55
Gray60 = White * 0.60
Gray65 = White * 0.65
Gray70 = White * 0.70
Gray75 = White * 0.75
Gray80 = White * 0.80
Gray85 = White * 0.85
Gray90 = White * 0.90
Gray95 = White * 0.95

# OTHER GRAYS
DimGrey = Color(red=0.329412, green=0.329412, blue=0.329412)
DimGray = DimGrey
Gray = Color(red=0.752941, green=0.752941, blue=0.752941)
Grey = Gray
LightGray = Color(red=0.658824, green=0.658824, blue=0.658824)
LightGrey = LightGray
VLightGray = Color(red=0.80, green=0.80, blue=0.80)
VLightGrey = VLightGray

Aquamarine = Color(red=0.439216, green=0.858824, blue=0.576471)
BlueViolet = Color(red=0.62352, green=0.372549, blue=0.623529)
Brown = Color(red=0.647059, green=0.164706, blue=0.164706)
CadetBlue = Color(red=0.372549, green=0.623529, blue=0.623529)
Coral = Color(red=1.0, green=0.498039, blue=0.0)
CornflowerBlue = Color(red=0.258824, green=0.258824, blue=0.435294)
DarkGreen = Color(red=0.184314, green=0.309804, blue=0.184314)
DarkOliveGreen = Color(red=0.309804, green=0.309804, blue=0.184314)
DarkOrchid = Color(red=0.6, green=0.196078, blue=0.8)
DarkSlateBlue = Color(red=0.119608, green=0.137255, blue=0.556863)
DarkSlateGray = Color(red=0.184314, green=0.309804, blue=0.309804)
DarkSlateGrey = Color(red=0.184314, green=0.309804, blue=0.309804)
DarkTurquoise = Color(red=0.439216, green=0.576471, blue=0.858824)
Firebrick = Color(red=0.556863, green=0.137255, blue=0.137255)
ForestGreen = Color(red=0.137255, green=0.556863, blue=0.137255)
Gold = Color(red=0.8, green=0.498039, blue=0.196078)
Goldenrod = Color(red=0.858824, green=0.858824, blue=0.439216)
GreenYellow = Color(red=0.576471, green=0.858824, blue=0.439216)
Indianred = Color(red=0.309804, green=0.184314, blue=0.184314)
Khaki = Color(red=0.623529, green=0.623529, blue=0.372549)
LightBlue = Color(red=0.74902, green=0.847059, blue=0.847059)
LightSteelBlue = Color(red=0.560784, green=0.560784, blue=0.737255)
LimeGreen = Color(red=0.196078, green=0.8, blue=0.196078)
Maroon = Color(red=0.556863, green=0.137255, blue=0.419608)
MediumAquamarine = Color(red=0.196078, green=0.8, blue=0.6)
MediumBlue = Color(red=0.196078, green=0.196078, blue=0.8)
MediumForestGreen = Color(red=0.419608, green=0.556863, blue=0.137255)
MediumGoldenrod = Color(red=0.917647, green=0.917647, blue=0.678431)
MediumOrchid = Color(red=0.576471, green=0.439216, blue=0.858824)
MediumSeaGreen = Color(red=0.258824, green=0.435294, blue=0.258824)
MediumSlateBlue = Color(red=0.498039, blue=1.0)
MediumSpringGreen = Color(red=0.498039, green=1.0)
MediumTurquoise = Color(red=0.439216, green=0.858824, blue=0.858824)
MediumVioletred = Color(red=0.858824, green=0.439216, blue=0.576471)
MidnightBlue = Color(red=0.184314, green=0.184314, blue=0.309804)
Navy = Color(red=0.137255, green=0.137255, blue=0.556863)
NavyBlue = Color(red=0.137255, green=0.137255, blue=0.556863)
Orange = Color(red=1, green=0.5, blue=0.0)
Orangered = Color(red=1.0, green=0.25)
Orchid = Color(red=0.858824, green=0.439216, blue=0.858824)
PaleGreen = Color(red=0.560784, green=0.737255, blue=0.560784)
Pink = Color(red=0.737255, green=0.560784, blue=0.560784)
Plum = Color(red=0.917647, green=0.678431, blue=0.917647)
Salmon = Color(red=0.435294, green=0.258824, blue=0.258824)
SeaGreen = Color(red=0.137255, green=0.556863, blue=0.419608)
Sienna = Color(red=0.556863, green=0.419608, blue=0.137255)
SkyBlue = Color(red=0.196078, green=0.6, blue=0.8)
SlateBlue = Color(green=0.498039, blue=1.0)
SpringGreen = Color(green=1.0, blue=0.498039)
SteelBlue = Color(red=0.137255, green=0.419608, blue=0.556863)
Tan = Color(red=0.858824, green=0.576471, blue=0.439216)
Thistle = Color(red=0.847059, green=0.74902, blue=0.847059)
Turquoise = Color(red=0.678431, green=0.917647, blue=0.917647)
Violet = Color(red=0.309804, green=0.184314, blue=0.309804)
Violetred = Color(red=0.8, green=0.196078, blue=0.6)
Wheat = Color(red=0.847059, green=0.847059, blue=0.74902)
YellowGreen = Color(red=0.6, green=0.8, blue=0.196078)
SummerSky = Color(red=0.22, green=0.69, blue=0.87)
RichBlue = Color(red=0.35, green=0.35, blue=0.67)
Brass = Color(red=0.71, green=0.65, blue=0.26)
Copper = Color(red=0.72, green=0.45, blue=0.20)
Bronze = Color(red=0.55, green=0.47, blue=0.14)
Bronze2 = Color(red=0.65, green=0.49, blue=0.24)
Silver = Color(red=0.90, green=0.91, blue=0.98)
BrightGold = Color(red=0.85, green=0.85, blue=0.10)
OldGold = Color(red=0.81, green=0.71, blue=0.23)
Feldspar = Color(red=0.82, green=0.57, blue=0.46)
Quartz = Color(red=0.85, green=0.85, blue=0.95)
Mica = Color(Black)  # needed in textures.inc
NeonPink = Color(red=1.00, green=0.43, blue=0.78)
DarkPurple = Color(red=0.53, green=0.12, blue=0.47)
NeonBlue = Color(red=0.30, green=0.30, blue=1.00)
CoolCopper = Color(red=0.85, green=0.53, blue=0.10)
MandarinOrange = Color(red=0.89, green=0.47, blue=0.20)
LightWood = Color(red=0.91, green=0.76, blue=0.65)
MediumWood = Color(red=0.65, green=0.50, blue=0.39)
DarkWood = Color(red=0.52, green=0.37, blue=0.26)
SpicyPink = Color(red=1.00, green=0.11, blue=0.68)
SemiSweetChoc = Color(red=0.42, green=0.26, blue=0.15)
BakersChoc = Color(red=0.36, green=0.20, blue=0.09)
Flesh = Color(red=0.96, green=0.80, blue=0.69)
NewTan = Color(red=0.92, green=0.78, blue=0.62)
NewMidnightBlue = Color(red=0.00, green=0.00, blue=0.61)
VeryDarkBrown = Color(red=0.35, green=0.16, blue=0.14)
DarkBrown = Color(red=0.36, green=0.25, blue=0.20)
DarkTan = Color(red=0.59, green=0.41, blue=0.31)
GreenCopper = Color(red=0.32, green=0.49, blue=0.46)
DkGreenCopper = Color(red=0.29, green=0.46, blue=0.43)
DustyRose = Color(red=0.52, green=0.39, blue=0.39)
HuntersGreen = Color(red=0.13, green=0.37, blue=0.31)
Scarlet = Color(red=0.55, green=0.09, blue=0.09)

Med_Purple = Color(red=0.73, green=0.16, blue=0.96)
Light_Purple = Color(red=0.87, green=0.58, blue=0.98)
Very_Light_Purple = Color(red=0.94, green=0.81, blue=0.99)


# Color manipulation macros

# Takes Hue value as input, returns RGB vector.
def CH2RGB(H):
    """
        @todo: Apidoc
        @Todo: Param Syntax checks
    """
    H %= 360
    if H < 0:
        H += 360
    if H in range(120):
        R = (120 - H) / 60
        G = (H - 0) / 60
        B = 0
    elif H in range(120, 240):
        R = 0
        G = (240 - H) / 60
        B = (H - 120) / 60
    elif H in range(240, 360):
        R = (H - 240) / 60
        G = 0
        B = (360 - H) / 60

    return Vector(min(R, 1), min(G, 1), min(B, 1))


# Takes RGB vector, Max component, and Span as input,
# returns Hue value.
def CRGB2H(RGB, Max, Span):
    """
        @todo: Apidoc
        @Todo: Param Syntax checks
    """
    R = RGB.red
    G = RGB.green
    B = RGB.blue
    if Span > 0:
        T1, T2, T3 = 0
        if R == Max & G != Max:
            T1 = 0 + (G - B) / Span
        if G == Max & B != Max:
            T2 = 2 + (B - R) / Span
        if B == Max & R != Max:
            T3 = 4 + (R - G) / Span
        return (T1 + T2 + T3) * 60
    return 0


# Converts a color in HSL color space to a color in RGB color space.
# Input:  < Hue, Saturation, Lightness, Filter, Transmit >
# Output: < Red, Green, Blue, Filter, Transmit >
#macro CHSL2RGB(Color)
   #local HSLFT = color Color;
   #local H = (HSLFT.red);
   #local S = (HSLFT.green);
   #local L = (HSLFT.blue);
   #local SatRGB = CH2RGB(H);
   #local Col = 2*S*SatRGB + (1-S)*<1,1,1>;
   #if (L<0.5)
      #local RGB = L*Col;
   #else
      #local RGB = (1-L)*Col + (2*L-1)*<1,1,1>;
   #end
   #<RGB.red,RGB.green,RGB.blue,(HSLFT.filter),(HSLFT.transmit)>
#end

# Converts a color in RGB color space to a color in HSL color space.
# Input:  < Red, Green, Blue, Filter, Transmit >
# Output: < Hue, Saturation, Lightness, Filter, Transmit >
#macro CRGB2HSL(Color)
   #local RGBFT = color Color;
   #local R = (RGBFT.red);
   #local G = (RGBFT.green);
   #local B = (RGBFT.blue);
   #local Min = min(R,min(G,B));
   #local Max = max(R,max(G,B));
   #local Span = Max-Min;
   #local L = (Min+Max)/2;
   #local S = 0;
   #if( L!=0 & L!=1 )
      #local S = Span / ( L<0.5 ? (L*2) : (2-L*2) );
   #end
   #local H = CRGB2H (<R,G,B>, Max, Span);
   #<H,S,L,(RGBFT.filter),(RGBFT.transmit)>
#end

# Converts a color in HSV color space to a color in RGB color space.
# Input:  < Hue, Saturation, Value, Filter, Transmit >
# Output: < Red, Green, Blue, Filter, Transmit >
#macro CHSV2RGB(Color)
   #local HSVFT = color Color;
   #local H = (HSVFT.red);
   #local S = (HSVFT.green);
   #local V = (HSVFT.blue);
   #local SatRGB = CH2RGB(H);
   #local RGB = ( ((1-S)*<1,1,1> + S*SatRGB) * V );
   #<RGB.red,RGB.green,RGB.blue,(HSVFT.filter),(HSVFT.transmit)>
#end

# Converts a color in RGB color space to a color in HSV color space.
# Input:  < Red, Green, Blue, Filter, Transmit >
# Output: < Hue, Saturation, Value, Filter, Transmit >
#macro CRGB2HSV(Color)
   #local RGBFT = color Color;
   #local R = (RGBFT.red);
   #local G = (RGBFT.green);
   #local B = (RGBFT.blue);
   #local Min = min(R,min(G,B));
   #local Max = max(R,max(G,B));
   #local Span = Max-Min;
   #local H = CRGB2H (<R,G,B>, Max, Span);
   #local S = 0; #if (Max!=0) #local S = Span/Max; #end
   #<H,S,Max,(RGBFT.filter),(RGBFT.transmit)>
#end

#version Colors_Inc_Temp;
#end
