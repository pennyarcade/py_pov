"""
LGEO Libray Include File

(C) lgeo@digitalbricks.org (Lutz Uhlmann)

19990514 Lutz Uhlmann

This file is in no way related to the LEGO(tm) Group.
It is provided for private non-commercial use only.

lg_4865: Panel 1 x 2 x 1
"""


from lgeo.include.common.lg_defs import LGCS, LGBW, LGPH, LG_E, LGBH
from lgeo.include.common.lg_defs import LG_WALL_WIDTH, LG_PLATE_INNER_HEIGHT

from pov.basic.Vector import Vector

from pov.csg.Union import Union
from pov.csg.Difference import Difference

from pov.finite_solid.Box import Box
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.Sphere import Sphere

from pov.object_modifier.Rotate import Rotate
from pov.object_modifier.Translate import Translate


def solid(length=2, width=1, height=1):
    """return lg_4865: Panel 1 x 2 x 1."""
    result = Union(
    )

    for rot in range(0, 2):
        rotation = Rotate(Vector(0, 0, 0))
        if rot == 1:
            rotation = Rotate(Vector(0, 0, 180))

        result.append(
            Union(
             Sphere(
              Vector(
                  length / 2 * LGBW - LGCS,
                  width / 2 * LGBW - LGCS,
                  -height * LGBH + LGCS
              ),
              LGCS
             ),
             Sphere(
              Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -height*LGBH+LGCS), LGCS
             ),
             Cylinder(
              Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -height*LGBH+LGCS),
              Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -height*LGBH+LGCS),
              LGCS
             ),
             Cylinder(
              Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -height*LGBH+LGCS),
              Vector(length/2*LGBW-LGCS, -width/2*LGBW+LGCS, -height*LGBH+LGCS),
              LGCS
             ),
             rotation
            ),
        )

    return result


#  #end
#  Cylinder(
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, width/2*LGBW-LGCS, -LGCS),
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, -width/2*LGBW+LGCS, -LGCS),
#   Vector(-length/2*LGBW+LGCS, -width/2*LGBW+LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -LGCS),
#   Vector(-length/2*LGBW+LGCS, -width/2*LGBW+LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, width/2*LGBW-LGCS, -LGCS),
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, -width/2*LGBW+LGCS, -LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, width/2*LGBW-LGCS, -LGCS), LGCS
#  ),
#  Sphere(
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, -width/2*LGBW+LGCS, -LGCS), LGCS
#  ),
#  Sphere(
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -LGCS), LGCS
#  ),
#  Sphere(
#   Vector(-length/2*LGBW+LGCS, -width/2*LGBW+LGCS, -LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -LGCS),
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -height*LGBH+LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW+LGCS, -width/2*LGBW+LGCS, -LGCS),
#   Vector(-length/2*LGBW+LGCS, -width/2*LGBW+LGCS, -height*LGBH+LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, -width/2*LGBW+LGCS, -LGCS),
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, width/2*LGBW-LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW-LGCS+LG_WALL_WIDTH, width/2*LGBW-LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW-LGCS+LG_WALL_WIDTH, -width/2*LGBW+LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   Vector(length/2*LGBW-LGCS, -width/2*LGBW+LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -height*LGBH+LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length/2*LGBW-LGCS, -width/2*LGBW+LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   Vector(length/2*LGBW-LGCS, -width/2*LGBW+LGCS, -height*LGBH+LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length/2*LGBW-LGCS, -width/2*LGBW+LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW-LGCS+LG_WALL_WIDTH, width/2*LGBW-LGCS, -LGCS),
#   Vector(-length/2*LGBW-LGCS+LG_WALL_WIDTH, width/2*LGBW-LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW-LGCS+LG_WALL_WIDTH, -width/2*LGBW+LGCS, -LGCS),
#   Vector(-length/2*LGBW-LGCS+LG_WALL_WIDTH, -width/2*LGBW+LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(length/2*LGBW-LGCS, -width/2*LGBW+LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),LGCS
#  ),
#  Sphere(
#   Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),LGCS
#  ),
#  difference {
#   Union(
#    box {
#     Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -height*LGBH+LG_PLATE_HEIGHT)
#     Vector(-length/2*LGBW+LGCS, -width/2*LGBW+LGCS, -height*LGBH)
#    ),
#    box {
#     Vector(length/2*LGBW, width/2*LGBW-LGCS, -height*LGBH+LG_PLATE_HEIGHT-LGCS)
#     Vector(-length/2*LGBW, -width/2*LGBW+LGCS, -height*LGBH+LGCS)
#    ),
#    box {
#     Vector(length/2*LGBW-LGCS, width/2*LGBW, -height*LGBH+LG_PLATE_HEIGHT-LGCS)
#     Vector(-length/2*LGBW+LGCS, -width/2*LGBW, -height*LGBH+LGCS)
#    ),
#   ),
#   box {
#    Vector(length/2*LGBW-LG_WALL_WIDTH, width/2*LGBW-LG_WALL_WIDTH, -height*LGBH+LG_PLATE_HEIGHT-LG_TOP_HEIGHT)
#    Vector(-length/2*LGBW+LG_WALL_WIDTH, -width/2*LGBW+LG_WALL_WIDTH, -height*LGBH-LG_E)
#   ),
#  ),
#  box {
#   Vector(-length/2*LGBW, width/2*LGBW-LGCS, -LGCS)
#   Vector(-length/2*LGBW+LG_WALL_WIDTH, -width/2*LGBW+LGCS, -height*LGBH+LGCS)
#  ),
#  box {
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW, -LGCS)
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, -width/2*LGBW, -height*LGBH+LGCS)
#  ),
#  box {
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -2*LGCS)
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, -width/2*LGBW+LGCS, 0)
#  ),
#  object {
#   lg_plate_column
#   translate Vector(0, 0, -height*LGBH)
#  ),
# ),

