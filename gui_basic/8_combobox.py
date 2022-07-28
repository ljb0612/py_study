import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("test")
root.geometry("640x480")

val = [str(i) + "day" for i in range(1,32)]
cb = ttk.Combobox(root,height=15,values=val)
cb.pack()
cb.set("list")

cb2 = ttk.Combobox(root,height=15,values=val,state="readonly")
cb2.current(0)
cb2.pack()


def cmd():
    print(cb.get())
    print(cb2.get())

b1 = Button(root,text="click",command=cmd)
b1.pack()

root.mainloop()