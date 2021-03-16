#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/time.h>

char name[0x80];

void readuntil(char t) {
  char c;
  do {
    c = getchar();
    if (c == EOF) exit(1);
  } while(c != t);
}

int ask_again(void) {
  char buf[0x10];
  printf("Play again? (Y/n) ");
  scanf("%s", buf);
  readuntil('\n');
  if (buf[0] == 'n' || buf[0] == 'N')
    return 0;
  else
    return 1;
}

void ask_time(double *t) {
  printf("Time[sec]: ");
  scanf("%lf", t);
  readuntil('\n');
}

/*
   0x40097b <ask_time+100>:     ret    
   0x40097c <play_game>:        push   rbp
   0x40097d <play_game+1>:      mov    rbp,rsp
=> 0x400980 <play_game+4>:      sub    rsp,0x60
   0x400984 <play_game+8>:      mov    rax,QWORD PTR fs:0x28
   0x40098d <play_game+17>:     mov    QWORD PTR [rbp-0x8],rax
   0x400991 <play_game+21>:     xor    eax,eax
   0x400993 <play_game+23>:     lea    rax,[rbp-0x48]
*/

/** Canary leak 
 * 
 [----------------------------------registers-----------------------------------]
RAX: 0x7ffc70a46768 --> 0xcbb7701b0c41f300 
RBX: 0x7ffc70a467c0 --> 0x40de68540e410b63 
RCX: 0x0 
RDX: 0x0 
RSI: 0x7ffc70a44120 ("-=-=-=-= CHALLENGE 001 =-=-=-=-\n")
RDI: 0x7f85ff7714c0 --> 0x0 
RBP: 0x7ffc70a467b0 --> 0x7ffc70a46890 --> 0x0 
RSP: 0x7ffc70a46750 --> 0x3000000008 
RIP: 0x400997 (<play_game+27>:  mov    rdi,rax)
R8 : 0x20 (' ')
R9 : 0x20 (' ')
R10: 0x40101f (" =-=-=-=-\n")
R11: 0x246 
R12: 0x400760 (<_start>:        xor    ebp,ebp)
R13: 0x7ffc70a46980 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x40098d <play_game+17>:     mov    QWORD PTR [rbp-0x8],rax
   0x400991 <play_game+21>:     xor    eax,eax
   0x400993 <play_game+23>:     lea    rax,[rbp-0x48]
=> 0x400997 <play_game+27>:     mov    rdi,rax
   0x40099a <play_game+30>:     call   0x400917 <ask_time>
   0x40099f <play_game+35>:     mov    rax,QWORD PTR [rbp-0x48]
   0x4009a3 <play_game+39>:     mov    QWORD PTR [rbp-0x58],rax
   0x4009a7 <play_game+43>:     movsd  xmm0,QWORD PTR [rbp-0x58]
[------------------------------------stack-------------------------------------]
 * 
 *
*/
double play_game(void) {
  struct timeval start, end;
  double delta, goal, diff;

  ask_time(&goal);
  printf("Stop the timer as close to %lf seconds as possible!\n", goal);
  puts("Press ENTER to start / stop the timer.");

  readuntil('\n');
  gettimeofday(&start, NULL);
  puts("Timer started.");

  readuntil('\n');
  gettimeofday(&end, NULL);
  puts("Timer stopped.");

  diff = end.tv_sec - start.tv_sec
    + (double)(end.tv_usec - start.tv_usec) / 1000000;

  if (diff == goal) {
    printf("Exactly %lf seconds! Congratulaions!\n", goal);
  } else if (diff < goal) {
    delta = goal - diff;
    printf("Faster by %lf sec!\n", delta);
  } else {
    delta = diff - goal;
    printf("Slower by %lf sec!\n", delta);
  }
  if (delta > 0.5) {
    puts("Too lazy. Try harder!");
  }

  return delta;
}

unsigned char ask_number(void) {
  unsigned int n;
  printf("How many times do you want to try?\n> ");
  scanf("%d", &n);
  return (unsigned char)n;
}

void ask_name(void) {
  char _name[0x80];
  printf("What is your name?\n> ");
  scanf("%s", _name);
  strcpy(name, _name);
}

/**
 * Entry Point
 */
int main(void) {
  unsigned char i, n;
  double *records, best = 31137.31337;

  ask_name();
  n = ask_number();
  records = (double*)alloca(n * sizeof(double));

  for(i = 0; i < n; i++) records[i] = 31137.31337;

  for(i = 0; ; i++) {
    printf("-=-=-=-= CHALLENGE %03d =-=-=-=-\n", i + 1);
    records[i] = play_game();
    if (i >= n - 1) break;
    if (!ask_again()) break;
  }

  for(i = 0; i < n; i++) {
    if (best > records[i]) {
      best = records[i];
    }
  }
  puts("-=-=-=-= RESULT =-=-=-=-");
  printf("Name: %s\n", name);
  printf("Best Score: %lf\n", best);

  return 0;
}

__attribute__((constructor))
void setup(void) {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  alarm(300);
}
