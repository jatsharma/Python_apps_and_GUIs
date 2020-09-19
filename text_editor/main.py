from tkinter import *
from tkmacosx import Button
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfile
import os

root = Tk()
root.title('Notepad')
root.geometry("644x788")

# Add text area
TextArea = Text(root)
file = None
TextArea.pack(expand=True, fill=BOTH)


def new_file():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def open_file():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All types", "*.*"),
                                      ("Text Documents", "*.txt")
                                      ])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(0.1, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def save_file():
    global file
    if file == None:
        file = asksaveasfile(initialfile='Untitled.txt', defaultextension=".txt",
                             filetypes=[("All types", "*.*"),
                                        ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + "-Notepad")

    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def cut():
    TextArea.event_generate("<<Cut>>")


def copy():
    TextArea.event_generate("<<Copy>>")


def paste():
    TextArea.event_generate("<<Paste>>")


def about():
    showinfo("Notepad", "Notepad by Jatin")


# Create a menu

MenuBar = Menu(root)
root.config(menu=MenuBar)
# File menu starts
FileMenu = Menu(MenuBar)
MenuBar.add_cascade(label="File", menu=FileMenu)
FileMenu.add_command(label="New", command=new_file)
FileMenu.add_command(label="Open", command=open_file)
FileMenu.add_command(label="Save", command=save_file)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=lambda: exit())

# File menu ends
# Edit menu starts
EditMenu = Menu(MenuBar)
MenuBar.add_cascade(label="Edit", menu=EditMenu)
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)

# Edit menu ends
HelpMenu = Menu(MenuBar)
MenuBar.add_cascade(label="Help", menu=HelpMenu)
HelpMenu.add_command(label="About Notepad", command=about)

Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()
