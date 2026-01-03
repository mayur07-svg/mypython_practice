import tkinter
from tkinter import *

root = tkinter.Tk()

root.title("event")
root.geometry("600x600")
btn1 = Button(root,text="click me",font="arial")
btn1.pack()

def entered(event):

btn1.bind("<button>",entered)


root.mainloop