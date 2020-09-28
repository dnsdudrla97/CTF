testData = open("testData").read().strip().split('\n')
testData = [e.split(', ') for e in testData]

for fn, ans in testData:
	testVector = open(fn).read().strip().split('\n')
	expectedVal = sum([int(a) * int(b) for a, b in zip(testVector[::2], testVector[1::2])])
	expectedVal = expectedVal // 100
	
	if expectedVal != int(ans):
		print ("Validation Failed!")
		print ((expectedVal, ans))
		break
else:
	print ("Validation Success!")
