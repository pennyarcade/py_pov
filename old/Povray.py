#!/usr/bin/env python

"""
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from __future__ import nested_scopes
import os
from math import sqrt
import Vector

##################################################

class File:
    """
    POV-Ray scene file object.

    """

    def lock(self, item):
        #print "lock",id(item)
        assert self.__lock is None
        self.__lock = item

    def unlock(self, item):
        #print "unlock",id(item)
        assert self.__lock is item
        self.__lock = None

    def indent(self):
        self.__indent += 1

    def dedent(self):
        self.__indent -= 1
        assert self.__indent >= 0

    def block_begin(self):
        self.writeln("{")
        self.indent()

    def block_end(self):
        self.dedent()
        self.writeln("}")
        if self.__indent == 0:
            # blank line if this is a top level end
            self.writeln()

    def writeln(self, s=""):
        #print "  "*self.__indent+s
        assert self.__lock is None
        self.file.write("  "*self.__indent+s+os.linesep)

    #######################################################
    # Public

    def __init__(self, fnam="out.pov", *items):
        """Open POV-Ray scene file.

        Open file and write some components.

        @param fnam: POV-Ray scene file name.
        @type fnam: string

        """
        assert type(fnam) == str
        self.file = open(fnam, "w")
        self.__indent = 0
        self.__lock = None
        self.write(*items)

    def include(self, *names):
        for name in names:
            self.writeln('#include "%s"' % name)
            self.writeln()

    def declare(self, name, item):
        self.writeln("#declare %s = " % name)
        self.indent()
        self.write(item)
        self.dedent()

    def write(self, *items):
        """Write commands into scene file."""
        for item in items:
            if type(item) == list:
                for _item in item:
                    self.write(_item)
            elif type(item) == str:
                self.include(item)
            else:
                item.write(self)

    def close(self):
        """Close POV-Ray scene file."""
        self.file.close()




######################################################

class Item:
    def __init__(self, name, args=[], opts=[], **kwargs):
        """
        Base class for POV objects.

        @param name: POV object name
        @param args: compulsory (comma separated?) pov args XX commas don't seem to matter?
        @param opts: eg. CSG items
        @param kwargs: key value pairs
        """
        #print "Item",name,args,opts,kwargs
        self.name = name

        args = list(args)
        for i in range(len(args)):
            args[i] = map_arg(args[i])
        self.args = flatten(args)

        opts = list(opts)
        for i in range(len(opts)):
            opts[i] = map_arg(opts[i])
        self.opts = flatten(opts)

        self.kwargs = dict(kwargs)  # take a copy
        for key, val in self.kwargs.items():
            if type(val) == tuple or type(val) == list:
                self.kwargs[key] = map_arg(val)

        #print "Item.__init__",self.name,self.args,self.opts

    def append(self, *opts, **kwargs):
        for item in flatten(opts):
            self.opts.append(item)
        for key, val in kwargs.items():
            self.kwargs[key] = val

    def begin_write(self, file):
        file.writeln(self.name)
        file.block_begin()
        if self.args:
            file.writeln(", ".join([str(arg) for arg in self.args]))
        file.lock(self)     # assert

    def opt_write(self, file, opt):
        file.unlock(self)   # assert
        if hasattr(opt, "write"):
            # opt is an Item
            opt.write(file)
        else:
            # whatever else
            file.writeln(str(opt))
        file.lock(self)     # assert

    def end_write(self, file):
        file.unlock(self)   # assert
        for key, val in self.kwargs.items():
            file.writeln("%s %s" % (key, val))
        file.block_end()

    def write(self, file):
        #print "Item.write",self.name,self.args,self.opts
        self.begin_write(file)
        for opt in self.opts:
            #print opt
            self.opt_write(file, opt)
        self.end_write(file)

    def __setattr__(self, name, val):
        self.__dict__[name] = val
        if name not in ["kwargs", "args", "opts", "name", "file"]:  # "reserved" words
            self.__dict__["kwargs"][name] = map_arg(val)
            #print "Item",self.name,self.kwargs

    def __setitem__(self, i, item):
        if i < len(self.args):
            self.args[i] = map_arg(item)
        else:
            i += len(args)
            if i < len(self.opts):
                self.opts[i] = map_arg(item)

    def __getitem__(self, i):
        if i < len(self.args):
            return self.args[i]
        else:
            i += len(args)
            if i < len(self.opts):
                return self.opts[i]

    #def append(self, item):
        #self.opts.append( map_arg(item) )

def py2pov(name):
    # eg. Color -> color
    return name.lower()   # XX underscores ?


class KWItem(object):
    """Keyword item handler

      @param val: data value
      @type val: many formats allowed
      @param name: parameter name
      @type name: string
    """
    def __init__(self, val, name=None):
        if name is None:
            name = py2pov(self.__class__.__name__)
        self.name = name
        self.val = map_arg(val)

    def __str__(self):
        return "%s %s" % (self.name, self.val)


#
# Problem with forcing ordering of these keywords.  POVray ordering
# does seem to matter.
#
for name in "Color Translate Scale Rotate Angle".split():
    globals()[name] = type(name, (KWItem,), {})    # nifty :)
    #print globals().keys()


class Texture(Item):
    """Create a texture"""
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "texture", (), opts, **kwargs)


class Pigment(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "pigment", (), opts, **kwargs)


class ColorEntry:
    """Single line entry for a color map"""
    def __init__(self, x, color):
        self.x = x
        self.color = color

    def __str__(self):
        return "[ %s %s ]" % (self.x, self.color)


class ColorMap(Item):
    """Assemble a color map from a collection of color entries."""
    def __init__(self, *opts):
        opts = list(opts)
        for i in range(len(opts)):
            x, color = opts[i]
            opts[i] = ColorEntry(x, color)
        Item.__init__(self, "color_map", (), opts)


class ImageMap(Item):
    """Map an image to an object"""
    def __init__(self, filename, *opts, **kwargs):
        hf_type = filename.split(".")[-1]
        if hf_type == "jpg":
            hf_type = "jpeg"
        if hf_type == "tif":
            hf_type = "tiff"
        opts = list(opts)
        opts.insert(0, "\"%s\"" % filename)
        opts.insert(0, hf_type)
        Item.__init__(self, "image_map", (), opts, **kwargs)


class Finish(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "finish", (), opts, **kwargs)


class Normal(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "normal", (), opts, **kwargs)


class Camera(Item):
    """Create a camera object"""
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "camera", (), opts, **kwargs)


class LightSource(Item):
    """Place light source object at specified position

    @param v: position
    @type v: tuple
    """
    #def __init__(self,v,c,*opts,**kwargs):
        #Item.__init__(self,"light_source",(Vector(v),Vector(c)),
            #opts,**kwargs)
    def __init__(self, v, *opts, **kwargs):
        Item.__init__(self, "light_source", (Vector(v),), opts, **kwargs)


class Background(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "background", (), opts, **kwargs)


class Box(Item):
    def __init__(self, v1, v2, *opts, **kwargs):
        """Construct a box object

        @param v1: vertex of box
        @type v1: Vector()
        @param v2: opposing vertex of box
        @type v2: Vector()
        """
        Item.__init__(self, "box", (v1, v2), opts, **kwargs)


class Cylinder(Item):
    """Construct cylinder object

    @param v1: coordinates of base point
    @type v1: L{Vector}
    @param v2: coordinates of cap point
    @type v2: L{Vector}
    @param r: radius of sphere
    @type r: float
    """
    def __init__(self, v1, v2, r, *opts, **kwargs):
        " opts: open "
        Item.__init__(self, "cylinder", (v1, v2, r), opts, **kwargs)


class Plane(Item):
    def __init__(self, v, r, *opts, **kwargs):
        Item.__init__(self, "plane", (v, r), opts, **kwargs)


class Torus(Item):
    def __init__(self, r1, r2, *opts, **kwargs):
        Item.__init__(self, "torus", (r1, r2), opts, **kwargs)


class Cone(Item):
    """Construct cylinder object

    @param v1: coordinates of base point
    @type v1: L{Vector}
    @param r1: radius of base
    @type r1: float
    @param v2: coordinates of cap point
    @type v2: L{Vector}
    @param r2: radius of cap point
    @type r2: float
    """
    def __init__(self, v1, r1, v2, r2, *opts, **kwargs):
        " opts: open "
        Item.__init__(self, "cone", (v1, r1, v2, r2), opts, **kwargs)


class Sphere(Item):
    """Sphere object

    @param v: position of center of sphere
    @type v: L{Vector}
    @param r: radius of sphere
    @type r: float
    """
    def __init__(self, v, r, *opts, **kwargs):
        Item.__init__(self, "sphere", (v, r), opts, **kwargs)


#class Plane(Item):
#    def __init__(self, v, r, *opts, **kwargs):
#        Item.__init__(self, "plane", (v, r), opts, **kwargs)


class LooksLike(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "looks_like", (), opts, **kwargs)


class Fog(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "fog", (), opts, **kwargs)


class Disc(Item):
    def __init__(self, v1, v2, r1, *opts, **kwargs):
        Item.__init__(self, "disc", (v1, v2, r1), opts, **kwargs)


##############################################
# Constructive Solid Geometry (CSG) components

class Union(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "union", (), opts, **kwargs)


class Intersection(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "intersection", (), opts, **kwargs)


class Difference(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "difference", (), opts, **kwargs)


class Merge(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "merge", (), opts, **kwargs)


class Polygon(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "polygon", (), opts, **kwargs)


class Text(Item):
    def __init__(self, font, string, thickness, offset, *opts, **kwargs):
        Item.__init__(
            self, "text",
            ('ttf "' + font + '" "' + string + '"', thickness, offset),
            opts, **kwargs)


class ThickCylinder(Difference):
    def __init__(self, v1, v2, r1, r2, *opts, **kwargs):
        v1 = Vector(v1)
        v2 = Vector(v2)
        # we make the second cyl a bit longer
        v = 0.001 * (v2 - v1).normalize()
        #print (v1,v2,r2), (v1-v,v2+v,r1), opts,kwargs
        Difference.__init__(
            self, Cylinder(v1, v2, r2),
            Cylinder(v1 - v, v2 + v, r1), *opts, **kwargs
        )


ThickCyl = ThickCylinder

##############################################


class Triangle(Item):
    def __init__(self, v1, v2, v3, *opts, **kwargs):
        Item.__init__(self, "triangle", (v1, v2, v3), opts, **kwargs)


class Mesh(Item):
    def __init__(self, file=None, *opts, **kwargs):
        Item.__init__(self, "mesh", (), opts, **kwargs)
        self.file = file      # "reserved" word
        if file is not None:
            self.begin_write(file)

    def append(self, item):
        if self.file is not None:
            self.opt_write(self.file, item)
        else:
            Item.append(self, item)

    def write(self, file):
        #print "Item.write",self.name,self.args,self.opts
        if self.file is None:
            self.begin_write(file)
            for opt in self.opts:
                #print opt
                self.opt_write(file, opt)
        self.end_write(file)

##############################################


class HeightField(Item):
    def __init__(self, filename, *opts, **kwargs):
        hf_type = filename.split(".")[-1]
        if hf_type == "jpg":
            hf_type = "jpeg"
        opts = list(opts)
        opts.insert(0, "\"%s\"" % filename)
        opts.insert(0, hf_type)
        Item.__init__(self, "height_field", (), opts, **kwargs)


from FieldIm import *

#
######################################################

X = x = Vector(1, 0, 0)
Y = y = Vector(0, 1, 0)
Z = z = Vector(0, 0, 1)
white = Texture(Pigment(color=(1, 1, 1)))


def tutorial31():
    " from the povray tutorial sec. 3.1"
    file = File("demo.pov", "colors.inc", "stones.inc")
    cam = Camera(location=(0, 2, -3), look_at=(0, 1, 2))
    sphere = Sphere((0, 1, 2), 2, Texture(Pigment(color=(1, 1, 1))))
    light = LightSource((2, 4, -3), (1, 1, 1))
    file.write(cam, sphere, light)


def test00():
    file = File("test.pov", "colors.inc", "stones.inc")
    cam = Camera(location=(0, 0, -3), look_at=(0, 0, 0), angle=45)
    boxs = []
    z = 100
    for i in range(50):
        for j in range(50):
            boxs.append(
                Box(
                    (i - 3, j - 3, z),
                    (i + 0.7-3, j + 0.7 - 3, z + 1),
                    Texture(Pigment(color=(i % 2, j % 2, 1)))
                )
            )
    light = LightSource((2, 4, -3), (1, 1, 1))
    file.write(cam, boxs, light)


if __name__ == "__main__":
    #  test00()
    tutorial31()

