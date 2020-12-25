#make private key from public key
from Crypto.PublicKey import RSA
import time

def xgcd(b, n):
    print('XGCD!')
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

# An application of extended GCD algorithm to finding modular inverses:
def mulinv(b, n):
    print("MUL")
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm


def isqrt(n):
    # print("ISQRT")
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def fermat(n, pub):
    print("fermating RSA")
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    while b*b != b2:
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p=a+b
    q=a-b
    assert n == p * q
    print('a=',a)
    print('b=',b)
    print('p=',p)
    print('q=',q)
    print('pq=',p*q)
    print('p-1*q-1=', (p-1)*(q-1))  

    assert pub.n == p * q
    print (pub.e)
    d = mulinv(pub.e, (p - 1) * (q - 1))
    priv = RSA.construct((pub.n, pub.e, d))
    print(priv.exportKey('PEM'))

    return p, q

def main():
    pub = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAg+XB0TAKQnxMS62J9ztp
nbDJgauvUjivONlVyqYJiKyS4n9awnW6OwmcMSWA9cRRLEFr9z8qqIndkE983Hcx
twhw7SXb5hFRALaouaqq+RT5Q81KQa1zM0/up4iFn69yShp8Q1V697for1RR5uYa
UyPe2WBXXCVAsPKcqZvRL504v0FgD5BiwfXL/jGIM3Tid3r2KfKV4b8hB6MYrNj2
oroR3II1is3CP8Xl4/sW+H2C9QnGgbmA/KFYh8ef4CMZc6wnkmabkUkvOqLvL39v
RvnjGpdb508zt5Fgy5frd97pNop/eGlr7VXjbTucReQh2wL+MT5t1ucp7f+LuzVA
VQIDAQAB
-----END PUBLIC KEY-----"""



    # with open('public_key.pem', 'r') as f:
    #     pub = f.read()
    pub = RSA.importKey(pub)
    print(pub.e, pub.n)
    fermat(pub.n, pub)

main()
