"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from SceneItem import *
from Vector import *


class PoVObject(SceneItem):
    """
        OBJECT:
            FINITE_SOLID_OBJECT | FINITE_PATCH_OBJECT |
            INFINITE_SOLID_OBJECT | ISOSURFACE_OBJECT | PARAMETRIC_OBJECT |
            CSG_OBJECT | LIGHT_SOURCE |
            object { OBJECT_IDENTIFIER [OBJECT_MODIFIERS...] }
    """


class FiniteSolid(PoVObject):
    """
        FINITE_SOLID_OBJECT:
            BLOB | BOX | CONE | CYLINDER | HEIGHT_FIELD | JULIA_FRACTAL |
            LATHE | PRISM | SPHERE | SPHERESWEEP | SUPERELLIPSOID | SOR |
            TEXT | TORUS
    """


class FinitePatch(PoVObject):
    """
        FINITE_PATCH_OBJECT:
            BICUBIC_PATCH | DISC | MESH | MESH2 | POLYGON | TRIANGLE |
            SMOOTH_TRIANGLE
    """


class IsoSurface(PoVObject):
    """
        ISOSURFACE_OBJECT:
            ISOSURFACE
    """


class ParametricObj(PoVObject):
    """
        PARAMETRIC_OBJECT:
            PARAMETRIC
    """


class Object(PoVObject):
    """
         object {
           OBJECT_IDENTIFIER | OBJECT {}
           LIST_ITEM_A, LIST_ITEM_B
         }
    """


class InfiniteSolid(PoVObject):
    """
        INFINITE_SOLID_OBJECT:
            PLANE | POLY | CUBIC | QUARTIC | QUADRIC
    """


class Csg(PoVObject):
    """
        CSG_OBJECT:
            UNION | INTERSECTION | DIFFERENCE | MERGE
    """


class Blob(FiniteSolid):
    """
        BLOB:
            blob { BLOB_ITEM... [BLOB_MODIFIERS...]}
        BLOB_ITEM:
            sphere{<Center>, Radius,
                   [ strength ] Strength[COMPONENT_MODIFIER...] } |
            cylinder{<End1>, <End2>, Radius,
                     [ strength ] Strength [COMPONENT_MODIFIER...] } |
            component Strength, Radius, <Center> |
            threshold Amount
        COMPONENT_MODIFIER:
            TEXTURE | PIGMENT | NORMAL | FINISH | TRANSFORMATION
        BLOB_MODIFIER:
            hierarchy [Boolean] | sturm [Boolean] | OBJECT_MODIFIER
    """

    def __init__(self, args=[], opts=[], **kwargs):
        """
            TODO: constructor apidoc
        """
        # TODO: Syntax Checking

        super(Blob, self).__init__("blob", args=[], opts=[], **kwargs)


class Box(FiniteSolid):
    """
        BOX:
            box
            {
                <Corner_1>, <Corner_2>
                [OBJECT_MODIFIERS...]
            }

    """
    def __init__(self, v1, v2, *opts, **kwargs):
        """
            Construct a box object

            @param v1: vertex of box
            @type v1: Vector()
            @param v2: opposing vertex of box
            @type v2: Vector()
        """

        # Syntax checking
        assert isinstance(v1, Vector)
        assert len(v1.v) == 3
        assert isinstance(v2, Vector)
        assert len(v2.v) == 3
        # TODO: make sure only valid object modifiers are passed
        for i in range(len(opts)):
            assert isInstance(i, ObjectModifier)

        super(Box, self).__init__("box", (v1, v2), opts, **kwargs)


class Cone(FiniteSolid):
    """
        CONE:
            cone
            {
                <Base_Point>, Base_Radius, <Cap_Point>, Cap_Radius
                [ open ][OBJECT_MODIFIERS...]
            }
    """
    def __init__(self, basepoint, baseradius, cappoint, capradius, *opts, **kwargs):
        """
            Construct a cone object

            @param basepoint: Base point of cone
            @type  basepoint: Vector
            @param baseradius: Base radius of cone
            @type  baseradius: Float
            @param cappoint: Cap point of cone
            @type  cappoint: Vector
            @param capradius: Cap radius of cone
            @type  capradius: Float

        """

        # Syntax checking
        assert isinstance(basepoint, Vector)
        assert len(basepoint.v) == 3
        assert type(baseradius) in (int, float)
        assert isinstance(cappoint, Vector)
        assert len(cappoint.v) == 3
        assert type(capradius) in (int, float)
        # TODO: Make sure only valid Object Modifiers are passed
        for i in range(len(opts)):
            assert isInstance(i, ObjectModifier)
        for key, val in kwargs.items():
            assert key in ['open']

        super(Cone, self).__init__(
            "cone",
            (basepoint, baseradius, cappoint, capradius),
            opts, **kwargs
        )


class cylinder(FiniteSolid):
    """
       CYLINDER:
            cylinder
            {
                <Base_Point>, <Cap_Point>, Radius
                [ open ][OBJECT_MODIFIERS...]
            }
    """
    def __init__(self, basepoint, cappoint, radius, *opts, **kwargs):
        """
            @param basepoint: Base point of cylinder
            @type  basepoint: Vector
            @param cappoint: Cap point of cylinder
            @type  cappoint: Vector
            @param radius: Radius of cylinder
            @type  radius: Float
        """

        assert isinstance(basepoint, Vector)
        assert len(basepoint.v) == 3
        assert type(baseradius) in (int, float)
        assert isinstance(cappoint, Vector)
        assert len(cappoint.v) == 3




