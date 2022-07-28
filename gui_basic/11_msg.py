import tkinter.messagebox as msg
from tkinter import *

root = Tk()
root.title("test")
root.geometry("640x480")

def cmd():
    msg.showinfo("tt","test")

def warn():
    msg.showwarning("warning","조심해")

def error():
    msg.showerror("error","종료헤")

def okcancel():
    msg.askokcancel("확인 / 취소", "어쩔래?")

def retrycancel():
    msg.askretrycancel("재시도/취소","어쩔래?")

def yesno():
    msg.askyesno("예/아니오","ㅋㅋㅋㅋ")

def btn_3():
    res = msg.askyesnocancel(title=None,message="akdwjdwldjkalsjdasd")
    print(res)
    if res==1:
        print("네")
    elif res==0:
        print("아니오")
    else:
        print("취소")

Button(root, command=cmd, text="click").pack()
Button(root, command=warn, text="click2").pack()
Button(root, command=error, text="click3").pack()
Button(root, command=okcancel, text="click4").pack()
Button(root, command=retrycancel, text="click5").pack()
Button(root, command=yesno, text="click6").pack()
Button(root, command=btn_3, text="click7").pack()

root.mainloop()