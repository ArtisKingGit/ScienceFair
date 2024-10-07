from customtkinter import *
import tkinter
from PIL import Image
import subprocess
from CTkTable import *
import psycopg2

# Connect to database and fetch data
def fetch_orders_data():
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' password='asdfghj3' host='localhost' port='5432'")
        cur = conn.cursor()

        # Execute the query to fetch data from the orders table
        cur.execute('SELECT order_name, customer_name, address_name, quantity FROM orders')

        # Fetch all rows
        orders_data = cur.fetchall()
        
        # Add header to the data
        table_data = [["Order Name", "Customer Name", "Address", "Quantity"]] + [list(row) for row in orders_data]

        return table_data

    except (psycopg2.DatabaseError, psycopg2.Error) as e:
        messagebox.showerror("Error", f"Database error: {e}")
        return []

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# GUI setup
app = CTk()
app.geometry("856x645")
app.resizable(0, 0)
set_appearance_mode("light")

# Functions to open other scripts
def open_feedback():
    app.destroy()
    try:
        subprocess.Popen(["python", "feedback.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing feedback.py:", e)

def open_settings():
    app.destroy()
    try:
        subprocess.Popen(["python", "settings.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing settings.py:", e)

def open_returns():
    app.destroy()
    try:
        subprocess.Popen(["python", "returns.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing returns.py:", e)

def open_dashboard():
    app.destroy()
    try:
        subprocess.Popen(["python", "Dashboard.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)

# Sidebar
sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55", width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

# Rocket Image
logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))
CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

# Dashboard Button
analytics_img_data = Image.open("analytics_icon.png")
analytics_img = CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data)
CTkButton(master=sidebar_frame, image=analytics_img, text="Dashboard", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=open_dashboard).pack(anchor="center", ipady=5, pady=(60, 0))

# Feedback Button
feedback_img_data = Image.open("feedback_icon.png")
feedback_img = CTkImage(dark_image=feedback_img_data, light_image=feedback_img_data)
CTkButton(master=sidebar_frame, image=feedback_img, text="Feedback", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=open_feedback).pack(anchor="center", ipady=5, pady=(16, 0))

# Orders Button
package_img_data = Image.open("package_icon.png")
package_img = CTkImage(dark_image=package_img_data, light_image=package_img_data)
CTkButton(master=sidebar_frame, image=package_img, text="Orders", fg_color="#fff", font=("Arial Bold", 14), text_color="#2A8C55", hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

# Lists Button
list_img_data = Image.open("list_icon.png")
list_img = CTkImage(dark_image=list_img_data, light_image=list_img_data)
CTkButton(master=sidebar_frame, image=list_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

# Returns Button
returns_img_data = Image.open("returns_icon.png")
returns_img = CTkImage(dark_image=returns_img_data, light_image=returns_img_data)
CTkButton(master=sidebar_frame, image=returns_img, text="Returns", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=open_returns).pack(anchor="center", ipady=5, pady=(16, 0))

# Settings Button
settings_img_data = Image.open("settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data)
CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=open_settings).pack(anchor="center", ipady=5, pady=(16, 0))

# Account Button
person_img_data = Image.open("person_icon.png")
person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
CTkButton(master=sidebar_frame, image=person_img, text="Account", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

# Main View
main_view = CTkFrame(master=app, fg_color="#fff", width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

CTkLabel(master=main_view, text="Thank you for Confirming your order!", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", pady=(29, 0), padx=27)
CTkLabel(master=main_view, text="Submit your feedback if needed to.", font=("Arial Black", 20), text_color="#2A8C55").pack(anchor="nw", pady=(30, 0), padx=27)

# Fetch and display table data from the database
table_data = fetch_orders_data()

table_frame = CTkScrollableFrame(master=main_view, fg_color="transparent")
table_frame.pack(expand=True, fill="both", padx=27, pady=21)

table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
table.pack(expand=True)

app.mainloop()
