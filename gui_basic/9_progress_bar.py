import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("test")
root.geometry("640x480")

#p = ttk.Progressbar(root, maximum=100, mode="indeterminate")    # indeterminate = 값을 정하지 않아 언제 끝날지 모름
# p = ttk.Progressbar(root, maximum=100, mode="determinate")
# p.start(10) # 10ms 마다 움직임
# p.pack()

# def cmd():
#     p.stop()

# b1 = Button(root,text="click",command=cmd)
# b1.pack()

pVar = DoubleVar()
p = ttk.Progressbar(root,maximum=100,length=150, variable=pVar)
p.pack()

def cmd():
    for i in range(1, 101):
        time.sleep(0.01)
        pVar.set(i)
        p.update()
        print(pVar.get())


b1 = Button(root,text="click",command=cmd)
b1.pack()

root.mainloop()