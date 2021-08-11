from tkinter import *
top=Tk()
top.title('LOGIN PAGE')
top.geometry('500x500')

var1=IntVar()
Checkbutton(top,text='male',variable=var1).grid(row=0,sticky= E)

var2=IntVar()
Checkbutton(top,text='female',variable=var2).grid(row=1,sticky=E)

def click():
    v1=var1.get()
    print(v1)
    v2=var2.get()
    print(v2)

       

b=Button(top,text='LOGIN',command=click)

b.place(x=250,y=300)

top.mainloop()

