from customtkinter import *
from tkinter import *
from PIL import Image
import subprocess
from tkintermapview import *
import tkintermapview

app = CTk()
app.geometry("856x645")
app.resizable(0,0)

set_appearance_mode("light")
def open_accounts():
    try: 
        subprocess.Popen(["python", "account.py"])
        app.destroy()
    except subprocess.CalledProcessError as e:
        print("Error executing account.py", e)

def open_dashboard():
    try:
        subprocess.Popen(["python", "Dashboard.py"])
        app.destroy()
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py", e)
        
def open_feedback():
    try:
        subprocess.Popen(["python", "feedback.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing feedback.py", e )

def open_returns():
    try:
        subprocess.Popen(["python", "returns.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing returns.py", e)

def open_settings():
    try:
        subprocess.Popen(["python", "settings.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing settings.py", e)

    
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
CTkButton(master=sidebar_frame, image=analytics_img, text="Dashboard", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command= open_dashboard).pack(anchor="center", ipady=5, pady=(60, 0))

#Feedback
feedback_img_data = Image.open("feedback_icon.png")
feedback_img = CTkImage(dark_image= feedback_img_data, light_image= feedback_img_data)
CTkButton(master = sidebar_frame, image = feedback_img, text = "Feedback", fg_color= "transparent", font = ("Arial Bold", 14), hover_color="#207244", anchor = "w",command= open_feedback).pack(anchor = "center", ipady =5, pady = (16, 0 ))
 
#The order lists
###CTkButton(master=sidebar_frame, image=list_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

#Returns
returns_img_data = Image.open("returns_icon.png")
returns_img = CTkImage(dark_image=returns_img_data, light_image=returns_img_data)
CTkButton(master=sidebar_frame, image=returns_img, text="Returns", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=open_returns).pack(anchor="center", ipady=5, pady=(16, 0))

#Settings
settings_img_data = Image.open("settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data)
CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=open_settings).pack(anchor="center", ipady=5, pady=(16, 0))

#Account
person_img_data = Image.open("person_icon.png")
person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
CTkButton(master=sidebar_frame, image=person_img, text="Account", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=open_accounts).pack(anchor="center", ipady=5, pady=(160, 0))

widget = TkinterMapView(app, width =600, height = 400)
widget.pack(fill = "both", expand=True)

widget.set_address("Kiserian, Kenya",marker=True)

app.mainloop()
        
 



