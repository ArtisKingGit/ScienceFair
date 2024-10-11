from customtkinter import *
import tkinter
from CTkTable import CTkTable
from PIL import Image
import subprocess
from tkinter import messagebox
import psycopg2

app = CTk()
app.geometry("856x645")
app.resizable(0,0)
app.title("School Library")
set_appearance_mode("light")
    
###########The Left hand side panel with the apps are in here -->>###########
def open_accounts():
    try: 
        subprocess.Popen(["python", "account.py"])
        app.destroy()
    except subprocess.CalledProcessError as e:
        print("Error executing account.py", e)
        
def open_orders():
    app.destroy()
    try:
        subprocess.Popen(["python", "Orders.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)
    
def open_feedback():
    app.destroy()
    try:
        subprocess.Popen(["python", "feedback.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)
    
def open_settings():
    app.destroy()
    try:
        subprocess.Popen(["python", "settings.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)
    
def open_dashboard():
    app.destroy()
        
    try:
        subprocess.Popen(["python", "Dashboard.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)
        
def fetch_orders_data():
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' password='asdfghj3' host='localhost' port='5432'")
        cur = conn.cursor()

        # Execute the query to fetch data from the orders table
        cur.execute('SELECT customer_name, items_name, item_quantity, address_name FROM returns_')

        # Fetch all rows
        orders_data = cur.fetchall()
        
        # Add header to the data
        table_data = [["Customer Name", "Item Name", "Item Quantity", "Address"]] + [list(row) for row in orders_data]

        return table_data
    except psycopg2.DatabaseError as e:
        print("Error", e)

#Sidebar- main
sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55",  width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

#Rocket image
logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))
CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

#Dashboard
analytics_img_data = Image.open("analytics_icon.png")
analytics_img = CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data)
CTkButton(master=sidebar_frame, image=analytics_img, text="Dashboard", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command = open_dashboard).pack(anchor="center", ipady=5, pady=(60, 0))

#Feedback
feedback_img_data = Image.open("feedback_icon.png")
feedback_img = CTkImage(dark_image= feedback_img_data, light_image= feedback_img_data)
CTkButton(master = sidebar_frame, image = feedback_img, text = "Feedback", fg_color= "transparent", font = ("Arial Bold", 14), hover_color="#207244", anchor = "w", command= open_feedback).pack(anchor = "center", ipady =5, pady = (16, 0 ))
 
#Orders
#package_img_data = Image.open("package_icon.png")
#package_img = CTkImage(dark_image=package_img_data, light_image=package_img_data)
#CTkButton(master=sidebar_frame, image=package_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command= open_orders).pack(anchor="center", ipady=5, pady=(16, 0))

#The order lists
list_img_data = Image.open("list_icon.png")
list_img = CTkImage(dark_image=list_img_data, light_image=list_img_data)
CTkButton(master=sidebar_frame, image=list_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

#Returns
returns_img_data = Image.open("returns_icon.png")
returns_img = CTkImage(dark_image=returns_img_data, light_image=returns_img_data)
CTkButton(master=sidebar_frame, image=returns_img, text="Returns", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

#Settings
settings_img_data = Image.open("settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data)
CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command = open_settings).pack(anchor="center", ipady=5, pady=(16, 0))

#Account
person_img_data = Image.open("person_icon.png")
person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
CTkButton(master=sidebar_frame, image=person_img, text="Account", fg_color="transparent", font=("Arial Black", 25), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

#Whats happening in the main form where the feedback page is
main_view = CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

CTkLabel(master= main_view, text = "Thank You! For returning your product", font = ("Arial Bold", 25), text_color= "#207244").pack(anchor = "nw", pady= (20, 0), padx = 24)
CTkLabel(master= main_view, text = """If you want to submit feedback, go to the feedback 
         page.""", font = ("Arial Bold", 25), text_color= "#207244").pack(anchor = "nw", pady= (20, 0), padx = 24)
CTkLabel(master= main_view, text = "Returns:", font = ("Arial Bold", 25), text_color= "#207244").pack(anchor = "nw", pady= (20, 0), padx = 24)

table_data = fetch_orders_data()

table_frame = CTkScrollableFrame(master=main_view, fg_color="transparent")
table_frame.pack(expand=True, fill="both", padx=27, pady=21)

table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
table.pack(expand=True)

app.mainloop()