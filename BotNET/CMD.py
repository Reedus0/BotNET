import os

def cmd(command):
    path = command
    print(path)
    os.system(path + " > file.txt")

    with open("file.txt", "r") as file:
        return file.read()


