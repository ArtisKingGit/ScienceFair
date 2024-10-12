from customtkinter import *
from tkinter import *
from PIL import Image
import subprocess

app = CTk()
app.geometry("856x645")
app.resizable(0,0)
app.title("School Library")
set_appearance_mode("light")

def change_mode(choice):
    global lightmode_set, darkmode_set
    if choice == "Light mode":
        set_appearance_mode("light")
        lightmode_set = True
        darkmode_set = False
    elif choice == "Dark mode":
        set_appearance_mode("dark")
        lightmode_set = False
        darkmode_set = True
    
    # Example of checking the variable
    if darkmode_set == True:
        main_view.configure(master=app, fg_color="#000",  width=680, height=650, corner_radius=0)
    
    elif darkmode_set == False:
        main_view.configure(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
        
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
        
def open_map():
    app.destroy()
    try:
        subprocess.Popen(["python", "map.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing map.", e)
        
def open_feedback_view():
    app.destroy()
    try:
        subprocess.Popen(["python", "feedback_view.py"])
        
    except subprocess.CalledProcessError as e:
        print("Error executing the Feedback View", e)
        
        
 
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
CTkButton(master=sidebar_frame, image=analytics_img, text="Dashboard", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command= open_dashboard).pack(anchor="center", ipady=5, pady=(60, 0))

#Feedback
feedback_img_data = Image.open("feedback_icon.png")
feedback_img = CTkImage(dark_image= feedback_img_data, light_image= feedback_img_data)
CTkButton(master = sidebar_frame, image = feedback_img, text = "Feedback", fg_color= "transparent", font = ("Arial Bold", 14), hover_color="#207244", anchor = "w", command= open_feedback).pack(anchor = "center", ipady =5, pady = (16, 0 ))
 
#Orders
#package_img_data = Image.open("package_icon.png")
#package_img = CTkImage(dark_image=package_img_data, light_image=package_img_data)
#CTkButton(master=sidebar_frame, image=package_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command= open_orders).pack(anchor="center", ipady=5, pady=(16, 0))

#The order lists
#list_img_data = Image.open("list_icon.png")
#list_img = CTkImage(dark_image=list_img_data, light_image=list_img_data)
#CTkButton(master=sidebar_frame, image=list_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

#Returns
returns_img_data = Image.open("returns_icon.png")
returns_img = CTkImage(dark_image=returns_img_data, light_image=returns_img_data)
CTkButton(master=sidebar_frame, image=returns_img, text="Returns", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command= open_returns).pack(anchor="center", ipady=5, pady=(16, 0))

#Settings
settings_img_data = Image.open("settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data)
CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

#Account
person_img_data = Image.open("person_icon.png")
person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
CTkButton(master=sidebar_frame, image=person_img, text="Account", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=open_accounts).pack(anchor="center", ipady=5, pady=(160, 0))

#Whats happening in the main form where the feedback page is
global main_view
main_view = CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

CTkLabel(master = main_view, text = "Settings", font=("Arial Black", 25), text_color="#207244").pack(anchor="nw", pady=(29,0), padx=24)

CTkLabel(master = main_view, text = "Change mode", font = ("Arial Bold", 17),text_color="#2A8C55").pack(anchor = "nw", pady = (31,0), padx = 24)

combobox_light = CTkComboBox(master = main_view, values=["Light mode", "Dark mode"], border_width= 1, border_color= "#207244", command= change_mode).pack(anchor = "nw", pady = (34,0), padx = 24)

CTkButton(master = main_view, text = "Map", font=("Arial Black", 25),bg_color= "#FFF", text_color="#207244", border_color="#207244", border_width=1, hover_color="#5c5e5e", command= open_map).pack(anchor="nw", pady=(29,0), padx=24)
CTkButton(master = main_view, text = "View Feedback", font=("Arial Black", 25), text_color="#207244", border_color="#207244", border_width=1, hover_color="#5c5e5e", command=open_feedback_view).pack(anchor="nw", pady=(29,0), padx=24)

app.mainloop()