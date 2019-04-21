#!/usr/bin/python
# -*- coding: UTF-8 -*-

global global_dict

global_dict = {}


def bank_set_value(key, value):
    global_dict[key] = value


def bank_get_value(key, def_value=None):
    try:
        return global_dict[key]
    except KeyError:
        return def_value


def gbl_all():
    return global_dict
