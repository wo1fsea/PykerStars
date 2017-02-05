# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2017/2/4
Description:
    handranks.py
----------------------------------------------------------------------------"""

import itertools

from pykerstars.utils.pokerenum import PokerEnum
from cards import Card, Rank, Suit


class HandRank(PokerEnum):
    __order__ = 'HIGH_CARD ONE_PAIR TWO_PAIR THREE_OF_A_KIND STRAIGHT FLUSH FULL_HOUSE FOUR_OF_A_KIND STRAIGHT_FLUSH'

    STRAIGHT_FLUSH = 'Straight Flush', '同花顺'
    FOUR_OF_A_KIND = 'Four of a Kind', '四条'
    FULL_HOUSE = 'Full House', '葫芦'
    FLUSH = 'Flush', '同花'
    STRAIGHT = 'Straight', '顺子'
    THREE_OF_A_KIND = 'Three of a kind', '三条'
    TWO_PAIR = 'Two pair', '两对'
    ONE_PAIR = 'One pair', '一对'
    HIGH_CARD = 'High card', '高牌'


def is_flush(cards):
    return len(filter(lambda x: x.suit != cards[0].suit, cards)) == 0


def is_straight(ordered_cards):
    if (Rank('2'), Rank('3'), Rank('4'), Rank('5'), Rank('A')) == tuple(map(lambda x: x.rank, ordered_cards)):
        return True

    index = ordered_cards[0].rank.index

    for card in ordered_cards[1:]:
        index += 1
        if card.rank.index != index:
            return False
    return True


def is_straight_flush(ordered_cards):
    return is_straight(ordered_cards) and is_flush(ordered_cards)


def count_rank(cards):
    rank_count = {}
    for card in cards:
        if card.rank not in rank_count:
            rank_count[card.rank] = 0
        rank_count[card.rank] += 1

    return rank_count


def is_four_of_a_kind(rank_count):
    return len(filter(lambda x: x == 4, rank_count.values())) == 1


def is_full_house(rank_count):
    return len(filter(lambda x: x == 3, rank_count.values())) == 1 and \
           len(filter(lambda x: x == 2, rank_count.values())) == 1


def is_three_of_a_kind(rank_count):
    return len(filter(lambda x: x == 3, rank_count.values())) == 1


def is_two_pair(rank_count):
    return len(filter(lambda x: x == 2, rank_count.values())) == 2


def is_one_pair(rank_count):
    return len(filter(lambda x: x == 2, rank_count.values())) == 1


def tell_hand_rank(cards):
    assert len(cards) == 5, 'wrong length of cards.'

    cards = sorted(cards, key=lambda x: x.suit.index + 4 * x.rank.index)
    rank_count = count_rank(cards)

    if is_straight_flush(cards):
        return HandRank.STRAIGHT_FLUSH
    elif is_four_of_a_kind(rank_count):
        return HandRank.FOUR_OF_A_KIND
    elif is_full_house(rank_count):
        return HandRank.FULL_HOUSE
    elif is_flush(cards):
        return HandRank.FLUSH
    elif is_straight(cards):
        return HandRank.STRAIGHT
    elif is_three_of_a_kind(rank_count):
        return HandRank.THREE_OF_A_KIND
    elif is_two_pair(rank_count):
        return HandRank.TWO_PAIR
    elif is_one_pair(rank_count):
        return HandRank.ONE_PAIR
    else:
        return HandRank.HIGH_CARD


def tell_hand_score(cards):
    assert len(cards) == 5, 'wrong length of cards.'

    len_rank = len(Rank)

    cards = sorted(cards, key=lambda x: x.rank.index)
    rank_count = count_rank(cards)

    hand_rank = HandRank.HIGH_CARD
    reordered_cards = sorted(cards, key=lambda x: rank_count[x.rank] * len_rank + x.rank.index, reverse=True)

    if is_straight_flush(cards):
        hand_rank = HandRank.STRAIGHT_FLUSH
    elif is_four_of_a_kind(rank_count):
        hand_rank = HandRank.FOUR_OF_A_KIND
    elif is_full_house(rank_count):
        hand_rank = HandRank.FULL_HOUSE
    elif is_flush(cards):
        hand_rank = HandRank.FLUSH
    elif is_straight(cards):
        hand_rank = HandRank.STRAIGHT
    elif is_three_of_a_kind(rank_count):
        hand_rank = HandRank.THREE_OF_A_KIND
    elif is_two_pair(rank_count):
        hand_rank = HandRank.TWO_PAIR
    elif is_one_pair(rank_count):
        hand_rank = HandRank.ONE_PAIR

    return "%02d" % hand_rank.index + "%02d" * (len(reordered_cards)) % tuple(
        map(lambda x: x.rank.index, reordered_cards))


def tell_best_hand_rank(cards):
    assert len(cards) >= 5, 'length of cards must >= 5.'

    combinations = itertools.combinations(cards, 5)
    ranks = map(lambda x: (x, tell_hand_rank(x)), combinations)

    return sorted(ranks, key=lambda x: x[1], reverse=True)[0]


def tell_best_hand_score(cards):
    assert len(cards) >= 5, 'length of cards must >= 5.'

    combinations = itertools.combinations(cards, 5)
    scores = map(lambda x: (x, tell_hand_score(x)), combinations)

    return sorted(scores, key=lambda x: x[1], reverse=True)[0]


cards0 = [Card('7d'), Card('3d'), Card('4c'), Card('4d'), Card('5d'), Card('Ad')]
cards1 = [Card('7d'), Card('3d'), Card('4d'), Card('4s'), Card('2d'), Card('Ah')]

print(tell_best_hand_score(cards0))
print(tell_best_hand_score(cards1))
