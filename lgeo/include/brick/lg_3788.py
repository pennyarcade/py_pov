"""
LGEO Libray Include File.

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19970801 Lutz Uhlmann
20080102 Lutz Uhlmann fixed stud orientation

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_3788: Car Mudguard 2 x 4
"""

from math import atan2, pi, cos

from lgeo.include.common.lg_defs import LGBW, LGCS, LG_PLATE_INNER_HEIGHT
from lgeo.include.common.lg_defs import LGPH, LG_KNOB_INNER_SPACE
from lgeo.include.common.lg_defs import LG_TOP_HEIGHT, LG_E, LG_WALL_WIDTH
from lgeo.include.common.lg_defs import get_lg_cylinder
from lgeo.include.common.brick_subparts import lg_knob

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference
from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere
from pov.object_modifier.Translate import Translate
from pov.object_modifier.Rotate import Rotate
from pov.other.Object import Object


LG_ANGLE = atan2(0.44, 0.38) * 180 / pi


def solid():
    """LG 3788 Solid brick."""
    mainpart = Union()

    for rot in (0, 1):
        rotpart = Union(
            Sphere(
                Vector(
                    LGBW - LGCS,
                    2 * LGBW - LGCS,
                    -LGCS
                ), LGCS
            ),
            Sphere(
                Vector(
                    LGBW - LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH + LGCS
                ), LGCS
            ),
            Sphere(
                Vector(
                    -LGBW + LGCS,
                    2 * LGBW - LGCS,
                    -LGCS
                ), LGCS
            ),
            Sphere(
                Vector(
                    -LGBW + LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH + LGCS
                ), LGCS
            ),
            Sphere(
                Vector(
                    -LGBW + LGCS,
                    LGBW + LGCS,
                    -LGCS
                ), LGCS
            ),
            Sphere(
                Vector(
                    LGBW - LGCS,
                    LGBW + LGCS,
                    -LGCS
                ), LGCS
            ),
            Sphere(
                Vector(
                    -LGBW + 0.12 - LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH + LGCS
                ), LGCS
            ),
            Sphere(
                Vector(
                    LGBW - 0.12 + LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH + LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    LGBW - LGCS,
                    2 * LGBW - LGCS,
                    -LGCS
                ),
                Vector(
                    LGBW - LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH + LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    -LGBW + LGCS,
                    2 * LGBW - LGCS,
                    -LGCS
                ),
                Vector(
                    -LGBW + LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH + LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    -LGBW + LGCS,
                    LGBW + LGCS,
                    -LGCS
                ),
                Vector(
                    LGBW - LGCS,
                    LGBW + LGCS,
                    -LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    -LGBW + LGCS,
                    2 * LGBW - LGCS,
                    -LGCS
                ),
                Vector(
                    LGBW - LGCS,
                    2 * LGBW - LGCS,
                    -LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    -LGBW + 0.12 - LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH + LGCS
                ),
                Vector(
                    -LGBW + LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH + LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    LGBW - 0.12 + LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH + LGCS
                ),
                Vector(
                    LGBW - LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH + LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    -LGBW + LGCS,
                    2 * LGBW - LGCS,
                    -LGCS
                ),
                Vector(
                    -LGBW + LGCS,
                    LGBW + LGCS,
                    -LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    LGBW - LGCS,
                    2 * LGBW - LGCS,
                    -LGCS
                ),
                Vector(
                    LGBW - LGCS,
                    LGBW + LGCS,
                    -LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    LGBW - LGCS,
                    -2 * LGBW + LGCS,
                    -2 * LGPH + LGCS
                ),
                Vector(
                    LGBW - LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH + LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    LGBW - 0.12 + LGCS,
                    LGBW - LGCS,
                    -2 * LGPH + LGCS
                ),
                Vector(
                    LGBW - 0.12 + LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH + LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    -LGBW + 0.12 - LGCS,
                    LGBW - LGCS,
                    -2 * LGPH + LGCS
                ),
                Vector(
                    -LGBW + 0.12 - LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH + LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    -LGBW + LGCS,
                    LGBW + LGCS,
                    -LGCS
                ),
                Vector(
                    -LGBW + LGCS,
                    LGBW + LGCS,
                    -LGPH - LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    LGBW - LGCS,
                    LGBW + LGCS,
                    -LGCS
                ),
                Vector(
                    LGBW - LGCS,
                    LGBW + LGCS,
                    -LGPH - LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    -LGBW + LGCS,
                    LGBW + LGCS,
                    -LGPH - LGCS
                ),
                Vector(
                    -LGBW + LGCS,
                    -LGBW - LGCS,
                    -LGPH - LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    LGBW - LGCS,
                    LGBW + LGCS,
                    -LGPH - LGCS
                ),
                Vector(
                    LGBW - LGCS,
                    -LGBW - LGCS,
                    -LGPH - LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    LGBW - 0.12 + LGCS,
                    LGBW - LGCS,
                    -2 * LGPH + LGCS
                ),
                Vector(
                    -LGBW + 0.12 - LGCS,
                    LGBW - LGCS,
                    -2 * LGPH + LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    LGBW - 0.12 + LGCS,
                    -LGBW + LGCS,
                    -2 * LGPH + LGCS
                ),
                Vector(
                    -LGBW + 0.12 - LGCS,
                    -LGBW + LGCS,
                    -2 * LGPH + LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(
                    -0.3 - LGCS,
                    2 * LGBW - LGCS,
                    -0.2 + LGCS
                ),
                Vector(
                    0.3 + LGCS,
                    2 * LGBW - LGCS,
                    -0.2 + LGCS
                ), LGCS
            ),
            Cylinder(
                Vector(0, 0, 0),
                Vector(0.38 / cos(LG_ANGLE * pi / 180), 0, 0),
                LGCS,
                Rotate(Vector(0, -LG_ANGLE, 0)),
                Translate(
                    Vector(
                        -LGBW + 0.12 - LGCS,
                        2 * LGBW - LGCS,
                        -2 * LGPH + LGCS
                    )
                )
            ),
            Cylinder(
                Vector(0, 0, 0),
                Vector(-0.38 / cos(LG_ANGLE * pi / 180), 0, 0),
                LGCS,
                Rotate(Vector(0, LG_ANGLE, 0)),
                Translate(
                    Vector(
                        LGBW - 0.12 + LGCS,
                        2 * LGBW - LGCS,
                        -2 * LGPH + LGCS
                    )
                )
            ),
            Difference(
                Union(
                    Box(
                        Vector(
                            LGBW - LGCS,
                            2 * LGBW - LGCS,
                            0
                        ),
                        Vector(
                            -LGBW + LGCS,
                            LGBW + LGCS,
                            -2 * LGPH
                        )
                    ),
                    Box(
                        Vector(
                            LGBW,
                            2 * LGBW - LGCS,
                            -LGCS
                        ),
                        Vector(
                            -LGBW,
                            LGBW + LGCS,
                            -2 * LGPH + LGCS
                        )
                    ),
                    Box(
                        Vector(
                            LGBW - LGCS,
                            2 * LGBW,
                            -LGCS
                        ),
                        Vector(
                            -LGBW + LGCS,
                            LGBW,
                            -2 * LGPH + LGCS
                        )
                    )
                ),
                Union(
                    Object(
                        LG_KNOB_INNER_SPACE,
                        Translate(
                            Vector(
                                LGBW / 2,
                                1.5 * LGBW,
                                -LG_TOP_HEIGHT
                            )
                        )
                    ),
                    Object(
                        LG_KNOB_INNER_SPACE,
                        Translate(
                            Vector(
                                -LGBW / 2,
                                1.5 * LGBW,
                                -LG_TOP_HEIGHT
                            )
                        )
                    ),
                    Box(
                        Vector(
                            LGBW - 0.12,
                            2 * LGBW - 0.12,
                            -LG_TOP_HEIGHT
                        ),
                        Vector(
                            -LGBW + 0.12,
                            LGBW - LG_E,
                            -2 * LGPH - LG_E
                        )
                    ),
                    Box(
                        Vector(
                            LGBW - 0.12 + LGCS,
                            2 * LGBW - 0.12,
                            -2 * LGPH + LGCS
                        ),
                        Vector(
                            -LGBW + 0.12 - LGCS,
                            LGBW - LGCS,
                            -2 * LGPH - LG_E
                        )
                    ),
                    Box(
                        Vector(-LGCS, -LG_WALL_WIDTH, 0),
                        Vector(
                            0.38 / cos(LG_ANGLE * pi / 180),
                            LGCS + LG_E,
                            -0.5
                        ),
                        Rotate(Vector(0, -LG_ANGLE, 0)),
                        Translate(
                            Vector(
                                -LGBW + 0.12 - LGCS,
                                2 * LGBW - LGCS,
                                -2 * LGPH + LGCS
                            )
                        )
                    ),
                    Box(
                        Vector(LGCS, -LG_WALL_WIDTH, 0),
                        Vector(
                            -0.38 / cos(LG_ANGLE * pi / 180),
                            LGCS + LG_E,
                            -0.5
                        ),
                        Rotate(Vector(0, LG_ANGLE, 0)),
                        Translate(
                            Vector(
                                LGBW - 0.12 + LGCS,
                                2 * LGBW - LGCS,
                                -2 * LGPH + LGCS
                            )
                        )
                    ),
                    Box(
                        Vector(
                            -0.3 - LGCS,
                            2 * LGBW - LG_WALL_WIDTH,
                            -0.2 + LGCS
                        ),
                        Vector(
                            0.3 + LGCS,
                            2 * LGBW + LG_E,
                            -2 * LGPH - LG_E
                        )
                    )
                )
            ),
            Difference(
                Box(
                    Vector(
                        LGBW - LGCS,
                        LGBW + 0.13,
                        -LGCS
                    ),
                    Vector(
                        -LGBW + LGCS,
                        LGBW - LG_WALL_WIDTH,
                        -2 * LGPH + LGCS
                    )
                ),
                Union(
                    Box(
                        Vector(LGBW, 0.2, 0),
                        Vector(-LGBW, 0, -0.4 / cos(18.00416161)),
                        Rotate(Vector(-18.00416161, 0, 0)),
                        Translate(Vector(0, LGBW + 0.13, -0.2))
                    ),
                    Box(
                        Vector(LGBW, LGBW, 0),
                        Vector(
                            -LGBW,
                            LGBW - 0.2,
                            -LGPH - LG_E
                        )
                    ),
                ),
            ),
            Box(
                Vector(
                    LGBW,
                    LGBW + 0.1,
                    -LGPH - LGCS
                ),
                Vector(
                    LGBW - 0.12 + LG_E,
                    -LGBW - 0.1,
                    -2 * LGPH + LGCS
                )
            ),
            Box(
                Vector(
                    LGBW - LGCS,
                    LGBW + 0.1,
                    -LGPH - LGCS
                ),
                Vector(
                    LGBW - 0.12 + LGCS,
                    -LGBW - 0.1,
                    -2 * LGPH
                )
            ),
            Box(
                Vector(
                    LGBW - 0.12,
                    LGBW - LGCS,
                    -LGPH - LGCS
                ),
                Vector(
                    LGBW - 0.12 + LGCS + LG_E,
                    -LGBW + LGCS,
                    -2 * LGPH
                )
            ),
            Box(
                Vector(
                    LGBW - LGCS,
                    LGBW - LGCS,
                    -2 * LGPH
                ),
                Vector(
                    -LGBW + LGCS,
                    LGBW - LG_WALL_WIDTH,
                    -2 * LGPH + LGCS + LG_E
                )
            ),
            Box(
                Vector(
                    LGBW - LG_WALL_WIDTH,
                    LGBW / 2 + 0.04,
                    -2 * LGPH + LGCS
                ),
                Vector(
                    LGBW - 0.1,
                    LGBW / 2 - 0.04,
                    -LGPH - LGCS
                )
            ),
            Box(
                Vector(
                    -LGBW + LG_WALL_WIDTH,
                    LGBW / 2 + 0.04,
                    -2 * LGPH + LGCS
                ),
                Vector(
                    -LGBW + 0.1,
                    LGBW / 2 - 0.04,
                    -LGPH - LGCS
                )
            ),
            Box(
                Vector(0, - 0.12 + LGCS, -LGCS),
                Vector(0.38 / cos(LG_ANGLE * pi / 180), 0, LG_E),
                Rotate(Vector(0, -LG_ANGLE, 0)),
                Translate(
                    Vector(
                        -LGBW + 0.12 - LGCS,
                        2 * LGBW - LGCS,
                        -2 * LGPH + LGCS
                    )
                )
            ),
            Box(
                Vector(0, -0.12 + LGCS, -LGCS),
                Vector(-0.38 / cos(LG_ANGLE * pi / 180), 0, LG_E),
                Rotate(Vector(0, LG_ANGLE, 0)),
                Translate(
                    Vector(
                        LGBW - 0.12 + LGCS,
                        2 * LGBW - LGCS,
                        -2 * LGPH + LGCS
                    )
                )
            ),
            Box(
                Vector(
                    -0.3 - LGCS,
                    2 * LGBW - 0.12,
                    -0.2 + LGCS
                ),
                Vector(
                    0.3 + LGCS,
                    2 * LGBW - LGCS,
                    -0.2
                )
            ),
            Box(
                Vector(
                    LGBW - 0.12 + LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH
                ),
                Vector(
                    LGBW - LGCS,
                    2 * LGBW - 0.12e0,
                    -2 * LGPH + LGCS
                )
            ),
            Box(
                Vector(
                    -LGBW + 0.12 - LGCS,
                    2 * LGBW - LGCS,
                    -2 * LGPH
                ),
                Vector(
                    -LGBW + LGCS,
                    2 * LGBW - 0.12e0,
                    -2 * LGPH + LGCS
                )
            ),
            Object(
                lg_knob(),
                Rotate(Vector(0, 0, 90 + 180 * rot)),
                Translate(
                    Vector(
                        LGBW / 2,
                        LGBW / 2,
                        -LGPH
                    )
                )
            ),
            Object(
                lg_knob(),
                Rotate(Vector(0, 0, 90 + 180 * rot)),
                Translate(
                    Vector(
                        -LGBW / 2,
                        LGBW / 2,
                        -LGPH
                    )
                )
            ),
            Object(
                lg_knob(),
                Rotate(Vector(0, 0, 90 + 180 * rot)),
                Translate(
                    Vector(LGBW / 2, 3 * LGBW / 2, 0)
                )
            ),
            Object(
                lg_knob(),
                Rotate(Vector(0, 0, 90 + 180 * rot)),
                Translate(
                    Vector(-LGBW / 2, 3 * LGBW / 2, 0)
                )
            )
        )

        if rot == 1:
            rotpart.append(
                Rotate(Vector(0, 0, 180))
            )
        mainpart.append(rotpart)

    mainpart.append(
        Difference(
            Box(
                Vector(
                    LGBW - LGCS,
                    LGBW + LGCS,
                    -LGPH
                ),
                Vector(
                    -LGBW + LGCS,
                    -LGBW - LGCS,
                    -LGPH - LG_TOP_HEIGHT
                )
            ),
            Union(
                Object(
                    LG_KNOB_INNER_SPACE,
                    Translate(
                        Vector(
                            LGBW / 2,
                            LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    LG_KNOB_INNER_SPACE,
                    Translate(
                        Vector(
                            -LGBW / 2,
                            LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    LG_KNOB_INNER_SPACE,
                    Translate(
                        Vector(
                            -LGBW / 2,
                            -LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                ),
                Object(
                    LG_KNOB_INNER_SPACE,
                    Translate(
                        Vector(
                            LGBW / 2,
                            -LGBW / 2,
                            -LGPH - LG_TOP_HEIGHT
                        )
                    )
                )
            )
        ),
        Object(
            get_lg_cylinder(Union, LG_PLATE_INNER_HEIGHT),
            Translate(Vector(0, 0, -2 * LGPH))
        )
    )

    return mainpart
