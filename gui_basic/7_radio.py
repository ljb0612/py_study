from cProfile import label
from logging.config import valid_ident
from msilib.schema import CheckBox
from tkinter import *

root = Tk()
root.title("test")
root.geometry("640x480")

label1 = Label(root, text="select").pack()

rVar1 = IntVar()
r1 = Radiobutton(root, text="a",value=1,variable=rVar1)
r2 = Radiobutton(root, text="b",value=2,variable=rVar1)
r3 = Radiobutton(root, text="c",value=3,variable=rVar1)
r1.select()
r1.pack()
r2.pack()
r3.pack()

label2 = Label(root, text="select2").pack()
rVar2 = StringVar()
r4 = Radiobutton(root,text="dd",value="ddd",variable=rVar2)
r5 = Radiobutton(root,text="ee",value="eee",variable=rVar2)
r6 = Radiobutton(root,text="ff",value="fff",variable=rVar2)
r4.select()
r4.pack()
r5.pack()
r6.pack()


def cmd():
    print(rVar1.get())
    print(rVar2.get())

b1 = Button(root,text="click",command=cmd)
b1.pack()

root.mainloop()