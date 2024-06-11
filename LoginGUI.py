
import customtkinter as ctk
from PIL import Image,ImageTk
# import rsvg,cairo 
import tkinter as tk

def Login_GUI():

    #Opens the window and forces it to stay in out of Fullscreen
    root = ctk.CTk()
    root.attributes("-fullscreen", False)
    root.resizable(False, False)  # Disable window resizing
    root.geometry('400x460')
    root.title('Sonic-AI')
    root.iconbitmap('Bild.ico')
    image_send1 = ImageTk.PhotoImage(Image.open('fluent--send-28-filled (1).png'))

    #Login Frames and the Login Label
    LoginFrameOuter = ctk.CTkFrame(root, width=320, height=400)
    LoginFrameInner = ctk.CTkFrame(root, width=180, height=100)
    LoginLabel = ctk.CTkLabel(root,width=280, height=140,font=("Arial", 70), text="Login",justify="center")

    #Enter the Data for Login so you can save it
    Users=ctk.CTkEntry(root, width=197, height=30, font=("Arial", 18), placeholder_text="Name")
    Age=ctk.CTkEntry(root, width=197, height=30, font=("Arial", 18), placeholder_text="Age")
    Knowledge=ctk.CTkEntry(root, width=197, height=30, font=("Arial", 18), placeholder_text="English knowledge lvl")
    Login_Button=ctk.CTkButton(root, width=197, height=50, text="",image=image_send1, font=('Arial', 18))
    #Places all UI elements
    Login_Button.place(x=100, y=360)
    LoginFrameOuter.place(x=40,y=35)
    LoginFrameInner.place(x=60,y=50)
    LoginLabel.place(x=60, y=50)
    Users.place(x=100, y=220)
    Age.place(x=100, y=270)
    Knowledge.place(x=100, y=320)
    root.mainloop()
