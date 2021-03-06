#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
from bank.bank import bank_set_value
from policy.pure_policy import *
from policy.advanced_policy import *
from basic.basic import *
from basic.advanced import *


# Symmetric NE
# 0.360945, 0.165931, 0.473124
# Low, Medium, High


# basic setting

max_game = 30000
n_player = 4
n_coin = 5
n_test = 100
lr = 5e-4
filename = "FF_prob_"+str(max_game)+"_"+str(lr)+"_uni"
bank_set_value("n_player", n_player)
bank_set_value("n_coin", n_coin)
bank_set_value("max_game", max_game)
chessboard = A2F_Chessboard([10, 5, 3, 5, 10])
chessboard_value = chessboard.get_value()
winning_rate = np.zeros((n_player, max_game))
player_list = [A2FP_Learner,
               A2FP_Random_Prob,
               A2FP_Random_Prob,
               A2FP_Random_Prob]
PARA_SYM_NE = [[0.360945, 0.165931, 0.473124],
             [0.360945, 0.473124, 0.165931],
             [0.165931, 0.473124, 0.360945],
             [0.473124, 0.165931, 0.360945]]

PARA_LIST = [[0.360945, 0.165931, 0.473124],
            [0.360945, 0.473124, 0.165931],
            [0.165931, 0.473124, 0.360945],
            [0.473124, 0.165931, 0.360945]]

PARA_UNI = [[1/3, 1/3, 1/3],
            [1/3, 1/3, 1/3],
            [1/3, 1/3, 1/3],
            [1/3, 1/3, 1/3]]

valid_table = [[0, 0, 0, 1, 1],
               [0, 1, 0, 0, 1],
               [1, 0, 0, 1, 0],
               [1, 1, 0, 0, 0]]

reverse_table = [[0, 1, 2, 9, 9],
                 [0, 9, 2, 1, 9],
                 [9, 1, 2, 9, 0],
                 [9, 9, 2, 1, 0]]

# reverse_table = [[2, 1, 0, 9, 9],
                 # [2, 9, 0, 1, 9],
                 # [9, 1, 0, 9, 2],
                 # [9, 9, 0, 1, 2]]
choice = np.subtract(1, valid_table)
# history_prob = np.zeros((max_game, n_test, n_player, 3))

# simulate
# for idx_game in range(max_game):
#
#     total_game = idx_game + 1
#
#     bank_set_value("total_game", total_game)
#     init_winner = np.zeros(n_player)
#
#     for idx_test in range(n_test):
#         game = A2F_Game()
#         para_list = copy.deepcopy(PARA_UNI)
#         for idx_round in range(total_game):
#
#             curr_action = invite_players(player_list=player_list,
#                                          game=game,
#                                          chessboard=chessboard,
#                                          para_list=para_list)
#
#             curr_round = A2F_Round(chessboard=chessboard, action=curr_action)
#
#             # two-direction training
#             curr_action_value = curr_action.get_value()
#             curr_result = np.sum(curr_action_value, axis=0)
#             new_para_list = []
#             for idx_update in range(n_player):
#                 curr_aim = list(curr_action_value[idx_update]).index(1)
#                 curr_coin = np.multiply(choice[idx_update], chessboard_value)
#                 curr_sum = np.sum(curr_coin)
#                 curr_para = para_list[idx_update]
#                 loc_aim = reverse_table[idx_update][curr_aim]
#                 if idx_update in [0, 1, 2, 3]:
#                     if curr_result[curr_aim] == 1:
#                         # right answer
#                         if curr_para[loc_aim] < 0.8:
#                             curr_para[loc_aim] *= 1+lr*(curr_coin[curr_aim]/curr_sum)
#                     else:
#                         # wrong answer
#                         if curr_para[loc_aim] > 0.1:
#                             curr_para[loc_aim] *= 1-lr*(curr_coin[curr_aim]/curr_sum)
#                 temp_sum = np.sum(curr_para)
#                 new_para = []
#                 for idx in curr_para:
#                     new_para.append(idx/temp_sum)
#                 if idx_round == max_game - 1:
#                     print("Round: ", idx_round, "Player: ", idx_update, "Prob: ", new_para)
#                 new_para_list.append(new_para)
#                 if idx_update in [0, 1, 2, 3]:
#                     history_prob[idx_game, idx_test, idx_update, :] = new_para
#
#             game.add_round(curr_round)
#             para_list = new_para_list
#             if idx_round == max_game - 1:
#                 print("-------------------")
#
#
#         final_coin, best_player = game.winner()
#         init_winner += best_player
#
#     print(idx_game)
#     print(init_winner)
#     winning_rate[:, idx_game] = init_winner/n_test
#
# # draw curve
# time_stamp = datetime.datetime.now().strftime("-%Y-%m-%d-%H-%M")
# xmesh = np.array(range(max_game))
# plt.figure(figsize=(8, 6), dpi=300)
# plt.scatter(xmesh, winning_rate[0, :])
# plt.scatter(xmesh, winning_rate[1, :])
# plt.scatter(xmesh, winning_rate[2, :])
# plt.scatter(xmesh, winning_rate[3, :])
# plt.xlabel("Number of total games")
# plt.ylabel("Winning rate of players")
# plt.ylim(bottom=0, top=1)
# plt.legend(show_player_ID(player_list))
# plt.savefig("WinningRate_MaxGame"+time_stamp+".png")

