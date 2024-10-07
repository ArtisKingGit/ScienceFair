from customtkinter import *
from PIL import Image
import subprocess

# Create the tkinter app instance
app = CTk()
app.geometry("856x645")
app.resizable(0, 0)
app.title("School Bookshop")
set_appearance_mode("light")

# Function to open Orders.py
def open_orders():
    app.destroy()
    try:
        subprocess.Popen(["python", "Orders.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)


# Function to open Settings.py
def open_settings():
    app.destroy()
    try:
        subprocess.Popen(["python", "settings.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)

# Function to open Returns.py
def open_returns():
    app.destroy()
    try:
        subprocess.Popen(["python", "returns.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)

# Function to open Dashboard.py
def open_dashboard():
    app.destroy()
    try:
        subprocess.Popen(["python", "Dashboard.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)

# Sidebar with buttons
sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55", width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

# Logo
logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))
CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

# Dashboard button
analytics_img_data = Image.open("analytics_icon.png")
analytics_img = CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data)
CTkButton(master=sidebar_frame, image=analytics_img, text="Dashboard", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=open_dashboard).pack(anchor="center", ipady=5, pady=(60, 0))

# Feedback button (no command attached to avoid circular dependencies)
feedback_img_data = Image.open("feedback_icon.png")
feedback_img = CTkImage(dark_image=feedback_img_data, light_image=feedback_img_data)
CTkButton(master=sidebar_frame, image=feedback_img, text="Feedback", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

# Orders button
list_img_data = Image.open("list_icon.png")
list_img = CTkImage(dark_image=list_img_data, light_image=list_img_data)
CTkButton(master=sidebar_frame, image=list_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=open_orders).pack(anchor="center", ipady=5, pady=(16, 0))

# Returns button
returns_img_data = Image.open("returns_icon.png")
returns_img = CTkImage(dark_image=returns_img_data, light_image=returns_img_data)
CTkButton(master=sidebar_frame, image=returns_img, text="Returns", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=open_returns).pack(anchor="center", ipady=5, pady=(16, 0))

# Settings button
settings_img_data = Image.open("settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data)
CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=open_settings).pack(anchor="center", ipady=5, pady=(16, 0))

# Account button
person_img_data = Image.open("person_icon.png")
person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
CTkButton(master=sidebar_frame, image=person_img, text="Account", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

# Main view for feedback form
main_view = CTkFrame(master=app, fg_color="#fff", width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

CTkLabel(master=main_view, text="Submit Customer Feedback", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", pady=(29, 0), padx=10)

CTkEntry(master=main_view, placeholder_text="Enter name...", font=("Arial Bold", 15), width=300, border_width=3, border_color="#207244").pack(anchor="nw", pady=(33, 0), padx=10)

CTkEntry(master=main_view, placeholder_text="Enter email...", font=("Arial Bold", 15), width=300, border_width=3, border_color="#207244").pack(anchor="nw", pady=(34, 0), padx=10)

CTkLabel(master=main_view, font=("Arial Bold", 18), text="Nature of the feedback", text_color="#2A8C55").pack(anchor="nw", pady=(34, 0), padx=10)

options = ["Report a bug", "State an Issue", "Concerns", "Improve on an area", "Other"]
CTkComboBox(master=main_view, values=options, border_width=1, border_color="#207244").pack(anchor="nw", pady=(35, 0), padx=10)

CTkTextbox(master=main_view, width=1000, border_color="#207244", border_width=5, scrollbar_button_color="#207244", corner_radius=16).pack(anchor="w", pady=(40, 0), padx=10)

message_img_data = Image.open("message_icon.png")
message_img = CTkImage(dark_image=message_img_data, light_image=message_img_data)
CTkButton(master=main_view, width=100, height=50, border_color="#207244", hover_color="#00A34F", corner_radius=15, text="Submit Feedback", fg_color="#207244", image=message_img, font=("Arial Bold", 14), anchor="w").pack(anchor="w", pady=(41, 0), padx=10)

# Start the tkinter main loop
app.mainloop()
