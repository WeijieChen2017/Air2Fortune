#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bank.bank import bank_set_value
from basic.basic import *

bank_set_value("n_player", 4)
bank_set_value("n_coin", 5)
bank_set_value("n_max_game", 5)

# test basic setting
chessboard_0 = A2F_Chessboard([2, 3, 5, 3, 2])
player_0 = A2F_Player([0, 0, 1, 0])
coin_0 = A2F_Coin([0, 0, 0, 0])
policy_0 = [0, 0, 1, 0, 0]
policy_1 = [1, 0, 0, 0, 0]
policy_2 = [0, 0, 1, 0, 0]
policy_3 = [0, 0, 0, 1, 0]
action_0 = A2F_Action([policy_0, policy_1, policy_2, policy_3])
round_0 = A2F_Round(chessboard=chessboard_0,
                    action=action_0)
coin_1 = round_0.run()
print(coin_0.get_value() + coin_1.get_value())

# test history
game_0 = A2F_Game()
game_0.add_round(round_0)
coin_11 = game_0.get_round(0).run()
print(coin_0.get_value() + coin_11.get_value())

