from tkinter import *
import sqlite3

def add():
    name=e1_value.get()
    walkers=e2_value.get()
    team=e3_value.get()
    conn=sqlite3.connect("survive.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO twd VALUES(?,?,?)",(name,walkers,team,))
    conn.commit()
    conn.close()

#Update data
def update():
    name=e1_value.get()
    walkers=e2_value.get()
    team=e3_value.get()
    conn=sqlite3.connect("survive.db")
    cur=conn.cursor()
    cur.execute("UPDATE twd SET walkers=? WHERE name=?",(walkers,name,))
    conn.commit()
    conn.close()
    display()

#delete using name
def delete():
    name=e1_value.get()
    walkers=e1_value.get()
    team=e1_value.get()
    conn=sqlite3.connect("survive.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM twd WHERE Name=?",(name,))
    conn.commit()
    conn.close()
    display()

#display full TABLE
def display():
    conn=sqlite3.connect("survive.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM twd")
    rows=cur.fetchall()
    lb1.delete(0,END)
    lb2.delete(0,END)
    lb3.delete(0,END)
    for items in rows:
        lb1.insert(END,items[0])
        lb2.insert(END,items[1])
        lb3.insert(END,items[2])

def update_selected():
    index=lb1.curselection()[0]
    selected_name=lb1.get(index)
    selected_walkers=lb2.get(index)
    selected_team=lb3.get(index)
    print(selected_name)
    e2_value=selected_walkers
    e3_value=selected_team

#Get Selected1
def get_selected1():
    index=lb1.curselection()[0]
    selected_name=lb1.get(index)
    selected_walkers=lb2.get(index)
    selected_team=lb3.get(index)
    row=(selected_name,selected_walkers,selected_team)
    e1_value=selected_name
    e2_value=selected_walkers
    e3_value=selected_team
    return(row)

def delete_selected():
    name=get_selected1()[0]
    walkers=get_selected1()[1]
    team=get_selected1()[2]
    conn=sqlite3.connect("survive.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM twd WHERE Name=?",(name,))
    conn.commit()
    conn.close()
    display()


#Create TABLE
conn=sqlite3.connect("survive.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS twd(name TEXT, walkers TEXT ,team TEXT) ")
conn.commit()
conn.close()

window=Tk()
window.wm_title("The Walking Dead")

l1=Label(window,text="Name:")
l1.grid(row=1,column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value )
e1.grid(row=1,column=1)

l2=Label(window,text="Walkers killed:")
l2.grid(row=1,column=2)

e2_value=StringVar()
e2=Entry(window, textvariable=e2_value )
e2.grid(row=1,column=3)

l3=Label(window,text="Team:")
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

b1=Button(window, text="Delete selected", width = 15, command=delete_selected)
b1.grid(row=7,column=0)

b1=Button(window, text="Update selected", width = 15, command=update_selected)
b1.grid(row=8,column=0)

b1=Button(window, text="Close", width = 15, command=window.destroy)
b1.grid(row=9,column=0)

l4=Label(window,text="Name:")
l4.grid(row=3,column=1)

lb1=Listbox(window ,width= 25)
lb1.grid(row=4,column=1, rowspan= 5, columnspan= 1)

l4=Label(window,text="Number of Walkers killed:")
l4.grid(row=3,column=2)

lb2=Listbox(window ,width= 25)
lb2.grid(row=4,column=2, rowspan= 5, columnspan= 1)

l4=Label(window,text="Team:")
l4.grid(row=3,column=3)

lb3=Listbox(window ,width= 25)
lb3.grid(row=4,column=3, rowspan= 5, columnspan= 1)

sb1=Scrollbar(window)
sb1.grid(row=3, column=6, rowspan=5, columnspan= 1)

lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

lb1.bind('<<listboxSelect>>',get_selected1)

window.mainloop()