# plt.figure(figsize=(8, 6), dpi=300)
# plt.scatter(xmesh, history_prob[:, 0, 0, 0], marker='^')
# plt.scatter(xmesh, history_prob[:, 0, 0, 1], marker='o')
# plt.scatter(xmesh, history_prob[:, 0, 0, 2], marker='s')
#
# plt.scatter(xmesh, history_prob[:, 0, 1, 0], marker='^')
# plt.scatter(xmesh, history_prob[:, 0, 1, 1], marker='o')
# plt.scatter(xmesh, history_prob[:, 0, 1, 2], marker='s')
#
# plt.scatter(xmesh, history_prob[:, 0, 2, 0], marker='^')
# plt.scatter(xmesh, history_prob[:, 0, 2, 1], marker='o')
# plt.scatter(xmesh, history_prob[:, 0, 2, 2], marker='s')
#
# plt.scatter(xmesh, history_prob[:, 0, 3, 0], marker='^')
# plt.scatter(xmesh, history_prob[:, 0, 3, 1], marker='o')
# plt.scatter(xmesh, history_prob[:, 0, 3, 2], marker='s')
#
#
# plt.xlabel("Number of total games")
# plt.ylabel("Prob over time")
# plt.ylim(bottom=0, top=1)
# plt.legend(["Prob L_1", "Prob M_1", "Prob H_!",
#             "Prob L_2", "Prob M_2", "Prob H_2",
#             "Prob L_3", "Prob M_3", "Prob H_3",
#             "Prob L_4", "Prob M_4", "Prob H_4"])
# plt.savefig("Prob"+time_stamp+".png")
# np.save("prob.npy",history_prob )


# simple find the prob
total_game = max_game

bank_set_value("total_game", total_game)
init_winner = np.zeros(n_player)
history_prob = np.zeros((max_game, n_test, n_player, 3))

for idx_test in range(n_test):
    game = A2F_Game()
    para_list = copy.deepcopy(PARA_UNI)
    for idx_round in range(total_game):

        curr_action = invite_players(player_list=player_list,
                                     game=game,
                                     chessboard=chessboard,
                                     para_list=para_list)

        curr_round = A2F_Round(chessboard=chessboard, action=curr_action)

        # two-direction training
        curr_action_value = curr_action.get_value()
        curr_result = np.sum(curr_action_value, axis=0)
        new_para_list = []
        for idx_update in range(n_player):
            curr_aim = list(curr_action_value[idx_update]).index(1)
            curr_coin = np.multiply(choice[idx_update], chessboard_value)
            curr_sum = np.sum(curr_coin)
            curr_para = para_list[idx_update]
            loc_aim = reverse_table[idx_update][curr_aim]
            if curr_result[curr_aim] == 1:
                # right answer
                if curr_para[loc_aim] < 0.8:
                    curr_para[loc_aim] *= 1+lr*(curr_coin[curr_aim]/curr_sum)
            else:
                # wrong answer
                if curr_para[loc_aim] > 0.1:
                    curr_para[loc_aim] *= 1-lr*(curr_coin[curr_aim]/curr_sum)
            temp_sum = np.sum(curr_para)
            new_para = []
            for idx in curr_para:
                new_para.append(idx/temp_sum)
            # if idx_round == max_game - 1:
            #     print("Round: ", idx_round, "Player: ", idx_update, "Prob: ", new_para)
            new_para_list.append(new_para)
            history_prob[idx_round, idx_test, idx_update, :] = new_para

        game.add_round(curr_round)
        para_list = new_para_list
        # if idx_round == max_game - 1:
        #     print("-------------------")
    final_coin, best_player = game.winner()
    init_winner += best_player

    print(idx_test)

np.save(filename+".npy", history_prob)


xmesh = np.array(range(max_game))
# print(history_prob[:, 0, 1])

plt.figure(figsize=(8, 6), dpi=300)

prob_low = np.zeros((max_game, n_player))
prob_medium = np.zeros((max_game, n_player))
prob_high = np.zeros((max_game, n_player))
for idx_game in range(max_game):
    prob_low[idx_game, 0] = np.mean(history_prob[idx_game, :, 0, 0])
    prob_low[idx_game, 1] = np.mean(history_prob[idx_game, :, 1, 0])
    prob_low[idx_game, 2] = np.mean(history_prob[idx_game, :, 2, 0])
    prob_low[idx_game, 3] = np.mean(history_prob[idx_game, :, 3, 0])

    prob_medium[idx_game, 0] = np.mean(history_prob[idx_game, :, 0, 1])
    prob_medium[idx_game, 1] = np.mean(history_prob[idx_game, :, 1, 1])
    prob_medium[idx_game, 2] = np.mean(history_prob[idx_game, :, 2, 1])
    prob_medium[idx_game, 3] = np.mean(history_prob[idx_game, :, 3, 1])

    prob_high[idx_game, 0] = np.mean(history_prob[idx_game, :, 0, 2])
    prob_high[idx_game, 1] = np.mean(history_prob[idx_game, :, 1, 2])
    prob_high[idx_game, 2] = np.mean(history_prob[idx_game, :, 2, 2])
    prob_high[idx_game, 3] = np.mean(history_prob[idx_game, :, 3, 2])


