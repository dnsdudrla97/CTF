from Crypto.Cipher import AES

def a(c, i):
    return (c & ((1 << i) ^ 65535)) & 0xffff
    
def b(c, i):
    return (c | (1 << i)) & 0xffff

def c(c, i):
    return ((c & (1 << i)) >> i) & 0xffff

def d(s, num):
    res = ''
    if num == 0:
        return ''
    for i in range(len(s)):
        charAt = ord(s[i])
        cc = num >> (i % 4)
        i3 = i % 3
        if i3 == 0:
            for j in range(0, 8, 2):
                c2 = c(charAt, j) ^ c(cc, j)
                if c2 == 0:
                    charAt = a(charAt, j)
                elif c2 == 1:
                    charAt = b(charAt, j)
        elif i3 == 1:
            for j in range(1, 8, 2):
                c3 = c(charAt, j) ^ c(cc, j)
                if c3 == 0:
                    charAt = a(charAt, j)
                elif c3 == 1:
                    charAt = b(charAt, j)
        elif i3 == 2:
            for j in range(8):
                c4 = c(charAt, j) ^ c(cc, j)
                if c4 == 0:
                    charAt = a(charAt, j)
                elif c4 == 1:
                    charAt = b(charAt, j)
        res += chr(charAt ^ 1)
    return res


arr = [
    "UEBxWw==".decode('base64'),
    "Sk5xVcOICw==".decode('base64'),
    "bnRX".decode('base64'),
    "S0BgWw==".decode('base64'),
    "Nw==".decode('base64'),
    "R0ZxRMOLElk=".decode('base64'),
    "TkJhWw==".decode('base64'),
    "dHZHdcOl".decode('base64'),
    "eWRNYQ==".decode('base64'),
    "bHRSeMOi".decode('base64'),
    "R05tVw==".decode('base64'),
    "d2hScA==".decode('base64'),
    "T0xyVMOADQ==".decode('base64'),
    "f2pQ".decode('base64'),
    "Q0xsVw==".decode('base64'),
    "Nw==".decode('base64')
]

key = ''
for i in range(len(arr)):
    key += d(arr[i], i ^ 137)[0]

unpad= lambda x: x[:-ord(x[-1])]

aes = AES.new(key, AES.MODE_CBC, key)
ct ='7E3Q5fm4lBSKXaHTnlCO52VL/iY6f+hQQ35oeFphtZIu3pf0QuOEpFB5nTeg8GTx'.decode('base64')
print unpad(aes.decrypt(ct))
