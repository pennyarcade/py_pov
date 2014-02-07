'''****************************************************************************/
*                                                                             */
* LGEO Libray Include File     (C) lgeo@digitalbricks.org (Lutz Uhlmann)      */
*                                                                             */
* 19970623 Lutz Uhlmann                                                       */
* 20070929 Lutz Uhlmann changed to use predefined finishes                    */
* 20070929 Lutz Uhlmann changed to use RGB values from ldconfig.ldr           */
* 20071124 Lutz Uhlmann added lg_quality for L3P compatibility                */
*                                                                             */
* This file is in no way related to the LEGO(tm) Group.                       */
* It is provided for private non-commercial use only.                         */
*                                                                             */
* lg_color: Color Definitions for LGEO POV-Ray Library                        */
*                                                                             */
****************************************************************************'''

from lgeo.config.lgeo_cfg import *

from pov.include.colors_inc import *


if lg_quality > 1:
    lg_solid_finish = Finish(
        ambient=0.1
    )
else:
    lg_solid_finish = Finish(
        ambient=0.1,
        phong=0.2,
        phong_size=20
    )


if lg_quality > 1:
    lg_chrome_finish = Finish(
        ambient=0.25
    )
else:
    lg_chrome_finish = Finish(
        ambient=0.25,
        brilliance=5,
        diffuse=0.6,
        metallic=True,
        specular=0.70,
        roughness=1/100,
        reflection=0.6,
    )


if (lg_quality > 1):
    lg_pearl_finish = Finish(
        ambient=0.22
    )
else:
    lg_pearl_finish = Finish(
        ambient=0.22,
        brilliance=2,
        diffuse=0.6,
        metallic=True,
        specular=0.1,
        roughness=32/100,
        reflection=0.07,
        Irid(
          0.2,
          thickness=0.5,
          turbulence=2.5
        )
    )


if (lg_quality > 1):
    lg_transparent_finish = Finish(
        ambient=0.3
    )
else:
    lg_transparent_finish = Finish(
        ambient=0.3,
        diffuse=0.2,
        reflection=0.25,
        phong=0.3,
        phong_size=60
    )


lg_ior = Interior(
    ior=1.4
)


# 0
lg_black = Texture(
    Pigment(Color(rgb=Vector(33/255, 33/255, 33/255))),
    Finish(lg_solid_finish)
)

# 1
lg_blue = Texture(
 pigment { rgb <0/255, 51/255, 178/255> ),
 Finish( lg_solid_finish ),
),

# 2
lg_green = Texture(
 pigment { rgb <0/255, 140/255, 20/255> ),
 Finish( lg_solid_finish ),
),

# 3
lg_teal = Texture(
 pigment { rgb <0/255, 153/255, 159/255> ),
 Finish( lg_solid_finish ),
),
lg_cyan = lg_teal

# 4
lg_red = Texture(
 pigment { rgb <196/255, 0/255, 38/255> ),
 Finish( lg_solid_finish ),
),

# 5
lg_dark_pink = Texture(
 pigment { rgb <223/255, 102/255, 149/255> ),
 Finish( lg_solid_finish ),
),

# 6
lg_brown = Texture(
 pigment { rgb <92/255, 32/255, 0/255> ),
 Finish( lg_solid_finish ),
),

# 7
lg_grey = Texture(
 pigment { rgb <193/255, 194/255, 193/255> ),
 Finish( lg_solid_finish ),
),

# 8
lg_dark_grey = Texture(
 pigment { rgb <99/255, 89/255, 82/255> ),
 Finish( lg_solid_finish ),
),

# 9
lg_light_blue = Texture(
 pigment { rgb <107/255, 172/255, 220/255> ),
 Finish( lg_solid_finish ),
),

# 10
lg_bright_green = Texture(
 pigment { rgb <97/255, 238/255, 104/255> ),
 Finish( lg_solid_finish ),
),

# 11
lg_turquoise = Texture(
 pigment { rgb <51/255, 166/255, 167/255> ),
 Finish( lg_solid_finish ),
),
lg_blue_green = lg_turquoise

# 12
lg_salmon = Texture(
 pigment { rgb <255/255, 133/255, 122/255> ),
 Finish( lg_solid_finish ),
),
lg_light_red = lg_salmon

# 13
lg_pink = Texture(
 pigment { rgb <249/255, 163/255, 198/255> ),
 Finish( lg_solid_finish ),
),
lg_rose = lg_pink

# 14
lg_yellow = Texture(
 pigment { rgb <255/255, 220/255, 0/255> ),
 Finish( lg_solid_finish ),
),

# 15
lg_white = Texture(
 pigment { rgb <255/255, 255/255, 255/255> ),
 Finish( lg_solid_finish ),
),

