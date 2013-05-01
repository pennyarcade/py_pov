"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import os
from logging import *


class SceneFile(list):
    """
    POV-Ray scene file object.

        @var private __lock
        @var private __indent
        @var public  file
    """

    def __lock(self, item):
        """
            Lock Item for processing
            TODO: Deprecated when using __str__() to generate code
        """
        debug("lock %s", id(item))
        assert self.__lock is None
        self.__lock = item

    def __unlock(self, item):
        """
            Unlock Item after processing
            TODO: Deprecated when using __str__() to generate code
        """
        debug("unlock %s", id(item))
        assert self.__lock is item
        self.__lock = None

'''
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
        self.writeln("{")
        self.indent()
        debug("begin block")

    def __block_end(self):
        """
            End code block
        """
        self.dedent()
        self.writeln("}")
        if self.__indent == 0:
            # blank line if this is a top level end
            self.writeln()
        debug("end block")

    def __writeln(self, s=""):
        """
            write line of code to file
        """
        info("  " * self.__indent + s)
        assert self.__lock is None
        self.file.write("  " * self.__indent + s + os.linesep)
'''


    #######################################################
    # Public

    def __init__(self, fnam="out.pov", *items):
        """Open POV-Ray scene file.

        Open file and write some components.

        @param fnam: POV-Ray scene file name.
        @type fnam: string
        @param items

        """
        assert type(fnam) == str
        self.file = open(fnam, "w")
        self.__indent = 0
        self.__lock = None
        self.write(*items)

    def include(self, *names):
        """
            Handle #include language directive
            TODO: move to own subclass
            TODO: syntax tests?
        """
        for name in names:
            self.writeln('#include "%s"' % name)
            self.writeln()

    def declare(self, name, item):
        """
            Handle #declare languge directive
            TODO: move to own subclass
            TODO: syntax tests?
        """
        self.writeln("#declare %s = " % name)
        self.indent()
        self.write(item)
        self.dedent()

    def write(self, *items):
        """
            Write commands into scene file.
            TODO: There should be no more type/syntax checking here
        """
        for item in items:
            if type(item) == list:
                for _item in item:
                    self.write(_item)
            elif type(item) == str:
                self.include(item)
            else:
                item.write(self)

    def close(self):
        """
            Close POV-Ray scene file.
        """
        self.file.close()
