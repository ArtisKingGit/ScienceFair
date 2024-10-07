from customtkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import Image
import subprocess
import psycopg2

window = CTk()
window.geometry("856x645")
window.resizable(0,0)
window.title("School Bookshop")

set_appearance_mode("dark")

sidebar_frame = CTkFrame(master=window, fg_color="transparent", width=330, height=645, corner_radius=10)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(anchor="nw", side="left")

sidebar_frame2 = CTkFrame(master=window, fg_color="transparent", width=526, height=645, corner_radius=10, border_color="#000", border_width=5)
sidebar_frame2.pack_propagate(0)
sidebar_frame2.pack(fill="y", anchor="center")


img_logo_data = Image.open("poopoo.jpeg")
img_logo = CTkImage(dark_image=img_logo_data, light_image=img_logo_data, size=(330, 650))
CTkLabel(master=sidebar_frame, text="", image=img_logo).pack(anchor="center")


# Function to open login form
def call():
    window.destroy()  # Destroy the main window
    subprocess.Popen(["python", "/Users/beginner/Desktop/Advanced Arthur/Python-Advanced-main/index2.py"])  # Update with the correct path to index2.py

def call2():
    window.destroy()
    subprocess.Popen(["python", "/Users/beginner/Desktop/Advanced Arthur/Python-Advanced-main/index2.py"])  # Update with the correct path to index2.py

# Function to open registration form
def opensecondarywindow():
    username = regist_entry.get()
    password = registpass_entry.get()
    password_confirm = registpassconfirm_entry.get()

    if username == "" or password == "" or password_confirm == "":
        messagebox.showwarning("Warning", "Input fields are empty")
    else:
        try:
            conn = psycopg2.connect("dbname='postgres' user='postgres' password='asdfghj3' host='localhost' port='5432'")
            cur = conn.cursor()
            cur.execute('INSERT INTO names(username, pass) VALUES (%s, %s)', (username, password))
            conn.commit()  # Commit the transaction
            messagebox.showinfo("Success", "Registration successful!")
            btn_regist._state("disabled")
            call()

        except (psycopg2.DatabaseError, psycopg2.Error) as e:
            messagebox.showerror("Error", f"Error inserting data: {e}")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

# Function to attempt login
def login_attempt(username, password):
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' password='asdfghj3' host='localhost' port='5432'")
        cur = conn.cursor()

        # Execute the query to fetch user with given username and password
        cur.execute('SELECT * FROM names WHERE username = %s AND pass = %s', (username, password))

        # Fetch the first row (if exists)
        user = cur.fetchone()

        if user:
            messagebox.showinfo("Success", "Successfully logged in!")
            # Close connection and open dashboard or do other actions here
            cur.close()
            conn.close()

            try:
                subprocess.check_call(["python", "/Users/beginner/Desktop/Advanced Arthur/Python-Advanced-main/Dashboard.py"])

            except subprocess.CalledProcessError as e:
                print("Error executing Dashboard.py:", e)
        else:
            messagebox.showerror("Error", "Login failed: Incorrect username or password.")

    except (psycopg2.DatabaseError, psycopg2.Error) as e:
        messagebox.showerror("Error", f"Database error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# Widgets for registration form
lbl_welcome =CTkLabel(master=sidebar_frame2, text="Register Your User", font=("Arial", 30))
lbl_welcome.pack(pady=50)

regist_entry = CTkEntry(sidebar_frame2, width=300, placeholder_text="Enter username...", border_color="grey", corner_radius= 10,)
regist_entry.pack(pady=10)

registpass_entry = CTkEntry(sidebar_frame2, width=300, placeholder_text="Enter password...", border_color="grey", corner_radius= 10, show = "*")
registpass_entry.pack(pady=10)

registpassconfirm_entry = CTkEntry(sidebar_frame2, width=300, placeholder_text="Confirm password...", border_color="grey",corner_radius= 10, show = "*")
registpassconfirm_entry.pack(pady=10)

img_regist = Image.open("register.png")
btn_regist = CTkButton(sidebar_frame2, width=300,height=40,border_spacing= 10,text_color="Black", font=("Arial", 20), fg_color="#fff", border_width=3, border_color="#207244", text="Register",corner_radius= 10,image=CTkImage(dark_image= img_regist), command=opensecondarywindow)
btn_regist.pack(pady=50)

grid = CTkButton(sidebar_frame2, text_color="Black",height=20, width=300, font=("Arial", 16), text="Already have an account? Sign in here", fg_color="#fff", border_width=3,corner_radius= 10, border_color="#207244", command=call)
grid.pack(pady=10)

# Centering buttons
btn_regist.pack(pady=(50, 10), anchor="center")
grid.pack(pady=(10, 50), anchor="center")

window.mainloop()
