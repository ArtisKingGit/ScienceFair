from customtkinter import *
from tkinter import *
from PIL import Image
from subprocess import call
import psycopg2

app = CTk()
app.geometry("856x645")
app.resizable(0, 0)
app.title("School Library")

set_appearance_mode("light")

def fetch_username():
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' password='asdfghj3' host='localhost' port='5432'")
        cur = conn.cursor()

        # Fetch the first username from the 'names' table
        cur.execute('SELECT username FROM names LIMIT 10')
        fetched_username = cur.fetchone()

        if fetched_username:
            print(f"Fetched username: {fetched_username[0]}")
            return fetched_username[0]  # Return the username
        else:
            print("No username found in the database.")
            return None
    
    except (psycopg2.DatabaseError, psycopg2.Error) as e:
        print(f"Database error: {e}")
        return None
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def fetch_account_name(username):
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' password='asdfghj3' host='localhost' port='5432'")
        cur = conn.cursor()

        # Fetch the account name for the given username
        cur.execute('SELECT username FROM names WHERE username = %s', (username,))
        account_name = cur.fetchone()

        if account_name:
            print(f"Fetched account name: {account_name[0]}")
            return account_name[0]
        else:
            print("No account name found for this username.")
            return "No account found"
    
    except (psycopg2.DatabaseError, psycopg2.Error) as e:
        print(f"Database error: {e}")
        return "Error fetching account name"
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# Sidebar- main
sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55", width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

# Rocket image
logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))
CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

# Dashboard
analytics_img_data = Image.open("analytics_icon.png")
analytics_img = CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data)
CTkButton(master=sidebar_frame, image=analytics_img, text="Dashboard", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))

# Feedback
feedback_img_data = Image.open("feedback_icon.png")
feedback_img = CTkImage(dark_image=feedback_img_data, light_image=feedback_img_data)
CTkButton(master=sidebar_frame, image=feedback_img, text="Feedback", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

# Orders
package_img_data = Image.open("package_icon.png")
package_img = CTkImage(dark_image=package_img_data, light_image=package_img_data)
CTkButton(master=sidebar_frame, image=package_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

# The order lists
list_img_data = Image.open("list_icon.png")
list_img = CTkImage(dark_image=list_img_data, light_image=list_img_data)
CTkButton(master=sidebar_frame, image=list_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

# Returns
returns_img_data = Image.open("returns_icon.png")
returns_img = CTkImage(dark_image=returns_img_data, light_image=returns_img_data)
CTkButton(master=sidebar_frame, image=returns_img, text="Returns", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

# Settings
settings_img_data = Image.open("settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data)
CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

# Account
person_img_data = Image.open("person_icon.png")
person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
CTkButton(master=sidebar_frame, image=person_img, text="Account", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

# Main view
main_view = CTkFrame(master=app, fg_color="#fff", width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

CTkLabel(master=main_view, text="Accounts", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", pady=(29, 0), padx=10)

CTkLabel(master=main_view, text="Your Account", font=("Arial Black", 18), text_color="#2A8C55").pack(anchor="nw", pady=(29, 0), padx=10)

# Fetch username and account name from the database
username = fetch_username()
account_person_img_data = Image.open("person_icon.png")
account_person_img = CTkImage(dark_image=account_person_img_data, light_image=account_person_img_data)

# Use the fetched account name as the text on the button
if username:
    account_name_text = fetch_account_name(username)
else:
    account_name_text = "No username found"

CTkButton(master=main_view, image=account_person_img, text=account_name_text, fg_color="#207244", font=("Arial Bold", 14), width=150, height=70).pack(anchor="nw", pady=(29, 0), padx=10)

app.mainloop()
