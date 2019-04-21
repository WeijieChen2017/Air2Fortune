#!/usr/bin/python
# -*- coding: UTF-8 -*-

import copy
import numpy as np
from bank.bank import bank_get_value

# n_player = bank_get_value("n_player")
# n_coin = bank_get_value("n_coin")
# total_game = bank_get_value("total_game")


class A2F_Data(object):

    def __init__(self, value):
        self._value = np.array(value)

    def get_value(self):
        value = copy.deepcopy(self._value)
        return value

    def set_value(self, value):
        self._value = value


class A2F_Chessboard(A2F_Data):

    def __init__(self, value):
        A2F_Data.__init__(self, value)


class A2F_Player(A2F_Data):

    def __init__(self, value):
        A2F_Data.__init__(self, value)


class A2F_Action(A2F_Data):

    def __init__(self, value):
        A2F_Data.__init__(self, value)


class A2F_Coin(A2F_Data):

    def __init__(self, value):
        A2F_Data.__init__(self, value)


class A2F_Round(object):

    def __init__(self,
                 chessboard: A2F_Chessboard,
                 action: A2F_Action):
        self._chessboard = chessboard
        self._action = action

    def run(self):
        temp_action = self._action.get_value()
        temp_chessboard = self._chessboard.get_value()

        result = np.sum(temp_action, axis=0)
        n_coin = bank_get_value("n_coin")
        n_player = bank_get_value("n_player")
        for i in range(n_coin):
            if result[i] > 1:
                temp_action[:, i] = np.zeros(n_player)
        current_coin = np.dot(temp_action, temp_chessboard)
        return A2F_Coin(current_coin)


class A2F_Error(Exception):

    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return repr(self.__value)




class A2F_Game(object):

    def __init__(self):
        self._process = []
        self._total_round = 0

    def add_round(self, a2f_round: A2F_Round):
        self._process.append(a2f_round)
        self._total_round += 1

    def get_round(self, idx_round):
        if idx_round >= self._total_round:
            raise A2F_Error("There is no such round.")
        return self._process[idx_round]

    def winner(self):
        total_game = bank_get_value("total_game")
        n_player = bank_get_value("n_player")
        if self._total_round < total_game-1:
            raise A2F_Error("The game is not over")
        else:
            init_coin = A2F_Coin(np.zeros(n_player))
            for idx_round in range(total_game):
                curr_coin = self._process[idx_round].run()
                init_coin.set_value(init_coin.get_value()+curr_coin.get_value())

            final_coin = init_coin.get_value()
            best_player = init_coin.get_value()
            best_profit = np.max(final_coin)
            best_player[best_player < best_profit] = 0
            best_player[best_player == best_profit] = 1
            return final_coin, best_player


class A2F_Policy(object):

    def __init__(self,
                 game: A2F_Game,
                 chessboard: A2F_Chessboard,
                 player: A2F_Player):
        n_coin = bank_get_value("n_coin")
        self._game = game
        self._chessboard = chessboard
        self._player = player
        self._target = np.zeros(n_coin)
        # in valid table, 0 is possible and 1 is impossible
        valid_table = [[0, 0, 0, 1, 1],
                       [0, 1, 0, 0, 1],
                       [1, 0, 0, 1, 0],
                       [1, 1, 0, 0, 0]]
        self._valid_table = np.asarray(valid_table)
        temp_player = self._player.get_value()
        # 1*D vector to express possible choice
        self._choice = np.dot(temp_player, np.subtract(1, self._valid_table))

    def predict(self):
        # design some algorigthms here
        self._target = self._target

    def decide(self):
        # check validity and generate the willing
        valid_table = self._valid_table
        temp_target = self._target
        temp_player = self._player.get_value()
        validity = valid_table.dot(temp_target).dot(temp_player)
        n_coin = bank_get_value("n_coin")
        if np.sum(validity) > 0:
            self._target = np.zeros(n_coin)
        return self._target


def invite_players(player_list, game:A2F_Game, chessboard:A2F_Chessboard):
    n_player = bank_get_value("n_player")
    action_list = []
    for idx in range(n_player):
        curr_player = player_list[idx](game=game,
                                       chessboard=chessboard,
                                       player=A2F_Player(np.eye(n_player)[idx]))
        curr_player.predict()
        action_list.append(curr_player.decide())
    return A2F_Action(action_list)


def show_player_ID(player_list):
    n_player = bank_get_value("n_player")
    player_ID = []
    for idx in range(n_player):
        player_ID.append(player_list[idx].__name__)

    return player_ID
