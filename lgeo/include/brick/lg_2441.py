"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19981228 Lutz Uhlmann
20071125 Lutz Uhlmann fixed stud orientation

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_2441: Car Base 4 x 7 x 2/3
"""

from math import cos, pi

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere
from pov.finite_solid.Torus import Torus

from pov.object_modifier.Matrix import Matrix
from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate
from pov.object_modifier.Scale import Scale

from pov.other.Object import Object
from pov.other.EmptyObject import EmptyObject

from lgeo.include.common.lg_defs import LGBW, LG_CORNER_SPACE
from lgeo.include.common.lg_defs import LGPH, LG_E, LG_KNOB_RADIUS
from lgeo.include.common.lg_defs import LG_TOP_HEIGHT, LG_WALL_WIDTH
from lgeo.include.common.lg_defs import LG_KNOB_INNER_RADIUS, lg_knob
from lgeo.include.common.lg_defs import lg_plate_cylinder, lg_knob_inner_space


LG_ANGLE = 23.57817847


def solid():
    """@Todo: DocString."""
    result = Union()

    mir = 0
    while mir < 2:
        subpart = Union()

        pin = -2
        while pin < 4:

            if pin == -2:
                pinbox = Box(
                    Vector(
                        0,
                        LGBW - LG_CORNER_SPACE - LG_E,
                        -LGPH + LG_E
                    ),
                    Vector(
                        -0.2 - LG_E,
                        LGBW + LG_CORNER_SPACE,
                        -0.4 - LG_E
                    )
                )
            else:
                pinbox = Box(
                    Vector(
                        0,
                        LGBW - LG_CORNER_SPACE - LG_E,
                        -LGPH + LG_E
                    ),
                    Vector(
                        0.2 + LG_E, LGBW + LG_CORNER_SPACE,
                        -0.4 - LG_E
                    )
                )

            subpart.append(
                Union(
                    Sphere(
                        Vector(
                            -0.225 + LG_CORNER_SPACE,
                            LGBW + 0.08 - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Sphere(
                        Vector(
                            0.225 - LG_CORNER_SPACE,
                            LGBW + 0.08 - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -0.225 + LG_CORNER_SPACE,
                            LGBW + 0.08 - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            0.225 - LG_CORNER_SPACE,
                            LGBW + 0.08 - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(0, 0, 0),
                        Vector(
                            (0.175 + LG_CORNER_SPACE) / cos(
                                LG_ANGLE * pi / 180
                            ),
                            0,
                            0
                        ),
                        LG_CORNER_SPACE,
                        Rotate(Vector(0, 0, -LG_ANGLE)),
                        Translate(
                            Vector(
                                0.225 - LG_CORNER_SPACE,
                                LGBW + 0.08 - LG_CORNER_SPACE,
                                -LGPH + LG_CORNER_SPACE
                            )
                        )
                    ),
                    Cylinder(
                        Vector(0, 0, 0),
                        Vector(
                            -(0.175 + LG_CORNER_SPACE) / cos(
                                LG_ANGLE * pi / 180
                            ),
                            0,
                            0
                        ),
                        LG_CORNER_SPACE,
                        Rotate(Vector(0, 0, LG_ANGLE)),
                        Translate(
                            Vector(
                                -0.225 + LG_CORNER_SPACE,
                                LGBW + 0.08 - LG_CORNER_SPACE,
                                -LGPH + LG_CORNER_SPACE
                            )
                        )
                    ),
                    Sphere(
                        Vector(
                            -0.225 + LG_CORNER_SPACE,
                            LGBW + 0.08 - LG_CORNER_SPACE,
                            -0.1 - LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Sphere(
                        Vector(
                            0.225 - LG_CORNER_SPACE,
                            LGBW + 0.08 - LG_CORNER_SPACE,
                            -0.1 - LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -0.225 + LG_CORNER_SPACE,
                            LGBW + 0.08 - LG_CORNER_SPACE,
                            -0.1 - LG_CORNER_SPACE
                        ),
                        Vector(
                            0.225 - LG_CORNER_SPACE,
                            LGBW + 0.08 - LG_CORNER_SPACE,
                            -0.1 - LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(0, 0, 0),
                        Vector(
                            (0.175 + LG_CORNER_SPACE) / cos(
                                LG_ANGLE * pi / 180
                            ),
                            0,
                            0
                        ),
                        LG_CORNER_SPACE,
                        Rotate(Vector(0, 0, -LG_ANGLE)),
                        Translate(
                            Vector(
                                0.225 - LG_CORNER_SPACE,
                                LGBW + 0.08 - LG_CORNER_SPACE,
                                -0.1 - LG_CORNER_SPACE
                            )
                        )
                    ),
                    Cylinder(
                        Vector(0, 0, 0),
                        Vector(
                            -(0.175 + LG_CORNER_SPACE) / cos(
                                LG_ANGLE * pi / 180
                            ),
                            0,
                            0
                        ),
                        LG_CORNER_SPACE,
                        Rotate(Vector(0, 0, LG_ANGLE)),
                        Translate(
                            Vector(
                                -0.225 + LG_CORNER_SPACE,
                                LGBW + 0.08 - LG_CORNER_SPACE,
                                -0.1 - LG_CORNER_SPACE
                            )
                        )
                    ),
                    Cylinder(
                        Vector(
                            0.225 - LG_CORNER_SPACE,
                            LGBW + 0.08 - LG_CORNER_SPACE,
                            -0.1 - LG_CORNER_SPACE
                        ),
                        Vector(
                            0.225 - LG_CORNER_SPACE,
                            LGBW + 0.08 - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -0.225 + LG_CORNER_SPACE,
                            LGBW + 0.08 - LG_CORNER_SPACE,
                            -0.1 - LG_CORNER_SPACE
                        ),
                        Vector(
                            -0.225 + LG_CORNER_SPACE,
                            LGBW + 0.08 - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Box(
                        Vector(
                            -0.225 + LG_CORNER_SPACE,
                            LGBW + 0.08,
                            -0.1 - LG_CORNER_SPACE
                        ),
                        Vector(
                            0.225 - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        )
                    ),
                    Box(
                        Vector(
                            -0.225 + LG_CORNER_SPACE,
                            LGBW + 0.08 - LG_CORNER_SPACE,
                            -0.1
                        ),
                        Vector(
                            0.225 - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH
                        )
                    ),
                    Box(
                        Vector(0, LG_CORNER_SPACE, -0.1 - LG_CORNER_SPACE),
                        Vector(
                            -(0.175 + LG_CORNER_SPACE) / cos(
                                LG_ANGLE * pi / 180
                            ),
                            -0.08,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        Rotate(Vector(0, 0, LG_ANGLE)),
                        Translate(
                            Vector(
                                -0.225 + LG_CORNER_SPACE,
                                LGBW + 0.08 - LG_CORNER_SPACE,
                                0
                            )
                        )
                    ),
                    Box(
                        Vector(0, 0, -0.1),
                        Vector(
                            -(0.175 + LG_CORNER_SPACE) / cos(
                                LG_ANGLE * pi / 180
                            ),
                            -0.08,
                            -LGPH
                        ),
                        Rotate(Vector(0, 0, LG_ANGLE)),
                        Translate(
                            Vector(
                                -0.225 + LG_CORNER_SPACE,
                                LGBW + 0.08 - LG_CORNER_SPACE,
                                0
                            )
                        )
                    ),
                    Box(
                        Vector(0, LG_CORNER_SPACE, -0.1 - LG_CORNER_SPACE),
                        Vector(
                            (0.175 + LG_CORNER_SPACE) / cos(
                                LG_ANGLE * pi / 180
                            ),
                            -0.08,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        Rotate(Vector(0, 0, -LG_ANGLE)),
                        Translate(
                            Vector(
                                0.225 - LG_CORNER_SPACE,
                                LGBW + 0.08 - LG_CORNER_SPACE,
                                0
                            )
                        )
                    ),
                    Box(
                        Vector(0, 0, -0.1),
                        Vector(
                            (0.175 + LG_CORNER_SPACE) / cos(
                                LG_ANGLE * pi / 180
                            ),
                            -0.08,
                            -LGPH
                        ),
                        Rotate(Vector(0, 0, -LG_ANGLE)),
                        Translate(
                            Vector(
                                0.225 - LG_CORNER_SPACE,
                                LGBW + 0.08 - LG_CORNER_SPACE,
                                0
                            )
                        )
                    ),
                    Box(
                        Vector(
                            -0.06,
                            LG_KNOB_RADIUS + LG_E,
                            -LG_TOP_HEIGHT + LG_E
                        ),
                        Vector(
                            0.06,
                            LGBW - LG_WALL_WIDTH + LG_E,
                            -LGPH + LG_CORNER_SPACE
                        )
                    ),
                    Cylinder(
                        Vector(0, LGBW, -0.2),
                        Vector(0, LGBW + 0.08, -0.2),
                        0.2 - LG_CORNER_SPACE
                    ),
                    Difference(
                        Cylinder(
                            Vector(
                                0,
                                LGBW - LG_CORNER_SPACE,
                                -0.2
                            ),
                            Vector(
                                0,
                                LGBW + 0.08 - LG_CORNER_SPACE,
                                -0.2
                            ),
                            0.2
                        ),
                        pinbox
                    ),
                    Torus(
                        0.2 - LG_CORNER_SPACE,
                        LG_CORNER_SPACE,
                        Translate(
                            Vector(0, LGBW + LG_CORNER_SPACE, -0.2)
                        )
                    ),
                    Torus(
                        0.2 - LG_CORNER_SPACE,
                        LG_CORNER_SPACE,
                        Translate(
                            Vector(
                                0,
                                LGBW + 0.08 - LG_CORNER_SPACE,
                                -0.2
                            )
                        ),
                    ),
                    Difference(
                        Union(
                            Cylinder(
                                Vector(0, LGBW + 0.08 - LG_E, -0.2),
                                Vector(0, LGBW + 0.56, -0.2),
                                LG_KNOB_INNER_RADIUS
                            ),
                            Torus(
                                LG_KNOB_INNER_RADIUS,
                                LG_CORNER_SPACE,
                                Translate(
                                    Vector(
                                        0,
                                        LGBW + 0.56 - LG_CORNER_SPACE,
                                        -0.2
                                    )
                                )
                            ),
                            Torus(
                                LG_KNOB_INNER_RADIUS,
                                LG_CORNER_SPACE,
                                Translate(
                                    Vector(
                                        0,
                                        LGBW + 0.48 + LG_CORNER_SPACE,
                                        -0.2
                                    )
                                )
                            ),
                            Cylinder(
                                Vector(
                                    0,
                                    LGBW + 0.48 + LG_CORNER_SPACE,
                                    -0.2
                                ),
                                Vector(
                                    0,
                                    LGBW + 0.56 - LG_CORNER_SPACE,
                                    -0.2
                                ),
                                LG_KNOB_INNER_RADIUS + LG_CORNER_SPACE
                            ),
                        ),
                        Union(
                            Box(
                                Vector(
                                    0.03, LGBW + 0.56 + LG_E, 0
                                ),
                                Vector(
                                    -0.03, LGBW + 0.3, -0.4 - LG_E
                                )
                            ),
                            Cylinder(
                                Vector(0, LGBW + 0.3, 0),
                                Vector(0, LGBW + 0.3, -0.4 - LG_E),
                                0.03
                            ),
                        ),
                    ),
                    Translate(Vector(pin * LGBW, 0, 0))
                )
            )
            pin = pin + 5

            if mir == 1:
                mirmatrix = Matrix(
                    Vector(1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0)
                )
            else:
                mirmatrix = EmptyObject()

            result.append(
                Union(
                    Sphere(
                        Vector(
                            2 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Sphere(
                        Vector(
                            4 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Sphere(
                        Vector(
                            -LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Sphere(
                        Vector(
                            -3 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Sphere(
                        Vector(
                            3 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Sphere(
                        Vector(
                            4 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Sphere(
                        Vector(
                            -2 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Sphere(
                        Vector(
                            -3 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -3 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LG_CORNER_SPACE
                        ),
                        Vector(
                            -3 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            4 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            LG_CORNER_SPACE
                        ),
                        Vector(
                            4 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LG_CORNER_SPACE
                        ),
                        Vector(
                            -LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            2 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            LG_CORNER_SPACE
                        ),
                        Vector(
                            2 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            LGPH - LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -2 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            -2 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            3 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            3 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            4 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            3 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -2 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            3 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -3 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            -2 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Sphere(
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Sphere(
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Sphere(
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Sphere(
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        Vector(
                            -LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            2 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            -3 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LG_CORNER_SPACE
                        ),
                        Vector(
                            -LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Cylinder(
                        Vector(
                            4 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LG_CORNER_SPACE
                        ),
                        Vector(
                            2 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LG_CORNER_SPACE
                        ),
                        LG_CORNER_SPACE
                    ),
                    Box(
                        Vector(
                            -3 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE + 2 * LG_E
                        ),
                        Vector(
                            -2 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_WALL_WIDTH,
                            -LGPH
                        )
                    ),
                    Box(
                        Vector(
                            -3 * LGBW + LG_CORNER_SPACE,
                            LGBW,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            -LGBW - LG_CORNER_SPACE,
                            LGBW - LG_WALL_WIDTH,
                            -LG_CORNER_SPACE
                        )
                    ),
                    Box(
                        Vector(
                            4 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -LGPH + LG_CORNER_SPACE + 2 * LG_E
                        ),
                        Vector(
                            3 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_WALL_WIDTH,
                            -LGPH
                        )
                    ),
                    Box(
                        Vector(
                            4 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_WALL_WIDTH,
                            -LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            2 * LGBW + LG_CORNER_SPACE,
                            LGBW,
                            -LG_CORNER_SPACE
                        )
                    ),
                    Box(
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            LGBW,
                            -2 * LGPH
                        ),
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            LGBW - LG_WALL_WIDTH,
                            -LGPH - LG_CORNER_SPACE
                        )
                    ),
                    Box(
                        Vector(
                            3 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_WALL_WIDTH,
                            -LGPH + LG_CORNER_SPACE + 2 * LG_E),
                        Vector(
                            2 * LGBW + LG_CORNER_SPACE,
                            LGBW,
                            -2 * LGPH + LG_CORNER_SPACE
                        )
                    ),
                    Box(
                        Vector(
                            -LGBW - LG_CORNER_SPACE,
                            LGBW - LG_WALL_WIDTH,
                            -LGPH + LG_CORNER_SPACE + 2 * LG_E
                        ),
                        Vector(
                            -2 * LGBW + LG_CORNER_SPACE,
                            LGBW,
                            -2 * LGPH + LG_CORNER_SPACE
                        )
                    ),
                    Box(
                        Vector(
                            -LGBW + LG_CORNER_SPACE + LG_E,
                            LGBW - LG_WALL_WIDTH,
                            -2 * LGPH
                        ),
                        Vector(
                            -2 * LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE + LG_E
                        )
                    ),
                    Box(
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE - LG_E,
                            LGBW - LG_WALL_WIDTH,
                            -2 * LGPH
                        ),
                        Vector(
                            3 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE + LG_E)
                    ),
                    Box(
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE - LG_E,
                            LGBW - LG_WALL_WIDTH,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        Vector(
                            2 * LGBW + LG_CORNER_SPACE + LG_E,
                            LGBW,
                            -2 * LGPH + LG_CORNER_SPACE
                        )
                    ),
                    Box(
                        Vector(
                            -LGBW - LG_CORNER_SPACE - LG_E,
                            LGBW - LG_WALL_WIDTH,
                            -LGPH - LG_CORNER_SPACE
                        ),
                        Vector(
                            -LGBW + LG_CORNER_SPACE + LG_E,
                            LGBW,
                            -2 * LGPH + LG_CORNER_SPACE
                        )
                    ),
                    Box(
                        Vector(
                            -LGBW + LG_WALL_WIDTH,
                            2 * LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE + 2 * LG_E
                        ),
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE - LG_E,
                            -2 * LGPH
                        )
                    ),
                    Box(
                        Vector(
                            2 * LGBW - LG_WALL_WIDTH,
                            2 * LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE + 2 * LG_E
                        ),
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            LGBW - LG_CORNER_SPACE - LG_E,
                            -2 * LGPH
                        )
                    ),
                    Box(
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            2 * LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE + 2 * LG_E
                        ),
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            2 * LGBW - LG_WALL_WIDTH,
                            -2 * LGPH
                        )
                    ),
                    Box(
                        Vector(
                            -LGBW + LG_WALL_WIDTH,
                            2 * LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            -LGBW,
                            LGBW - LG_CORNER_SPACE - LG_E,
                            -LGPH - LG_CORNER_SPACE
                        )
                    ),
                    Box(
                        Vector(
                            2 * LGBW - LG_WALL_WIDTH,
                            2 * LGBW - LG_CORNER_SPACE,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            2 * LGBW,
                            LGBW - LG_CORNER_SPACE - LG_E,
                            -LGPH - LG_CORNER_SPACE
                        )
                    ),
                    Box(
                        Vector(
                            2 * LGBW - LG_CORNER_SPACE,
                            2 * LGBW,
                            -2 * LGPH + LG_CORNER_SPACE
                        ),
                        Vector(
                            -LGBW + LG_CORNER_SPACE,
                            2 * LGBW - LG_WALL_WIDTH,
                            -LGPH - LG_CORNER_SPACE
                        )
                    ),
                    Box(
                        Vector(
                            3 * LGBW - LG_CORNER_SPACE,
                            2 * LG_WALL_WIDTH,
                            -LGPH
                        ),
                        Vector(
                            3 * LGBW + LG_WALL_WIDTH,
                            3 * LG_WALL_WIDTH,
                            -LG_TOP_HEIGHT + LG_E
                        )
                    ),
                    Box(
                        Vector(
                            -2 * LGBW + LG_CORNER_SPACE,
                            2 * LG_WALL_WIDTH,
                            -LGPH
                        ),
                        Vector(
                            -2 * LGBW - LG_WALL_WIDTH,
                            3 * LG_WALL_WIDTH,
                            -LG_TOP_HEIGHT + LG_E
                        )
                    ),
                    Box(
                        Vector(
                            -LGBW - LG_CORNER_SPACE,
                            2 * LG_WALL_WIDTH,
                            -2 * LGPH
                        ),
                        Vector(
                            -LGBW + LG_WALL_WIDTH,
                            3 * LG_WALL_WIDTH,
                            -LGPH - LG_TOP_HEIGHT + LG_E
                        )
                    ),
                    Box(
                        Vector(
                            2 * LGBW + LG_CORNER_SPACE,
                            2 * LG_WALL_WIDTH,
                            -2 * LGPH
                        ),
                        Vector(
                            2 * LGBW - LG_WALL_WIDTH,
                            3 * LG_WALL_WIDTH,
                            -LGPH - LG_TOP_HEIGHT + LG_E
                        )
                    ),
                    Box(
                        Vector(
                            1.5 * LGBW - 0.06,
                            LGBW - LG_E,
                            -2 * LGPH
                        ),
                        Vector(
                            1.5 * LGBW + 0.06,
                            LGBW + LG_WALL_WIDTH,
                            -LGPH - LG_TOP_HEIGHT + LG_E
                        )
                    ),
                    Box(
                        Vector(
                            0.5 * LGBW - 0.06,
                            LGBW - LG_E,
                            -2 * LGPH
                        ),
                        Vector(
                            0.5 * LGBW + 0.06,
                            LGBW + LG_WALL_WIDTH,
                            -LGPH - LG_TOP_HEIGHT + LG_E
                        )
                    ),
                    Box(
                        Vector(
                            -0.5 * LGBW - 0.06,
                            LGBW - LG_E,
                            -2 * LGPH
                        ),
                        Vector(
                            -0.5 * LGBW + 0.06,
                            LGBW + LG_WALL_WIDTH,
                            -LGPH - LG_TOP_HEIGHT + LG_E
                        )
                    ),
                    Cylinder(
                        Vector(
                            LGBW,
                            1.5 * LGBW,
                            -2 * LGPH
                        ),
                        Vector(
                            LGBW,
                            1.5 * LGBW,
                            -LGPH - LG_TOP_HEIGHT + LG_E
                        ),
                        LG_WALL_WIDTH
                    ),
                    Cylinder(
                        Vector(
                            0,
                            1.5 * LGBW,
                            -2 * LGPH
                        ),
                        Vector(
                            0,
                            1.5 * LGBW,
                            -LGPH - LG_TOP_HEIGHT + LG_E
                        ),
                        LG_WALL_WIDTH
                    ),
                    Object(
                        lg_knob(),
                        Rotate(Vector(0, 0, 90)),
                        Scale(Vector(1, 1 - 2 * mir, 1)),
                        Translate(
                            Vector(3.5 * LGBW, LGBW / 2, 0)
                        )
                    ),
                    Object(
                        lg_knob(),
                        Rotate(Vector(0, 0, 90)),
                        Scale(Vector(1, 1 - 2 * mir, 1)),
                        Translate(
                            Vector(2.5 * LGBW, LGBW / 2, 0)
                        )
                    ),
                    Object(
                        lg_knob(),
                        Rotate(Vector(0, 0, 90)),
                        Scale(Vector(1, 1 - 2 * mir, 1)),
                        Translate(
                            Vector(
                                1.5 * LGBW,
                                LGBW / 2,
                                -LGPH
                            )
                        )
                    ),
                    Object(
                        lg_knob(),
                        Rotate(Vector(0, 0, 90)),
                        Scale(Vector(1, 1 - 2 * mir, 1)),
                        Translate(
                            Vector(
                                0.5 * LGBW,
                                LGBW / 2,
                                -LGPH
                            )
                        )
                    ),
                    Object(
                        lg_knob(),
                        Rotate(Vector(0, 0, 90)),
                        Scale(Vector(1, 1 - 2 * mir, 1)),
                        Translate(
                            Vector(
                                -0.5 * LGBW,
                                LGBW / 2,
                                -LGPH
                            )
                        )
                    ),
                    Object(
                        lg_knob(),
                        Rotate(Vector(0, 0, 90)),
                        Scale(Vector(1, 1 - 2 * mir, 1)),
                        Translate(
                            Vector(
                                1.5 * LGBW,
                                3 * LGBW / 2,
                                -LGPH
                            )
                        )
                    ),
                    Object(
                        lg_knob(),
                        Rotate(Vector(0, 0, 90)),
                        Scale(Vector(1, 1 - 2 * mir, 1)),
                        Translate(
                            Vector(
                                0.5 * LGBW,
                                3 * LGBW / 2,
                                -LGPH
                            )
                        )
                    ),
                    Object(
                        lg_knob(),
                        Rotate(Vector(0, 0, 90)),
                        Scale(Vector(1, 1 - 2 * mir, 1)),
                        Translate(
                            Vector(
                                -0.5 * LGBW,
                                3 * LGBW / 2,
                                -LGPH
                            )
                        )
                    ),
                    Object(
                        lg_knob(),
                        Rotate(Vector(0, 0, 90)),
                        Scale(Vector(1, 1 - 2 * mir, 1)),
                        Translate(
                            Vector(-1.5 * LGBW, LGBW / 2, 0)
                        )
                    ),
                    Object(
                        lg_knob(),
                        Rotate(Vector(0, 0, 90)),
                        Scale(Vector(1, 1 - 2 * mir, 1)),
                        Translate(
                            Vector(-2.5 * LGBW, LGBW / 2, 0)
                        )
                    ),
                    subpart,
                    mirmatrix
                )
            )
            mir = mir + 1

    result.append(
        Cylinder(
            Vector(
                2 * LGBW + LG_CORNER_SPACE,
                LGBW - LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            Vector(
                2 * LGBW + LG_CORNER_SPACE,
                -LGBW + LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                4 * LGBW - LG_CORNER_SPACE,
                LGBW - LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            Vector(
                4 * LGBW - LG_CORNER_SPACE,
                -LGBW + LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                -LGBW - LG_CORNER_SPACE,
                LGBW - LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            Vector(
                -LGBW - LG_CORNER_SPACE,
                -LGBW + LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                -3 * LGBW + LG_CORNER_SPACE,
                LGBW - LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            Vector(
                -3 * LGBW + LG_CORNER_SPACE,
                -LGBW + LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                3 * LGBW - LG_CORNER_SPACE,
                LGBW - LG_CORNER_SPACE,
                -2 * LGPH + LG_CORNER_SPACE
            ),
            Vector(
                3 * LGBW - LG_CORNER_SPACE,
                -LGBW + LG_CORNER_SPACE,
                -2 * LGPH + LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                4 * LGBW - LG_CORNER_SPACE,
                LGBW - LG_CORNER_SPACE,
                -LGPH + LG_CORNER_SPACE
            ),
            Vector(
                4 * LGBW - LG_CORNER_SPACE,
                -LGBW + LG_CORNER_SPACE,
                -LGPH + LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                -2 * LGBW + LG_CORNER_SPACE,
                LGBW - LG_CORNER_SPACE,
                -2 * LGPH + LG_CORNER_SPACE
            ),
            Vector(
                -2 * LGBW + LG_CORNER_SPACE,
                -LGBW + LG_CORNER_SPACE,
                -2 * LGPH + LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(
                -3 * LGBW + LG_CORNER_SPACE,
                LGBW - LG_CORNER_SPACE,
                -LGPH + LG_CORNER_SPACE
            ),
            Vector(
                -3 * LGBW + LG_CORNER_SPACE,
                -LGBW + LG_CORNER_SPACE,
                -LGPH + LG_CORNER_SPACE
            ),
            LG_CORNER_SPACE
        ),
        Cylinder(
            Vector(3.5 * LGBW, 0, -LG_TOP_HEIGHT + LG_E),
            Vector(3.5 * LGBW, 0, -LGPH),
            LG_WALL_WIDTH
        ),
        Cylinder(
            Vector(-2.5 * LGBW, 0, -LG_TOP_HEIGHT + LG_E),
            Vector(-2.5 * LGBW, 0, -LGPH),
            LG_WALL_WIDTH
        ),
        Object(
            lg_plate_cylinder,
            Translate(Vector(LGBW, 0, -2 * LGPH))
        ),
        Object(
            lg_plate_cylinder,
            Translate(Vector(0, 0, -2 * LGPH))
        ),
        Cylinder(
            Vector(2.5 * LGBW, 0, -LG_TOP_HEIGHT + LG_E),
            Vector(2.5 * LGBW, 0, -2 * LGPH),
            LG_KNOB_INNER_RADIUS
        ),
        Cylinder(
            Vector(-1.5 * LGBW, 0, -LG_TOP_HEIGHT + LG_E),
            Vector(-1.5 * LGBW, 0, -2 * LGPH),
            LG_KNOB_INNER_RADIUS
        ),
        Box(
            Vector(
                2 * LGBW + LG_CORNER_SPACE,
                0.04,
                -LG_TOP_HEIGHT + LG_E
            ),
            Vector(
                3 * LGBW - LG_CORNER_SPACE,
                -0.04,
                -LGPH
            )
        ),
        Box(
            Vector(
                -2 * LGBW + LG_CORNER_SPACE,
                0.04,
                -LG_TOP_HEIGHT + LG_E
            ),
            Vector(
                -LGBW - LG_CORNER_SPACE,
                -0.04,
                -LGPH
            )
        ),
        Box(
            Vector(
                4 * LGBW - LG_CORNER_SPACE,
                LGBW - LG_CORNER_SPACE,
                -LGPH
            ),
            Vector(
                4 * LGBW - LG_WALL_WIDTH,
                -LGBW + LG_CORNER_SPACE,
                -LGPH + LG_CORNER_SPACE + 2 * LG_E
            )
        ),
        Box(
            Vector(
                3 * LGBW - LG_CORNER_SPACE,
                LGBW - LG_CORNER_SPACE,
                -2 * LGPH
            ),
            Vector(
                3 * LGBW - LG_WALL_WIDTH,
                -LGBW + LG_CORNER_SPACE,
                -2 * LGPH + LG_CORNER_SPACE + 2 * LG_E
            )
        ),
        Box(
            Vector(
                -2 * LGBW + LG_CORNER_SPACE,
                LGBW - LG_CORNER_SPACE,
                -2 * LGPH
            ),
            Vector(
                -2 * LGBW + LG_WALL_WIDTH,
                -LGBW + LG_CORNER_SPACE,
                -2 * LGPH + LG_CORNER_SPACE + 2 * LG_E
            )
        ),
        Box(
            Vector(
                -3 * LGBW + LG_CORNER_SPACE,
                LGBW - LG_CORNER_SPACE,
                -LGPH
            ),
            Vector(
                -3 * LGBW + LG_WALL_WIDTH,
                -LGBW + LG_CORNER_SPACE,
                -LGPH + LG_CORNER_SPACE + 2 * LG_E
            )
        ),
        Box(
            Vector(
                4 * LGBW,
                LGBW - LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            Vector(
                4 * LGBW - LG_WALL_WIDTH,
                -LGBW + LG_CORNER_SPACE,
                -LGPH + LG_CORNER_SPACE
            )
        ),
        Box(
            Vector(
                3 * LGBW,
                LGBW - LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            Vector(
                3 * LGBW - LG_WALL_WIDTH,
                -LGBW + LG_CORNER_SPACE,
                -2 * LGPH + LG_CORNER_SPACE
            )
        ),
        Box(
            Vector(
                -2 * LGBW,
                LGBW - LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            Vector(
                -2 * LGBW + LG_WALL_WIDTH,
                -LGBW + LG_CORNER_SPACE,
                -2 * LGPH + LG_CORNER_SPACE
            )
        ),
        Box(
            Vector(
                -3 * LGBW,
                LGBW - LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            Vector(
                -3 * LGBW + LG_WALL_WIDTH,
                -LGBW + LG_CORNER_SPACE,
                -LGPH + LG_CORNER_SPACE
            )
        ),
        Box(
            Vector(
                2 * LGBW,
                LGBW - LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            Vector(
                2 * LGBW + LG_WALL_WIDTH,
                -LGBW + LG_CORNER_SPACE,
                -2 * LGPH
            )
        ),
        Box(
            Vector(
                2 * LGBW - LG_CORNER_SPACE - LG_E,
                LGBW - LG_CORNER_SPACE,
                -LGPH
            ),
            Vector(
                2 * LGBW + LG_WALL_WIDTH / 2,
                -LGBW + LG_CORNER_SPACE,
                -LGPH - LG_TOP_HEIGHT
            )
        ),
        Box(
            Vector(
                -LGBW + LG_CORNER_SPACE + 2 * LG_E,
                LGBW - LG_CORNER_SPACE,
                -LGPH
            ),
            Vector(
                -LGBW - LG_WALL_WIDTH / 2,
                -LGBW + LG_CORNER_SPACE,
                -LGPH - LG_TOP_HEIGHT
            )
        ),
        Box(
            Vector(
                -LGBW,
                LGBW - LG_CORNER_SPACE,
                -LG_CORNER_SPACE
            ),
            Vector(
                -LGBW - LG_WALL_WIDTH,
                -LGBW + LG_CORNER_SPACE,
                -2 * LGPH
            )
        ),
        Difference(
            Box(
                Vector(
                    4 * LGBW - LG_CORNER_SPACE,
                    LGBW - LG_CORNER_SPACE,
                    0
                ),
                Vector(
                    2 * LGBW + LG_CORNER_SPACE,
                    -LGBW + LG_CORNER_SPACE,
                    -LG_TOP_HEIGHT
                )
            ),
            Union(
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            3.5 * LGBW,
                            LGBW / 2,
                            -LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            2.5 * LGBW,
                            LGBW / 2,
                            -LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            3.5 * LGBW,
                            -LGBW / 2,
                            -LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            2.5 * LGBW,
                            -LGBW / 2,
                            -LG_TOP_HEIGHT
                        )
                    )
                ),
            )
        ),
        Difference(
            Box(
                Vector(
                    -LGBW - LG_CORNER_SPACE,
                    LGBW - LG_CORNER_SPACE,
                    0
                ),
                Vector(
                    -3 * LGBW + LG_CORNER_SPACE,
                    -LGBW + LG_CORNER_SPACE,
                    -LG_TOP_HEIGHT
                )
            ),
            Union(
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            -2.5 * LGBW,
                            LGBW / 2,
                            -LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            -1.5 * LGBW,
                            LGBW / 2,
                            -LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            -2.5 * LGBW,
                            -LGBW / 2,
                            -LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            -1.5 * LGBW,
                            -LGBW / 2,
                            -LG_TOP_HEIGHT
                        )
                    )
                )
            )
        ),
        Difference(
            Box(
                Vector(
                    -LGBW + LG_CORNER_SPACE,
                    2 * LGBW - LG_CORNER_SPACE,
                    -LGPH
                ),
                Vector(
                    2 * LGBW - LG_CORNER_SPACE,
                    -2 * LGBW + LG_CORNER_SPACE,
                    -LGPH - LG_TOP_HEIGHT
                )
            ),
            Union(
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            1.5 * LGBW,
                            LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            0.5 * LGBW,
                            LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            -0.5 * LGBW,
                            LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            1.5 * LGBW,
                            -LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            0.5 * LGBW,
                            -LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            -0.5 * LGBW,
                            -LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            1.5 * LGBW,
                            3 * LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            0.5 * LGBW,
                            3 * LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            -0.5 * LGBW,
                            3 * LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            1.5 * LGBW,
                            -3 * LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            0.5 * LGBW,
                            -3 * LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    lg_knob_inner_space,
                    Translate(
                        Vector(
                            -0.5 * LGBW,
                            -3 * LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                )
            )
        ),
        Translate(Vector(-0.5 * LGBW, 0, 0))

    )

    return result


# #declare lg_2441_clear =
# merge {
#  #declare MIR = 0;
#  #while (MIR < 2)
#   merge {
#    sphere {
#     Vector(2 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    sphere {
#     Vector(4 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    sphere {
#     Vector(-LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    sphere {
#     Vector(-3 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    sphere {
#     Vector(3 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#          -2 * LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    sphere {
#     Vector(4 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#          -LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    sphere {
#     Vector(-2 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#          -2 * LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    sphere {
#     Vector(-3 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#          -LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(-3 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#     Vector(-3 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#          -LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(4 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#     Vector(4 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#          -LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(-LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#     Vector(-LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LGPH - LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(2 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#     Vector(2 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LGPH - LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(-2 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     Vector(-2 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(3 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     Vector(3 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(4 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE),
#     Vector(3 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(-2 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     Vector(-LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(3 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(-3 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE),
#     Vector(-2 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(-LGBW + LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    sphere {
#     Vector(-LGBW + LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    sphere {
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(-LGBW + LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    sphere {
#     Vector(-LGBW + LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    sphere {
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(-LGBW + LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     Vector(-LGBW + LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(-LGBW + LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     Vector(-LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(-LGBW + LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     Vector(-LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(-LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     Vector(-LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(2 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH - LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(-3 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#     Vector(-LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Cylinder(
#     Vector(4 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#     Vector(2 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#     LG_CORNER_SPACE
#    ),
#    Box(
#     Vector(-3 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPAC2 * LG_E),
#     Vector(-2 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_WALL_WIDTH, -LGPH)
#    ),
#    Box(
#     Vector(-3 * LGBW + LG_CORNER_SPACE,
#         LGBW, -LGPH + LG_CORNER_SPACE),
#     Vector(-LGBW - LG_CORNER_SPACE,
#         LGBW - LG_WALL_WIDTH, -LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(4 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPAC2 * LG_E),
#     Vector(3 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_WALL_WIDTH, -LGPH)
#    ),
#    Box(
#     Vector(4 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_WALL_WIDTH, -LGPH + LG_CORNER_SPACE),
#     Vector(2 * LGBW + LG_CORNER_SPACE,
#         LGBW, -LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         LGBW, -2 * LGPH),
#     Vector(-LGBW + LG_CORNER_SPACE,
#         LGBW - LG_WALL_WIDTH, -LGPH - LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(3 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_WALL_WIDTH,
#         -LGPH + LG_CORNER_SPAC2 * LG_E),
#     Vector(2 * LGBW + LG_CORNER_SPACE,
#         LGBW, -2 * LGPH + LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(-LGBW - LG_CORNER_SPACE,
#         LGBW - LG_WALL_WIDTH,
#         -LGPH + LG_CORNER_SPAC2 * LG_E),
#     Vector(-2 * LGBW + LG_CORNER_SPACE,
#         LGBW, -2 * LGPH + LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(-LGBW + LG_CORNER_SPAC2 * LG_E,
#         LGBW - LG_WALL_WIDTH, -2 * LGPH),
#     Vector(-2 * LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPAC2 * LG_E)
#    ),
#    Box(
#     Vector(2 * LGBW - LG_CORNER_SPACE - LG_E,
#         LGBW - LG_WALL_WIDTH, -2 * LGPH),
#     Vector(3 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPAC2 * LG_E)
#    ),
#    Box(
#     Vector(2 * LGBW - LG_CORNER_SPACE - LG_E,
#         LGBW - LG_WALL_WIDTH, -LGPH - LG_CORNER_SPACE),
#     Vector(2 * LGBW + LG_CORNER_SPAC2 * LG_E,
#         LGBW, -2 * LGPH + LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(-LGBW - LG_CORNER_SPACE - LG_E,
#         LGBW - LG_WALL_WIDTH, -LGPH - LG_CORNER_SPACE),
#     Vector(-LGBW + LG_CORNER_SPAC2 * LG_E,
#         LGBW, -2 * LGPH + LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(-LGBW + LG_WALL_WIDTH,
#         2 * LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPAC2 * LG_E),
#     Vector(-LGBW + LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE - LG_E,
#         -2 * LGPH)
#    ),
#    Box(
#     Vector(2 * LGBW - LG_WALL_WIDTH,
#         2 * LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPAC2 * LG_E),
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         LGBW - LG_CORNER_SPACE - LG_E,
#         -2 * LGPH)
#    ),
#    Box(
#     Vector(2 * LGBW - LG_CORNER_SPACE,
#         2 * LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPAC2 * LG_E),
#     Vector(-LGBW + LG_CORNER_SPACE,
#         2 * LGBW - LG_WALL_WIDTH, -2 * LGPH)
#    ),
#    Box(
#     Vector(-LGBW + LG_WALL_WIDTH,
#         2 * LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     Vector(-LGBW, LGBW - LG_CORNER_SPACE - LG_E,
#         -LGPH - LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(2 * LGBW - LG_WALL_WIDTH,
#         2 * LGBW - LG_CORNER_SPACE,
#         -2 * LGPH + LG_CORNER_SPACE),
#     Vector(2 * LGBW, LGBW - LG_CORNER_SPACE - LG_E,
#         -LGPH - LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(2 * LGBW - LG_CORNER_SPACE, 2 * LGBW,
#         -2 * LGPH + LG_CORNER_SPACE),
#     Vector(-LGBW + LG_CORNER_SPACE,
#         2 * LGBW - LG_WALL_WIDTH,
#         -LGPH - LG_CORNER_SPACE)
#    ),
#    Box(
#     Vector(3 * LGBW - LG_CORNER_SPACE, 2 * LG_WALL_WIDTH,
#         -LGPH),
#     Vector(3 * LGBW + LG_WALL_WIDTH, 3 * LG_WALL_WIDTH,
#         -LG_TOP_HEIGHT + LG_E)
#    ),
#    Box(
#     Vector(-2 * LGBW + LG_CORNER_SPACE,
#         2 * LG_WALL_WIDTH, -LGPH),
#     Vector(-2 * LGBW - LG_WALL_WIDTH,
#         3 * LG_WALL_WIDTH, -LG_TOP_HEIGHT + LG_E)
#    ),
#    Box(
#     Vector(-LGBW - LG_CORNER_SPACE,
#         2 * LG_WALL_WIDTH, -2 * LGPH),
#     Vector(-LGBW + LG_WALL_WIDTH,
#         3 * LG_WALL_WIDTH, -LGPH - LG_TOP_HEIGHT + LG_E)
#    ),
#    Box(
#     Vector(2 * LGBW + LG_CORNER_SPACE,
#         2 * LG_WALL_WIDTH, -2 * LGPH),
#     Vector(2 * LGBW - LG_WALL_WIDTH, 3 * LG_WALL_WIDTH,
#         -LGPH - LG_TOP_HEIGHT + LG_E)
#    ),
#    Box(
#     Vector(1.5 * LGBW - 0.06, LGBW - LG_E,
#         -2 * LGPH),
#     Vector(1.5 * LGBW + 0.06, LGBW + LG_WALL_WIDTH,
#         -LGPH - LG_TOP_HEIGHT + LG_E)
#    ),
#    Box(
#     Vector(0.5 * LGBW - 0.06, LGBW - LG_E,
#         -2 * LGPH),
#     Vector(0.5 * LGBW + 0.06, LGBW + LG_WALL_WIDTH,
#         -LGPH - LG_TOP_HEIGHT + LG_E)
#    ),
#    Box(
#     Vector(-0.5 * LGBW - 0.06, LGBW - LG_E,
#         -2 * LGPH),
#     Vector(-0.5 * LGBW + 0.06, LGBW + LG_WALL_WIDTH,
#         -LGPH - LG_TOP_HEIGHT + LG_E)
#    ),
#    Cylinder(
#     Vector(LGBW, 1.5 * LGBW,
#         -2 * LGPH),
#     Vector(LGBW, 1.5 * LGBW,
#         -LGPH - LG_TOP_HEIGHT + LG_E),
#     LG_WALL_WIDTH
#    ),
#    Cylinder(
#     Vector(0, 1.5 * LGBW, -2 * LGPH),
#     Vector(0, 1.5 * LGBW, -LGPH - LG_TOP_HEIGHT + LG_E),
#     LG_WALL_WIDTH
#    ),
#    Object(
#     lg_knob_clear
#     rotate Vector(0, 0, 90)
#     scale Vector(1, 1-2*MIR, 1)
#     Translate(Vector(3.5 * LGBW, LGBW / 2, 0)
#    ),
#    Object(
#     lg_knob_clear
#     rotate Vector(0, 0, 90)
#     scale Vector(1, 1-2*MIR, 1)
#     Translate(Vector(2.5 * LGBW, LGBW / 2, 0)
#    ),
#    Object(
#     lg_knob_clear
#     rotate Vector(0, 0, 90)
#     scale Vector(1, 1-2*MIR, 1)
#     Translate(Vector(1.5 * LGBW,
#         LGBW / 2, -LGPH)
#    ),
#    Object(
#     lg_knob_clear
#     rotate Vector(0, 0, 90)
#     scale Vector(1, 1-2*MIR, 1)
#     Translate(Vector(0.5 * LGBW,
#         LGBW / 2, -LGPH)
#    ),
#    Object(
#     lg_knob_clear
#     rotate Vector(0, 0, 90)
#     scale Vector(1, 1-2*MIR, 1)
#     Translate(Vector(-0.5 * LGBW,
#         LGBW / 2, -LGPH)
#    ),
#    Object(
#     lg_knob_clear
#     rotate Vector(0, 0, 90)
#     scale Vector(1, 1-2*MIR, 1)
#     Translate(Vector(1.5 * LGBW,
#         3 * LGBW / 2, -LGPH)
#    ),
#    Object(
#     lg_knob_clear
#     rotate Vector(0, 0, 90)
#     scale Vector(1, 1-2*MIR, 1)
#     Translate(Vector(0.5 * LGBW,
#         3 * LGBW / 2, -LGPH)
#    ),
#    Object(
#     lg_knob_clear
#     rotate Vector(0, 0, 90)
#     scale Vector(1, 1-2*MIR, 1)
#     Translate(Vector(-0.5 * LGBW,
#         3 * LGBW / 2, -LGPH)
#    ),
#    Object(
#     lg_knob_clear
#     rotate Vector(0, 0, 90)
#     scale Vector(1, 1-2*MIR, 1)
#     Translate(Vector(-1.5 * LGBW, LGBW / 2, 0)
#    ),
#    Object(
#     lg_knob_clear
#     rotate Vector(0, 0, 90)
#     scale Vector(1, 1-2*MIR, 1)
#     Translate(Vector(-2.5 * LGBW, LGBW / 2, 0)
#    ),
#    #declare PIN = -2;
#    #while (PIN < 4)
#     merge {
#      sphere {
#       Vector(-0.225 + LG_CORNER_SPACE, LGBW + 0.08 - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE),
#       LG_CORNER_SPACE
#      ),
#      sphere {
#       Vector(0.225 - LG_CORNER_SPACE, LGBW + 0.08 - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE),
#       LG_CORNER_SPACE
#      ),
#      Cylinder(
#       Vector(-0.225 + LG_CORNER_SPACE, LGBW + 0.08 - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE),
#       Vector(0.225 - LG_CORNER_SPACE, LGBW + 0.08 - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE),
#       LG_CORNER_SPACE
#      ),
#      Cylinder(
#       Vector(0, 0, 0),
#       Vector((0.175 + LG_CORNER_SPACE) / cos(LG_ANGLE * pi / 180), 0, 0),
#       LG_CORNER_SPACE
#       rotate Vector(0, 0, -LG_ANGLE)
#       Translate(Vector(0.225 - LG_CORNER_SPACE,
#         LGBW + 0.08 - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE)
#      ),
#      Cylinder(
#       Vector(0, 0, 0),
#       Vector(-(0.175 + LG_CORNER_SPACE) / cos(LG_ANGLE * pi / 180), 0, 0),
#       LG_CORNER_SPACE
#       rotate Vector(0, 0, LG_ANGLE)
#       Translate(Vector(-0.225 + LG_CORNER_SPACE,
#         LGBW + 0.08 - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE)
#      ),
#      sphere {
#       Vector(-0.225 + LG_CORNER_SPACE, LGBW + 0.08 - LG_CORNER_SPACE,
#         -0.1 - LG_CORNER_SPACE),
#       LG_CORNER_SPACE
#      ),
#      sphere {
#       Vector(0.225 - LG_CORNER_SPACE, LGBW + 0.08 - LG_CORNER_SPACE,
#         -0.1 - LG_CORNER_SPACE),
#       LG_CORNER_SPACE
#      ),
#      Cylinder(
#       Vector(-0.225 + LG_CORNER_SPACE, LGBW + 0.08 - LG_CORNER_SPACE,
#         -0.1 - LG_CORNER_SPACE),
#       Vector(0.225 - LG_CORNER_SPACE, LGBW + 0.08 - LG_CORNER_SPACE,
#         -0.1 - LG_CORNER_SPACE),
#       LG_CORNER_SPACE
#      ),
#      Cylinder(
#       Vector(0, 0, 0),
#       Vector((0.175 + LG_CORNER_SPACE) / cos(LG_ANGLE * pi / 180), 0, 0),
#       LG_CORNER_SPACE
#       rotate Vector(0, 0, -LG_ANGLE)
#       Translate(Vector(0.225 - LG_CORNER_SPACE,
#         LGBW + 0.08 - LG_CORNER_SPACE, -0.1 - LG_CORNER_SPACE)
#      ),
#      Cylinder(
#       Vector(0, 0, 0),
#       Vector(-(0.175 + LG_CORNER_SPACE) / cos(LG_ANGLE * pi / 180), 0, 0),
#       LG_CORNER_SPACE
#       rotate Vector(0, 0, LG_ANGLE)
#       Translate(Vector(-0.225 + LG_CORNER_SPACE,
#         LGBW + 0.08 - LG_CORNER_SPACE, -0.1 - LG_CORNER_SPACE)
#      ),
#      Cylinder(
#       Vector(0.225 - LG_CORNER_SPACE, LGBW + 0.08 - LG_CORNER_SPACE,
#         -0.1 - LG_CORNER_SPACE),
#       Vector(0.225 - LG_CORNER_SPACE, LGBW + 0.08 - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE),
#       LG_CORNER_SPACE
#      ),
#      Cylinder(
#       Vector(-0.225 + LG_CORNER_SPACE, LGBW + 0.08 - LG_CORNER_SPACE,
#         -0.1 - LG_CORNER_SPACE),
#       Vector(-0.225 + LG_CORNER_SPACE, LGBW + 0.08 - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE),
#       LG_CORNER_SPACE
#      ),
#      Box(
#       Vector(-0.225 + LG_CORNER_SPACE, LGBW + 0.08,
#         -0.1 - LG_CORNER_SPACE),
#       Vector(0.225 - LG_CORNER_SPACE, LGBW - LG_CORNER_SPACE,
#         -LGPH + LG_CORNER_SPACE)
#      ),
#      Box(
#       Vector(-0.225 + LG_CORNER_SPACE,
#         LGBW + 0.08 - LG_CORNER_SPACE, -0.1),
#       Vector(0.225 - LG_CORNER_SPACE, LGBW - LG_CORNER_SPACE,
#         -LGPH)
#      ),
#      Box(
#       Vector(0, LG_CORNER_SPACE, -0.1 - LG_CORNER_SPACE),
#       Vector(-(0.175 + LG_CORNER_SPACE) / cos(LG_ANGLE * pi / 180), -0.08,
#         -LGPH + LG_CORNER_SPACE)
#       rotate Vector(0, 0, LG_ANGLE)
#       Translate(Vector(-0.225 + LG_CORNER_SPACE,
#         LGBW + 0.08 - LG_CORNER_SPACE, 0)
#      ),
#      Box(
#       Vector(0, 0, -0.1),
#       Vector(-(0.175 + LG_CORNER_SPACE) / cos(LG_ANGLE * pi / 180),
#         -0.08, -LGPH)
#       rotate Vector(0, 0, LG_ANGLE)
#       Translate(Vector(-0.225 + LG_CORNER_SPACE,
#         LGBW + 0.08 - LG_CORNER_SPACE, 0)
#      ),
#      Box(
#       Vector(0, LG_CORNER_SPACE, -0.1 - LG_CORNER_SPACE),
#       Vector((0.175 + LG_CORNER_SPACE) / cos(LG_ANGLE * pi / 180),
#         -0.08, -LGPH + LG_CORNER_SPACE)
#       rotate Vector(0, 0, -LG_ANGLE)
#       Translate(Vector(0.225 - LG_CORNER_SPACE,
#         LGBW + 0.08 - LG_CORNER_SPACE, 0)
#      ),
#      Box(
#       Vector(0, 0, -0.1),
#       Vector((0.175 + LG_CORNER_SPACE) / cos(LG_ANGLE * pi / 180),
#         -0.08, -LGPH)
#       rotate Vector(0, 0, -LG_ANGLE)
#       Translate(Vector(0.225 - LG_CORNER_SPACE,
#         LGBW + 0.08 - LG_CORNER_SPACE, 0)
#      ),
#      Box(
#       Vector(-0.06, LG_KNOB_RADIUS + LG_E,
#         -LG_TOP_HEIGHT + LG_E),
#       Vector(0.06, LGBW - LG_WALL_WIDTH + LG_E,
#         -LGPH + LG_CORNER_SPACE)
#      ),
#      Cylinder(
#       Vector(0, LGBW, -0.2),
#       Vector(0, LGBW + 0.08, -0.2),
#       0.2 - LG_CORNER_SPACE
#      ),
#      Difference(
#       Cylinder(
#        Vector(0, LGBW - LG_CORNER_SPACE, -0.2),
#        Vector(0, LGBW + 0.08 - LG_CORNER_SPACE, -0.2),
#        0.2
#       ),
#       #if (PIN = -2)
#        Box(
#         Vector(0, LGBW - LG_CORNER_SPACE - LG_E,
#             -LGPH + LG_E),
#         Vector(-0.2 - LG_E, LGBW + LG_CORNER_SPACE,
#             -0.4 - LG_E)
#        ),
#       #else
#        Box(
#         Vector(0, LGBW - LG_CORNER_SPACE - LG_E,
#             -LGPH + LG_E),
#         Vector(0.2 + LG_E, LGBW + LG_CORNER_SPACE,
#             -0.4 - LG_E)
#        ),
#       #end
#      ),
#      torus {
#       0.2 - LG_CORNER_SPACE,
#       LG_CORNER_SPACE
#       Translate(Vector(0, LGBW + LG_CORNER_SPACE, -0.2)
#      ),
#      torus {
#       0.2 - LG_CORNER_SPACE,
#       LG_CORNER_SPACE
#       Translate(Vector(0, LGBW + 0.08 - LG_CORNER_SPACE, -0.2)
#      ),
#      Difference(
#       merge {
#        Cylinder(
#         Vector(0, LGBW + 0.08 - LG_E, -0.2),
#         Vector(0, LGBW + 0.56, -0.2),
#         LG_KNOB_INNER_RADIUS
#        ),
#        torus {
#         LG_KNOB_INNER_RADIUS,
#         LG_CORNER_SPACE
#         Translate(Vector(0, LGBW + 0.56 - LG_CORNER_SPACE, -0.2)
#        ),
#        torus {
#          LG_KNOB_INNER_RADIUS,
#         LG_CORNER_SPACE
#         Translate(Vector(0, LGBW + 0.48 + LG_CORNER_SPACE, -0.2)
#        ),
#        Cylinder(
#         Vector(0, LGBW + 0.48 + LG_CORNER_SPACE, -0.2),
#         Vector(0, LGBW + 0.56 - LG_CORNER_SPACE, -0.2),
#         LG_KNOB_INNER_RADIUS + LG_CORNER_SPACE
#        ),
#       ),
#       Union(
#        Box(
#         Vector(0.03, LGBW + 0.56 + LG_E, 0),
#         Vector(-0.03, LGBW + 0.3, -0.4 - LG_E)
#        ),
#        Cylinder(
#         Vector(0, LGBW + 0.3, 0),
#         Vector(0, LGBW + 0.3, -0.4 - LG_E),
#         0.03
#        ),
#       ),
#      ),
#      Translate(Vector(PIN*LGBW, 0, 0)
#     ),
#     #declare PIN = PIN + 5;
#    #end
#    #if (MIR = 1)
#     matrix Vector(1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0)
#    #end
#   ),
#   #declare MIR = MIR + 1;
#  #end
#  Cylinder(
#   Vector(2 * LGBW + LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   Vector(2 * LGBW + LG_CORNER_SPACE,
#     -LGBW + LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(4 * LGBW - LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   Vector(4 * LGBW - LG_CORNER_SPACE,
#     -LGBW + LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(-LGBW - LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   Vector(-LGBW - LG_CORNER_SPACE,
#     -LGBW + LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(-3 * LGBW + LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   Vector(-3 * LGBW + LG_CORNER_SPACE,
#     -LGBW + LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(3 * LGBW - LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, -2 * LGPH + LG_CORNER_SPACE),
#   Vector(3 * LGBW - LG_CORNER_SPACE,
#     -LGBW + LG_CORNER_SPACE, -2 * LGPH + LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(4 * LGBW - LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, -LGPH + LG_CORNER_SPACE),
#   Vector(4 * LGBW - LG_CORNER_SPACE,
#     -LGBW + LG_CORNER_SPACE, -LGPH + LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(-2 * LGBW + LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, -2 * LGPH + LG_CORNER_SPACE),
#   Vector(-2 * LGBW + LG_CORNER_SPACE,
#     -LGBW + LG_CORNER_SPACE, -2 * LGPH + LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(-3 * LGBW + LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, -LGPH + LG_CORNER_SPACE),
#   Vector(-3 * LGBW + LG_CORNER_SPACE,
#     -LGBW + LG_CORNER_SPACE, -LGPH + LG_CORNER_SPACE),
#   LG_CORNER_SPACE
#  ),
#  Cylinder(
#   Vector(3.5 * LGBW, 0, -LG_TOP_HEIGHT + LG_E),
#   Vector(3.5 * LGBW, 0, -LGPH),
#   LG_WALL_WIDTH
#  ),
#  Cylinder(
#   Vector(-2.5 * LGBW, 0, -LG_TOP_HEIGHT + LG_E),
#   Vector(-2.5 * LGBW, 0, -LGPH),
#   LG_WALL_WIDTH
#  ),
#  Object(
#   lg_plate_cylinder_clear
#   Translate(Vector(LGBW, 0, -2 * LGPH)
#  ),
#  Object(
#   lg_plate_cylinder_clear
#   Translate(Vector(0, 0, -2 * LGPH)
#  ),
#  Cylinder(
#   Vector(2.5 * LGBW, 0, -LG_TOP_HEIGHT + LG_E),
#   Vector(2.5 * LGBW, 0, -2 * LGPH),
#   LG_KNOB_INNER_RADIUS
#  ),
#  Cylinder(
#   Vector(-1.5 * LGBW, 0, -LG_TOP_HEIGHT + LG_E),
#   Vector(-1.5 * LGBW, 0, -2 * LGPH),
#   LG_KNOB_INNER_RADIUS
#  ),
#  Box(
#   Vector(2 * LGBW + LG_CORNER_SPACE,
#     0.04, -LG_TOP_HEIGHT + LG_E),
#   Vector(3 * LGBW - LG_CORNER_SPACE,
#     -0.04, -LGPH)
#  ),
#  Box(
#   Vector(-2 * LGBW + LG_CORNER_SPACE,
#     0.04, -LG_TOP_HEIGHT + LG_E),
#   Vector(-LGBW - LG_CORNER_SPACE,
#     -0.04, -LGPH)
#  ),
#  Box(
#   Vector(4 * LGBW - LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, -LGPH),
#   Vector(4 * LGBW - LG_WALL_WIDTH,
#     -LGBW + LG_CORNER_SPACE,
#     -LGPH + LG_CORNER_SPAC2 * LG_E)
#  ),
#  Box(
#   Vector(3 * LGBW - LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, -2 * LGPH),
#   Vector(3 * LGBW - LG_WALL_WIDTH,
#     -LGBW + LG_CORNER_SPACE,
#     -2 * LGPH + LG_CORNER_SPAC2 * LG_E)
#  ),
#  Box(
#   Vector(-2 * LGBW + LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, -2 * LGPH),
#   Vector(-2 * LGBW + LG_WALL_WIDTH,
#     -LGBW + LG_CORNER_SPACE,
#     -2 * LGPH + LG_CORNER_SPAC2 * LG_E)
#  ),
#  Box(
#   Vector(-3 * LGBW + LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, -LGPH),
#   Vector(-3 * LGBW + LG_WALL_WIDTH,
#     -LGBW + LG_CORNER_SPACE,
#     -LGPH + LG_CORNER_SPAC2 * LG_E)
#  ),
#  Box(
#   Vector(4 * LGBW,
#     LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   Vector(4 * LGBW - LG_WALL_WIDTH,
#     -LGBW + LG_CORNER_SPACE,
#     -LGPH + LG_CORNER_SPACE)
#  ),
#  Box(
#   Vector(3 * LGBW,
#     LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   Vector(3 * LGBW - LG_WALL_WIDTH,
#     -LGBW + LG_CORNER_SPACE,
#     -2 * LGPH + LG_CORNER_SPACE)
#  ),
#  Box(
#   Vector(-2 * LGBW,
#     LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   Vector(-2 * LGBW + LG_WALL_WIDTH,
#     -LGBW + LG_CORNER_SPACE,
#     -2 * LGPH + LG_CORNER_SPACE)
#  ),
#  Box(
#   Vector(-3 * LGBW,
#     LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   Vector(-3 * LGBW + LG_WALL_WIDTH,
#     -LGBW + LG_CORNER_SPACE, -LGPH + LG_CORNER_SPACE)
#  ),
#  Box(
#   Vector(2 * LGBW,
#     LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   Vector(2 * LGBW + LG_WALL_WIDTH,
#     -LGBW + LG_CORNER_SPACE, -2 * LGPH)
#  ),
#  Box(
#   Vector(2 * LGBW - LG_CORNER_SPACE - LG_E,
#     LGBW - LG_CORNER_SPACE, -LGPH),
#   Vector(2 * LGBW + LG_WALL_WIDTH / 2,
#     -LGBW + LG_CORNER_SPACE, -LGPH - LG_TOP_HEIGHT)
#  ),
#  Box(
#   Vector(-LGBW + LG_CORNER_SPAC2 * LG_E,
#     LGBW - LG_CORNER_SPACE, -LGPH),
#   Vector(-LGBW - LG_WALL_WIDTH / 2,
#     -LGBW + LG_CORNER_SPACE, -LGPH - LG_TOP_HEIGHT)
#  ),
#  Box(
#   Vector(-LGBW,
#     LGBW - LG_CORNER_SPACE, -LG_CORNER_SPACE),
#   Vector(-LGBW - LG_WALL_WIDTH,
#    -LGBW + LG_CORNER_SPACE, -2 * LGPH)
#  ),
#  Difference(
#   Box(
#    Vector(4 * LGBW - LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, 0),
#    Vector(2 * LGBW + LG_CORNER_SPACE,
#     -LGBW + LG_CORNER_SPACE, -LG_TOP_HEIGHT)
#   ),
#   Union(
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(3.5 * LGBW,
#         LGBW / 2, -LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(2.5 * LGBW,
#         LGBW / 2, -LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(3.5 * LGBW,
#         -LGBW / 2, -LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(2.5 * LGBW,
#         -LGBW / 2, -LG_TOP_HEIGHT)
#    ),
#   ),
#  ),
#  Difference(
#   Box(
#    Vector(-LGBW - LG_CORNER_SPACE,
#     LGBW - LG_CORNER_SPACE, 0),
#    Vector(-3 * LGBW + LG_CORNER_SPACE,
#     -LGBW + LG_CORNER_SPACE, -LG_TOP_HEIGHT)
#   ),
#   Union(
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(-2.5 * LGBW,
#         LGBW / 2, -LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(-1.5 * LGBW,
#         LGBW / 2, -LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(-2.5 * LGBW,
#         -LGBW / 2, -LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(-1.5 * LGBW,
#         -LGBW / 2, -LG_TOP_HEIGHT)
#    ),
#   ),
#  ),
#  Difference(
#   Box(
#    Vector(-LGBW + LG_CORNER_SPACE,
#     2 * LGBW - LG_CORNER_SPACE, -LGPH),
#    Vector(2 * LGBW - LG_CORNER_SPACE,
#     -2 * LGBW + LG_CORNER_SPACE, -LGPH - LG_TOP_HEIGHT)
#   ),
#   Union(
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(1.5 * LGBW,
#         LGBW / 2, -LGPH - LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(0.5 * LGBW,
#         LGBW / 2, -LGPH - LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(-0.5 * LGBW,
#         LGBW / 2, -LGPH - LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(1.5 * LGBW,
#         -LGBW / 2, -LGPH - LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(0.5 * LGBW,
#         -LGBW / 2, -LGPH - LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(-0.5 * LGBW,
#         -LGBW / 2, -LGPH - LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(1.5 * LGBW,
#         3 * LGBW / 2, -LGPH - LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(0.5 * LGBW,
#         3 * LGBW / 2, -LGPH - LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(-0.5 * LGBW,
#         3 * LGBW / 2, -LGPH - LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(1.5 * LGBW,
#         -3 * LGBW / 2, -LGPH - LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(0.5 * LGBW,
#         -3 * LGBW / 2, -LGPH - LG_TOP_HEIGHT)
#    ),
#    Object(
#     lg_knob_inner_space_clear
#     Translate(Vector(-0.5 * LGBW,
#         -3 * LGBW / 2, -LGPH - LG_TOP_HEIGHT)
#    ),
#   ),
#  ),
#  Translate(Vector(-0.5 * LGBW, 0, 0)
# ),
