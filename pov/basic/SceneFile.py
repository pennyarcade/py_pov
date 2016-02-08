# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import info
from pov.basic.SceneItem import SceneItem
from pov.other.SdlSyntaxException import SdlSyntaxException


class SceneFile(object):
    """
    POV-Ray scene file object.

    @Todo: Proper Apidoc
    @Todo: Add param for PovRay Ini file

    @var private __lock
    @var private __indent
    @var public  file
    """

    #######################################################
    # Public

    def __init__(self, fnam="out.pov", *items):
        """
        Open POV-Ray scene file.

        Open file and write some components.

        @param fnam: POV-Ray scene file name.
        @type fnam: string
        @param items

        @Todo: check if file is writeable?
        """
        if type(fnam) != str:
            raise TypeError(
                'Filename String expected but got %s'
                % fnam.__class__.__name__
            )

        # initialize item list
        self.items = list()

        items = list(items)
        for i in items:
            self.append(i)

        # self.file = open(fnam, "w")

    def __str__(self):
        """Return PoV source code for complete scene file."""
        code = ''

        for i in self.items:
            code += str(i)

        info('SceneFile.str(): ' + code)

        return code

    def append(self, *items):
        """Append Scene Item(s) to Scene Filename."""
        for i in items:
            # each item has to be derived of SceneItem
            if not isinstance(i, SceneItem):
                raise SdlSyntaxException(
                    'Item is expectet to be a SceneItem object but got %s'
                    % (i.__class__.__name__)
                )

            self.items.append(i)

    def write(self):
        """
        Write commands into scene file.

        @TODO: There should be no more type/syntax checking here
        @Todo: Write to file code
        """
        # for item in items:
        #    if type(item) == list:
        #        for _item in item:
        #            self.write(_item)
        #    elif type(item) == str:
        #        self.include(item)
        #    else:
        #        item.write(self)

    def close(self):
        """Close POV-Ray scene file."""
        # self.file.close()
