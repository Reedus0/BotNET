import requests
import os
import re
import bs4
import urllib

values = []

def getText(list):
    for state in list:
        text = state.get_text()
        values.append(text)

def update(current_ver):
    status = 0
    r = requests.get("https://github.com/Reedus0/BotNET/tags")
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    list = soup.select('h4.flex-auto.min-width-0.pr-2.pb-1.commit-title')
    getText(list)
    ver = values[0]
    mystr = re.sub(" ", "", ver)
    mystr = re.sub("…", "", mystr)
    mystr = re.sub("\n", "", mystr)
    version = float(mystr)

    if (version > current_ver):
        url = 'https://github.com/Reedus0/BotNET/releases/download/1.1/BotNET.exe'
        urllib.request.urlretrieve(url, "lastnet.exe")
        os.system("lastnet.exe")
    else:
        status = 0
        pass
    return status

import urllib.request