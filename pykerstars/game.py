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


class Hand(object):
    def __init__(self):
        self.players = []
        self.board = [] * 5
        self.cards = []


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
        pass

    def preflop(self):
        pass

    def flop(self):
        pass

    def turn(self):
        pass

    def river(self):
        pass
