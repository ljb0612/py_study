from cProfile import label
from tkinter import *

root = Tk()
root.title("test")
root.geometry("640x480")

label1 = Label(root,text="hi")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root,image=photo)
label2.pack()

def change():
    label1.config(text="hello")

    global photo2
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()


root.mainloop()