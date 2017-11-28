from Tkinter import *
import Tkinter as ttk
import Tkinter as tk
from ttk import *
from tkFont import Font
import tkMessageBox
import os

root = Tk()
text = tk.Text(root)


root.title("Welcome to the Nestor Analytics")
root.geometry("500x500")

def view():
    f=open("try.html","w")
    f.write("Name: "+h.get())
    f.close()
    f = open('try.html','r')
    print f.read()	    	
    f.close()


h=StringVar()
v=StringVar()
w=StringVar()
y=StringVar()
t=StringVar()
r=StringVar()
s=StringVar()
a=StringVar()
  
root1 = Frame(root)
root1.pack(pady = 100, padx = 100)
root.configure(background='lightgreen')

profession = [
"Menu",
"Teacher",
"Principal",
"Headmaster",
"Academic Head"
] 

label_1=Label(root1,text="Name")
label_3=Label(root1,text="Email")
label_4=Label(root1,text="Class")
label_5=Label(root1,text="Address")
label_6=Label(root1,text="City")
label_7=Label(root1,text="School Name")
label_8=Label(root1,text="Subject")

label_1.grid(row=0,column=0)
#label_2.grid(row=1,sticky=E)
label_3.grid(row=2,column=0)
label_4.grid(row=3,column=0)
label_5.grid(row=4,column=0)
label_6.grid(row=5,column=0)
label_7.grid(row=6,column=0)
label_8.grid(row=7,column=0)


entry_1=Entry(root1,textvariable=h,width=100)
#entry_2=Entry(root)
entry_3=Entry(root1,textvariable=r,width=100)
entry_4=Entry(root1,textvariable=w,width=100) 
entry_5=Entry(root1,textvariable=t,width=100)
entry_6=Entry(root1,textvariable=y,width=100)
entry_7=Entry(root1,textvariable=s,width=100)
entry_8=Entry(root1,textvariable=a,width=100)

entry_1.grid(row=0,column=1,)
#entry_2.grid(row=1,column=1)
entry_3.grid(row=2,column=1,)
entry_4.grid(row=3,column=1)
entry_5.grid(row=4,column=1)
entry_6.grid(row=5,column=1)
entry_7.grid(row=6,column=1)
entry_8.grid(row=7,column=1)
# on change dropdown value
myFont = Font(family="Times New Roman", size=15)
text.configure(font=myFont)

e=Entry(root,textvariable=v)

    #etc
    
variable = StringVar(root)
variable.set(profession[0]) # default value

w = OptionMenu(root, variable,'choose profession', *profession)
w.grid(row=2,column=1)
w.pack()


def ok():
    print ("value is:" + variable.get())
    print(v.get())
    print(h.get())
    print(r.get())
    print(t.get())
    print(y.get())
    print(variable.get())
    
button = Button(root, text="submit", command=ok)
button.pack()    
button1= Button(root,text="print",command=view)
button1.pack()
root.mainloop()
