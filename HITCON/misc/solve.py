# from pwn import *

# if __name__ == "__main__":
#     # context.log_level = 'debug'
#     # context.arch = 'amd64'
#     # l = listen()
#     s = ssh(user='oshell', host='54.150.148.61', password='oshell')
#     r1 = s1.remote(s.host, 22)


    
#     print(r1.recv())
    
#     # print(s)
#     # s.send('1a2764c4-ff45-494f-b0e9-30b95a90fdfd')
#     # print(s.recv())
#     # sc = s.connect_remote('54.150.148.61')

    
import paramiko
import getpass
 
cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
 
server = '54.150.148.61'
user = 'oshell'
pwd = 'oshell'
 
print(cli.connect(server, port=22, username=user, password=pwd))
# stdin, stdout, stderr = cli.exec_command('1a2764c4-ff45-494f-b0e9-30b95a90fdfd')
# print(stdout)
# # stdin, stdout, stderr = cli.exec_command("ls -la")
# # lines = stdout.readlines()
# # print(''.join(lines))
 
# # cli.close()