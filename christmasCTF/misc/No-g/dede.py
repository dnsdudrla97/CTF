# lo = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'D'}
lo = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'D':'6'}

data = [
'D','E','D','E','D','D','D','C',
'E','B','D','C','D','C','D','E',
'B','E','D','D','E','D','E','D',
'E','D','D','D','E','D','D','D',
'E','D','D','D','D','B','E','E',
'B','B','D','D','D','D','D','D',
'D','D','D','D','D','E','D','C',
'D','D','D','A','B','A','A','A',
'B','A','A','A','B','A','B','A',
'C','D','C','A','B','B','D','B',
'C','C','A','B','B','A','B','B',
'B','A','B','B','A','A','A','B',
'C','C','B','E','C','E','D','B',
'B','C','C','D','D','C','C','A',
'D','B','A','D','D','C','B','E',
'B','B','A','B','E','B','C','D',
'C','D','A','C','A','D','E','B',
'B','D','B','D','D','D','D','D',
'B','D','D','C','C','D','D','D',
'E','B','A','B','E','B','C','C',
'A','A','B','A','B','A','A','D',
'B','D','C','C','B','A','B','B',
'A','C','B','C','D','D','E','D',
'D','E','D','E']


result = [lo[x] for x in data]

print(result)