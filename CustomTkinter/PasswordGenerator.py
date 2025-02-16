import customtkinter as ctk
import tkinter.messagebox as messagebox
import random

window=ctk.CTk()
window.geometry("1400x600")
window.title("MyApp")
# window.config(bg="navy")

def generate_password():
    password=''
    i1=n.get()
    i2=pno.get()
    i3=int(combo_var.get())
    n1=random.randint(2,len(i1))
    for i in range(n1):
        password = password + random.choice(i1)
    n2 = i3 - n1
    for i in range(n2):
        password=password+random.choice(i2)
    
    templist=list(password)
    random.shuffle(templist)
    password=''.join(templist)
    messagebox.showinfo("Congratulations",f"Your generated password is:  {password}. Do not share it with anyone!!")
    #return password

def reset():
    e1.delete(0,ctk.END)
    e2.delete(0,ctk.END)
    combo.set("Define the length")

def exit1():
    window.quit()

# Labels and Entry for entry
l0=ctk.CTkLabel(window, text="Password Generator", fg_color="spring green", font=("Arial",15,"bold"), corner_radius=10, text_color="black")
l0.place(x=650, y=200)
l1=ctk.CTkLabel(window, text="Enter your name:", fg_color="spring green", text_color="black", font=("Arial",12,"bold"), corner_radius=10)
l1.place(x=550, y=275)
n=ctk.StringVar()
e1=ctk.CTkEntry(window, textvariable=n, width=200, font=("Arial",12))
e1.place(x=800,y=275)
l2=ctk.CTkLabel(window, text="Enter your Phone No. :",fg_color="spring green",text_color="black",font=("arial",12,"bold"), corner_radius=10)
l2.place(x=550, y=320)
pno=ctk.StringVar()
e2=ctk.CTkEntry(window, textvariable=pno)
e2.place(x=800,y=320)

# Combobox for length of password
l3=ctk.CTkLabel(window, text="Enter length of the password :",fg_color="spring green", text_color="black",font=("Arial",12,"bold"), corner_radius=10)
l3.place(x=550,y=360)
lengthlist=[str(i) for i in range(3,20)]
combo_var=ctk.StringVar()
combo=ctk.CTkComboBox(window, values=lengthlist, variable=combo_var, width=200, font=("Arial",12))
combo.place(x=800,y=360)
combo_var.set("Define the length")

# Buttons for function
b1=ctk.CTkButton(window, text="Generate", text_color="yellow", fg_color="red", command=generate_password, width=100)
b1.place(x=550,y=450)
b2=ctk.CTkButton(window, text="Reset", fg_color="red", text_color="yellow", command=reset, width=100)
b2.place(x=700,y=450)
b3=ctk.CTkButton(window, text="Exit", fg_color="red", text_color="yellow", command=exit1, width=100)
b3.place(x=840,y=450)

window.mainloop()