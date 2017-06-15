# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2017/6/15
Description:
    poker_enum_meta.py
----------------------------------------------------------------------------"""


class PokerEnumMeta(type):
    def __new__(mcs, cls, bases, classdict):

        cls = super(PokerEnumMeta, mcs).__new__(mcs, cls, bases, classdict)

        _order = classdict.pop('__order__', None)
        enum_names = _order.split() if _order else []

        enum2value_map = dict([(enum_name,
                                classdict[enum_name] if isinstance(classdict[enum_name], (tuple, list)) else (
                                    classdict[enum_name],)) for enum_name in enum_names])
        value2enum_map = {}

        for name, values in enum2value_map.items():
            for v in values:
                value2enum_map[v] = name

            setattr(cls, name, None)

        cls._enum_names = enum_names
        cls._enum2value_map = enum2value_map
        cls._value2enum_map = value2enum_map

        for name, values in enum2value_map.items():
            setattr(cls, name, cls(values[0]))

        return cls

    def __getitem__(self, name):
        return getattr(self, name)

    def __iter__(self):
        return (getattr(self, name) for name in self._enum_names)

    def __len__(self):
        return len(self._enum_names)
