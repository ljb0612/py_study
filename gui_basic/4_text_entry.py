from cProfile import label
from tkinter import *

root = Tk()
root.title("test")
root.geometry("640x480")

txt = Text(root,  width=30, height=5)
txt.pack()

txt.insert(END, "asdkpwkdpwqdjpqwjdkpwd")

# 한줄 입력받을때
e = Entry(root, width=30)
e.pack()
e.insert(0,"sdowodw")

def cmd():
    print(txt.get("1.0",END))
    print(e.get())
    txt.delete("1.0",END)
    e.delete(0, END)

b1 = Button(root,text="click",command=cmd)
b1.pack()

root.mainloop()