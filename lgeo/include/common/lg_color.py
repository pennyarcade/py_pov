"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970623 Lutz Uhlmann
20070929 Lutz Uhlmann changed to use predefined finishes
20070929 Lutz Uhlmann changed to use RGB values from ldconfig.ldr
20071124 Lutz Uhlmann added LG_QUALITY for L3P compatibility

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_color: Color Definitions for LGEO POV-Ray Library
"""

from lgeo.config.lgeo_cfg import LG_QUALITY

from pov.basic.Color import Color
from pov.basic.Vector import Vector

# from pov.object_modifier.Interior import Interior

from pov.texture.Finish import Finish
# from pov.texture.Irid import Irid
from pov.texture.Pigment import Pigment
from pov.texture.Texture import Texture


if LG_QUALITY > 1:
    LG_SOLID_FINISH = Finish(
        ambient=0.1
    )
else:
    LG_SOLID_FINISH = Finish(
        ambient=0.1,
        phong=0.2,
        phong_size=20
    )


# if LG_QUALITY > 1:
#     LG_CHROME_FINISH = Finish(
#         ambient=0.25
#     )
# else:
#     LG_CHROME_FINISH = Finish(
#         ambient=0.25,
#         brilliance=5,
#         diffuse=0.6,
#         metallic=True,
#         specular=0.70,
#         roughness=1 / 100,
#         reflection=0.6,
#     )


# if LG_QUALITY > 1:
#     LG_PEARL_FINISH = Finish(
#         ambient=0.22
#     )
# else:
#     LG_PEARL_FINISH = Finish(
#         Irid(
#             0.2,
#             thickness=0.5,
#             turbulence=2.5
#         ),
#         ambient=0.22,
#         brilliance=2,
#         diffuse=0.6,
#         metallic=True,
#         specular=0.1,
#         roughness=32 / 100,
#         reflection=0.07
#     )


LG_TRANSPARENT_FINISH = Finish(
    ambient=0.3,
    diffuse=0.2,
    reflection=0.25,
    phong=0.3,
    phong_size=60
)

if LG_QUALITY > 1:
    LG_TRANSPARENT_FINISH = Finish(
        ambient=0.3
    )


# LG_IOR = Interior(
#     ior=1.4
# )


# 0
# LG_BLACK = Texture(
#     Pigment(Color(rgb=Vector(33 / 255.0, 33 / 255.0, 33 / 255.0))),
#     LG_SOLID_FINISH
# )

# 1
# LG_BLUE = Texture(
#     Pigment(Color(rgb=Vector(0 / 255.0, 51 / 255.0, 178 / 255.0))),
#     LG_SOLID_FINISH
# )

# 2
# LG_GREEN = Texture(
#     Pigment(Color(rgb=Vector(0 / 255.0, 140 / 255.0, 20 / 255.0))),
#     LG_SOLID_FINISH
# )

# 3
# LG_TEAL = Texture(
#     Pigment(Color(rgb=Vector(0 / 255.0, 153 / 255.0, 159 / 255.0))),
#     LG_SOLID_FINISH
# )
# LG_CYAN = LG_TEAL

# 4
LG_RED = Texture(
    Pigment(Color(rgb=Vector(196 / 255.0, 0 / 255.0, 38 / 255.0))),
    LG_SOLID_FINISH
)

# 5
# LG_DARK_PINK = Texture(
#     Pigment(Color(rgb=Vector(223 / 255.0, 102 / 255.0, 149 / 255.0))),
#     LG_SOLID_FINISH
# )

# 6
# LG_BROWN = Texture(
#     Pigment(Color(rgb=Vector(92 / 255.0, 32 / 255.0, 0 / 255.0))),
#     LG_SOLID_FINISH
# )

# 7
# LG_GREY = Texture(
#     Pigment(Color(rgb=Vector(193 / 255.0, 194 / 255.0, 193 / 255.0))),
#     LG_SOLID_FINISH
# )

# 8
# LG_DARK_GREY = Texture(
#     Pigment(Color(rgb=Vector(99 / 255.0, 89 / 255.0, 82 / 255.0))),
#     LG_SOLID_FINISH
# )

# 9
# LG_LIGHT_BLUE = Texture(
#     Pigment(Color(rgb=Vector(107 / 255.0, 172 / 255.0, 220 / 255.0))),
#     LG_SOLID_FINISH
# )

# 10
# LG_BRIGHT_GREEN = Texture(
#     Pigment(Color(rgb=Vector(97 / 255.0, 238 / 255.0, 104 / 255.0))),
#     LG_SOLID_FINISH
# )

# 11
# LG_TURQUOISE = Texture(
#     Pigment(Color(rgb=Vector(51 / 255.0, 166 / 255.0, 167 / 255.0))),
#     LG_SOLID_FINISH
# )
# LG_BLUE_GREEN = LG_TURQUOISE

# 12
# LG_SALMON = Texture(
#     Pigment(Color(rgb=Vector(255 / 255.0, 133 / 255.0, 122 / 255.0))),
#     LG_SOLID_FINISH
# )
# LG_LIGHT_RED = LG_SALMON

# 13
# LG_PINK = Texture(
#     Pigment(Color(rgb=Vector(249 / 255.0, 163 / 255.0, 198 / 255.0))),
#     LG_SOLID_FINISH
# )
# LG_ROSE = LG_PINK

# 14
LG_YELLOW = Texture(
    Pigment(Color(rgb=Vector(1, 220 / 255.0, 0 / 255.0))),
    LG_SOLID_FINISH
)

# 15
LG_WHITE = Texture(
    Pigment(Color(rgb=Vector(255 / 255.0, 255 / 255.0, 255 / 255.0))),
    LG_SOLID_FINISH
)

# 17
# LG_LIGHT_GREEN = Texture(
#     Pigment(Color(rgb=Vector(186 / 255.0, 255 / 255.0, 206 / 255.0))),
#     LG_SOLID_FINISH
# )

# 18
# LG_LIGHT_YELLOW = Texture(
#     Pigment(Color(rgb=Vector(253 / 255.0, 232 / 255.0, 150 / 255.0))),
#     LG_SOLID_FINISH
# )

# 19
# LG_TAN = Texture(
#     Pigment(Color(rgb=Vector(232 / 255.0, 207 / 255.0, 161 / 255.0))),
#     LG_SOLID_FINISH
# )

# 20
# LG_LIGHT_VIOLET = Texture(
#     Pigment(Color(rgb=Vector(215 / 255.0, 196 / 255.0, 230 / 255.0))),
#     LG_SOLID_FINISH
# )

# 22
# LG_PURPLE = Texture(
#     Pigment(Color(rgb=Vector(129 / 255.0, 0 / 255.0, 124 / 255.0))),
#     LG_SOLID_FINISH
# )
# LG_VIOLET = LG_PURPLE

# 23
# LG_VIOLET_BLUE = Texture(
#     Pigment(Color(rgb=Vector(71 / 255.0, 50 / 255.0, 176 / 255.0))),
#     LG_SOLID_FINISH
# )

# 25
# LG_ORANGE = Texture(
#     Pigment(Color(rgb=Vector(249 / 255.0, 96 / 255.0, 0 / 255.0))),
#     LG_SOLID_FINISH
# )

# 26
# LG_MAGENTA = Texture(
#     Pigment(Color(rgb=Vector(232 / 255.0, 27 / 255.0, 109 / 255.0))),
#     LG_SOLID_FINISH
# )

# 27
# LG_LIME = Texture(
#     Pigment(Color(rgb=Vector(231 / 255.0, 240 / 255.0, 0 / 255.0))),
#     LG_SOLID_FINISH
# )

# 27
# LG_DARK_TAN = Texture(
#     Pigment(Color(rgb=Vector(187 / 255.0, 141 / 255.0, 75 / 255.0))),
#     LG_SOLID_FINISH
# )

# 29
# LG_LIGHT_PURPLE = Texture(
#     Pigment(Color(rgb=Vector(205 / 255.0, 173 / 255.0, 200 / 255.0))),
#     LG_SOLID_FINISH
# )


# Helper to build complex colors
def get_clear_color(cvector, quality):
    """@Todo: DocString."""
    if quality > 1:
        return Texture(
            Pigment(
                Color(rgb=cvector),
                filter=0.9
            ),
            LG_TRANSPARENT_FINISH
        )
    else:
        return Texture(
            Pigment(
                Color(rgb=cvector)
            ),
            LG_TRANSPARENT_FINISH
        )


# 33
# LG_CLEAR_BLUE = get_clear_color(
#     Vector(0 / 255.0, 32 / 255.0, 160 / 255.0),
#     LG_QUALITY
# )
# @Todo: Check Constant name

# 34
# LG_CLEAR_GREEN = get_clear_color(
#     Vector(6 / 255.0, 98 / 255.0, 50 / 255.0),
#     LG_QUALITY
# )
# @Todo: Check Constant name


# 36
# LG_CLEAR_RED = get_clear_color(
#     Vector(196 / 255.0, 0 / 255.0, 38 / 255.0),
#     LG_QUALITY
# )


# 37
# LG_CLEAR_VIOLET = get_clear_color(
#     Vector(100 / 255.0, 0 / 255.0, 97 / 255.0),
#     LG_QUALITY
# )


# 40
# LG_CLEAR_BROWN = get_clear_color(
#     Vector(99 / 255.0, 89 / 255.0, 82 / 255.0),
#     LG_QUALITY
# )


# 41
# LG_CLEAR_CYAN = get_clear_color(
#     Vector(174 / 255.0, 239 / 255.0, 237 / 255.0),
#     LG_QUALITY
# )


# 42
# LG_CLEAR_NEON_YELLOW = get_clear_color(
#     Vector(192 / 255.0, 255 / 255.0, 0 / 255.0),
#     LG_QUALITY
# )


# 45
# LG_CLEAR_PINK = get_clear_color(
#     Vector(223 / 255.0, 102 / 255.0, 149 / 255.0),
#     LG_QUALITY
# )


# 46
LG_CLEAR_YELLOW = get_clear_color(
    Vector(202 / 255.0, 176 / 255.0, 0 / 255.0),
    LG_QUALITY
)


# 47
# LG_CLEAR = get_clear_color(
#     Vector(255 / 255.0, 255 / 255.0, 255 / 255.0),
#     LG_QUALITY
# )


# 57
# LG_CLEAR_NEON_ORANGE = get_clear_color(
#     Vector(249 / 255.0, 96 / 255.0, 0 / 255.0),
#     LG_QUALITY
# )


# 69
# LG_BRIGHT_PURPLE = Texture(
#     Pigment(Color(rgb=Vector(205 / 255.0, 98 / 255.0, 152 / 255.0))),
#     LG_SOLID_FINISH
# )


# 70
# LG_REDDISH_BROWN = Texture(
#     Pigment(Color(rgb=Vector(105 / 255.0, 64 / 255.0, 39 / 255.0))),
#     LG_SOLID_FINISH
# )


# 71
# LG_BLUISH_GREY = Texture(
#     Pigment(Color(rgb=Vector(163 / 255.0, 162 / 255.0, 164 / 255.0))),
#     LG_SOLID_FINISH
# )


# 72
# LG_DARK_BLUISH_GREY = Texture(
#     Pigment(Color(rgb=Vector(99 / 255.0, 95 / 255.0, 97 / 255.0))),
#     LG_SOLID_FINISH
# )


# 73
# LG_MEDIUM_BLUE = Texture(
#     Pigment(Color(rgb=Vector(110 / 255.0, 153 / 255.0, 201 / 255.0))),
#     LG_SOLID_FINISH
# )


# 74
# LG_MEDIUM_GREEN = Texture(
#     Pigment(Color(rgb=Vector(161 / 255.0, 196 / 255.0, 139 / 255.0))),
#     LG_SOLID_FINISH
# )


# 77
# LG_PARADISA_PINK = Texture(
#     Pigment(Color(rgb=Vector(254 / 255.0, 204 / 255.0, 204 / 255.0))),
#     LG_SOLID_FINISH
# )


# 78
# LG_LIGHT_FLESH = Texture(
#     Pigment(Color(rgb=Vector(250 / 255.0, 215 / 255.0, 195 / 255.0))),
#     LG_SOLID_FINISH
# )


# 85
# LG_MEDIUM_VIOLET = Texture(
#     Pigment(Color(rgb=Vector(52 / 255.0, 43 / 255.0, 117 / 255.0))),
#     LG_SOLID_FINISH
# )


# 86
# LG_DARK_FLESH = Texture(
#     Pigment(Color(rgb=Vector(124 / 255.0, 92 / 255.0, 69 / 255.0))),
#     LG_SOLID_FINISH
# )


# 89
# LG_ROYAL_BLUE = Texture(
#     Pigment(Color(rgb=Vector(155 / 255.0, 178 / 255.0, 239 / 255.0))),
#     LG_SOLID_FINISH
# )


# 92
# LG_FLESH = Texture(
#     Pigment(Color(rgb=Vector(204 / 255.0, 142 / 255.0, 104 / 255.0))),
#     LG_SOLID_FINISH
# )


# 134
# LG_PEARL_COPPER = Texture(
#     Pigment(Color(rgb=Vector(147 / 255.0, 135 / 255.0, 103 / 255.0))),
#     LG_PEARL_FINISH,
# )


# 135
# LG_PEARL_GREY = Texture(
#     Pigment(Color(rgb=Vector(171 / 255.0, 173 / 255.0, 172 / 255.0))),
#     LG_PEARL_FINISH,
# )


# 137
# LG_PEARL_BLUE = Texture(
#     Pigment(Color(rgb=Vector(106 / 255.0, 122 / 255.0, 150 / 255.0))),
#     LG_PEARL_FINISH,
# )


# 142
# LG_PEARL_GOLD = Texture(
#     Pigment(Color(rgb=Vector(215 / 255.0, 169 / 255.0, 75 / 255.0))),
#     LG_PEARL_FINISH,
# )


# 151
# LG_VERY_LIGHT_BLUISH_GREY = Texture(
#     Pigment(Color(rgb=Vector(229 / 255.0, 228 / 255.0, 222 / 255.0))),
#     LG_SOLID_FINISH
# )


# 272
# LG_DARK_BLUE = Texture(
#     Pigment(Color(rgb=Vector(0 / 255.0, 29 / 255.0, 104 / 255.0))),
#     LG_SOLID_FINISH
# )


# 288
# LG_DARK_GREEN = Texture(
#     Pigment(Color(rgb=Vector(39 / 255.0, 70 / 255.0, 44 / 255.0))),
#     LG_SOLID_FINISH
# )


# 320
# LG_DARK_RED = Texture(
#     Pigment(Color(rgb=Vector(120 / 255.0, 0 / 255.0, 28 / 255.0))),
#     LG_SOLID_FINISH
# )


# 313
# LG_MAERSK_BLUE = Texture(
#     Pigment(Color(rgb=Vector(53 / 255.0, 162 / 255.0, 189 / 255.0))),
#     LG_SOLID_FINISH
# )


# 334
# LG_GOLD_CHROME = Texture(
#     Pigment(Color(rgb=Vector(233 / 255.0, 110 / 255.0, 19 / 255.0))),
#     LG_CHROME_FINISH,
# )


# 373
# LG_SAND_PURPLE = Texture(
#     Pigment(Color(rgb=Vector(132 / 255.0, 94 / 255.0, 132 / 255.0))),
#     LG_SOLID_FINISH
# )


# 335
# LG_SAND_RED = Texture(
#     Pigment(Color(rgb=Vector(191 / 255.0, 135 / 255.0, 130 / 255.0))),
#     LG_SOLID_FINISH
# )


# 366
# LG_EARTH_ORANGE = Texture(
#     Pigment(Color(rgb=Vector(209 / 255.0, 131 / 255.0, 4 / 255.0))),
#     LG_SOLID_FINISH
# )


# 373
# LG_SAND_PURPLE = Texture(
#     Pigment(Color(rgb=Vector(132 / 255.0, 94 / 255.0, 132 / 255.0))),
#     LG_SOLID_FINISH
# )


# 378
# LG_SAND_GREEN = Texture(
#     Pigment(Color(rgb=Vector(160 / 255.0, 188 / 255.0, 172 / 255.0))),
#     LG_SOLID_FINISH
# )


# 379
# LG_SAND_BLUE = Texture(
#     Pigment(Color(rgb=Vector(106 / 255.0, 122 / 255.0, 150 / 255.0))),
#     LG_SOLID_FINISH
# )

# 383
# LG_CHROME = Texture(
#     Pigment(Color(rgb=Vector(232 / 255.0, 232 / 255.0, 232 / 255.0))),
#     Finish(LG_CHROME_FINISH),
# )


# 462
# LG_LIGHT_ORANGE = Texture(
#     Pigment(Color(rgb=Vector(254 / 255.0, 159 / 255.0, 6 / 255.0))),
#     LG_SOLID_FINISH
# )


# 484
# LG_DARK_ORANGE = Texture(
#     Pigment(Color(rgb=Vector(179 / 255.0, 62 / 255.0, 0 / 255.0))),
#     LG_SOLID_FINISH
# )


# 503
# LG_VERY_LIGHT_GREY = Texture(
#     Pigment(Color(rgb=Vector(230 / 255.0, 227 / 255.0, 219 / 255.0))),
#     LG_SOLID_FINISH
# )


# 999
# LG_UNDEFINED = Texture(
#     Pigment(Color(rgb=Vector(0.5, 0.7, 0.9))),
# )


# 998 (no code known)
# LG_MEDIUM_ORANGE = Texture(
#     Pigment(Color(rgb=Vector(224 / 255.0, 129 / 255.0, 6 / 255.0))),
#     LG_SOLID_FINISH
# )
