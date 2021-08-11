from tkinter import *
top=Tk()
mb=Menubutton(top,text='MENU')
mb.grid()
mb.menu=Menu(mb, tearoff=0)
mb['menu']=mb.menu
cVar=IntVar()
aVar=IntVar()

mb.menu.add_checkbutton (label='home',variable=cVar)
mb.menu.add_checkbutton (label='profile',variable=aVar)

mb.pack()
top.mainloop()