# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2017/2/3
Description:
    poker_enum.py
----------------------------------------------------------------------------"""

from functools import total_ordering

import sys

if sys.version_info < (3, 0):
    from ._poker_enum2 import PokerEnumAdapter
else:
    from ._poker_enum3 import PokerEnumAdapter


@total_ordering
class PokerEnum(PokerEnumAdapter):
    value_style = 0

    def __new__(cls, value):

        if type(value) is cls:
            return value

        enum_name = cls._value2enum_map.get(value)

        assert enum_name, 'can not convert value %s to enum.' % enum_name

        obj = getattr(cls, enum_name)

        if not obj:
            obj = super(PokerEnum, cls).__new__(cls)
            obj._index = cls._enum_names.index(enum_name)
            setattr(cls, enum_name, obj)

        return obj

    def __str__(self):
        return self._enum2value_map[self.enum_name][self.value_style]

    def __repr__(self):
        return '{0}("{1}")'.format(self.__class__.__name__, str(self))

    def __eq__(self, other):
        return self.index == other.index

    def __lt__(self, other):
        return self.index < other.index

    def __hash__(self):
        return self.index

    @property
    def enum_name(self):
        return self._enum_names[self.index]

    @property
    def index(self):
        return self._index

    @property
    def values(self):
        return self._enum2value_map[self.enum_name]
