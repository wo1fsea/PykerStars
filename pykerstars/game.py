# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2017/2/4
Description:
    game.py
----------------------------------------------------------------------------"""

import random
from .cards import Card


class Hand(object):
    def __init__(self, table):
        self.table = table
        self.players = list(self.table.players)
        self.board = []
        self.cards = []
        self.pots = []

        # self.actions = [[preflop actions], [flop actions], [turn actions], [river actions]]
        self.actions = []

        self.start_stack = {self.table.stack[player] for player in self.players}
        self.end_stack = {}

    def set_end_stack(self):
        self.end_stack = {self.table.stack[player] for player in self.players}

    def dumps(self):
        pass

    def __str__(self):
        return ''


class Table(object):
    small_blind = 1
    big_blind = 2
    max_buy_in = 100 * big_blind

    def __init__(self, dealer, max_player_num=9):
        self.players = [None] * max_player_num
        self.dealer = dealer
        self.stack = {}
        self.history = []

    def sit(self, player, buy_in=max_buy_in, position=None):
        max_player_num = len(self.players)
        for i in range(max_player_num):
            pos = (position + i) % max_player_num
            if not self.players[pos]:
                self.players[pos] = player
                self.stack[player] = buy_in
                return True

        return False

    def stand(self, player):
        max_player_num = len(self.players)
        for i in range(max_player_num):
            if self.players[i] == player:
                self.players[i] = None
                del self.stack[player]

    def get_info(self):
        pass


class Dealer(object):
    def __init__(self, table):
        self.table = table
        self.cards = list(Card)
        self.cur_hand = None

        self._cur_player_num = len(self.table.players)
        self._cur_cards_index = 0

    def shuffle(self):
        random.shuffle(self.cards)

    def start_new_hand(self):
        if self.cur_hand:
            self.table.history.append(self.cur_hand.dumps())

        self.cur_hand = Hand(self.table)
        self._cur_player_num = len(self.table.players)

    def deal(self):
        pass

    def preflop(self):
        cards = []
        for i in range(self._cur_player_num):
            cards.append([])

        for i, cs in enumerate(cards):
            cs.append(self.cards[self._cur_cards_index + i])
            cs.append(self.cards[self._cur_cards_index + i + self._cur_player_num])

        self._cur_cards_index += 2 * self._cur_player_num

        self.cur_hand.cards = cards

        # todo: actions

    def flop(self):
        self.cur_hand.board.extend([self.cards[self._cur_cards_index + i] for i in range(3)])
        self._cur_cards_index += 3

        # todo: actions

    def turn(self):
        self.cur_hand.board.append(self.cards[self._cur_cards_index])
        self._cur_cards_index += 1

        # todo: actions

    def river(self):
        self.cur_hand.board.append(self.cards[self._cur_cards_index])
        self._cur_cards_index += 1

        # todo: actions
