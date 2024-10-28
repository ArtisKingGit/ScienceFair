from customtkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import Image
import subprocess

window = CTk()
window.geometry("856x645")
window.resizable(0,0)
window.title("School Library")

set_appearance_mode("light")

sidebar_frame = CTkFrame(master=window, fg_color="#207244", width=330, height=645, corner_radius=10)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(anchor="nw", side="left")

sidebar_frame2 = CTkFrame(master=window, fg_color="#FFF", width=526, height=645, corner_radius=10,)
sidebar_frame2.pack_propagate(0)
sidebar_frame2.pack(fill="y", anchor="center")

frame = CTkFrame(master=sidebar_frame, fg_color="#FFF", width =300, height=70, border_color="#000", border_width=5, corner_radius=20)
frame.pack_propagate(0)
frame.pack(anchor ="n", pady = 20)

CTkLabel(master=frame, text="Get Started", font=("Arial Bold", 25)).pack(side="top", pady = 20)

my_tab = CTkTabview(sidebar_frame2, height= 400, width=510, fg_color="#207244", border_color="#000", border_width=2, segmented_button_fg_color="#000", segmented_button_selected_color="#FFF", text_color="#000", segmented_button_unselected_color="#00B650")
my_tab.pack(pady =10, anchor = "center")

tab_1 = my_tab.add("What We Do")
tab_2 = my_tab.add("What you expect")

label_tab = CTkLabel(master= tab_1, text="""In our School Library System, created using Python, 
we focus on making it easy for students and staff to
manage and access library resources. The system 
allowsusers to search for books by title, author,
or genre, check availability, and keep track of 
borrowed books. Administrators can manage the 
inventory by adding, updating, or removing books
as needed. With clear and user-friendly menus, 
the system provides a straightforward experience
for both students and staff, helping to keep the
library organized and making book borrowing 
fast and efficient.""", font=("Arial Bold", 19),text_color="#FFF")
label_tab.pack(pady=20)

label_tab_2 = CTkLabel(master=tab_2, text="""I expect the School Library System to make book 
management much easier and efficient for both library
staff and students. It should provide quick access
to information about available books, simplify the
borrowing and returning process, and keep an 
accurate record of all transactions. By automating
tasks like catalog management and book tracking, 
this system aims to save time, reduce errors, and
offer a smooth user experience for everyone 
involved. Ultimately, I hope it will become a 
valuable tool for our school library and make 
accessing books more convenient for students and
staff alike.""",font=("Arial Bold", 19), text_color="#FFF")
label_tab_2.pack(pady=20)

button_sign_in = CTkButton(master=sidebar_frame2, text="Sign In", fg_color="#207244", corner_radius=5, width=300, height=50, font=("Arial Bold", 18))
button_sign_in.pack(side="bottom", pady = 20)

button_sign_up = CTkButton(master=sidebar_frame2, text="Sign Up", fg_color="#207244", corner_radius=5, width=300, height=50, font=("Arial Bold", 18))
button_sign_up.pack(side="bottom", pady = 20)




window.mainloop()
