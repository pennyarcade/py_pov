"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013
based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from __future__ import nested_scopes
from logging import *
import os
import Vector

class SceneItem(object):
    """
        Base class for POV objects.

        SCENE_ITEM:
            LANGUAGE_DIRECTIVES        |
            camera { CAMERA_ITEMS... } |
            OBJECTS                    |
            ATMOSPHERIC_EFFECTS        |
            global_settings { GLOBAL_ITEMS }
    """
    def __init__(self, name, args=[], opts=[], **kwargs):
        """
            Base class for POV objects.

            @param name: POV object name
            @param args: compulsory (comma separated?) pov args XX commas don't seem to matter?
            @param opts: eg. CSG items
            @param kwargs: key value pairs
        """
        debug("Item %s, %s, %s, %s", name, args, opts, kwargs)

        self.name = name

        if not "indentation" in globals():
            global indentation
            indentation = 0

        args = list(args)
        for i in range(len(args)):
            args[i] = self.map_arg(args[i])
        self.args = self.flatten(args)

        opts = list(opts)
        for i in range(len(opts)):
            opts[i] = self.map_arg(opts[i])
        self.opts = self.flatten(opts)

        self.kwargs = dict(kwargs)  # take a copy
        for key, val in self.kwargs.items():
            if type(val) == tuple or type(val) == list:
                self.kwargs[key] = self.map_arg(val)

        debug("Item.__init__ %s, %s, %s", self.name, self.args, self.opts)

    def __indent(self):
        """
            Indent PoV code
        """
        global indentation
        indentation += 1
        debug("indent: %s", indentation)

    def __dedent(self):
        """
            Dedent PoV code
        """
        global indentation
        indentation -= 1
        debug("dedent: %s", indentation)
        assert indentation >= 0

    def __block_begin(self):
        """
            Begin code block
        """
        self.__indent()
        debug("begin block")

        return self.__getLine("{")

    def __block_end(self):
        """
            End code block
        """
        debug("end block")

        if indentation == 0:
            # blank line if this is a top level end
            code = self.__getLine()
        else:
            code = self.__getLine("}")

        self.__dedent()
        return code


    def __getLine(self, s=""):
        """
            get line of code
        """
        global indentation
        info("  " * indentation + s)
        return "  " * indentation + s + os.linesep

    def __getBeginCode(self):
        """
            Start block of code
        """
        code = self.__getLine(self.name) + self.__block_begin()
        if self.args:
            code = code + self.__getLine(", ".join([str(arg) for arg in self.args]))
        return code

    def __getEndCode(self):
        """
            End block of code
        """
        code = ""
        for key, val in self.kwargs.items():
            code += self.__getLine("%s %s" % (key, val))
        code += self.__block_end()
        return code

    def append(self, *opts, **kwargs):
        """
            append Subitem(s) to Item
        """
        for item in self.flatten(opts):
            self.opts.append(item)
        for key, val in kwargs.items():
            self.kwargs[key] = val

    #def append(self, item):
        #self.opts.append( map_arg(item) )

    def __str__(self):
        """
            return PoV code as string representation
        """
        debug("Item.__str__ %s, %s, %s", self.name, self.args, self.opts)

        code = ""
        code += self.__getBeginCode()
        for opt in self.opts:
            code += str(opt)
        code += self.__getEndCode()
        return code

#    def __setattr__(self, name, val):
#       """
#            Set Attribute magic method
#        """
#        self.__dict__[name] = val
#        if name not in ["kwargs", "args", "opts", "name", "file"]:  # "reserved" words
#            self.__dict__["kwargs"][name] = map_arg(val)
#            debug("Item %s %s", self.name, self.kwargs)

    def __setitem__(self, i, item):
        """
            Set Item magic method
        """
        if i < len(self.args):
            self.args[i] = map_arg(item)
        else:
            i += len(args)
            if i < len(self.opts):
                self.opts[i] = map_arg(item)

    def __getitem__(self, i):
        """
            Get Item magic method
        """
        if i < len(self.args):
            return self.args[i]
        else:
            i += len(args)
            if i < len(self.opts):
                return self.opts[i]

    def map_arg(self, arg):
        """Map an argument list to an appropriate format"""
        if type(arg) in (tuple, list):
            # if multiple-component, floating-point value, return a vector
            if len(arg) and hasattr(arg[0], "__float__"):
                return Vector(arg)
        # else return the same format as the input value
        return arg

    def flatten(self, seq):
        seq = list(seq)
        i = 0
        while i < len(seq):
            if type(seq[i]) in (list, tuple):
                x = seq.pop(i)
                for item in x:
                    seq.insert(i, item)
                    i += 1
            else:
                i += 1
        return seq




