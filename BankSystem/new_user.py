import mysql.connector as mc
import bcrypt
import customtkinter as ctk
from customtkinter import CTkLabel
from tkinter import messagebox

def connection():
    mydb=mc.connect(host='localhost',user='root',password='IMnj734204',database='bank')
    return mydb

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def new_user():
    mydb=connection()
    cur=mydb.cursor(dictionary=True)
    signup_window = ctk.CTk()
    signup_window.geometry('1200x600')
    signup_window.title("New User Sign-up")
    signup_window.config(bg="whitesmoke")
    def signup():
        email = entry_email.get()
        phone = entry_phone.get()
        username = entry_username.get()
        password = entry_password.get()
        confirm_password = entry_confirm_password.get()
        account_type = dropdown.get()
        if password != confirm_password:
            messagebox.showerror("Unmatched Password", "Passwords do not match")
            return
        
        # Hash the password
        hashed_password = hash_password(password)

        try:
            cur.execute("INSERT INTO users (username, password_hash, email, phone_number) VALUES (%s, %s, %s, %s)",
            (username, hashed_password, email, phone))
            mydb.commit()
            
            user_id = cur.lastrowid
            cur.execute("INSERT INTO accounts (user_id, account_type) VALUES (%s, %s)",(user_id,account_type))
            mydb.commit()
            
            account_id = cur.lastrowid
            cur.execute("INSERT INTO transactions (account_id, transaction_type, amount, balance_after, remarks) VALUES (%s, 'deposit', 0, 0, 'Account Created')",(account_id,))
            mydb.commit()

            messagebox.showinfo("Success!", f"New user registered successfully! Your account ID is {account_id}")
        except mc.Error as err:
            messagebox.showerror("Database Error!",f"Error: {err}")

    # GUI components
    lbl_email = ctk.CTkLabel(signup_window, text="Email:")
    lbl_email.grid(row=0, column=0, padx=10, pady=10)
    entry_email = ctk.CTkEntry(signup_window)
    entry_email.grid(row=0, column=1, padx=10, pady=10)

    lbl_phone = ctk.CTkLabel(signup_window, text="Phone Number:")
    lbl_phone.grid(row=1, column=0, padx=10, pady=10)
    entry_phone = ctk.CTkEntry(signup_window)
    entry_phone.grid(row=1, column=1, padx=10, pady=10)

    lbl_username = ctk.CTkLabel(signup_window, text="Username:")
    lbl_username.grid(row=2, column=0, padx=10, pady=10)
    entry_username = ctk.CTkEntry(signup_window)
    entry_username.grid(row=2, column=1, padx=10, pady=10)

    lbl_password = ctk.CTkLabel(signup_window, text="Password:")
    lbl_password.grid(row=3, column=0, padx=10, pady=10)
    entry_password = ctk.CTkEntry(signup_window, show="*") # show * for each character
    entry_password.grid(row=3, column=1, padx=10, pady=10)

    lbl_confirm_password = ctk.CTkLabel(signup_window, text="Confirm Password:")
    lbl_confirm_password.grid(row=4, column=0, padx=10, pady=10)
    entry_confirm_password = ctk.CTkEntry(signup_window, show="*")
    entry_confirm_password.grid(row=4, column=1, padx=10, pady=10)
    
    lbl_dropdown = ctk.CTkLabel(signup_window, text="Choose Account Type:")
    lbl_dropdown.grid(row=5, column=0, padx=10, pady=10)
    dropdown = ctk.CTkOptionMenu(signup_window, values=["savings","checking"])
    dropdown.grid(row=5, column=1, padx=10, pady=10)

    btn_signup = ctk.CTkButton(signup_window, text="Sign Up", command=signup)
    btn_signup.grid(row=6, column=1, padx=10, pady=20)

    signup_window.mainloop()
    mydb.commit()
    cur.close()
    mydb.close()