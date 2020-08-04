#import statements
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
import datetime

#Intro
root = Tk()
root.geometry("600x400")
root.title("Untitled-Notepad")
root.wm_iconbitmap("notepad.ico")

#Functions
def newfile():
    global file
    root.title("Untitled-Notepad")
    file = None
    textarea.delete(1.0,END)

def openfile():
    global file
    file = askopenfilename(defaultextension = ".txt",filetypes = [("All Files", "*.*"),("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        fullname = os.path.basename(file)
        root.title(fullname[:fullname.rfind(".")]+"-Notepad")
        textarea.delete(1.0,END)
        f = open(file, "r")
        textarea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file == None:
        saveasfile()
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0,END))
        f.close()

def saveasfile():
    global file
    file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = ".txt",filetypes = [("All Files", "*.*"),("Text Documents", "*.txt")])
    f = open(file, "w")
    f.write(textarea.get(1.0,END))
    f.close()
    fullname = os.path.basename(file)
    root.title(fullname[:fullname.rfind(".")]+"-Notepad")



def undo():
    textarea.event_generate("<<Undo>>")

def redo():
    textarea.event_generate("<<Redo>>")

def cut():
    textarea.event_generate("<<Cut>>")

def copy():
    textarea.event_generate("<<Copy>>")

def paste():
    textarea.event_generate("<<Paste>>")

def delete():
    textarea.delete(1.0,END)

def selectall():
    textarea.event_generate("<<SelectAll>>")

def knowtime():
    textarea.insert(INSERT,datetime.datetime.now().strftime("%H:%M %d-%m-%Y"))


def viewhelp():
    showinfo("Notepad","This notepad is so simple why u need help?")

def about():
    showinfo("Notepad","Notepad By Vedant")

#Designing
mainmenu = Menu(root)

submenu1 = Menu(mainmenu, tearoff = 0)
submenu1.add_command(label = "New", command = newfile)
submenu1.add_command(label = "Open", command = openfile)
submenu1.add_command(label = "Save", command = savefile)
submenu1.add_command(label = "Save As", command = saveasfile)
submenu1.add_separator()
submenu1.add_command(label = "Exit", command = quit)
root.config(menu = mainmenu)
mainmenu.add_cascade(label = "File", menu = submenu1)

submenu2 = Menu(mainmenu, tearoff = 0)
submenu2.add_command(label = "Undo", command = undo)
submenu2.add_command(label = "Redo", command = redo)
submenu2.add_separator()
submenu2.add_command(label = "Cut", command = cut)
submenu2.add_command(label = "Copy", command = copy)
submenu2.add_command(label = "Paste", command = paste)
submenu2.add_command(label = "Delete", command = delete)
submenu2.add_separator()
submenu2.add_command(label = "Select All", command = selectall)
submenu2.add_command(label = "Time/Date", command = knowtime)
root.config(menu = mainmenu)
mainmenu.add_cascade(label = "Edit", menu = submenu2)

submenu3 = Menu(mainmenu, tearoff = 0)
submenu3.add_command(label = "View Help", command = viewhelp)
submenu3.add_separator()
submenu3.add_command(label = "About Notepad", command = about)
root.config(menu = mainmenu)
mainmenu.add_cascade(label = "Help", menu = submenu3)

textarea = Text(root, undo = True, font = "lucida 14")
file = None
textarea.pack(expand = True, fill = BOTH)

scrollbar = Scrollbar(textarea)
scrollbar.pack(side = RIGHT, fill = Y)
scrollbar.config(command = textarea.yview)
textarea.config(yscrollcommand = scrollbar.set)

#Rungui
root.mainloop()