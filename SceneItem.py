"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import *


class SceneItem(object):
    """
        Base class for POV objects.

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

        debug("Item.__init__ %s, %s, %s", self.name, self.args, self.opts)

    def __indent(self):
        """
            Indent PoV code
         """
        self.__indent += 1
        debug("indent: %s", self.__indent)

    def __dedent(self):
        """
            Dedent PoV code
        """
        self.__indent -= 1
        debug("dedent: %s", self.__indent)
        assert self.__indent >= 0

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
        self.__dedent()
        if self.__indent == 0:
            # blank line if this is a top level end
            self.__getLine()
        debug("end block")

        return self.__getLine("}")

    def __getLine(self, s=""):
        """
            write line of code to file
        """
        info("  " * self.__indent + s)
        assert self.__lock is None
        return "  " * self.__indent + s + os.linesep

    def __getBeginCode(self, file):
        """
            Start writing stuff to file
        """
        code = __getLine(self.name) + __getBeginCode
        if self.args:
            code = code + __getLine(", ".join([str(arg) for arg in self.args]))
        return code

    def __getEndCode(self, file):
        """
            Stop writing stuff to file
        """
        code = ""
        for key, val in self.kwargs.items():
            code += __getLine("%s %s" % (key, val))

    def __getOptGode(self, file, opt):
        """
            Write Options to file
            TODO: convert to using __str__
        """
        file.unlock(self)   # assert
        if hasattr(opt, "write"):
            # opt is an Item
            opt.write(file)
        else:
            # whatever else
            file.writeln(str(opt))
        file.lock(self)     # assert

    def append(self, *opts, **kwargs):
        """
            append Subitem(s) to Item
        """
        for item in flatten(opts):
            self.opts.append(item)
        for key, val in kwargs.items():
            self.kwargs[key] = val

    def write(self, file):
        """
            Write Item to file
            TODO: Move to File class
        """
        debug("Item.write %s, %s, %s", self.name, self.args, self.opts)
        self.begin_write(file)
        for opt in self.opts:
            #print opt
            self.opt_write(file, opt)
        self.end_write(file)

    def __str__(self):
        """
            return PoV code as string representation
        """

    def __setattr__(self, name, val):
        """
            Set Attribute magic method
        """
        self.__dict__[name] = val
        if name not in ["kwargs", "args", "opts", "name", "file"]:  # "reserved" words
            self.__dict__["kwargs"][name] = map_arg(val)
            debug("Item %s %s", self.name, self.kwargs)

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

    #def append(self, item):
        #self.opts.append( map_arg(item) )
