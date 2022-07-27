from cProfile import label
from tkinter import *

root = Tk()
root.title("test")
root.geometry("640x480")

list = Listbox(root,selectmode="extended",height=0)
list.insert(0,"apple")
list.insert(1,"straw")
list.insert(2,"banana")
list.insert(END,"melon")
list.insert(END,"grape")
list.pack()


def cmd():
    #list.delete(0)
    #print(list.size())
    #print(list.get(0,2))
    print(list.curselection())

b1 = Button(root,text="click",command=cmd)
b1.pack()

root.mainloop()