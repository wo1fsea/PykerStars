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

from utils import PokerEnum

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


class Card(PokerEnum):
    __order__ = " ".join(['{0}_{1}'.format(r.enum_name, s.enum_name) for s in list(Suit) for r in list(Rank)])

    for s in list(Suit):
        for r in list(Rank):
            exec('{0}_{1} = "{2}{3}"'.format(r.enum_name, s.enum_name, str(r), str(s)))


print list(Suit)
print list(Rank)
print list(Card)

for c in list(Card):
    print c.enum_name
