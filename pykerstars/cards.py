# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2017/2/3
Description:
    cards.py
----------------------------------------------------------------------------"""

from pykerstars.utils.poker_enum import PokerEnum

__all__ = ['Suit', 'Rank', 'Card']


class Suit(PokerEnum):
    __order__ = 'CLUBS DIAMONDS HEARTS SPADES'

    CLUBS = '♣', 'c', 'clubs'
    DIAMONDS = '♦', 'd', 'diamonds'
    HEARTS = '♥', 'h', 'hearts'
    SPADES = '♠', 's', 'spades'


class Rank(PokerEnum):
    __order__ = 'DEUCE THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JACK QUEEN KING ACE'

    DEUCE = '2', 2
    THREE = '3', 3
    FOUR = '4', 4
    FIVE = '5', 5
    SIX = '6', 6
    SEVEN = '7', 7
    EIGHT = '8', 8
    NINE = '9', 9
    TEN = 'T', 10
    JACK = 'J', 11
    QUEEN = 'Q', 12
    KING = 'K', 13
    ACE = 'A', 1


def _values(s, r):
    values = []
    for rv in r.values:
        for sv in s.values:
            values.append("'%s%s'" % (str(rv), str(sv)))
    return values


class Card(PokerEnum):
    __order__ = " ".join(['{0}_{1}'.format(r.enum_name, s.enum_name) for s in list(Suit) for r in list(Rank)])

    for s in list(Suit):
        for r in list(Rank):
            exec('{0}_{1} = {2}'.format(r.enum_name, s.enum_name,
                                        ",".join(_values(s, r))))

    @property
    def suit(self):
        return getattr(Suit, self.enum_name.split('_')[1])

    @property
    def rank(self):
        return getattr(Rank, self.enum_name.split('_')[0])
