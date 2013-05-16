# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013
based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from __future__ import nested_scopes
from logging import *
from Vector import *
import os


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

            @TODO: move indentation check to own function
            @TODO: make sure all params are passed through map_arg / flatten before syntax checks
        """
        debug("creating SceneItem %s, %s, %s, %s", name, args, opts, kwargs)

        self.name = name

        if not "indentation" in globals():
            global indentation
            indentation = 0
            debug("set initial indentation to 0")

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

    def _indent(self):
        """
            Indent PoV code
        """
        global indentation
        indentation += 1
        debug("indent: %s", indentation)

    def _dedent(self):
        """
            Dedent PoV code
        """
        global indentation
        indentation -= 1
        debug("dedent: %s", indentation)
        if not indentation >= 0:
            raise IllegalStateException('Indentation below zero')

    def _getIndent(self):
        """
            Get indentation
        """
        global indentation
        return indentation

    def _block_begin(self):
        """
            Begin code block
        """
        debug("begin block")
        code = " {" + os.linesep

        self._indent()

        return code

    def _block_end(self):
        """
            End code block
        """
        debug("end block: indentation= %s", indentation)

        if indentation == 0:
            # blank line if this is a top level end
            code = self._getLine()
        else:
            self._dedent()
            code = self._getLine("}")

        return code

    def _getLine(self, s=""):
        """
            get line of code
        """
        global indentation
        info("'" + "  " * indentation + s + "'")
        return "  " * indentation + s + os.linesep

    def append(self, *opts, **kwargs):
        """
            append Subitem(s) to Item
        """
        for item in self.flatten(opts):
            self.opts.append(item)
        for key, val in kwargs.items():
            self.kwargs[key] = val

    def __str__(self):
        """
            return PoV code as string representation
        """
        debug("SceneItem.__str__ %s, %s, %s", self.name, self.args, self.opts)

        return self.name

    def __setitem__(self, i, item):
        """
            Set Item magic method
        """
        if i < len(self.args):
            self.args[i] = self.map_arg(item)
        else:
            i -= len(self.args)
            if i < len(self.opts):
                self.opts[i] = self.map_arg(item)
            else:
                raise IndexError()

    def __getitem__(self, i):
        """
            Get Item magic method
        """
        if i < len(self.args):
            return self.args[i]
        else:
            i -= len(self.args)
            if i < len(self.opts):
                return self.opts[i]
            else:
                raise IndexError()

    def __eq__(self, other):
        if not isinstance(other, SceneItem):
            raise ArgumentError()
        a = self.name == other.name
        debug(str(self.name) + ' = ' + str(self.name))
        b = self.args == other.args
        debug(str(self.args) + ' = ' + str(self.args))
        c = self.opts == other.opts
        debug(str(self.opts) + ' = ' + str(self.opts))
        d = self.kwargs == other.kwargs
        debug(str(self.kwargs) + ' = ' + str(self.kwargs))
        return a & b & c & d

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




