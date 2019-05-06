#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from bank.bank import bank_set_value
from policy.pure_policy import *
from policy.advanced_policy import *
from basic.basic import *
from basic.advanced import *

# basic setting

max_game = 100
n_player = 4
n_coin = 5
n_test = 30
bank_set_value("n_player", n_player)
bank_set_value("n_coin", n_coin)
bank_set_value("max_game", max_game)
chessboard = A2F_Chessboard([2, 3, 5, 3, 2])
winning_rate = np.zeros((n_player, max_game))
player_list = [A2FP_Observer, A2FP_Random_Prob, A2FP_Random_Prob, A2FP_Random_Prob]
para_list = [[0.7, 0.2, 0.1],
             [0.2, 0.1, 0.7],
             [0.7, 0.1, 0.2],
             [0.1, 0.7, 0.2]]

# simulate
for idx_game in range(max_game):

    total_game = idx_game + 1

    bank_set_value("total_game", total_game)
    init_winner = np.zeros(n_player)

    for idx_test in range(n_test):
        game = A2F_Game()
        for idx_round in range(total_game):

            curr_action = invite_players(player_list=player_list,
                                         game=game,
                                         chessboard=chessboard,
                                         para_list=para_list)

            curr_round = A2F_Round(chessboard=chessboard, action=curr_action)
            # print(curr_action.get_value())
            # print("-------------")
            game.add_round(curr_round)
            # print(game._total_round)

        final_coin, best_player = game.winner()
        init_winner += best_player

    print(idx_game)
    print(init_winner)
    winning_rate[:, idx_game] = init_winner/n_test

# draw curve
time_stamp = datetime.datetime.now().strftime("-%Y-%m-%d-%H-%M")
xmesh = np.array(range(max_game))
plt.figure(figsize=(8, 6), dpi=300)
plt.scatter(xmesh, winning_rate[0, :])
plt.scatter(xmesh, winning_rate[1, :])
plt.scatter(xmesh, winning_rate[2, :])
plt.scatter(xmesh, winning_rate[3, :])
plt.xlabel("Number of total games")
plt.ylabel("Winning rate of the greedy player")
plt.ylim(bottom=0, top=1)
plt.legend(show_player_ID(player_list))
plt.savefig("WinningRate_MaxGame"+time_stamp+".png")
