from scapy.all import *
from Crypto.Cipher import AES

cipher = AES.new("TPONEMESH_Kf!xn?", AES.MODE_CBC, "1234567890abcdef")

packet = rdpcap('ac1750.pcapng')

for p in packet:
    if UDP in p:
        try:
            c = raw(p.load)[16:]
            try:
                d = str(cipher.decrypt(c))
                tmp = d.split(',')[3]
                
                if 'printf' in tmp:
                    print(tmp[27], end="")
            except:
                pass
        except:
            pass