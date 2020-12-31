# BotNET
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FReedus0%2FBotNET.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FReedus0%2FBotNET?ref=badge_shield)


BotNET - is program that can do GET and POST request on command. With this program you can create your own BotNET.

# What's new in the last version 1.3?
In 1.3 version BotNET was fully reworked and moved to new messenger: **Telegram**. 

# Installing 

To use BotNET you need to install you can type in your console:
```
pip install -r requirements.txt            
```
 
Or you can install each one by one:
```
pyTelegramBotApi
requests
getpass3
```

To make BotNET work you need create Bot in Telegram. To create bot you need to message **@BotFather**. When you create new bot, **@BotFather** will give you **token**. You need use this token in your **config.py**

Example:
```
config = {
    "name" : "@KUCOLDBOT",
    "token" : "1207495309:AAHk2rF6QHor5qWl0BWVIQ1stmiqV91Mw_k", # <- Here's your token
    "json_file" : dir,
}
```

# Functional 

To start work with BotNET you need to run BotNET.py and write message to your community to your Bot in Telegram with text that you can change(It's like password). I have:

```
Reeuds 16080305
```

When you write your username + password community write you that you logined in and you can use commands.

# Commands

Here's be all commands that your BotNET can do
```
DDoS - enter in POST/GET requests panel.
Check - check for new users that now have runned BotNET.
online - show all users who have BotNET running right now.
cmd - allows you to use cmd on your bot(only allows on bots, except admins)
```
Below be more advanced description

# DDoS

In POST/GET requests panel you can see 2 type of requests POST and GET(captain obvious)
```
1. To make GET requests you need write "GET" after entering in requests panel.
2. When you write "GET" you need to paste link to which requests will be made.
3. Next you writing link you need to write count of requests(from 1 to 99999)
```
After writing all information BotNET being do requests.

With POST requests be a bit harder
```
1. To make POST requests you need write "POST" after entering in requests panel.
2. After writing link you need to write "data" of POST request(data is cortage of information that request transmitt to server).
3. Next step you need again write count of requests(from 1 to 99999)
```
After writing all information BotNET beging do requests.

After end of sending requests you need type "Выход" to exit(if you done POST requests you need type "Выход" 2 times).

# Check 

Where you type "Check" to your BotNET him check for new users that now have run BotNET.

What it meens?

You user and you logined as **admin**. When you type **"Check"** all other users become online.
When you enter in requests panel other users enter in it too. If you begin sending requests as admin, all other users begin do it too.

# online 

This is very easy.

When you type **"online"** to you community - all users who have run BotNET right now is shown you

# cmd

**cmd** is new command that has appeared in BotNET from 1.2 version. This command allows you control cmd of chosen bot. 
It's very helpful when you need to do something with files of your bot or when you want to have a little fun :).

**cmd** has a subcommand that called cd. You can enter in cmd mode by the command: **"Bot name + cmd"**.

It's looks like:
```
Reedus cmd
```
When you are in the **cmd mode** you can turn cd to change current directory. 
After you write **cd** - BotNET asks you to choose directory which you want to get into. 
You can check all directories by turning into cmd command called "dir". 
After this command you will know all directories in the folder.
It's allows you to manipulate with all files on bot's computer.


        

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FReedus0%2FBotNET.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FReedus0%2FBotNET?ref=badge_large)

