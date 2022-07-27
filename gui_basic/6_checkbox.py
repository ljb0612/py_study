from cProfile import label
from msilib.schema import CheckBox
from tkinter import *

root = Tk()
root.title("test")
root.geometry("640x480")

checkvar = IntVar()
ck = Checkbutton(root,text="test",variable=checkvar)
ck.select()
ck.deselect()
ck.pack()

checkvar2 = IntVar()
ck2 = Checkbutton(root, text="test2",variable=checkvar2)
ck2.pack()


def cmd():
    print(checkvar.get())
    print(checkvar2.get())

b1 = Button(root,text="click",command=cmd)
b1.pack()

root.mainloop()