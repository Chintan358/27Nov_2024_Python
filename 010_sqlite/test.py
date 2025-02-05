from sqlite3 import *


db = connect("data.db")
# db.execute("create table student(id int primary key,name varchar(20),email varchar(50))")
# db.execute("insert into student values(5,'Nisha','nisha@gmail.com')")
# db.execute("update student set email='nisha@yahoo.com' where id=5")
# db.execute("delete from student where id=5")
# db.commit()

# data = db.execute("select * from student")



# for i in data.fetchall():
#     for k in i:
#         print(k,end=" ")
#     print()