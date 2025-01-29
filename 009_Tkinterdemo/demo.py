from tkinter import *

top = Tk()
top.geometry("500x500")

# btn1 = Button(top,text="Red", fg="red")
# btn1.pack(side=LEFT)

# btn2 = Button(top,text="White", fg="white")
# btn2.pack(side=RIGHT)

# btn3 = Button(top,text="Blue", fg="blue")
# btn3.pack(side=TOP)

# btn4 = Button(top,text="Green", fg="green")
# btn4.pack(side=BOTTOM)


# l1 = Label(top,text="Username")
# l1.grid(row=1,column=1)

# l2 = Label(top,text="Email")
# l2.grid(row=2,column=1)

# l3 = Label(top,text="Phone")
# l3.grid(row=3,column=1)

# e1 = Entry(top)
# e1.grid(row=1,column=2)

# e2 = Entry(top)
# e2.grid(row=2,column=2)


# e3 = Entry(top)
# e3.grid(row=3,column=2)


# btn = Button(top,text="Submit")
# btn.grid(row=4,column=2)


l1 = Label(top,text="Username")
l1.place(x=100,y=100)

l2 = Label(top,text="Email")
l2.place(x=100,y=150)

l3 = Label(top,text="Phone")
l3.place(x=100,y=200)

e1 = Entry(top)
e1.place(x=200,y=100)

e2 = Entry(top)
e2.place(x=200,y=150)


e3 = Entry(top)
e3.place(x=200,y=200)


btn = Button(top,text="Submit",width=15)
btn.place(x=200,y=250)

top.mainloop()