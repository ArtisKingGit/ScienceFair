from customtkinter import *
import tkinter
from PIL import Image
import subprocess
from tkinter import messagebox
import psycopg2

app = CTk()
app.geometry("856x645")
app.resizable(0,0)

set_appearance_mode("light")
    
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
    
def open_returns():
    app.destroy()
    try:
        subprocess.Popen(["python", "returns.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)
    
def open_dashboard():
    app.destroy()
    try:
        subprocess.Popen(["python", "Dashboard.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)


quauntity_frame_no = 1
def quauntity_frame_count():
    global quauntity_frame_no
    quauntity_frame_no += 1
    lbl_quantity_count.configure(text = str(quauntity_frame_no))

def quantity_frame_count_subtraction():
    global quauntity_frame_no
    quauntity_frame_no -= 1
    lbl_quantity_count.configure(text = str(quauntity_frame_no))
    
def other_page():
    itemname_value = entry_item_name.get()
    customername_value = entry_customer_name.get()
    addressname_value = entry_address_name.get()
    quantity = quauntity_frame_no

    if itemname_value == "" or customername_value == "" or addressname_value == "":
        messagebox.showwarning("Warning", "Input fields are empty")
    else:
        try:
            conn = psycopg2.connect("dbname='postgres' user='postgres' password='asdfghj3' host='localhost' port='5432'")
            cur = conn.cursor()
            cur.execute('INSERT INTO orders(order_name, customer_name, address_name, quantity) VALUES (%s, %s, %s, %s)', (itemname_value, customername_value, addressname_value, quantity))
            conn.commit()  # Commit the transaction
            subprocess.Popen(["python", "/Users/beginner/Desktop/Advanced Arthur/Python-Advanced-main/Orders_second.py"])

        except Exception as e:
            print(f"Error launching Orders_second.py: {e}")

#Sidebar
sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55",  width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

#Rocket Image
logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))
CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

#Dashboard
analytics_img_data = Image.open("analytics_icon.png")
analytics_img = CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data)
CTkButton(master=sidebar_frame, image=analytics_img, text="Dashboard", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command= open_dashboard).pack(anchor="center", ipady=5, pady=(60, 0))

#Feedback
feedback_img_data = Image.open("feedback_icon.png")
feedback_img = CTkImage(dark_image= feedback_img_data, light_image= feedback_img_data)
CTkButton(master = sidebar_frame, image = feedback_img, text = "Feedback", fg_color= "transparent", font = ("Arial Bold", 14), hover_color="#207244", anchor = "w",command = open_feedback).pack(anchor = "center", ipady =5, pady = (16, 0 ))

#Orders
package_img_data = Image.open("package_icon.png")
package_img = CTkImage(dark_image=package_img_data, light_image=package_img_data)
CTkButton(master=sidebar_frame, image=package_img, text="Orders", fg_color="#fff", font=("Arial Bold", 14), text_color="#2A8C55", hover_color="#eee", anchor="w", ).pack(anchor="center", ipady=5, pady=(16, 0))

#Lists
list_img_data = Image.open("list_icon.png")
list_img = CTkImage(dark_image=list_img_data, light_image=list_img_data)
CTkButton(master=sidebar_frame, image=list_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

#Returns
returns_img_data = Image.open("returns_icon.png")
returns_img = CTkImage(dark_image=returns_img_data, light_image=returns_img_data)
CTkButton(master=sidebar_frame, image=returns_img, text="Returns", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command= open_returns).pack(anchor="center", ipady=5, pady=(16, 0))

#Settings
settings_img_data = Image.open("settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data)
CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command = open_settings).pack(anchor="center", ipady=5, pady=(16, 0))

#Accounts
person_img_data = Image.open("person_icon.png")
person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
CTkButton(master=sidebar_frame, image=person_img, text="Account", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

main_view = CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

CTkLabel(master=main_view, text="Create Order", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", pady=(29,0), padx=27)

#Entry item name
CTkLabel(master=main_view, text="Item Name", font=("Arial Bold", 17), text_color="#52A476").pack(anchor="nw", pady=(25,0), padx=27)
entry_item_name = CTkEntry(master=main_view, fg_color="#F0F0F0", border_width=0)
entry_item_name.pack(fill="x", pady=(12,0), padx=27, ipady=10)

grid = CTkFrame(master=main_view, fg_color="transparent")
grid.pack(fill="both", padx=27, pady=(31,0))

#Entry Customer name
CTkLabel(master=grid, text="Customer", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=0, column=0, sticky="w")
entry_customer_name = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
entry_customer_name.grid(row=1, column=0, ipady=10)

#Entry Address name
CTkLabel(master=grid, text="Address", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=0, column=1, sticky="w", padx=(25,0))
entry_address_name = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
entry_address_name.grid(row=1, column=1, ipady=10, padx=(24,0))

CTkLabel(master=grid, text="Status", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=2, column=0, sticky="w", pady=(38, 0))

status_var = tkinter.IntVar(value=0)

CTkRadioButton(master=grid, variable=status_var, value=0, text="Confirmed", font=("Arial Bold", 14), text_color="#52A476", fg_color="#52A476", border_color="#52A476", hover_color="#207244").grid(row=3, column=0, sticky="w", pady=(16,0))
CTkRadioButton(master=grid, variable=status_var, value=1,text="Pending", font=("Arial Bold", 14), text_color="#52A476", fg_color="#52A476", border_color="#52A476", hover_color="#207244").grid(row=4, column=0, sticky="w", pady=(16,0))
CTkRadioButton(master=grid, variable=status_var, value=2,text="Cancelled", font=("Arial Bold", 14), text_color="#52A476", fg_color="#52A476", border_color="#52A476", hover_color="#207244").grid(row=5, column=0, sticky="w", pady=(16,0))

CTkLabel(master=grid, text="Quantity", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=6, column=0, sticky="w", pady=(42, 0))

quantity_frame = CTkFrame(master=grid, fg_color="transparent")
quantity_frame.grid(row=7, column=0, pady=(21,0), sticky="w")

#Quantity count buttons
CTkButton(master=quantity_frame, text="-", width=25, fg_color="#2A8C55", hover_color="#207244", font=("Arial Black", 16), command = quantity_frame_count_subtraction).pack(side="left", anchor="w")
lbl_quantity_count = CTkLabel(master=quantity_frame, text="01", text_color="#2A8C55", font=("Arial Black", 16))
lbl_quantity_count.pack(side="left", anchor="w", padx=10)
CTkButton(master=quantity_frame, text="+", width=25,  fg_color="#2A8C55",hover_color="#207244", font=("Arial Black", 16), command = quauntity_frame_count).pack(side="left", anchor="w")

CTkLabel(master=grid, text="Description", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=2, column=1, sticky="w", pady=(42, 0), padx=(25,0))

txtbox_description = CTkTextbox(master=grid, fg_color="#F0F0F0", width=300, corner_radius=8)
txtbox_description.grid(row=3, column=1, rowspan=5, sticky="w", pady=(16, 0), padx=(25,0), ipady=10)

actions= CTkFrame(master=main_view, fg_color="transparent")
actions.pack(fill="both")

CTkButton(master=actions, text="Back", width=300, fg_color="transparent", font=("Arial Bold", 17), border_color="#2A8C55", hover_color="#eee", border_width=2, text_color="#2A8C55").pack(side="left", anchor="sw", pady=(30,0), padx=(27,24))
CTkButton(master=actions, text="Create", width=300, font=("Arial Bold", 17), hover_color="#207244", fg_color="#2A8C55", text_color="#fff", command = other_page).pack(side = "left", anchor="se", pady=(30,0), padx=(0,27))

app.mainloop()