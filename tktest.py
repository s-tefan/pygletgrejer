from math import *
from tkinter import *
root = Tk()
w=Label(root,text="Hello, world!")
w.pack()
c=Canvas(root,width=400,height=400)
c.pack()
c.create_rectangle(0, 0, 400, 400, fill="yellow")
c.pack()
root.mainloop()
