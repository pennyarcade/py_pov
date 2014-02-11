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

from pov.basic.Color import Color
from pov.basic.Vector import Vector

from pov.include.colors_inc import *

from pov.object_modifier.Interior import Interior

from pov.texture.Finish import Finish
from pov.texture.Irid import Irid
from pov.texture.Pigment import Pigment
from pov.texture.Texture import Texture


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
        Irid(
            0.2,
            thickness=0.5,
            turbulence=2.5
        ),
        ambient=0.22,
        brilliance=2,
        diffuse=0.6,
        metallic=True,
        specular=0.1,
        roughness=32/100,
        reflection=0.07
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
    Pigment(Color(rgb=Vector(33/255.0, 33/255.0, 33/255.0))),
    lg_solid_finish
)

# 1
lg_blue = Texture(
    Pigment(Color(rgb=Vector(0/255.0, 51/255.0, 178/255.0))),
    lg_solid_finish
)

# 2
lg_green = Texture(
    Pigment(Color(rgb=Vector(0/255.0, 140/255.0, 20/255.0))),
    lg_solid_finish
)

# 3
lg_teal = Texture(
    Pigment(Color(rgb=Vector(0/255.0, 153/255.0, 159/255.0))),
    lg_solid_finish
)
lg_cyan = lg_teal

# 4
lg_red = Texture(
    Pigment(Color(rgb=Vector(196/255.0, 0/255.0, 38/255.0))),
    lg_solid_finish
)

# 5
lg_dark_pink = Texture(
    Pigment(Color(rgb=Vector(223/255.0, 102/255.0, 149/255.0))),
    lg_solid_finish
)

# 6
lg_brown = Texture(
    Pigment(Color(rgb=Vector(92/255.0, 32/255.0, 0/255.0))),
    lg_solid_finish
)

# 7
lg_grey = Texture(
    Pigment(Color(rgb=Vector(193/255.0, 194/255.0, 193/255.0))),
    lg_solid_finish
)

# 8
lg_dark_grey = Texture(
    Pigment(Color(rgb=Vector(99/255.0, 89/255.0, 82/255.0))),
    lg_solid_finish
)

# 9
lg_light_blue = Texture(
    Pigment(Color(rgb=Vector(107/255.0, 172/255.0, 220/255.0))),
    lg_solid_finish
)

# 10
lg_bright_green = Texture(
    Pigment(Color(rgb=Vector(97/255.0, 238/255.0, 104/255.0))),
    lg_solid_finish
)

# 11
lg_turquoise = Texture(
    Pigment(Color(rgb=Vector(51/255.0, 166/255.0, 167/255.0))),
    lg_solid_finish
)
lg_blue_green = lg_turquoise

# 12
lg_salmon = Texture(
    Pigment(Color(rgb=Vector(255/255.0, 133/255.0, 122/255.0))),
    lg_solid_finish
)
lg_light_red = lg_salmon

# 13
lg_pink = Texture(
    Pigment(Color(rgb=Vector(249/255.0, 163/255.0, 198/255.0))),
    lg_solid_finish
)
lg_rose = lg_pink

# 14
lg_yellow = Texture(
    Pigment(Color(rgb=Vector(1, 220/255.0, 0/255.0))),
    lg_solid_finish
)

# 15
lg_white = Texture(
    Pigment(Color(rgb=Vector(255/255.0, 255/255.0, 255/255.0))),
    lg_solid_finish
)

# 17
lg_light_green = Texture(
    Pigment(Color(rgb=Vector(186/255.0, 255/255.0, 206/255.0))),
    lg_solid_finish
)

# 18
lg_light_yellow = Texture(
    Pigment(Color(rgb=Vector(253/255.0, 232/255.0, 150/255.0))),
    lg_solid_finish
)

# 19
lg_tan = Texture(
    Pigment(Color(rgb=Vector(232/255.0, 207/255.0, 161/255.0))),
    lg_solid_finish
)

# 20
lg_light_violet = Texture(
    Pigment(Color(rgb=Vector(215/255.0, 196/255.0, 230/255.0))),
    lg_solid_finish
)

# 22
lg_purple = Texture(
    Pigment(Color(rgb=Vector(129/255.0, 0/255.0, 124/255.0))),
    lg_solid_finish
)
lg_violet = lg_purple

# 23
lg_violet_blue = Texture(
    Pigment(Color(rgb=Vector(71/255.0, 50/255.0, 176/255.0))),
    lg_solid_finish
)

