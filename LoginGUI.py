import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
import Save as s

def Login_GUI():
    # Opens the window and forces it to stay out of Fullscreen
    root = ctk.CTk()
    root.attributes("-fullscreen", False)
    root.resizable(False, False)  # Disable window resizing
    root.geometry('400x460')
    root.title('Sonic-AI')
    root.iconbitmap('Bild.ico')

    # Login Frames and the Login Label
    LoginFrameOuter = ctk.CTkFrame(root, width=320, height=400)
    LoginFrameInner = ctk.CTkFrame(root, width=180, height=100)
    LoginLabel = ctk.CTkLabel(root, width=280, height=140, font=("Arial", 70), text="Login", justify="center")

    # Enter the Data for Login so you can save it
    Users = ctk.CTkEntry(root, width=197, height=30, font=("Arial", 18), placeholder_text="Name")
    Age = ctk.CTkEntry(root, width=197, height=30, font=("Arial", 18), placeholder_text="Age")
    Knowledge = ctk.CTkEntry(root, width=197, height=30, font=("Arial", 18), placeholder_text="English knowledge lvl")

    def submit_action():
        usrname = Users.get()
        usrage = Age.get()
        knlvl = Knowledge.get()
    
        # Debugging prints
        print(usrname)
        print(usrage)
        print(knlvl)

        # Collecting user information from the person class
        s.collect_user_info(usrname, usrage, knlvl)
        root.quit()

    Login_Button = ctk.CTkButton(root, width=197, height=50, text="Submit", font=('Arial', 18), command=submit_action)

    # Places all UI elements
    LoginFrameOuter.place(x=40, y=35)
    LoginFrameInner.place(x=60, y=50)
    LoginLabel.place(x=60, y=50)
    Users.place(x=100, y=220)
    Age.place(x=100, y=270)
    Knowledge.place(x=100, y=320)
    Login_Button.place(x=100, y=360)

    root.mainloop()

Login_GUI()
