import telebot
import config
import requests
from dbworker import set_state, get_current_state

client = telebot.TeleBot(config.config["token"])

def postDDoS(url, data):
    r = requests.post(url, data=data)
    print(r.status_code)
    # Function that send POST requests

def getDDoS(url):
    r = requests.get(url)
    print(r.status_code)
    # Function that send GET requests