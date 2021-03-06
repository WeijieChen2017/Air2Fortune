#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
from basic.basic import *
from bank.bank import bank_get_value


class A2FP_Prudent(A2F_Policy):

    # always choose maximum value

    def __init__(self,
                 game: A2F_Game,
                 chessboard: A2F_Chessboard,
                 player: A2F_Player,
                 para: list):
        A2F_Policy.__init__(self,
                            game=game,
                            chessboard=chessboard,
                            player=player,
                            para=para)

    def predict(self):
        choice = self._choice
        chessboard = self._chessboard.get_value()
        benefit = np.multiply(choice, chessboard)
        n_coin = bank_get_value("n_coin")
        self._target = np.eye(n_coin)[np.argmin(benefit)]


class A2FP_Greedy(A2F_Policy):

    # always choose maximum value

    def __init__(self,
                 game: A2F_Game,
                 chessboard: A2F_Chessboard,
                 player: A2F_Player,
                 para: list):
        A2F_Policy.__init__(self,
                            game=game,
                            chessboard=chessboard,
                            player=player,
                            para=para)

    def predict(self):
        choice = self._choice
        chessboard = self._chessboard.get_value()
        benefit = np.multiply(choice, chessboard)
        n_coin = bank_get_value("n_coin")
        self._target = np.eye(n_coin)[np.argmax(benefit)]


class A2FP_Null(A2F_Policy):

    # random choice from possible location

    def __init__(self,
                 game: A2F_Game,
                 chessboard: A2F_Chessboard,
                 player: A2F_Player,
                 para: list):
        A2F_Policy.__init__(self,
                            game=game,
                            chessboard=chessboard,
                            player=player,
                            para=para)

    def predict(self):
        n_coin = bank_get_value("n_coin")
        self._target = np.zeros(n_coin)
