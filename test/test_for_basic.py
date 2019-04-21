#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bank.bank import bank_set_value
from basic.basic import *

bank_set_value("n_player", 4)
bank_set_value("n_coin", 5)

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
                    player=player_0,
                    action=action_0,
                    coin=coin_0)
round_0.run()
print(round_0.get_coin().get_value())

# test history
history_0 = A2F_History()
history_0.add_round(round_0)
coin_00 = history_0.get_round(0).get_coin()
print(coin_00.get_value())