# plt.scatter(xmesh, prob_high[:, 0], marker='^', c=sns.xkcd_rgb["windows blue"], alpha=0.7)
# plt.scatter(xmesh, prob_high[:, 1], marker='^', c=sns.xkcd_rgb["amber"], alpha=0.7)
# plt.scatter(xmesh, prob_high[:, 2], marker='^', c=sns.xkcd_rgb["faded green"], alpha=0.7)
# plt.scatter(xmesh, prob_high[:, 3], marker='^', c=sns.xkcd_rgb["pale red"], alpha=0.7)

trans = 0.7

plt.scatter(xmesh, prob_low[:, 0], marker='^', c=sns.xkcd_rgb["medium green"], alpha=trans)
plt.scatter(xmesh, prob_low[:, 1], marker='s', c=sns.xkcd_rgb["medium green"], alpha=trans)
plt.scatter(xmesh, prob_low[:, 2], marker='.', c=sns.xkcd_rgb["medium green"], alpha=trans)
plt.scatter(xmesh, prob_low[:, 3], marker='+', c=sns.xkcd_rgb["medium green"], alpha=trans)

plt.scatter(xmesh, prob_medium[:, 0], marker='^', c=sns.xkcd_rgb["denim blue"], alpha=trans)
plt.scatter(xmesh, prob_medium[:, 1], marker='s', c=sns.xkcd_rgb["denim blue"], alpha=trans)
plt.scatter(xmesh, prob_medium[:, 2], marker='.', c=sns.xkcd_rgb["denim blue"], alpha=trans)
plt.scatter(xmesh, prob_medium[:, 3], marker='+', c=sns.xkcd_rgb["denim blue"], alpha=trans)

plt.scatter(xmesh, prob_high[:, 0], marker='^', c=sns.xkcd_rgb["pale red"], alpha=trans)
plt.scatter(xmesh, prob_high[:, 1], marker='s', c=sns.xkcd_rgb["pale red"], alpha=trans)
plt.scatter(xmesh, prob_high[:, 2], marker='.', c=sns.xkcd_rgb["pale red"], alpha=trans)
plt.scatter(xmesh, prob_high[:, 3], marker='+', c=sns.xkcd_rgb["pale red"], alpha=trans)

avg_low = round(float(np.mean(prob_low[-1, :])), 6)
avg_medium = round(float(np.mean(prob_medium[-1, :])), 6)
avg_high = round(float(np.mean(prob_high[-1, :])), 6)

plt.title("[Low, Medium, High] = ["+str(avg_low)+", "+str(avg_medium)+", "+str(avg_high)+"], lr="+str(lr))
plt.legend(["Prob L_1", "Prob L_2", "Prob L_3", "Prob L_4",
            "Prob M_1", "Prob M_2", "Prob M_3", "Prob M_4",
            "Prob H_1", "Prob H_2", "Prob H_3", "Prob H_4"])


# plt.scatter(xmesh, history_prob[:, 0, 0, 0], marker='^')
# plt.scatter(xmesh, history_prob[:, 0, 0, 1], marker='o')
# plt.scatter(xmesh, history_prob[:, 0, 0, 2], marker='s')

# plt.scatter(xmesh, history_prob[:, 0, 1, 0], marker='^')
# plt.scatter(xmesh, history_prob[:, 0, 1, 1], marker='o')
# plt.scatter(xmesh, history_prob[:, 0, 1, 2], marker='s')

# plt.scatter(xmesh, history_prob[:, 0, 2, 0], marker='^')
# plt.scatter(xmesh, history_prob[:, 0, 2, 1], marker='o')
# plt.scatter(xmesh, history_prob[:, 0, 2, 2], marker='s')

# plt.scatter(xmesh, history_prob[:, 0, 3, 0], marker='^')
# plt.scatter(xmesh, history_prob[:, 0, 3, 1], marker='o')
# plt.scatter(xmesh, history_prob[:, 0, 3, 2], marker='s')

# plt.legend(["Prob L_1", "Prob M_1", "Prob H_!",
#             "Prob L_2", "Prob M_2", "Prob H_2",
#             "Prob L_3", "Prob M_3", "Prob H_3",
#             "Prob L_4", "Prob M_4", "Prob H_4"])


plt.xlabel("Number of total games")
plt.ylabel("Prob over time")
plt.ylim(bottom=0, top=1)
plt.savefig(filename+".png")
# np.save("prob.npy",history_prob )
