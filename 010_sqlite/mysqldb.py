import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="27nov_pyython"
)

mycursor = mydb.cursor()

# qry = "create table users(id int primary key,username varchar(20),email varchar(50),phone varchar(15))"
# mycursor.execute(qry)

# qry = "insert into users values(1,'Ankit','ankit@gmail.com','4585859685')"
# mycursor.execute(qry)

# qry = "insert into users values(%s,%s,%s,%s)"
# val = (9,"Nisha","nisha@gmail.com","9685748585")
# mycursor.execute(qry,val)

# qry = "update users set username=%s where id=%s"
# val = ("sarfraz",7)
# mycursor.execute(qry,val)

# qry = "delete from users where id=%s"
# val = (7,)
# mycursor.execute(qry,val)

mydb.commit()


