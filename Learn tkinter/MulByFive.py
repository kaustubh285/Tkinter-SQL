from tkinter import *

window=Tk()

def calc():
    ans=int(e1_value.get())*5
    t1.insert(END,ans)

b1=Button(window, text="Submit", command=calc)
b1.grid(row=1,column=1)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value )
e1.grid(row=1,column=0)

t1=Text(window, height=1,width=20)
t1.grid(row=1,column=2)

window.mainloop()
