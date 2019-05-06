#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

max_game = 200
n_player = 4
xmesh = np.array(range(max_game))
history_prob = np.load("prob.npy")
print(history_prob.shape)
# print(history_prob[:, 0, 1])

plt.figure(figsize=(8, 6), dpi=300)

prob_low = np.zeros((max_game, n_player))
prob_medium = np.zeros((max_game, n_player))
prob_high = np.zeros((max_game, n_player))
for idx_game in range(max_game):
    prob_low[idx_game, 0] = np.mean(history_prob[idx_game, :, 0, 0])
    prob_low[idx_game, 1] = np.mean(history_prob[idx_game, :, 1, 0])
    prob_low[idx_game, 2] = np.mean(history_prob[idx_game, :, 2, 2])
    prob_low[idx_game, 3] = np.mean(history_prob[idx_game, :, 3, 2])

    prob_medium[idx_game, 0] = np.mean(history_prob[idx_game, :, 0, 1])
    prob_medium[idx_game, 1] = np.mean(history_prob[idx_game, :, 1, 2])
    prob_medium[idx_game, 2] = np.mean(history_prob[idx_game, :, 2, 0])
    prob_medium[idx_game, 3] = np.mean(history_prob[idx_game, :, 3, 1])

    prob_high[idx_game, 0] = np.mean(history_prob[idx_game, :, 0, 2])
    prob_high[idx_game, 1] = np.mean(history_prob[idx_game, :, 1, 1])
    prob_high[idx_game, 2] = np.mean(history_prob[idx_game, :, 2, 1])
    prob_high[idx_game, 3] = np.mean(history_prob[idx_game, :, 3, 0])


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
plt.savefig("Prob_200.png")
np.save("prob.npy",history_prob )