# 25
lg_orange = Texture(
    Pigment(Color(rgb=Vector(249/255.0, 96/255.0, 0/255.0))),
    lg_solid_finish
)

# 26
lg_magenta = Texture(
    Pigment(Color(rgb=Vector(232/255.0, 27/255.0, 109/255.0))),
    lg_solid_finish
)

# 27
lg_lime = Texture(
    Pigment(Color(rgb=Vector(231/255.0, 240/255.0, 0/255.0))),
    lg_solid_finish
)

# 27
lg_dark_tan = Texture(
    Pigment(Color(rgb=Vector(187/255.0, 141/255.0, 75/255.0))),
    lg_solid_finish
)

# 29
lg_light_purple = Texture(
    Pigment(Color(rgb=Vector(205/255.0, 173/255.0, 200/255.0))),
    lg_solid_finish
)


# Helper to build complex colors
def get_clear_color(cvector, quality):
    if (quality > 1):
        return Texture(
            Pigment(
                Color(rgb=cvector),
                filter=0.9
            ),
            lg_transparent_finish
        )
    else:
        return Texture(
            Pigment(
                Color(rgb=cvector)
            ),
            lg_transparent_finish
        )


# 33
lg_clear_blue = get_clear_color(
    Vector(0/255.0, 32/255.0, 160/255.0),
    lg_quality
)


#34
lg_clear_blue = get_clear_color(
    Vector(6/255.0, 98/255.0, 50/255.0),
    lg_quality
)


# 36
lg_clear_blue = get_clear_color(
    Vector(196/255.0, 0/255.0, 38/255.0),
    lg_quality
)


# 37
lg_clear_blue = get_clear_color(
    Vector(100/255.0, 0/255.0, 97/255.0),
    lg_quality
)


# 40
lg_clear_blue = get_clear_color(
    Vector(99/255.0, 89/255.0, 82/255.0),
    lg_quality
)


# 41
lg_clear_blue = get_clear_color(
    Vector(174/255.0, 239/255.0, 237/255.0),
    lg_quality
)


# 42
lg_clear_blue = get_clear_color(
    Vector(192/255.0, 255/255.0, 0/255.0),
    lg_quality
)


# 45
lg_clear_blue = get_clear_color(
    Vector(223/255.0, 102/255.0, 149/255.0),
    lg_quality
)


# 46
lg_clear_blue = get_clear_color(
    Vector(202/255.0, 176/255.0, 0/255.0),
    lg_quality
)


# 47
lg_clear = get_clear_color(
    Vector(255/255.0, 255/255.0, 255/255.0),
    lg_quality
)


# 57
lg_clear_neon_orange = get_clear_color(
    Vector(249/255.0, 96/255.0, 0/255.0),
    lg_quality
)


# 69
lg_bright_purple = Texture(
    Pigment(Color(rgb=Vector(205/255.0, 98/255.0, 152/255.0))),
    lg_solid_finish
)


# 70
lg_reddish_brown = Texture(
    Pigment(Color(rgb=Vector(105/255.0, 64/255.0, 39/255.0))),
    lg_solid_finish
)


# 71
lg_bluish_grey = Texture(
    Pigment(Color(rgb=Vector(163/255.0, 162/255.0, 164/255.0))),
    lg_solid_finish
)


# 72
lg_dark_bluish_grey = Texture(
    Pigment(Color(rgb=Vector(99/255.0, 95/255.0, 97/255.0))),
    lg_solid_finish
)


# 73
lg_medium_blue = Texture(
    Pigment(Color(rgb=Vector(110/255.0, 153/255.0, 201/255.0))),
    lg_solid_finish
)


# 74
lg_medium_green = Texture(
    Pigment(Color(rgb=Vector(161/255.0, 196/255.0, 139/255.0))),
    lg_solid_finish
)


# 77
lg_paradisa_pink = Texture(
    Pigment(Color(rgb=Vector(254/255.0, 204/255.0, 204/255.0))),
    lg_solid_finish
)


# 78
lg_light_flesh = Texture(
    Pigment(Color(rgb=Vector(250/255.0, 215/255.0, 195/255.0))),
    lg_solid_finish
)


# 85
lg_medium_violet = Texture(
    Pigment(Color(rgb=Vector(52/255.0, 43/255.0, 117/255.0))),
    lg_solid_finish
)


