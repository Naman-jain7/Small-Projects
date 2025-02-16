import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.geometry("1400x600")
window.title("Registration Form")
window.minsize(300, 100)

def exit1():
    window.quit()

def abt():
    messagebox.showinfo(title="Welcome to authors", message="This is the demo for menu field")

def search(event):
    value = event.widget.get()  # gets the text entered by user
    if value == '':
        combo.configure(values=list_of_lang)  # combo['values'] syntax is prop of combobox widget which holds the dropdown list
    else:
        data = []
        for i in list_of_lang:
            if value.lower() in i.lower():
                data.append(i)
        combo.configure(values=data)

m = tk.Menu()  # creates menu object 'm'
window.config(menu=m)  # sets m as main menu bar
subm1 = tk.Menu(tearoff=0)  # creates submenu for File menu
subm2 = tk.Menu(tearoff=0)  # creates submenu for Options menu
# Prepare subm1 and subm2 with commands
subm1.add_command(label="New File", command=None)
subm1.add_command(label="Open", command=None)
subm1.add_separator()
subm1.add_command(label="Exit", command=exit1)
subm2.add_command(label="About", command=abt)

m.add_cascade(label="File", menu=subm1)
m.add_cascade(label="Options", menu=subm2)

# Title
l0 = ctk.CTkLabel(window,text="Registration Form", font=("arial", 20, "bold"), fg_color="lightblue", corner_radius=5)
l0.place(x=600, y=150)

# Entry
l1 = ctk.CTkLabel(window,text="First Name:", font=("arial", 10, "bold"))
l1.place(x=550, y=240)
fn = ctk.StringVar()  # variable to store input
e1 = ctk.CTkEntry(window,textvariable=fn, width=200)
e1.place(x=650, y=240)

l2 = ctk.CTkLabel(window,text="Last Name:", font=("arial", 10, "bold"))
l2.place(x=550, y=280)
ln = ctk.StringVar()
e2 = ctk.CTkEntry(window,textvariable=ln, width=200)
e2.place(x=650, y=280)

# OptionMenu
l3 = ctk.CTkLabel(window,text="Country:", font=("arial", 10, "bold"))
l3.place(x=550, y=320)
list = ["Nepal", "India", "Canada"]
var = ctk.StringVar()
menu = ctk.CTkOptionMenu(window, values=list, variable=var)
menu.place(x=650, y=320)
var.set("select country")

# RadioButton
l5 = ctk.CTkLabel(window,text="Gender:", font=("arial", 10, "bold"))
l5.place(x=550, y=400)
var_r = ctk.StringVar()
r1 = ctk.CTkRadioButton(window,text="Male", variable=var_r, value="Male")
r1.place(x=650, y=400)
r2 = ctk.CTkRadioButton(window,text="Female", variable=var_r, value="Female")
r2.place(x=750, y=400)

def write():
    first = fn.get()
    second = ln.get()
    cntry = var.get()
    gender = var_r.get()
    messagebox.showinfo(title="Welcome", message=f"Your full name is {first} {second} and you live in {cntry}. You are a {gender}.")

b1 = ctk.CTkButton(window,text="Signup", fg_color="red", text_color="white", command=write)
b1.place(x=500, y=450)
b2 = ctk.CTkButton(window,text="Quit", fg_color="red", text_color="white", command=exit1)
b2.place(x=650, y=450)
b3 = ctk.CTkButton(window,text="Login", fg_color="red", text_color="white", command=None)
b3.place(x=800, y=450)

list_of_lang = ["java", "python", "js", "c", "cpp", "ruby", "rust", "php", "django", "mysql"]
combo = ctk.CTkComboBox(window,values=list_of_lang)
combo.set('search')
combo.place(x=730, y=500)
combo.bind('<KeyRelease>', search)

window.mainloop()