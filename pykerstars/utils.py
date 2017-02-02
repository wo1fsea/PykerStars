# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2017/2/3
Description:
    utils.py
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


class PokerEnum(object):
    __metaclass__ = PokerEnumMeta

    _style = 0

    def __new__(cls, value):

        if type(value) is cls:
            return value

        enum_name = cls._value2enum_map.get(value)

        assert enum_name, "can not convert value %s to enum." % enum_name

        obj = getattr(cls, enum_name)

        if not obj:
            obj = super(PokerEnum, cls).__new__(cls)
            obj._value = cls._enum_names.index(enum_name)
            setattr(cls, enum_name, obj)

        return obj

    def __str__(self):
        return self._enum2value_map[self._enum_names[self._value]][self._style]

    def __repr__(self):
        return "{0}('{1}')".format(self.__class__.__name__, str(self))

    @property
    def enum_name(self):
        return self._enum_names[self._value]
