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
        n_player = bank_get_value("n_player")
        chessboard = self._chessboard.get_value()
        choice = self._choice
        history = self._game
        history_action = []
        if history._total_round > 0:
            for idx_round in range(history._total_round):
                history_action.append(history.get_round(idx_round)._action.get_value())
            history_action = np.asarray(history_action)
            history_action = np.sum(history_action, axis=0)
            idx_player = np.nonzero(self._player.get_value())[0][0]

            history_action[idx_player].fill(0)

            # two choice, expectation of value or counts
            # counts
            # print(history_action)
            # history_action = np.sum(history_action, axis=0)
            #
            # estimation = np.multiply(history_action, choice)
            # estimation[estimation == 0] = bank_get_value("max_game")
            # print(np.argmin(estimation))
            # self._target = np.eye(n_coin)[np.argmin(estimation)]

            # value
            # history_action = np.sum(history_action, axis=0)
            # estimation = np.multiply(history_action, choice)
            # estimation[estimation == 0] = bank_get_value("max_game")
            # estimation = np.subtract(history._total_round, estimation)
            # benefit = np.multiply(estimation, chessboard)
            # # print(np.argmin(estimation))
            # self._target = np.eye(n_coin)[np.argmax(benefit)]

            # improved value
            for idx in range(n_player):
                if idx != idx_player:
                    curr_count = history_action[idx]
                    history_action[idx] = np.eye(n_coin)[np.argmax(curr_count)]

            # print("choice:", choice)
            # print("history action:", history_action)
            history_action = np.sum(history_action, axis=0)
            estimation = np.multiply(history_action, choice)
            # print("estimatione", estimation)
            estimation[estimation == 0] = 3
            estimation = np.subtract(3, estimation)
            # print("estimatione", estimation)
            # print("chessboard:", chessboard)
            benefit = np.multiply(estimation, chessboard)

            # print(choice)
            # print(history_action)
            # print(estimation)
            # print("decision:", np.argmax(benefit))
            # print("------------")

            # print(np.argmin(estimation))
            self._target = np.eye(n_coin)[np.argmax(benefit)]


        else:
            benefit = np.multiply(choice, chessboard)
            self._target = np.eye(n_coin)[np.argmax(benefit)]

            # print("MAB explore")
            # print("Total round:", history._total_round)
            # print(history_action)
            # print(idx_player)
            # print(choice)
            # print(estimation)
            # print("MAB ends")
            # print("-------------")
        # self._target = [0, 0, 0, 0, 0]
        # action_list = self.para
        # chessboard = self._chessboard.get_value()
        #
        # other_action = np.sum(action_list, axis=0)
        # possible_choice = np.subtract(choice, other_action)
        # possible_choice[possible_choice<0] = 0
        # benefits = np.multiply(possible_choice, chessboard)
        # self._target = np.eye(n_coin)[np.argmax(benefits)]

        # choice = self._choice
        # chessboard = self._chessboard.get_value()
        # benefit = np.multiply(choice, chessboard)
        # n_coin = bank_get_value("n_coin")
        # self._target = np.eye(n_coin)[np.argmax(benefit)]
