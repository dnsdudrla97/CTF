from pwn import *
import string, random, hashlib
import pow


RANDOMSTRING = string.ascii_letters
RANDOMINT = string.digits
PAYLOAD = ''

def remoteGET():
    r = remote('any.ctf.zer0pts.com', 11011)
    data = r.recvline().decode().split('=')
    hiddenKey = (data[0].strip('').split("\""))[1][4:]
    hashResult = data[1].replace(" ", "")
    # print(hiddenKey)
    # print(hashResult)
    return hiddenKey, hashResult    

def generateRandom():
    global PAYLOAD
    for i in range(0x20, 0x7E):
        PAYLOAD += chr(i)

def random4ourHash():
    result = ''
    generateRandom()
    for i in range(4):
        result += random.choice(PAYLOAD)
    return result
def randomRandom():
    hiddenKey, hashResult = remoteGET()


    while(True):    
        frontInput = random4ourHash()
        hashEncode = (frontInput+hiddenKey).encode()
        encodeDigest = hashlib.sha256(hashEncode).hexdigest()
        
        if (encodeDigest):
            log.info(f'BF KEY = ${frontInput}[${hiddenKey}]')
            log.info(f'BF KEY hash = ${encodeDigest}')
            log.info(f'Origin hash = ${hashResult}')
            if (encodeDigest == hashResult):
                log.success(frontInput)
                break
            else:
                log.critical("FUCK") 
                pass
        else:
            log.critical("fUCK")
            break    

def remoteGET():
    r = remote('any.ctf.zer0pts.com', 11011)
    data = r.recvline().decode().split('=')
    print(data)
    hiddenKey = (data[0].strip('').split("\""))[1][4:]
    hashResult = data[1].replace(" ", "")
    pow.pow_py(hiddenKey, hashResult)

remoteGET()


