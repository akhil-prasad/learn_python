from tkinter import *
home=Tk()
home.title('home')
home.geometry('600x500')


l=Label(home,text='user_name')
l.place(x=200,y=300)

txt=Entry(home,textvariable=' ')
txt.place(x=400, y=300)

def click():
    g=txt.get()
    print(g)
    print(l)

b=Button(home,text='Click Here',command=click)
b.place(x=300,y=400)



home.mainloop()