#SQLite 접속하기

import sqlite3
con = sqlite3.connect('c:/temp/userDB') #데이터베이스 지정(또는 연결)
cur =con.cursor() #연결 통로 생성 (쿼리문을 날린 통로)

#테이블 만들기
try :
    sql = "CREATE TABLE userTable(userID CHAR(10),userName CHAR(5),userAge INT);"
    cur.execute(sql)
except :
    pass

while True:
    userID = input('아이디-->')
    if userID =="":
        break
    userName = input('이름-->')
    userAge = input('나이-->')
    sql = "INSERT INTO userTable(userID,userName,userAge) VALUES('"
    sql += userID+ "','"+userName+ "',"+userAge+ ")"
    cur.execute(sql)

sql="INSERT INTO userTable VALUES('AAA','에이',21);"
cur.execute(sql)
sql="INSERT INTO userTable VALUES('BBB','비이',23);"
cur.execute(sql)
sql="INSERT INTO userTable VALUES('CCC','씨이',32);"
cur.execute(sql)

con.commit()

cur.close()
con.close() #데이터베이스 연결 종료
print('ok')