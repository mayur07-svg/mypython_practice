import tkinter
from tkinter import *
root = tkinter.Tk()

root.title("welcome")
# btn1 = Button(root,text="button1")
# btn2 = Button(root,text="button2")
# btn3 = Button(root,text="button3")
# btn1.grid(row=0,column=0)
# btn2.grid(row=0,column=1)
# btn3.grid(row = 0,column= 2)

root.geometry("500x600") # here noted that , must be use "x" not use "*"
root.configure(bg="light blue")

"""# dropdown menu
options = ["pyhton","java","c++","c#","js"]
selected_option = StringVar()
selected_option.set(options[0])

# creating dropdown
dropdown = OptionMenu(root,selected_option,*options)
dropdown.pack(pady=20)
"""


# radio box

"""v_radiobox = IntVar()
Radiobutton(root,text = "male",variable=v_radiobox,value=1).pack()
Radiobutton(root,text = "female",variable=v_radiobox,value=2).pack()"""

# new_box = Radiobutton(root,text = "male",variable=v_radiobox,value=1)
# new_box.pack()


#message box

"""from tkinter import messagebox
messagebox.showinfo("new message","hello now we are learning tkinter")
messagebox.showerror("error","please check !")
messagebox.showwarning("warning","virus in your sysem !")"""

#entry widget
"""
new_widget = Entry(root,font=("verdana",15))
new_widget.pack(ipadx=10,ipady=10)
new_widget.pack(ipadx=10,pady=100)"""


#listbox

'''Scrollbar1 = Scrollbar(root)
Scrollbar1.pack(side=RIGHT,fill=Y)

scroll_list = Listbox(root,font=("arial",15),height=5)
scroll_list.pack(padx=10,pady=10,ipadx=10,ipady=10)

scroll_list.config(yscrollcommand=Scrollbar1.set)
Scrollbar1.config(command=scroll_list.yview) 

for i in range(50):
    scroll_list.insert(i,i)'''




# text widget

'''import tkinter as tk
from tkinter import *
root =Tk()

text_widget = tk.Text(root, height=5, width=40)
text_widget.pack()
'''

# 2

'''import tkinter
from tkinter import *
root = tkinter.Tk()

text_widget = tkinter.Text(root, height=5, width=40)
text_widget.pack()

root.mainloop()'''

'''frame  = tkinter.Frame(root)
frame.pack()
b1 = Button(frame,text="button1")
b1.pack()


root.mainloop() 
'''

Label = Label(root,text="select")
Label.pack()
list_b0x = Listbox(root)

for i in range(1,51):
    list_b0x.insert(i,i)

list_b0x.pack()

msg = Message(root, text="Thanks for trying this app! Submit below to see your data.", width=300)
msg.pack(pady=10)

root.mainloop()
 








    