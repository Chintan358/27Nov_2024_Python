import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import messagebox,ttk



root = Tk()
root.geometry("800x500")

def show():
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="27nov_pyython")
    mycursor = mydb.cursor()
    mycursor.execute("select * from users")
    records = mycursor.fetchall()
    for i, (id,uname,email,phone) in enumerate(records,start=1):
        table.insert("","end",values=(id,uname,email,phone))










global e1
global e2
global e3
global e4


Label(root,text="User Registration", font=(None,25)).place(x=250,y=10)
Label(root,text="Id").place(x=250,y=70)
Label(root,text="Username").place(x=250,y=100)
Label(root,text="Email").place(x=250,y=130)
Label(root,text="Phone").place(x=250,y=160)

e1 = Entry(root)
e1.place(x=350,y=70)


e2 = Entry(root)
e2.place(x=350,y=100)

e3 = Entry(root)
e3.place(x=350,y=130)

e4 = Entry(root)
e4.place(x=350,y=160)


Button(root,text="Add",width=7).place(x=250,y=190)
Button(root,text="Update",width=7).place(x=330,y=190)
Button(root,text="Delete",width=7).place(x=410,y=190)

cols = ("Id","Username","Email","Phone")
table = ttk.Treeview(root,columns=cols,show="headings")
for col in cols:
    table.heading(col,text=col)
    table.place(x=10,y=250)

show()
root.mainloop()

