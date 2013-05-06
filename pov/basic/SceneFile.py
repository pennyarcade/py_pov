# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import *


class SceneFile(list):
    """
    POV-Ray scene file object.

        @var private __lock
        @var private __indent
        @var public  file
    """

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
