from tkinter import *

root = Tk()
root.title("test")
root.geometry("640x480")

def create_new_file():
    print("Create New File")

m = Menu(root)

m_file = Menu(m,tearoff=0)
m_file.add_command(label="new file", command=create_new_file)
m_file.add_command(label="new window")
m_file.add_separator()
m_file.add_command(label="open files..")
m_file.add_separator()
m_file.add_command(label="save all", state="disable")
m_file.add_separator()
m_file.add_command(label="exit", command=root.quit)

m.add_cascade(label="file",menu=m_file)

m.add_cascade(label="edit")

m_lang = Menu(m,tearoff=0)
m_lang.add_radiobutton(label="a")
m_lang.add_radiobutton(label="b")
m_lang.add_radiobutton(label="c")
m.add_cascade(label="Language",menu=m_lang)

# checkbox
m_ck = Menu(m,tearoff=0)
m_ck.add_checkbutton(label="aa")
m.add_cascade(label="view",menu=m_ck)

root.config(menu=m)
root.mainloop()