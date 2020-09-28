## ExpectedValue

---

### CHALLENGE
 This is a simple shellcoding challenge.
 You should write a shellcode for x64 linux machine to evaluate an [expected value](https://en.wikipedia.org/wiki/Expected_value).

 The shellcod should
  * start with the x64 function prologue(push rbp; mov rbp, rsp)
  * end with the x64 function epilogue(leave; ret)
  * have max 128 byte length
  * cannot contain 0x00, 0xcd, 0x0f or 0x95

### FILES
  * **selftest and selftest.c** These are provided to test your shellcode on your local machine. selftest will only check the length limitation and your shellcode is working or not, with sample test data. Run './selftest' for more information.
  * **payload_for_test** A sample working payload. But not keeps the restrictions.
  * **samples and testData** Test data
  * **validate.py** Test data validator. Just run 'python2 validate.py'
  * **readme.md** It's me :)
