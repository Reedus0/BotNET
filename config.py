import os

dir = os.path.abspath(os.curdir) + "\database.json"

config = {
    "name" : "@KUCOLDBOT",
    "token" : "1207495309:AAHk2rF6QHor5qWl0BWVIQR1SmiqV91Mw_k",
    "json_file" : dir,
}

class States():
    S_LOGIN = 0
    S_LOGINED_A = 1
    S_DDOS_A = 2
    S_DDOS_GET1_A = 3
    S_DDOS_GET2_A = 4
    S_DDOS_POST1_A = 5
    S_DDOS_POST2_A = 6
    S_DDOS_POST3_A = 7
    S_LOGINED_B = 8
    S_DDOS_B = 9
    S_DDOS_GET1_B = 10
    S_DDOS_GET2_B = 11
    S_DDOS_POST1_B = 12
    S_DDOS_POST2_B = 13
    S_DDOS_POST3_B = 14
    S_CMD_B = 15
    S_CMD_CD_B = 16