import subprocess as sup
import hashlib
import base64 as b64
import random 
import sys

PATH = b""

IS_ELF_FILE_MSG = b"bin%d: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2"
IS_NOT_STRIPPED = b"not stripped"

BAN_LIST = [ "sys", "exec", "scanf", "open", "read", "write", "socket", "send", "recv", "print", "thread", "close", "listen", "bind", "accept", "get", "mprotect", "alloc", "free", "map", "fork", "wait", "warn", "Please solve this challenge by my intent ^___^" ]

def _print(msg, end="\n"):
    print(msg, end=end)
    sys.stdout.flush()
    
def fail(stage):
    sup.call([b"rm", b"-rf", PATH])
    _print("%s FAIL..."%stage)
    exit(-1)

def filterSyscall(res) :
    if b"\x0f\x05" in res :
        fail("STAGE2")

def filterFunction(data) :
    for ban in BAN_LIST:
        if ban.encode() in data:
            print(data)
            _print(ban)
            fail("STAGE1")

def getData():
    size1 = int(input("Size of base64 encoded Data 1: "))
    size2 = int(input("Size of base64 encoded Data 2: "))
    _print("Data 1 (base64 encoded): ", end="")
    data1 = sys.stdin.read(size1)
    _print("Data 2 (base64 encoded): ", end="")
    data2 = sys.stdin.read(size2)
    data1 = b64.b64decode(data1)
    data2 = b64.b64decode(data2)
    return data1, data2

def stage1():
    try:
        data1, data2 = getData()
        filterFunction(data1)
        filterFunction(data2)
        filterSyscall(data1)
        filterSyscall(data2)
        return data1, data2
    except:
        fail("STAGE1")

def stage2(data1, data2):
    print("STAGE2")
    with open(PATH + b"bin1", "wb") as f:
        f.write(data1)
    with open(PATH + b"bin2", "wb") as f:
        f.write(data2)
    res1 = sup.check_output([b"file", PATH + b"bin1"])
    res2 = sup.check_output([b"file", PATH + b"bin2"])
    
    if IS_ELF_FILE_MSG%1 not in res1 :
        fail("STAGE2")
    if IS_ELF_FILE_MSG%2 not in res2 :
        fail("STAGE2")
    
    print("Success ELF")

    if IS_NOT_STRIPPED not in res1 :
        fail("STAGE2")
    if IS_NOT_STRIPPED not in res2 :
        fail("STAGE2")


def stage3():
    res1 = sup.check_output([b"md5sum", PATH + b"bin1"]).split(b" ")[0]
    res2 = sup.check_output([b"md5sum", PATH + b"bin2"]).split(b" ")[0]
    if res1 != res2 :
        fail("STAGE3")

def stage4():
    try:
        sup.call([b"chmod", b"+x", PATH + b"bin1"])
        sup.call([b"chmod", b"+x", PATH + b"bin2"])
        res1 = sup.check_output([PATH + b"bin1"])
        res2 = sup.check_output([PATH + b"bin2"])
        if res1 == res2 :
            fail("STAGE4")
    except:
        fail("STAGE4")

def clear(): 
    sup.call([b"rm", b"-rf", PATH])
    _print("="*50)
    _print("Congraturation~")
    _print("You know about md5 hash well!")
    _print("Do you want this?")
    with open(b"/home/md5_call_re_jeon/flag", "r") as f:
        flag = f.read()
    _print("FLAG: " + flag)
    _print("="*50)

def main():
    global PATH # to byte
    PATH += b"/tmp/" + str(random.randint(0x100000000000000000000000, 0xffffffffffffffffffffffff) * 0x31337).encode() + b"/"
    sup.call([b"mkdir", PATH])
    data1, data2 = stage1()
    stage2(data1, data2)
    stage3()
    stage4()
    clear()

if __name__ == "__main__": 
    main()

    # XHg3Zlx4NDVceDRjXHg0Nlx4MDJceDAxXHgwMVx4MzFceGMwXHgzMVx4ZDJceDUwXHg2OFx4MmZceDJmXHg3M1x4NjhceDY4XHgyZlx4NjJceDY5XHg2ZVx4ODlceGUzXHg1Mlx4NTNceDg5XHhlMVx4YjBceDBiXHhjZFx4ODA=

"\x7f\x45\x4c\x46\x02\x01\x01\x00\x4c\x53\x42\x20\x73\x68\x61\x72\x65\x64\x20\x6f\x62\x6a\x65\x63\x74\x20\x78\x38\x36\x2d\x36\x34\x20\x76\x65\x72\x73\x69\x6f\x6e\x20\x31\x20\x28\x53\x59\x53\x56\x29\x20\x64\x79\x6e\x61\x6d\x69\x63\x61\x6c\x6c\x79\x20\x6c\x69\x6e\x6b\x65\x64\x20\x69\x6e\x74\x65\x72\x70\x72\x65\x74\x65\x72\x20\x2f\x6c\x69\x62\x36\x34\x2f\x6c\x64\x2d\x6c\x69\x6e\x75\x78\x2d\x78\x38\x36\x2d\x36\x34\x2e\x73\x6f\x2e\x32\x20\x6e\x6f\x74\x20\x73\x74\x72\x69\x70\x70\x65\x64"

