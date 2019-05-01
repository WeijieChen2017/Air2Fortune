#!/usr/bin/python
# -*- coding: UTF-8 -*-

import copy
import numpy as np
from bank.bank import bank_get_value
from basic.basic import *
from policy.pure_policy import *
from policy.advanced_policy import *


def invite_players(player_list, game:A2F_Game, chessboard:A2F_Chessboard, para_list):
    n_player = bank_get_value("n_player")
    action_list = []
    for idx in range(n_player):
        if player_list[idx].__name__ != "A2FP_Cheat":
            curr_player = player_list[idx](game=game,
                                           chessboard=chessboard,
                                           player=A2F_Player(np.eye(n_player)[idx]),
                                           para=para_list[idx])
            curr_player.predict()
            action_list.append(curr_player.decide())
        else:
            curr_player = player_list[idx](game=game,
                                           chessboard=chessboard,
                                           player=A2F_Player(np.eye(n_player)[idx]),
                                           para=action_list)
            curr_player.predict()
            action_list.append(curr_player.decide())
    return A2F_Action(action_list)


def show_player_ID(player_list):
    n_player = bank_get_value("n_player")
    player_ID = []
    for idx in range(n_player):
        player_ID.append(player_list[idx].__name__)

    return player_ID
