from tkinter import *

window=Tk()

def calc():
    grams=int(e1_value.get())*1000
    pounds=int(e1_value.get())*2.2046
    ounces=int(e1_value.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END,grams)
    t2.delete("1.0",END)
    t2.insert(END,pounds)
    t3.delete("1.0",END)
    t3.insert(END,ounces)

b1=Button(window, text="Convert", command=calc)
b1.grid(row=2,column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value )
e1.grid(row=0,column=0)

e2=Label(window,text="Kg")
e2.grid(row=0,column=1)

t1=Text(window, height=1,width=14)
t1.grid(row=1,column=0)

l1=Label(window,text="grams")
l1.grid(row=1,column=1)

t2=Text(window, height=1,width=14)
t2.grid(row=1,column=2)

l2=Label(window,text="pounds")
l2.grid(row=1,column=3)


t3=Text(window, height=1,width=14)
t3.grid(row=1,column=4)

l3=Label(window,text="ounces")
l3.grid(row=1,column=5)

window.mainloop()
