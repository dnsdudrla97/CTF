import haslib, string, random

payload = 'touch'
for i in range(0, 10000):
    payload += ' '
    payload +=''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(8))
    payload += str(i)