# 86
lg_dark_flesh = Texture(
    Pigment(Color(rgb=Vector(124/255.0, 92/255.0, 69/255.0))),
    lg_solid_finish
)


# 89
lg_royal_blue = Texture(
    Pigment(Color(rgb=Vector(155/255.0, 178/255.0, 239/255.0))),
    lg_solid_finish
)


# 92
lg_flesh = Texture(
    Pigment(Color(rgb=Vector(204/255.0, 142/255.0, 104/255.0))),
    lg_solid_finish
)


# 134
lg_pearl_copper = Texture(
    Pigment(Color(rgb=Vector(147/255.0, 135/255.0, 103/255.0))),
    lg_pearl_finish,
)


# 135
lg_pearl_grey = Texture(
    Pigment(Color(rgb=Vector(171/255.0, 173/255.0, 172/255.0))),
    lg_pearl_finish,
)


# 137
lg_pearl_blue = Texture(
    Pigment(Color(rgb=Vector(106/255.0, 122/255.0, 150/255.0))),
    lg_pearl_finish,
)


# 142
lg_pearl_gold = Texture(
    Pigment(Color(rgb=Vector(215/255.0, 169/255.0, 75/255.0))),
    lg_pearl_finish,
)


# 151
lg_very_light_bluish_grey = Texture(
    Pigment(Color(rgb=Vector(229/255.0, 228/255.0, 222/255.0))),
    lg_solid_finish
)


# 272
lg_dark_blue = Texture(
    Pigment(Color(rgb=Vector(0/255.0, 29/255.0, 104/255.0))),
    lg_solid_finish
)


# 288
lg_dark_green = Texture(
    Pigment(Color(rgb=Vector(39/255.0, 70/255.0, 44/255.0))),
    lg_solid_finish
)


# 320
lg_dark_red = Texture(
    Pigment(Color(rgb=Vector(120/255.0, 0/255.0, 28/255.0))),
    lg_solid_finish
)


# 313
lg_maersk_blue = Texture(
    Pigment(Color(rgb=Vector(53/255.0, 162/255.0, 189/255.0))),
    lg_solid_finish
)


# 334
lg_gold_chrome = Texture(
    Pigment(Color(rgb=Vector(233/255.0, 110/255.0, 19/255.0))),
    lg_chrome_finish,
)


# 373
lg_sand_purple = Texture(
    Pigment(Color(rgb=Vector(132/255.0, 94/255.0, 132/255.0))),
    lg_solid_finish
)


# 335
lg_sand_red = Texture(
    Pigment(Color(rgb=Vector(191/255.0, 135/255.0, 130/255.0))),
    lg_solid_finish
)


# 366
lg_earth_orange = Texture(
    Pigment(Color(rgb=Vector(209/255.0, 131/255.0, 4/255.0))),
    lg_solid_finish
)


# 373
lg_sand_purple = Texture(
    Pigment(Color(rgb=Vector(132/255.0, 94/255.0, 132/255.0))),
    lg_solid_finish
)


# 378
lg_sand_green = Texture(
    Pigment(Color(rgb=Vector(160/255.0, 188/255.0, 172/255.0))),
    lg_solid_finish
)


# 379
lg_sand_blue = Texture(
    Pigment(Color(rgb=Vector(106/255.0, 122/255.0, 150/255.0))),
    lg_solid_finish
)

# 383
lg_chrome = Texture(
    Pigment(Color(rgb=Vector(232/255.0, 232/255.0, 232/255.0))),
    Finish( lg_chrome_finish ),
)


# 462
lg_light_orange = Texture(
    Pigment(Color(rgb=Vector(254/255.0, 159/255.0, 6/255.0))),
    lg_solid_finish
)


# 484
lg_dark_orange = Texture(
    Pigment(Color(rgb=Vector(179/255.0, 62/255.0, 0/255.0))),
    lg_solid_finish
)


# 503
lg_very_light_grey = Texture(
    Pigment(Color(rgb=Vector(230/255.0, 227/255.0, 219/255.0))),
    lg_solid_finish
)


# 999
lg_undefined = Texture(
    Pigment(Color(rgb=Vector(0.5, 0.7, 0.9))),
)


# 998 (no code known)
lg_medium_orange = Texture(
    Pigment(Color(rgb=Vector(224/255.0, 129/255.0, 6/255.0))),
    lg_solid_finish
)
