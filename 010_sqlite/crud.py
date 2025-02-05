import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import *

def Getval(event):
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        row_id=listbox.selection()[0]
        select = listbox.set(row_id)
        e1.insert(0,select['id'])
        e2.insert(0,select['username'])
        e3.insert(0,select['email'])
        e4.insert(0,select['phone'])




def Add():
    id = e1.get()
    uname = e2.get()
    email = e3.get()
    phone = e4.get()

    mysqldb = mysql.connector.connect(host="localhost",user="root",password="root",database="13nov_python")
    mycursor=mysqldb.cursor()

    try : 
        sql = "insert into users(id,uname,email,phone)values(%s,%s,%s,%s)"
        val = (id,uname,email,phone)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information","User added successfully")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e1.focus_set()
        for i in listbox.get_children():
             listbox.delete(i)
        Show()

    except Exception as e:
        print(e)
        mysqldb.rollback
        mysqldb.close()


def Show():
    mysqldb = mysql.connector.connect(host="localhost",user="root",password="root",database="13nov_python")
    mycursor=mysqldb.cursor()
    mycursor.execute("select * from users")
    records = mycursor.fetchall()
    
    for i, (id,uname,email,phone) in enumerate(records,start=1):
        listbox.insert("","end",values=(id,uname,email,phone))
        mysqldb.close()



root  = Tk()
root.geometry("800x500")
global e1
global e2
global e3

tk.Label(root,text="User Registration", fg="black", font=(None,30)).place(x=400,y=5)

Label(root,text="Id").place(x=10,y=10)
Label(root,text="Username").place(x=10,y=40)
Label(root,text="Email").place(x=10,y=70)
Label(root,text="phone").place(x=10,y=100)

e1 = Entry(root)
e1.place(x=140,y=10)


e2 = Entry(root)
e2.place(x=140,y=40)


e3 = Entry(root)
e3.place(x=140,y=70)

e4 = Entry(root)
e4.place(x=140,y=100)

Button(root, text="Add", command=Add, height=3,width=13).place(x=30,y=130)
Button(root, text="Update", height=3,width=13).place(x=140,y=130)
Button(root, text="Delete", height=3,width=13).place(x=250,y=130)

cols =('id','username','email','phone')
listbox = ttk.Treeview(root,columns=cols,show="headings")

for col in cols:
    listbox.heading(col,text=col)
    listbox.place(x=10,y=200)

Show()
listbox.bind('<Double-Button-1>',Getval)
root.mainloop()