# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2017/6/14
Description:
    player.py
----------------------------------------------------------------------------"""

from pykerstars.utils.pokerenum import PokerEnum


class Action(PokerEnum):
    __order__ = 'FOLD CHECK CALL RAISE'

    FOLD = 'fold', 'F'
    CHECK = 'check', 'X'
    CALL = 'call', 'C'
    RAISE = 'raise', 'R'


class Player(object):
    ACTIONS = []

    def __init__(self):
        pass

    def action(self):
        pass
