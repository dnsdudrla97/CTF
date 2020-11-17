; t.asm
BITS 64
GLOBAL _start
SECTION .text
_start:
              mov     rax, 1
              mov     rbx, 42  
              int     0x80
