#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bank.bank import bank_set_value
from basic.basic import *
from policy.pure_policy import *


# basic setting
bank_set_value("n_player", 4)
bank_set_value("n_coin", 5)
bank_set_value("n_max_game", 5)

chessboard = A2F_Chessboard([2, 3, 5, 3, 2])
player_0 = A2F_Player([1, 0, 0, 0])
player_1 = A2F_Player([0, 1, 0, 0])
player_2 = A2F_Player([0, 0, 1, 0])
player_3 = A2F_Player([0, 0, 0, 1])
player_list = [player_0, player_1, player_2, player_3]

coin_0 = A2F_Coin([0, 0, 0, 0])
game = A2F_Game()
coin_list = []

for idx_round in range(bank_get_value("n_max_game")):
    action_list = []
    for idx_player in range(bank_get_value("n_player")):
        random_player = A2FP_Random(game=game,
                                    chessboard=chessboard,
                                    player=player_list[idx_player])
        random_player.predict()
        action_list.append(random_player.decide())
    curr_action = A2F_Action(action_list)
    curr_round = A2F_Round(chessboard=chessboard, action=curr_action)
    coin_list.append(curr_round.run())
    game.add_round(curr_round)

final_coin, best_player = game.winner()
print("Final coin:", final_coin)
print("Best player", best_player)


