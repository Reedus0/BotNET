import requests

def postDDoS(url, data):
    r = requests.post(url, data=data)
    print(r.status_code)
    # Function that send POST requests

def getDDoS(url):
    r = requests.get(url)
    print(r.status_code)
    # Function that send GET requests

