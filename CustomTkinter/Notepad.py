import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox as messagebox

window = ctk.CTk()
window.geometry("644x400")
window.title("Notepad")

file = None

def newfile():
    global file
    window.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, tk.END)  # Clear the text area

def openfile():
    global file
    pass

def savefile():
    pass

def exitfile():
    window.quit()

# Function to cut text
def cut():
    textarea.event_generate(("<<Cut>>"))

# Function to copy text
def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    messagebox.showinfo("Notepad", "Notepad by Naman")

menubar = tk.Menu(window)  # Create menu object 'menubar'
window.config(menu=menubar)  # Set 'menubar' as the main menu bar

# File menu
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exitfile)

# Edit menu
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)

# Help menu
helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

scrollbar = ctk.CTkScrollbar(window)
scrollbar.pack(side="right", fill="y")

textarea = ctk.CTkTextbox(window, font=("Arial", 13), yscrollcommand=scrollbar.set)
textarea.pack(side="left", fill="both", expand=True)
scrollbar.configure(command=textarea.yview)

window.mainloop()