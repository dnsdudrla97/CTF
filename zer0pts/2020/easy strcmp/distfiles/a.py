import requests
BASE = 'https://maplestory.nexon.com/News/Notice/Notice/133315'

while (True):
    res = requests.get(BASE)
    print(res)