# #declare lg_4865_clear =
# merge {
#  #declare ROT = 0;
#  #while (ROT Vector( 2)
#   merge {
#    Sphere(
#     Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -height*LGBH+LGCS), LGCS
#    ),
#    Sphere(
#     Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -height*LGBH+LGCS), LGCS
#    ),
#    Cylinder(
#     Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -height*LGBH+LGCS),
#     Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -height*LGBH+LGCS),
#     LGCS
#    ),
#    Cylinder(
#     Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -height*LGBH+LGCS),
#     Vector(length/2*LGBW-LGCS, -width/2*LGBW+LGCS, -height*LGBH+LGCS),
#     LGCS
#    ),
#    #if (ROT=1)
#     rotate Vector(0, 0, 180)
#    #end
#   ),
#   #declare ROT = ROT + 1;
#  #end
#  Cylinder(
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, width/2*LGBW-LGCS, -LGCS),
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, -width/2*LGBW+LGCS, -LGCS),
#   Vector(-length/2*LGBW+LGCS, -width/2*LGBW+LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -LGCS),
#   Vector(-length/2*LGBW+LGCS, -width/2*LGBW+LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, width/2*LGBW-LGCS, -LGCS),
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, -width/2*LGBW+LGCS, -LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, width/2*LGBW-LGCS, -LGCS), LGCS
#  ),
#  Sphere(
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, -width/2*LGBW+LGCS, -LGCS), LGCS
#  ),
#  Sphere(
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -LGCS), LGCS
#  ),
#  Sphere(
#   Vector(-length/2*LGBW+LGCS, -width/2*LGBW+LGCS, -LGCS), LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -LGCS),
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -height*LGBH+LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW+LGCS, -width/2*LGBW+LGCS, -LGCS),
#   Vector(-length/2*LGBW+LGCS, -width/2*LGBW+LGCS, -height*LGBH+LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, -width/2*LGBW+LGCS, -LGCS),
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, width/2*LGBW-LGCS, -LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW-LGCS+LG_WALL_WIDTH, width/2*LGBW-LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW-LGCS+LG_WALL_WIDTH, -width/2*LGBW+LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   Vector(length/2*LGBW-LGCS, -width/2*LGBW+LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -height*LGBH+LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length/2*LGBW-LGCS, -width/2*LGBW+LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   Vector(length/2*LGBW-LGCS, -width/2*LGBW+LGCS, -height*LGBH+LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(length/2*LGBW-LGCS, -width/2*LGBW+LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW-LGCS+LG_WALL_WIDTH, width/2*LGBW-LGCS, -LGCS),
#   Vector(-length/2*LGBW-LGCS+LG_WALL_WIDTH, width/2*LGBW-LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   LGCS
#  ),
#  Cylinder(
#   Vector(-length/2*LGBW-LGCS+LG_WALL_WIDTH, -width/2*LGBW+LGCS, -LGCS),
#   Vector(-length/2*LGBW-LGCS+LG_WALL_WIDTH, -width/2*LGBW+LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),
#   LGCS
#  ),
#  Sphere(
#   Vector(length/2*LGBW-LGCS, -width/2*LGBW+LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),LGCS
#  ),
#  Sphere(
#   Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -(height*3-1)*LG_PLATE_HEIGHT-LGCS),LGCS
#  ),
#  difference {
#   merge {
#    box {
#     Vector(length/2*LGBW-LGCS, width/2*LGBW-LGCS, -height*LGBH+LG_PLATE_HEIGHT)
#     Vector(-length/2*LGBW+LGCS, -width/2*LGBW+LGCS, -height*LGBH)
#    ),
#    box {
#     Vector(length/2*LGBW, width/2*LGBW-LGCS, -height*LGBH+LG_PLATE_HEIGHT-LGCS)
#     Vector(-length/2*LGBW, -width/2*LGBW+LGCS, -height*LGBH+LGCS)
#    ),
#    box {
#     Vector(length/2*LGBW-LGCS, width/2*LGBW, -height*LGBH+LG_PLATE_HEIGHT-LGCS)
#     Vector(-length/2*LGBW+LGCS, -width/2*LGBW, -height*LGBH+LGCS)
#    ),
#   ),
#   box {
#    Vector(length/2*LGBW-LG_WALL_WIDTH, width/2*LGBW-LG_WALL_WIDTH, -height*LGBH+LG_PLATE_HEIGHT-LG_TOP_HEIGHT)
#    Vector(-length/2*LGBW+LG_WALL_WIDTH, -width/2*LGBW+LG_WALL_WIDTH, -height*LGBH-LG_E)
#   ),
#  ),
#  box {
#   Vector(-length/2*LGBW, width/2*LGBW-LGCS, -LGCS)
#   Vector(-length/2*LGBW+LG_WALL_WIDTH, -width/2*LGBW+LGCS, -height*LGBH+LGCS)
#  ),
#  box {
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW, -LGCS)
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, -width/2*LGBW, -height*LGBH+LGCS)
#  ),
#  box {
#   Vector(-length/2*LGBW+LGCS, width/2*LGBW-LGCS, -2*LGCS)
#   Vector(-length/2*LGBW+LG_WALL_WIDTH-LGCS, -width/2*LGBW+LGCS, 0)
#  ),
#  object {
#   lg_plate_column_clear
#   translate Vector(0, 0, -height*LGBH)
#  ),
# ),

# #end
