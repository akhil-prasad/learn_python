from tkinter import *
top=Tk()
top.title('LOGIN PAGE')
top.geometry('500x500')

l= Label(top,text='User Name')
l.place(x=100,y=200)

txt=Entry(top, text=" ")
txt.place(x=300, y=200)

def click():
    
    n =txt.get()
    print('password:',n)
    print('LOGGING IN')

b=Button(top,text='LOGIN',command=click)

b.place(x=250,y=300)

top.mainloop()
