# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.
Borg Pattern by Alex Martelli
"""


class Borg(object):
    u"""Alex Martelli's 'Borg'.

    Singleton like shared storage class
    @see http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
    @see http://www.aleax.it/Python/5ep.html
    """

    _shared_state = {}

    def __init__(self):
        """Link each Instances storage to the same object"""
        self.__dict__ = self._shared_state
