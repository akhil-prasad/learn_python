from tkinter import *
root=Tk()
frame= Frame(root)
frame.pack()

bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)

rbutton=Button(frame,text='red',fg='red')
rbutton.pack(side=LEFT)

bbutton=Button(frame,text='blue',fg='blue')
bbutton.pack(side=LEFT)

gbutton=Button(frame,text='green',fg='green')
gbutton.pack(side=LEFT)

Blackbutton=Button(bottomframe,text='black',fg='black')
Blackbutton.pack(side=BOTTOM)

root.mainloop()



