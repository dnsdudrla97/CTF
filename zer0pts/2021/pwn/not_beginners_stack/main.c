global _start
section .text

#define call(__stack_shadow[__stack_depth++] = return_address) goto function
#define __stack_shadow[--_stack_depth]

// .bss (_start)
call(notvuln)
call(exit)


void notvuln() {
    char buf[0x100];
    vuln();
    write(1, "Data: ", 6);
    read(0, buf, 0x100);
    return 0;
}
void vuln() {
    char buf[0x100];
    write(1, "Data: ", 6);
    read(0, buf, 0x1000);
    return;
}
read:
  xor eax, eax
  syscall
  ret

write:
  xor eax, eax
  inc eax
  syscall
  ret

exit:
  mov eax, 60
  syscall
  hlt
  
section .data
int __stack_depth =0;
char __stack_shadow[1024]