# 17
lg_light_green = Texture(
 pigment { rgb <186/255, 255/255, 206/255> ),
 Finish( lg_solid_finish ),
),

# 18
lg_light_yellow = Texture(
 pigment { rgb <253/255, 232/255, 150/255> ),
 Finish( lg_solid_finish ),
),

# 19
lg_tan = Texture(
 pigment { rgb <232/255, 207/255, 161/255> ),
 Finish( lg_solid_finish ),
),

# 20
lg_light_violet = Texture(
 pigment { rgb <215/255, 196/255, 230/255> ),
 Finish( lg_solid_finish ),
),

# 22
lg_purple = Texture(
 pigment { rgb <129/255, 0/255, 124/255> ),
 Finish( lg_solid_finish ),
),
lg_violet = lg_purple

# 23
lg_violet_blue = Texture(
 pigment { rgb <71/255, 50/255, 176/255> ),
 Finish( lg_solid_finish ),
),

# 25
lg_orange = Texture(
 pigment { rgb <249/255, 96/255, 0/255> ),
 Finish( lg_solid_finish ),
),

# 26
lg_magenta = Texture(
 pigment { rgb <232/255, 27/255, 109/255> ),
 Finish( lg_solid_finish ),
),

# 27
lg_lime = Texture(
 pigment { rgb <231/255, 240/255, 0/255> ),
 Finish( lg_solid_finish ),
),

# 27
lg_dark_tan = Texture(
 pigment { rgb <187/255, 141/255, 75/255> ),
 Finish( lg_solid_finish ),
),

# 29
lg_light_purple = Texture(
 pigment { rgb <205/255, 173/255, 200/255> ),
 Finish( lg_solid_finish ),
),

# 33
lg_clear_blue = Texture(
 pigment { rgb <0/255, 32/255, 160/255>
  #if (lg_quality > 1)
   filter 0.9
  #end
 ),
 Finish( lg_transparent_finish ),
),

# 34
lg_clear_green = Texture(
 pigment { rgb <6/255, 98/255, 50/255>
  #if (lg_quality > 1)
   filter 0.9
  #end
 ),
 Finish( lg_transparent_finish ),
),

# 36
lg_clear_red = Texture(
 pigment { rgb <196/255, 0/255, 38/255>
  #if (lg_quality > 1)
   filter 0.9
  #end
 ),
 Finish( lg_transparent_finish ),
),

# 37
lg_clear_violet = Texture(
 pigment { rgb <100/255, 0/255, 97/255>
  #if (lg_quality > 1)
   filter 0.9
  #end
 ),
 Finish( lg_transparent_finish ),
),

# 40
lg_clear_brown = Texture(
 pigment { rgb <99/255, 89/255, 82/255>
  #if (lg_quality > 1)
   filter 0.9
  #end
 ),
 Finish( lg_transparent_finish ),
),

# 41
lg_clear_cyan = Texture(
 pigment { rgb <174/255, 239/255, 237/255>
  #if (lg_quality > 1)
   filter 0.9
  #end
 ),
 Finish( lg_transparent_finish ),
),

# 42
lg_clear_neon_yellow = Texture(
 pigment { rgb <192/255, 255/255, 0/255>
  #if (lg_quality > 1)
   filter 0.85
  #end
 ),
 Finish( lg_transparent_finish ),
),

# 45
lg_clear_pink = Texture(
 pigment { rgb <223/255, 102/255, 149/255>
  #if (lg_quality > 1)
   filter 0.9
  #end
 ),
 Finish( lg_transparent_finish ),
),

# 46
lg_clear_yellow = Texture(
 pigment { rgb <202/255, 176/255, 0/255>
  #if (lg_quality > 1)
   filter 0.9
  #end
 ),
 Finish( lg_transparent_finish ),
),

# 47
lg_clear = Texture(
 pigment { rgb <255/255, 255/255, 255/255>
  #if (lg_quality > 1)
   filter 0.9
  #end
 ),
 Finish( lg_transparent_finish ),
),

# 57
lg_clear_neon_orange = Texture(
 pigment { rgb <249/255, 96/255, 0/255>
  #if (lg_quality > 1)
   filter 0.8
  #end
 ),
 Finish( lg_transparent_finish ),
),

# 69
lg_bright_purple = Texture(
 pigment { rgb <205/255, 98/255, 152/255> ),
 Finish( lg_solid_finish ),
),

# 70
lg_reddish_brown = Texture(
 pigment { rgb <105/255, 64/255, 39/255> ),
 Finish( lg_solid_finish ),
),

# 71
lg_bluish_grey = Texture(
 pigment { rgb <163/255, 162/255, 164/255> ),
 Finish( lg_solid_finish ),
),

# 72
lg_dark_bluish_grey = Texture(
 pigment { rgb <99/255, 95/255, 97/255> ),
 Finish( lg_solid_finish ),
),

