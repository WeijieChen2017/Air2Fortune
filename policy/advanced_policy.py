#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
from basic.basic import *
from basic.advanced import *
from bank.bank import bank_get_value


class A2FP_Random(A2F_Policy):

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
        choice = self._choice
        n_coin = bank_get_value("n_coin")
        random_choice = np.random.choice(np.nonzero(choice)[0])
        self._target = np.eye(n_coin)[random_choice]


class A2FP_Random_Prob(A2F_Policy):
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
        self.para = para

    def predict(self):
        n_coin = bank_get_value("n_coin")
        choice = self._choice
        possible_target = np.where(choice==1)[0]
        random_choice = np.random.choice(possible_target, p=self.para)
        self._target = np.eye(n_coin)[random_choice]


class A2FP_Cheat(A2F_Policy):
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
        self.para = para

    def predict(self):
        n_coin = bank_get_value("n_coin")
        choice = self._choice
        action_list = self.para
        chessboard = self._chessboard.get_value()

        other_action = np.sum(action_list, axis=0)
        possible_choice = np.subtract(choice, other_action)
        possible_choice[possible_choice<0] = 0
        benefits = np.multiply(possible_choice, chessboard)
        self._target = np.eye(n_coin)[np.argmax(benefits)]


class A2FP_MAB(A2F_Policy):
    # Multi-arm Bandit
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
        self.para = para

    def predict(self):
        n_coin = bank_get_value("n_coin")
        choice = self._choice
        history = self._game
        # print(history._total_round)
        if history._total_round > 0:
            curr_round = history.get_round(0)
            curr_action = curr_round
            print("MAB explore")
            print("Total round:", history._total_round)
            print(curr_action._action.get_value())
            print("MAB ends")
        # self._target = [0, 0, 0, 0, 0]
        # action_list = self.para
        # chessboard = self._chessboard.get_value()
        #
        # other_action = np.sum(action_list, axis=0)
        # possible_choice = np.subtract(choice, other_action)
        # possible_choice[possible_choice<0] = 0
        # benefits = np.multiply(possible_choice, chessboard)
        # self._target = np.eye(n_coin)[np.argmax(benefits)]

        choice = self._choice
        chessboard = self._chessboard.get_value()
        benefit = np.multiply(choice, chessboard)
        n_coin = bank_get_value("n_coin")
        self._target = np.eye(n_coin)[np.argmax(benefit)]
