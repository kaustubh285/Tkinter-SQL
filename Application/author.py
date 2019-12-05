from tkinter import *
import sqlite3

window=Tk()

def add():
    name=e1_value.get()
    dob=e2_value.get()
    gender=e3_value.get()
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Character VALUES(?,?,?)",(name,dob,gender,))
    conn.commit()
    conn.close()

def update():
    name=e1_value.get()
    dob=e1_value.get()
    gender=e1_value.get()
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("UPDATE Character SET Name=? WHERE DOB=?",(name,dob,))
    conn.commit()
    conn.close()

def delete():
    name=e1_value.get()
    dob=e1_value.get()
    gender=e1_value.get()
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Character WHERE Name=?",(name,))
    conn.commit()
    conn.close()

def display():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Character")
    rows=cur.fetchall()
    lb1.delete(0,END)
    conn.close()
    print(rows)
    for items in rows:
        lb1.insert(END,items)


#Create TABLE
conn=sqlite3.connect("data.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Characte(Name TEXT, DOB TEXT ,Gender TEXT) ")
conn.commit()
conn.close()

l1=Label(window,text="Name:")
l1.grid(row=1,column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value )
e1.grid(row=1,column=1)

l2=Label(window,text="Born:")
l2.grid(row=1,column=2)

e2_value=StringVar()
e2=Entry(window, textvariable=e2_value )
e2.grid(row=1,column=3)

l3=Label(window,text="Gender:")
l3.grid(row=2,column=0)

e3_value=StringVar()
e3=Entry(window, textvariable=e3_value )
e3.grid(row=2,column=1)

b1=Button(window, text="View All", command=display, width = 15)
b1.grid(row=3,column=0)

b1=Button(window, text="Add Character", command=add, width = 15)
b1.grid(row=4,column=0)

b1=Button(window, text="Remove Character", command=delete, width = 15)
b1.grid(row=5,column=0)

b1=Button(window, text="Update Char Info", command=update, width = 15)
b1.grid(row=6,column=0)

b1=Button(window, text="Close", width = 15)
b1.grid(row=7,column=0)

lb1=Listbox(window ,width= 75)
lb1.grid(row=3,column=1, rowspan= 5, columnspan= 5)

sb1=Scrollbar(window)
sb1.grid(row=3, column=6, rowspan=5, columnspan= 1)

lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

window.mainloop()
