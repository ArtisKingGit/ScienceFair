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

def other_page():
    customer_name = customer_name_value.get()
    item_name = combobox.get()
    item_quantity = item_quantity_value.get()
    address_name = address_value.get()

    if customer_name == "" or item_name == "" or item_quantity == "" or address_name =="":
        messagebox.showwarning("Warning", "Input fields are empty")
    else:
        try:
            conn = psycopg2.connect("dbname='postgres' user='postgres' password='asdfghj3' host='localhost' port='5432'")
            cur = conn.cursor()
            cur.execute('INSERT INTO returns_(customer_name, items_name, item_quantity, address_name) VALUES (%s, %s, %s, %s)', (customer_name, item_name, item_quantity, address_name ))
            conn.commit()  # Commit the transaction

        except Exception as e:
            print(f"Error launching Orders_second.py: {e}")

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

CTkLabel(master= main_view, text = "Returns", font = ("Arial Bold", 25), text_color= "#207244").pack(anchor = "nw", pady= (20, 0), padx = 24)

customer_name_value = CTkEntry(master = main_view, placeholder_text= "Customer name...", width = 250, font = ("Arial Bold", 14), border_width= 3, border_color= "#207244")
customer_name_value.pack(anchor = "nw", pady =(22, 0), padx = 24)

combobox_values = ["Pencil", "Chemistry book", "Debit Card", "Mackbook pro", "Camera", "Printer", "Smartwatch", "Football", "Monitor", "External hard drive", "Other"]

combobox = CTkComboBox(master = main_view, values= combobox_values, width = 150,border_width= 3, border_color= "#207244")
combobox.pack(anchor = "nw", pady = (23,0), padx = 24)

item_quantity_value = CTkEntry(master = main_view, placeholder_text= "Item quantity...", width = 250, font = ("Arial Bold", 14), border_width= 3, border_color= "#207244")
item_quantity_value.pack(anchor = "nw", pady =(23, 0), padx = 24)

address_value = CTkEntry(master = main_view, placeholder_text= "Your address...", width = 250, font = ("Arial Bold", 14), border_width= 3, border_color= "#207244")
address_value.pack(anchor = "nw", pady =(24, 0), padx = 24)

package_img_data_2 = Image.open("package_icon.png")
package_img_2 = CTkImage(dark_image= package_img_data_2, light_image= package_img_data_2 )
CTkButton(master=main_view, image= package_img_2, text = "Submit", font= ("Arial Black", 14), border_color= "#207244", fg_color= "#fff", border_width= 3, command= other_page).pack(anchor = "nw", pady = 25, padx = 24)

#Tables
table_data = [
    ["Return ID", "Item Name", "Customer", "Address", "Status", "Quantity"],
    ['1', 'Pencil', 'Patrick Gichui', '123 Dawamu Street', 'Confirmed', '8'],
    ['2', 'Chemistry book', 'Ryan Kamau', '456 Elm St', 'Packing', '1'],
    ['3', 'Debit Card', 'Benjamin Baraka', '789 Oak St', 'Delivered', '1'],
    ['4', 'Macbook Pro', 'Jacinta', '101 Pine St', 'Confirmed', '9'],
    ['5', 'Camera', 'Boniface', '202 Cedar St', 'Processing', '2'],
    ['6', 'Printer', 'Tr Timothy', '303 Maple St', 'Cancelled', '2'],
    ['7', 'Smartwatch', 'Mr Mwau', '404 Birch St', 'Shipping', '6'],
    ['8', 'Football', 'Favour Keli', '505 Redwood St', 'Cancelled', '10'],
    ['9', 'Monitor', 'Trevor Mutai', '606 Fir St', 'Shipping', '6'],
    ['10', 'External Hard Drive', 'Benjamin Ombaka', '707 Oak St', 'Delivered', '10'],
    ['11', 'Table Lamp', 'Shaun Justin', '808 Pine St', 'Confirmed', '4'],
    ['12', 'Desk Chair', 'Samuel Omondi', '909 Cedar St', 'Processing', '9'],
    ['13', 'Coffee Maker', 'Lucas Junior', '1010 Elm St', 'Confirmed', '6'],
    ['14', 'Blender', 'David Gumbao', '1111 Redwood St', 'Shipping', '2'],
    ['15', 'Toaster', 'Emmanuel', '1212 Maple St', 'Processing', '1'],
    ['16', 'Microwave', 'Malek Marseil', '1313 Cedar St', 'Confirmed', '8'],
    ['17', 'Refrigerator', 'Cynthia Ogana', '1414 Oak St', 'Processing', '5'],
    ['18', 'Vacuum Cleaner', 'James Rogoi', '1515 Pine St', 'Cancelled', '10']
]

table_frame = CTkScrollableFrame(master=main_view, fg_color="transparent")
table_frame.pack(expand=True, fill="both", padx=27, pady=30)
table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
table.pack(expand=True)

app.mainloop()