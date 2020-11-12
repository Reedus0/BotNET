import os

def cmd(command):
    path = command
    os.system(path + " > file.txt")

    with open("file.txt", "r") as file:
        info = file.read()
        file.close()
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')
    os.remove(path)
    return info
   # Function that let us work with cmd
