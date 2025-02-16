import mysql.connector as mc
import bcrypt
import customtkinter as ctk
from customtkinter import CTkLabel
from tkinter import messagebox
from PIL import Image

def logout():
    exit()

def support():
    messagebox.showinfo("Help and Support", "For any inquiries you can contact at +91-8307370347!")
    
def security():
    pass

def connection():
    mydb = mc.connect(host='localhost', user='root', password='IMnj734204', database='bank')
    return mydb

def old_user():
    mydb = connection()
    cur = mydb.cursor(dictionary=True)

    login_window = ctk.CTk()
    login_window.geometry('1200x600')
    login_window.title("Login Window")
    login_window.config(bg="whitesmoke")
    
    # Load and set the image with CTkImage
    image = Image.open("blank-profile-picture.webp")
    ctk_image = ctk.CTkImage(image, size=(200, 200))
    CTkLabel(login_window, image=ctk_image, text="").place(x=500, y=10)
    
    # Other buttons
    profile_button = ctk.CTkButton(login_window, command=None, text="User Profile", width=160)
    profile_button.place(x=500, y=180)
    
    account_button = ctk.CTkButton(login_window, command=None, text="Account Management", width=160)
    account_button.grid(row=1, column=1, pady=(250, 0), padx=(140, 30))
    transaction_button = ctk.CTkButton(login_window, command=None, text="Transaction Management", width=160)
    transaction_button.grid(row=1, column=2, pady=(250, 0), padx=30)
    loan_button = ctk.CTkButton(login_window, command=None, text="Loan Management", width=160)
    loan_button.grid(row=1, column=3, pady=(250, 0), padx=30)
    security_button = ctk.CTkButton(login_window, command=security, text="Change Password", width=160)
    security_button.grid(row=1, column=4, pady=(250, 0), padx=30)
    
    help_button = ctk.CTkButton(login_window, command=support, text="Help and Support", width=160)
    help_button.grid(row=2, column=2, pady=(30, 0))
    logout_button = ctk.CTkButton(login_window, command=logout, text="Logout", width=160)
    logout_button.grid(row=2, column=3, pady=(30, 0))
    
    login_window.mainloop()
