import mysql.connector as sq
myconn=sq.connect(user='root',host='localhost',password='password')
cur=myconn.cursor()
def listdenewala():
    l=[]
    cur.execute('''show databases''')
    c=cur.fetchall()
    for i in c:
        print(i)
        l.append(i[0])
    return l
p=listdenewala()
print(p)

def deletekarnawala(n):

    cur.execute(f"drop database {n}")
for i in p:
   try:
    deletekarnawala(i)
   except:
       pass
p=listdenewala()
print(p)
