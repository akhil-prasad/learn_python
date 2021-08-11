from tkinter import *
top=Tk()
top.title('LOGIN PAGE')
top.geometry('500x500')

s=Canvas(top,width=400,height=500)
s.create_line(15, 25, 200, 25)
s.create_line(15, 250, 200, 250)
s.create_line(15, 25, 15, 250)
s.create_line(200, 25, 200, 250)
s.pack()



top.mainloop()