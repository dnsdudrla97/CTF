note = ['fa', 'mi', 'fa', 'mi', 'fa', 'fa'
, 're', 'do', 'mi', 'ti', 'fa', 'do'
, 'fa', 'do', 're', 'mi', 'ti'
, 'mi', 'fa', 're', 'mi', 're', 'mi'
, 're', 'mi', 'fa', 're', 're', 'mi', 're', 're', 'fa'
, 'mi', 're', 'fa', 're'
, 'fa', 'ti', 'mi', 'mi', 'ti', 'ti', 'fa', 're'
, 'fa', 'fa', 're', 'fa', 'fa', 're', 'fa'
, 're', 'fa', 'mi', 'fa', 'do', 'fa', 'fa', 'fa'
, 'la', 'ti', 'la', 'la', 'la'
, 'ti', 'la', 'la', 'la', 'ti', 'la', 'ti', 'la', 'do'
, 're', 'do', 'la', 'ti', 'ti', 're', 'ti', 'do', 'do'
, 'la', 'ti', 'ti', 'la', 'ti'
, 'ti', 'ti', 'la', 'ti', 'ti', 'la', 'la', 'la', 'ti'
, 'do', 'do', 'ti', 'mi', 'do', 'mi', 're', 'ti', 'ti'
, 'do', 'do', 're', 'fa', 'do', 'do', 'la', 'mi', 'ti'
, 'la', 're', 're', 'do', 'ti', 'mi', 'ti', 'ti'
, 'la', 'ti', 'mi', 'ti', 'do', 're'
, 'do', 're', 'la', 'do', 'la', 're', 'mi', 'ti'
, 'ti', 'mi', 'ti', 'fa', 're', 'fa', 're', 're'
, 'ti', 'fa', 'fa', 'do', 'do', 'fa', 'fa', 'fa'
, 'mi', 'ti', 'la', 'ti', 'mi', 'ti', 'do', 'do'
, 'la', 'la', 'ti', 'la', 'ti', 'la', 'la'
, 'fa', 'ti', 're', 'do'
, 'do', 'ti', 'la', 'ti', 'ti', 'la', 'do', 'ti'
, 'do', 're', 'fa', 'mi', 're', 'fa', 'mi', 'fa', 'mi']

idx = [6, 6, 5, 6, 9
, 4, 8, 7, 8, 5
, 9, 9, 5, 9
, 9, 9, 8, 6
, 8, 8, 8, 8
, 7, 4, 8, 9]

flag = []

pre_chk = 0

while(len(flag) < len(idx)):
	cur_chk = idx[len(flag)]
	buf = note[pre_chk:pre_chk+cur_chk]
	result = 0
	
	for i in range(len(buf)):
		 if(buf[i] == 'la'):
		 	result += 0xa
		 elif(buf[i] == 'ti'):
		 	result += 0xb
		 elif(buf[i] == 'do'):
		 	result += 0xc
		 elif(buf[i] == 're'):
		 	result += 0xd
		 elif(buf[i] == 'mi'):
		 	result += 0xe
		 elif(buf[i] == 'fa'):
		 	result += 0xf
			
	flag.append(chr(result))
	print(''.join(flag))
	pre_chk += cur_chk