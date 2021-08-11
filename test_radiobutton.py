from tkinter import *
top=Tk()
v=IntVar()
Radiobutton(top,text="male", variable=v, value=1).pack(anchor=W)
Radiobutton(top,text="female", variable=v, value=2).pack(anchor=W)
top.mainloop()