# 73
lg_medium_blue = Texture(
 pigment { rgb <110/255, 153/255, 201/255> ),
 Finish( lg_solid_finish ),
),

# 74
lg_medium_green = Texture(
 pigment { rgb <161/255, 196/255, 139/255> ),
 Finish( lg_solid_finish ),
),

# 77
lg_paradisa_pink = Texture(
 pigment { rgb <254/255, 204/255, 204/255> ),
 Finish( lg_solid_finish ),
),

# 78
lg_light_flesh = Texture(
 pigment { rgb <250/255, 215/255, 195/255> ),
 Finish( lg_solid_finish ),
),

# 85
lg_medium_violet = Texture(
 pigment { rgb <52/255, 43/255, 117/255> ),
 Finish( lg_solid_finish ),
),

# 86
lg_dark_flesh = Texture(
 pigment { rgb <124/255, 92/255, 69/255> ),
 Finish( lg_solid_finish ),
),

# 89
lg_royal_blue = Texture(
 pigment { rgb <155/255, 178/255, 239/255> ),
 Finish( lg_solid_finish ),
),

# 92
lg_flesh = Texture(
 pigment { rgb <204/255, 142/255, 104/255> ),
 Finish( lg_solid_finish ),
),

# 134
lg_pearl_copper = Texture(
 pigment { color rgb <147/255, 135/255, 103/255> ),
 Finish( lg_pearl_finish ),
),

# 135
lg_pearl_grey = Texture(
 pigment { color rgb <171/255, 173/255, 172/255> ),
 Finish( lg_pearl_finish ),
),

# 137
lg_pearl_blue = Texture(
 pigment { color rgb <106/255, 122/255, 150/255> ),
 Finish( lg_pearl_finish ),
),

# 142
lg_pearl_gold = Texture(
 pigment { color rgb <215/255, 169/255, 75/255> ),
 Finish( lg_pearl_finish ),
),

# 151
lg_very_light_bluish_grey = Texture(
 pigment { rgb <229/255, 228/255, 222/255> ),
 Finish( lg_solid_finish ),
),

# 272
lg_dark_blue = Texture(
 pigment { rgb <0/255, 29/255, 104/255> ),
 Finish( lg_solid_finish ),
),

# 288
lg_dark_green = Texture(
 pigment { rgb <39/255, 70/255, 44/255> ),
 Finish( lg_solid_finish ),
),

# 320
lg_dark_red = Texture(
 pigment { rgb <120/255, 0/255, 28/255> ),
 Finish( lg_solid_finish ),
),

# 313
lg_maersk_blue = Texture(
 pigment { rgb <53/255, 162/255, 189/255> ),
 Finish( lg_solid_finish ),
),

# 334
lg_gold_chrome = Texture(
 pigment { rgb <233/255, 110/255, 19/255> ),
 Finish( lg_chrome_finish ),
),

# 373
lg_sand_purple = Texture(
 pigment { rgb <132/255, 94/255, 132/255> ),
 Finish( lg_solid_finish ),
),

# 335
lg_sand_red = Texture(
 pigment { rgb <191/255, 135/255, 130/255> ),
 Finish( lg_solid_finish ),
),

# 366
lg_earth_orange = Texture(
 pigment { rgb <209/255, 131/255, 4/255> ),
 Finish( lg_solid_finish ),
),

# 373
lg_sand_purple = Texture(
 pigment { rgb <132/255, 94/255, 132/255> ),
 Finish( lg_solid_finish ),
),

# 378
lg_sand_green = Texture(
 pigment { rgb <160/255, 188/255, 172/255> ),
 Finish( lg_solid_finish ),
),

# 379
lg_sand_blue = Texture(
 pigment { rgb <106/255, 122/255, 150/255> ),
 Finish( lg_solid_finish ),
),

# 383
lg_chrome = Texture(
 pigment { rgb <232/255, 232/255, 232/255> ),
 Finish( lg_chrome_finish ),
),

# 462
lg_light_orange = Texture(
 pigment { rgb <254/255, 159/255, 6/255> ),
 Finish( lg_solid_finish ),
),

# 484
lg_dark_orange = Texture(
 pigment { rgb <179/255, 62/255, 0/255> ),
 Finish( lg_solid_finish ),
),

# 503
lg_very_light_grey = Texture(
 pigment { rgb <230/255, 227/255, 219/255> ),
 Finish( lg_solid_finish ),
),

# 999
lg_undefined = Texture(
 pigment { rgb <0.5, 0.7, 0.9> ),
),

# 998 (no code known)
lg_medium_orange = Texture(
 pigment { rgb <224/255, 129/255, 6/255> ),
 Finish( lg_solid_finish ),
),

#end
