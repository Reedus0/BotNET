import os

def cmd(command):
    path = command
    os.system(path + " > file.txt")

    with open("file.txt", "r") as file:
        info = file.read()
        file.close()
    return info
   # Function that let us work with cmd
