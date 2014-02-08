'''****************************************************************************/
* FO O                                                                           */
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
    Pigment(Color(rgb=Vector(0/255, 51/255, 178/255))),
    Finish(lg_solid_finish)
)

# 2
lg_green = Texture(
    Pigment(Color(rgb=Vector(0/255, 140/255, 20/255))),
    Finish(lg_solid_finish)
)

# 3
lg_teal = Texture(
    Pigment(Color(rgb=Vector(0/255, 153/255, 159/255))),
    Finish(lg_solid_finish)
)
lg_cyan = lg_teal

# 4
lg_red = Texture(
    Pigment(Color(rgb=Vector(196/255, 0/255, 38/255))),
    Finish(lg_solid_finish)
)

# 5
lg_dark_pink = Texture(
    Pigment(Color(rgb=Vector(223/255, 102/255, 149/255))),
    Finish(lg_solid_finish)
)

# 6
lg_brown = Texture(
    Pigment(Color(rgb=Vector(92/255, 32/255, 0/255))),
    Finish(lg_solid_finish)
)

# 7
lg_grey = Texture(
    Pigment(Color(rgb=Vector(193/255, 194/255, 193/255))),
    Finish(lg_solid_finish)
)

# 8
lg_dark_grey = Texture(
    Pigment(Color(rgb=Vector(99/255, 89/255, 82/255))),
    Finish(lg_solid_finish)
)

# 9
lg_light_blue = Texture(
    Pigment(Color(rgb=Vector(107/255, 172/255, 220/255))),
    Finish(lg_solid_finish)
)

# 10
lg_bright_green = Texture(
    Pigment(Color(rgb=Vector(97/255, 238/255, 104/255))),
    Finish(lg_solid_finish)
)

# 11
lg_turquoise = Texture(
    Pigment(Color(rgb=Vector(51/255, 166/255, 167/255))),
    Finish(lg_solid_finish)
)
lg_blue_green = lg_turquoise

# 12
lg_salmon = Texture(
    Pigment(Color(rgb=Vector(255/255, 133/255, 122/255))),
    Finish(lg_solid_finish)
)
lg_light_red = lg_salmon

# 13
lg_pink = Texture(
    Pigment(Color(rgb=Vector(249/255, 163/255, 198/255))),
    Finish(lg_solid_finish)
)
lg_rose = lg_pink

# 14
lg_yellow = Texture(
    Pigment(Color(rgb=Vector(255/255, 220/255, 0/255))),
    Finish(lg_solid_finish)
)

# 15
lg_white = Texture(
    Pigment(Color(rgb=Vector(255/255, 255/255, 255/255))),
    Finish(lg_solid_finish)
)

# 17
lg_light_green = Texture(
    Pigment(Color(rgb=Vector(186/255, 255/255, 206/255))),
    Finish(lg_solid_finish)
)

# 18
lg_light_yellow = Texture(
    Pigment(Color(rgb=Vector(253/255, 232/255, 150/255))),
    Finish(lg_solid_finish)
)

# 19
lg_tan = Texture(
    Pigment(Color(rgb=Vector(232/255, 207/255, 161/255))),
    Finish(lg_solid_finish)
)

# 20
lg_light_violet = Texture(
    Pigment(Color(rgb=Vector(215/255, 196/255, 230/255))),
    Finish(lg_solid_finish)
)

# 22
lg_purple = Texture(
    Pigment(Color(rgb=Vector(129/255, 0/255, 124/255))),
    Finish(lg_solid_finish)
)
lg_violet = lg_purple

# 23
lg_violet_blue = Texture(
    Pigment(Color(rgb=Vector(71/255, 50/255, 176/255))),
    Finish(lg_solid_finish)
)

# 25
lg_orange = Texture(
    Pigment(Color(rgb=Vector(249/255, 96/255, 0/255))),
    Finish(lg_solid_finish)
)

# 26
lg_magenta = Texture(
    Pigment(Color(rgb=Vector(232/255, 27/255, 109/255))),
    Finish(lg_solid_finish)
)

# 27
lg_lime = Texture(
    Pigment(Color(rgb=Vector(231/255, 240/255, 0/255))),
    Finish(lg_solid_finish)
)

# 27
lg_dark_tan = Texture(
    Pigment(Color(rgb=Vector(187/255, 141/255, 75/255))),
    Finish(lg_solid_finish)
)

# 29
lg_light_purple = Texture(
    Pigment(Color(rgb=Vector(205/255, 173/255, 200/255))),
    Finish(lg_solid_finish)
)


# Helper to build complex colors
def get_clear_color(cvector, quality):
    if (quality > 1):
        return Texture(
            Pigment(
                Color(rgb=cvector),
                filter=0.9
            ),
            Finish(lg_transparent_finish)
        )
    else:
        return Texture(
            Pigment(
                Color(rgb=cvector)
            ),
            Finish(lg_transparent_finish)
        )


# 33
lg_clear_blue = get_clear_color(
    Vector(0/255, 32/255, 160/255),
    lg_quality
)


#34
lg_clear_blue = get_clear_color(
    Vector(6/255, 98/255, 50/255),
    lg_quality
)


# 36
lg_clear_blue = get_clear_color(
    Vector(196/255, 0/255, 38/255),
    lg_quality
)


# 37
lg_clear_blue = get_clear_color(
    Vector(100/255, 0/255, 97/255),
    lg_quality
)


# 40
lg_clear_blue = get_clear_color(
    Vector(99/255, 89/255, 82/255),
    lg_quality
)


# 41
lg_clear_blue = get_clear_color(
    Vector(174/255, 239/255, 237/255),
    lg_quality
)


# 42
lg_clear_blue = get_clear_color(
    Vector(192/255, 255/255, 0/255),
    lg_quality
)


# 45
lg_clear_blue = get_clear_color(
    Vector(223/255, 102/255, 149/255),
    lg_quality
)


# 46
lg_clear_blue = get_clear_color(
    Vector(202/255, 176/255, 0/255),
    lg_quality
)


# 47




lg_clear = Texture(
    Pigment(Color(rgb=Vector(255/255, 255/255, 255/255)),
  #if (lg_quality > 1)
   filter=0.9
  #end
 ),
    Finish(lg_transparent_finish)
)

# 57
lg_clear_neon_orange = Texture(
    Pigment(Color(rgb=Vector(249/255, 96/255, 0/255)),
  #if (lg_quality > 1)
   filter 0.8
  #end
 ),
    Finish(lg_transparent_finish)
)

# 69
lg_bright_purple = Texture(
    Pigment(Color(rgb=Vector(205/255, 98/255, 152/255)), ),
    Finish(lg_solid_finish)
)

# 70
lg_reddish_brown = Texture(
    Pigment(Color(rgb=Vector(105/255, 64/255, 39/255)), ),
    Finish(lg_solid_finish)
)

# 71
lg_bluish_grey = Texture(
    Pigment(Color(rgb=Vector(163/255, 162/255, 164/255)), ),
    Finish(lg_solid_finish)
)

# 72
lg_dark_bluish_grey = Texture(
    Pigment(Color(rgb=Vector(99/255, 95/255, 97/255)), ),
    Finish(lg_solid_finish)
)

# 73
lg_medium_blue = Texture(
    Pigment(Color(rgb=Vector(110/255, 153/255, 201/255)), ),
    Finish(lg_solid_finish)
)

# 74
lg_medium_green = Texture(
    Pigment(Color(rgb=Vector(161/255, 196/255, 139/255)), ),
    Finish(lg_solid_finish)
)

# 77
lg_paradisa_pink = Texture(
    Pigment(Color(rgb=Vector(254/255, 204/255, 204/255)), ),
    Finish(lg_solid_finish)
)

# 78
lg_light_flesh = Texture(
    Pigment(Color(rgb=Vector(250/255, 215/255, 195/255)), ),
    Finish(lg_solid_finish)
)

# 85
lg_medium_violet = Texture(
    Pigment(Color(rgb=Vector(52/255, 43/255, 117/255)), ),
    Finish(lg_solid_finish)
)

# 86
lg_dark_flesh = Texture(
    Pigment(Color(rgb=Vector(124/255, 92/255, 69/255)), ),
    Finish(lg_solid_finish)
)

# 89
lg_royal_blue = Texture(
    Pigment(Color(rgb=Vector(155/255, 178/255, 239/255)), ),
    Finish(lg_solid_finish)
)

# 92
lg_flesh = Texture(
    Pigment(Color(rgb=Vector(204/255, 142/255, 104/255)), ),
    Finish(lg_solid_finish)
)

# 134
lg_pearl_copper = Texture(
    Pigment( colorColor(rgb=Vector(147/255, 135/255, 103/255)), ),
    Finish( lg_pearl_finish ),
)

# 135
lg_pearl_grey = Texture(
    Pigment( colorColor(rgb=Vector(171/255, 173/255, 172/255)), ),
    Finish( lg_pearl_finish ),
)

# 137
lg_pearl_blue = Texture(
    Pigment( colorColor(rgb=Vector(106/255, 122/255, 150/255)), ),
    Finish( lg_pearl_finish ),
)

# 142
lg_pearl_gold = Texture(
    Pigment( colorColor(rgb=Vector(215/255, 169/255, 75/255)), ),
    Finish( lg_pearl_finish ),
)

# 151
lg_very_light_bluish_grey = Texture(
    Pigment(Color(rgb=Vector(229/255, 228/255, 222/255)), ),
    Finish(lg_solid_finish)
)

# 272
lg_dark_blue = Texture(
    Pigment(Color(rgb=Vector(0/255, 29/255, 104/255)), ),
    Finish(lg_solid_finish)
)

# 288
lg_dark_green = Texture(
    Pigment(Color(rgb=Vector(39/255, 70/255, 44/255)), ),
    Finish(lg_solid_finish)
)

# 320
lg_dark_red = Texture(
    Pigment(Color(rgb=Vector(120/255, 0/255, 28/255)), ),
    Finish(lg_solid_finish)
)

# 313
lg_maersk_blue = Texture(
    Pigment(Color(rgb=Vector(53/255, 162/255, 189/255)), ),
    Finish(lg_solid_finish)
)

# 334
lg_gold_chrome = Texture(
    Pigment(Color(rgb=Vector(233/255, 110/255, 19/255)), ),
    Finish( lg_chrome_finish ),
)

# 373
lg_sand_purple = Texture(
    Pigment(Color(rgb=Vector(132/255, 94/255, 132/255)), ),
    Finish(lg_solid_finish)
)

# 335
lg_sand_red = Texture(
    Pigment(Color(rgb=Vector(191/255, 135/255, 130/255)), ),
    Finish(lg_solid_finish)
)

# 366
lg_earth_orange = Texture(
    Pigment(Color(rgb=Vector(209/255, 131/255, 4/255)), ),
    Finish(lg_solid_finish)
)

# 373
lg_sand_purple = Texture(
    Pigment(Color(rgb=Vector(132/255, 94/255, 132/255)), ),
    Finish(lg_solid_finish)
)

# 378
lg_sand_green = Texture(
    Pigment(Color(rgb=Vector(160/255, 188/255, 172/255)), ),
    Finish(lg_solid_finish)
)

# 379
lg_sand_blue = Texture(
    Pigment(Color(rgb=Vector(106/255, 122/255, 150/255)), ),
    Finish(lg_solid_finish)
)

# 383
lg_chrome = Texture(
    Pigment(Color(rgb=Vector(232/255, 232/255, 232/255)), ),
    Finish( lg_chrome_finish ),
)

# 462
lg_light_orange = Texture(
    Pigment(Color(rgb=Vector(254/255, 159/255, 6/255)), ),
    Finish(lg_solid_finish)
)

# 484
lg_dark_orange = Texture(
    Pigment(Color(rgb=Vector(179/255, 62/255, 0/255)), ),
    Finish(lg_solid_finish)
)

# 503
lg_very_light_grey = Texture(
    Pigment(Color(rgb=Vector(230/255, 227/255, 219/255)), ),
    Finish(lg_solid_finish)
)

# 999
lg_undefined = Texture(
    Pigment(Color(rgb=Vector(0.5, 0.7, 0.9> ),
)

# 998 (no code known)
lg_medium_orange = Texture(
    Pigment(Color(rgb=Vector(224/255, 129/255, 6/255)), ),
    Finish(lg_solid_finish)
)

#end
