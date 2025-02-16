import customtkinter as ctk
from tkinter import messagebox
from customtkinter import CTkLabel
import mysql.connector as mc
from new_user import new_user
from old_user import old_user
from PIL import Image, ImageTk
import bcrypt

def connection():
    mydb = mc.connect(host="localhost", user="root", password="IMnj734204", database="bank")
    return mydb


def check_login():
    account_id = account_entry.get()
    password = password_entry.get()
    mydb = connection()
    cur = mydb.cursor(dictionary=True)
    cur.execute("select user_id from accounts where account_id=%s", (account_id,))
    result = cur.fetchone()
    if result is None:
        messagebox.showerror("Wrong Credentials!", "Account No. or Password is incorrect!")
        cur.close()
        mydb.close()
        return

    user_id = result["user_id"]
    cur.execute("select password_hash from users where user_id=%s", (user_id,))
    user_data = cur.fetchone()

    if user_data is None or not bcrypt.checkpw(password.encode(), user_data["password_hash"].encode()):
        messagebox.showerror("Wrong Credentials", "Account No. or Password is incorrect!")
        cur.close()
        mydb.close()
        return

    messagebox.showinfo("Login Success", "Welcome back!")
    cur.close()
    mydb.close()
    old_user()

# Basic GUI Settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.geometry("1200x600")
window.title("Bank Management System")
window.config(bg="whitesmoke")

# 2 Frames
left_frame = ctk.CTkFrame(window, width=700)
left_frame.pack(side="left", fill="y")
right_frame = ctk.CTkFrame(window, fg_color="blue")
right_frame.pack(side="right", fill="both", expand=True)

# Left Frame
account_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter Account ID", width=200, height=40)
account_entry.place(x=200, y=200)
password_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter Password", width=200, height=40)
password_entry.place(x=200, y=260)

forgot = ctk.CTkButton(left_frame, command=None, text="Forgot Password?")
forgot.place(x=200, y=320)
login = ctk.CTkButton(left_frame, command=check_login, text="Login", width=200, height=40)
login.place(x=200, y=370)
signup = ctk.CTkButton(left_frame, command=new_user, text="Sign Up", width=200, height=40)
signup.place(x=200, y=430)

window.mainloop()