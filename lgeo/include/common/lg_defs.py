"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970623 Lutz Uhlmann
2002xxxx Lutz Uhlmann added LGEO logo derived from Larc C. Hassings L3Logo
20071112 Lutz Uhlmann added lg_knob_dot for patterned baseplates
20071124 Lutz Uhlmann added lg_quality for L3P comptibility
20071129 Lutz Uhlmann added lg_tech_knob_logo for lg_quality > 3
20080229 Lutz Uhlmann added lg_test variable for development
20080720 Lutz Uhlmann added lg_studs variable

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_defs: Definitions of standard sub-parts and sizes
"""

from lgeo.config.lgeo_cfg import LG_STUD_LOGO
from lgeo.config.lgeo_cfg import LG_QUALITY

from pov.csg.Difference import Difference
from pov.csg.Intersection import Intersection
from pov.csg.Merge import Merge
from pov.csg.Union import Union

from pov.basic.Vector import *

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere
from pov.finite_solid.Torus import Torus

from pov.infinite_solid.Plane import Plane

from pov.object_modifier.ClippedBy import ClippedBy
from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Scale import Scale
from pov.object_modifier.Translate import Translate

from pov.other.Object import Object

# **********************************************************************
#  Dimensions
# **********************************************************************

LG_KNOB_RADIUS = 0.24
LG_KNOB_HEIGHT = 0.16
LG_KNOB_HEIGHT_LOGO = 0.16
LG_KNOB_INNER_RADIUS = 0.16
LG_WALL_WIDTH = 0.16
LG_BRICK_WIDTH = 0.8
LG_BRICK_HEIGHT = 0.96
LG_BRICK_INNER_HEIGHT = 0.84
LG_PLATE_HEIGHT = 0.32
LG_PLATE_INNER_HEIGHT = 0.2
LG_TOP_HEIGHT = LG_BRICK_HEIGHT - LG_BRICK_INNER_HEIGHT
LG_CYLINDER_RADIUS = (sqrt(2) * LG_BRICK_WIDTH / 2 - LG_KNOB_RADIUS)
LG_CYLINDER_WALL_WIDTH = (LG_CYLINDER_RADIUS - LG_KNOB_RADIUS)
LG_CORNER_SPACE = 0.016   # 0.025
LG_KNOB_CORNER_SPACE = LG_CORNER_SPACE * 1.5
LG_CROSSAXLE_WIDTH = 0.18
LG_GRID_WIDTH = LG_BRICK_WIDTH / sqrt(2) - 2 * LG_KNOB_RADIUS
LG_E = 0.01


"""
Custom Shorthands
"""
LDU = 0.8 / 20
LGBW = LG_BRICK_WIDTH
LGBH = LG_BRICK_HEIGHT
LGPH = LG_PLATE_HEIGHT


"""
*  Stud Logo
*
*  Declare lg_quality < 3 if you do not want the LGEO logo on the studs.
*  Remove the translate statements to rearrange letters of logo...
*
"""


def lego_logo_text():
    """@Todo: ApiDoc."""
    letter_e = Union(
        # Letter E
        Sphere(Vector(-59, 0, -36), 6),
        Cylinder(Vector(-59, 0, -36), Vector(-59, 0, 1), 6),
        Sphere(Vector(-59, 0, 1), 6),
        Cylinder(Vector(0, 0, -49), Vector(0, 0, -25), 6),
        Sphere(Vector(0, 0, -25), 6),
        Sphere(Vector(59, 0, -62), 6),
        Cylinder(Vector(59, 0, -62), Vector(59, 0, -24), 6),
        Sphere(Vector(59, 0, -24), 6),
        Cylinder(Vector(-59, 0, -36), Vector(59, 0, -62), 6),
    ),
    if LG_STUD_LOGO > 0:
        letter_e.append(
            Translate(Vector(0, 0, 60))
        )

    letter_g = Union(
        # Letter G
        Sphere(Vector(-35.95, 0, 57), 6),
        Torus(
            18.45, 6,
            ClippedBy(Plane(Vector(40, 0, -9), 0)),
            Translate(Vector(-40, 0, 39))
        ),
        Cylinder(Vector(-44.05, 0, 21), Vector(35.95, 0, 3), 6),
        Torus(
            18.45, 6,
            ClippedBy(Plane(Vector(-40, 0, 9), 0),),
            Translate(Vector(40, 0, 21))
        ),
        Cylinder(Vector(44.05, 0, 39), Vector(0, 0, 49), 6),
        Sphere(Vector(0, 0, 49), 6),
        Cylinder(Vector(0, 0, 49), Vector(0, 0, 34), 6),
        Sphere(Vector(0, 0, 34), 6),
    )
    if LG_STUD_LOGO > 0:
        letter_g.append(
            Translate(Vector(0, 0, -65))
        )

    if LG_QUALITY > 2:
        return Union(
            Union(
                # Letter L
                Sphere(Vector(-59, 0, -96), 6),
                Cylinder(Vector(-59, 0, -96), Vector(59, 0, -122), 6),
                Sphere(Vector(59, 0, -122), 6),
                Cylinder(Vector(59, 0, -122), Vector(59, 0, -84), 6),
                Sphere(Vector(59, 0, -84), 6),
            ),
            letter_e,
            letter_g,
            Union(
                # Letter O
                Torus(
                    18.45, 6,
                    ClippedBy(Plane(Vector(40, 0, -9), 0)),
                    Translate(Vector(-40, 0, 99))
                ),
                Cylinder(Vector(-44.05, 0, 81), Vector(35.95, 0, 63), 6),
                Torus(
                    18.45, 6,
                    ClippedBy(Plane(Vector(-40, 0, 9), 0)),
                    Translate(Vector(40, 0, 81))
                ),
                Cylinder(Vector(44.05, 0, 99), Vector(-35.95, 0, 117), 6),
            ),
            Scale(Vector(4.5/128, 4.5/128, 4.5/128)),
            Rotate(y*90),
            Rotate(x*-90),
            Scale(Vector(-1, 1, 1)),
            Scale(Vector(1, 1, 1) * .08 * LG_KNOB_RADIUS * 2)
        )
    else:
        return Object()


def lego_logo_text_clear():
    """@Todo: ApiDoc."""
    letter_e = Merge(
        # Letter E
        Sphere(Vector(-59, 0, -36), 6),
        Cylinder(Vector(-59, 0, -36), Vector(-59, 0, 1), 6),
        Sphere(Vector(-59, 0, 1), 6),
        Cylinder(Vector(0, 0, -49), Vector(0, 0, -25), 6),
        Sphere(Vector(0, 0, -25), 6),
        Sphere(Vector(59, 0, -62), 6),
        Cylinder(Vector(59, 0, -62), Vector(59, 0, -24), 6),
        Sphere(Vector(59, 0, -24), 6),
        Cylinder(Vector(-59, 0, -36), Vector(59, 0, -62), 6),
    ),
    if LG_STUD_LOGO > 0:
        letter_e.append(
            Translate(Vector(0, 0, 60))
        )

    letter_g = Merge(
        # Letter G
        Sphere(Vector(-35.95, 0, 57), 6),
        Torus(
            18.45, 6,
            ClippedBy(Plane(Vector(40, 0, -9), 0)),
            Translate(Vector(-40, 0, 39))
        ),
        Cylinder(Vector(-44.05, 0, 21), Vector(35.95, 0, 3), 6),
        Torus(
            18.45, 6,
            ClippedBy(Plane(Vector(-40, 0, 9), 0)),
            Translate(Vector(40, 0, 21))
        ),
        Cylinder(Vector(44.05, 0, 39), Vector(0, 0, 49), 6),
        Sphere(Vector(0, 0, 49), 6),
        Cylinder(Vector(0, 0, 49), Vector(0, 0, 34), 6),
        Sphere(Vector(0, 0, 34), 6),
    ),
    if LG_STUD_LOGO > 0:
        letter_g.append(
            Translate(Vector(0, 0, -65))
        )

    return Merge(
        Merge(
            # Letter L
            Sphere(Vector(-59, 0, -96), 6),
            Cylinder(Vector(-59, 0, -96), Vector(59, 0, -122), 6),
            Sphere(Vector(59, 0, -122), 6),
            Cylinder(Vector(59, 0, -122), Vector(59, 0, -84), 6),
            Sphere(Vector(59, 0, -84), 6),
        ),
        letter_e,
        letter_g,
        Merge(
            # Letter O
            Torus(
                18.45, 6,
                ClippedBy(Plane(Vector(40, 0, -9), 0)),
                Translate(Vector(-40, 0, 99))
            ),
            Cylinder(Vector(-44.05, 0, 81), Vector(35.95, 0, 63), 6),
            Torus(
                18.45, 6,
                ClippedBy(Plane(Vector(-40, 0, 9), 0)),
                Translate(Vector(40, 0, 81))
            ),
            Cylinder(Vector(44.05, 0, 99), Vector(-35.95, 0, 117), 6),
        ),
        Scale(4.5 / 128),
        Rotate(y * 90),
        Rotate(x * -90),
        Scale(Vector(-1, 1, 1)),
        Scale(.08 * LG_KNOB_RADIUS * 2)
    ),


# ***
# LGEO Primitives
# ***


# solid stud
def lg_knob():
    """@Todo: ApiDoc."""
    result = Union(
        Union(
            Cylinder(
                Vector(0, 0, LG_KNOB_HEIGHT - LG_KNOB_CORNER_SPACE),
                Vector(0, 0, -LG_E),
                (LG_KNOB_RADIUS)
            ),
            Cylinder(
                Vector(0, 0, LG_KNOB_HEIGHT),
                Vector(0, 0, -LG_E),
                (LG_KNOB_RADIUS - LG_KNOB_CORNER_SPACE)
            ),
        ),
        Torus(
            (LG_KNOB_RADIUS - LG_KNOB_CORNER_SPACE),
            (LG_KNOB_CORNER_SPACE),
            Rotate(Vector(90, 0, 0)),
            Translate(Vector(0, 0, (LG_KNOB_HEIGHT - LG_KNOB_CORNER_SPACE)))
        )
    )

    if LG_QUALITY > 2:
        result.append(
            Object(
                lego_logo_text(),
                Translate(Vector(0, 0, LG_KNOB_HEIGHT))
            )
        )

    return result


# solid stud top for dotted baseplates
lg_knob_dot = Intersection(
    Object(
        lg_knob(),
        Translate(Vector(0, 0, 0.001))
    ),
    Cylinder(
        Vector(0, 0, LG_KNOB_HEIGHT - 0.001),
        Vector(0, 0, LG_KNOB_HEIGHT + 0.1),
        LG_KNOB_INNER_RADIUS
    )
)


# hollow stud
lg_tech_knob = Union(
    Difference(
        Union(
            Cylinder(
                Vector(0, 0, LG_KNOB_HEIGHT - LG_CORNER_SPACE),
                Vector(0, 0, -LG_E),
                (LG_KNOB_RADIUS)
            ),
            Difference(
                Cylinder(
                    Vector(0, 0, LG_KNOB_HEIGHT),
                    Vector(0, 0, -LG_E),
                    (LG_KNOB_RADIUS - LG_CORNER_SPACE)
                ),
                Cylinder(
                    Vector(0, 0, LG_KNOB_HEIGHT + LG_E),
                    Vector(0, 0, -2 * LG_E),
                    (LG_KNOB_INNER_RADIUS + LG_CORNER_SPACE)
                )
            )
        ),
        Cylinder(
            Vector(0, 0, (LG_KNOB_HEIGHT + 2 * LG_E)),
            Vector(0, 0, -3 * LG_E),
            (LG_KNOB_INNER_RADIUS)
        )
    ),
    Torus(
        (LG_KNOB_INNER_RADIUS + LG_CORNER_SPACE),
        (LG_CORNER_SPACE),
        Rotate(Vector(90, 0, 0)),
        Translate(Vector(0, 0, (LG_KNOB_HEIGHT - LG_CORNER_SPACE)))
    ),
    Torus(
        (LG_KNOB_RADIUS - LG_CORNER_SPACE),
        (LG_CORNER_SPACE),
        Rotate(Vector(90, 0, 0)),
        Translate(Vector(0, 0, (LG_KNOB_HEIGHT - LG_CORNER_SPACE)))
    )
)


# hollow stud with logo
# def lg_tech_knob_logo():
#     #if (lg_quality > 3)
#         Union(
#     #end
#     Object( lg_tech_knob
#         #if (lg_test ) 0)
#             Scale(Vector(1, 1, .1)
#         #end
#     ),
#     #if (lg_quality > 3)
#         Object( lego_logo_text Scale(Vector(3/4, 3/4, 3/4) ),
#     #end
#     #if (lg_quality > 3)
#         ),
#     #end

# brick inner cylinder to fit stud inside
lg_brick_cylinder = Union(
    Difference(
        Cylinder(
            Vector(0, 0, LG_BRICK_INNER_HEIGHT + LG_E),
            Vector(0, 0, (LG_CYLINDER_WALL_WIDTH / 2)),
            (LG_CYLINDER_RADIUS)
        ),
        Cylinder(
            Vector(0, 0, LG_BRICK_INNER_HEIGHT + LG_CORNER_SPACE),
            Vector(0, 0, 0),
            (LG_KNOB_RADIUS)
        )
    ),
    Torus(
        (LG_CYLINDER_RADIUS - LG_CYLINDER_WALL_WIDTH / 2),
        (LG_CYLINDER_WALL_WIDTH / 2),
        Rotate(Vector(90, 0, 0)),
        Translate(Vector(0, 0, (LG_CYLINDER_WALL_WIDTH / 2)))
    )
)


# plate inner cylinder to fit stud inside
lg_plate_cylinder = Union(
    Difference(
        Cylinder(
            Vector(0, 0, LG_PLATE_INNER_HEIGHT + LG_E),
            Vector(0, 0, (LG_CYLINDER_WALL_WIDTH / 2)),
            (LG_CYLINDER_RADIUS)
        ),
        Cylinder(
            Vector(0, 0, LG_PLATE_INNER_HEIGHT + LG_CORNER_SPACE),
            Vector(0, 0, 0),
            (LG_KNOB_RADIUS)
        )
    ),
    Torus(
        (LG_CYLINDER_RADIUS - LG_CYLINDER_WALL_WIDTH / 2),
        (LG_CYLINDER_WALL_WIDTH / 2),
        Rotate(Vector(90, 0, 0)),
        Translate(Vector(0, 0, (LG_CYLINDER_WALL_WIDTH / 2)))
    )
)


# brick inner cylinder to fit into hollow stud
lg_brick_column = Cylinder(
    Vector(0, 0, LG_BRICK_INNER_HEIGHT + LG_E),
    Vector(0, 0, 0),
    (LG_KNOB_INNER_RADIUS)
)


# plate inner cylinder to fit into hollow stud
lg_plate_column = Difference(
    Cylinder(
        Vector(0, 0, LG_PLATE_INNER_HEIGHT + LG_E),
        Vector(0, 0, 0),
        (LG_KNOB_INNER_RADIUS)
    ),
    Cylinder(
        Vector(0, 0, 1),
        Vector(0, 0, -1),
        (0.06)
    )
)


# wall between brick cylinder and brick wall
lg_support_wall = Box(
    Vector(-LG_CYLINDER_WALL_WIDTH / 2, -LG_E, 0.225),
    Vector(
        LG_CYLINDER_WALL_WIDTH / 2,
        LG_BRICK_WIDTH - LG_CYLINDER_RADIUS - LG_WALL_WIDTH + LG_E,
        LG_BRICK_HEIGHT
    )
)


# cutout for solid stud
lg_knob_inner_space = Cylinder(
    Vector(0, 0, -LG_CORNER_SPACE),
    Vector(0, 0, 0.15),
    (0.125)
)

"""
*  LGEO Primitives Clear versions
"""


def lg_knob_clear():
    result = Merge(
        Merge(
            Cylinder(
                Vector(0, 0, LG_KNOB_HEIGHT - LG_KNOB_CORNER_SPACE),
                Vector(0, 0, -LG_E),
                (LG_KNOB_RADIUS)
            ),
            Cylinder(
                Vector(0, 0, LG_KNOB_HEIGHT),
                Vector(0, 0, -LG_E),
                (LG_KNOB_RADIUS - LG_KNOB_CORNER_SPACE)
            )
        ),
        Torus(
            (LG_KNOB_RADIUS - LG_KNOB_CORNER_SPACE),
            (LG_KNOB_CORNER_SPACE),
            Rotate(Vector(90, 0, 0)),
            Translate(Vector(0, 0, (LG_KNOB_HEIGHT - LG_KNOB_CORNER_SPACE)))
        )
    )

    if (LG_QUALITY > 2):
        result.append(
            Object(
                lego_logo_text_clear(),
                Translate(Vector(0, 0, LG_KNOB_HEIGHT))
            )
        )
    return result

lg_tech_knob_clear = Merge(
    Difference(
        Merge(
            Cylinder(
                Vector(0, 0, LG_KNOB_HEIGHT - LG_CORNER_SPACE),
                Vector(0, 0, -LG_E),
                (LG_KNOB_RADIUS)
            ),
            Difference(
                Cylinder(
                    Vector(0, 0, LG_KNOB_HEIGHT),
                    Vector(0, 0, -LG_E),
                    (LG_KNOB_RADIUS - LG_CORNER_SPACE)
                ),
                Cylinder(
                    Vector(0, 0, LG_KNOB_HEIGHT + LG_E),
                    Vector(0, 0, -2 * LG_E),
                    (LG_KNOB_INNER_RADIUS + LG_CORNER_SPACE)
                )
            )
        ),
        Cylinder(
            Vector(0, 0, (LG_KNOB_HEIGHT + 2 * LG_E)),
            Vector(0, 0, -3 * LG_E),
            (LG_KNOB_INNER_RADIUS)
        )
    ),
    Torus(
        (LG_KNOB_INNER_RADIUS + LG_CORNER_SPACE),
        (LG_CORNER_SPACE),
        Rotate(Vector(90, 0, 0)),
        Translate(Vector(0, 0, (LG_KNOB_HEIGHT - LG_CORNER_SPACE)))
    ),
    Torus(
        (LG_KNOB_RADIUS - LG_CORNER_SPACE),
        (LG_CORNER_SPACE),
        Rotate(Vector(90, 0, 0)),
        Translate(Vector(0, 0, (LG_KNOB_HEIGHT - LG_CORNER_SPACE)))
    )
)


def lg_tech_knob_logo_clear():
    if (LG_QUALITY > 3):
        return Union(
            lg_tech_knob_clear,
            Object(lego_logo_text(), Scale(Vector(3 / 4, 3 / 4, 3 / 4)))
        )
    else:
        return lg_tech_knob_clear


lg_brick_cylinder_clear = Merge(
    Difference(
        Cylinder(
            Vector(0, 0, LG_BRICK_INNER_HEIGHT + LG_E),
            Vector(0, 0, (LG_CYLINDER_WALL_WIDTH / 2)),
            (LG_CYLINDER_RADIUS)
        ),
        Cylinder(
            Vector(0, 0, LG_BRICK_INNER_HEIGHT + LG_CORNER_SPACE),
            Vector(0, 0, 0),
            (LG_KNOB_RADIUS)
        ),
    ),
    Torus(
        (LG_CYLINDER_RADIUS - LG_CYLINDER_WALL_WIDTH / 2),
        (LG_CYLINDER_WALL_WIDTH / 2),
        Rotate(Vector(90, 0, 0)),
        Translate(Vector(0, 0, (LG_CYLINDER_WALL_WIDTH / 2)))
    )
)


lg_plate_cylinder_clear = Merge(
    Difference(
        Cylinder(
            Vector(0, 0, LG_PLATE_INNER_HEIGHT + LG_E),
            Vector(0, 0, (LG_CYLINDER_WALL_WIDTH / 2)),
            (LG_CYLINDER_RADIUS)
        ),
        Cylinder(
            Vector(0, 0, LG_PLATE_INNER_HEIGHT + LG_CORNER_SPACE),
            Vector(0, 0, 0),
            (LG_KNOB_RADIUS)
        ),
    ),
    Torus(
        (LG_CYLINDER_RADIUS - LG_CYLINDER_WALL_WIDTH / 2),
        (LG_CYLINDER_WALL_WIDTH / 2),
        Rotate(Vector(90, 0, 0)),
        Translate(Vector(0, 0, (LG_CYLINDER_WALL_WIDTH / 2)))
    )
)


lg_brick_column_clear = Cylinder(
    Vector(0, 0, LG_BRICK_INNER_HEIGHT + LG_E),
    Vector(0, 0, 0),
    (LG_KNOB_INNER_RADIUS)
)


lg_plate_column_clear = Difference(
    Cylinder(
        Vector(0, 0, LG_PLATE_INNER_HEIGHT + LG_E),
        Vector(0, 0, 0),
        (LG_KNOB_INNER_RADIUS)
    ),
    Cylinder(
        Vector(0, 0, 1),
        Vector(0, 0, -1),
        (0.06)
    )
)


lg_support_wall_clear = Box(
    Vector(-LG_CYLINDER_WALL_WIDTH / 2, -LG_E, 0.225),
    Vector(
        LG_CYLINDER_WALL_WIDTH / 2,
        LG_BRICK_WIDTH - LG_CYLINDER_RADIUS - LG_WALL_WIDTH + LG_E,
        LG_BRICK_HEIGHT
    )
)


lg_knob_inner_space_clear = Cylinder(
    Vector(0, 0, -LG_CORNER_SPACE),
    Vector(0, 0, 0.15),
    (0.125)
)
