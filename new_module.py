import tkinter
from tkinter import *

root = tkinter.Tk()
root.geometry("400x400")
root.configure(bg="red")
f1 = tkinter.Frame(root)
f1.pack()
b1 = Button(f1,text="b1")
b2 = Button(f1,text="b2")
b3 = Button(root,text="b3")
b1.pack(side=RIGHT)
b2.pack(side=LEFT)
b3.pack(fill="y")
root.mainloop()
