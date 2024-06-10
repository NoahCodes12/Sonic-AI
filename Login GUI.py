import customtkinter as ctk
from PIL import Image,ImageTk
# import rsvg,cairo 
import tkinter as tk



#Opens the window and forces it to stay in out of Fullscreen
root = ctk.CTk()
root.attributes("-fullscreen", False)
root.resizable(False, False)  # Disable window resizing
root.geometry('400x440')
root.title('Sonic-AI')
root.iconbitmap('Bild.ico')
image_send= ImageTk.PhotoImage(Image.open('mingcute--send-fill (1).png'))

#Login Frames and the Login Label
LoginFrameOuter = ctk.CTkFrame(root, width=320, height=360, border_color="Green")
LoginFrameInner = ctk.CTkFrame(root, width=180, height=100, border_color="White")
LoginLabel = ctk.CTkLabel(root,width=280, height=140,font=("Arial", 70), text="Login",justify="center")

UserLabel = ctk.CTkLabel(root, width=90, height=50, font=("Arial", 10), text="  Name:                                                          ")
AgeLabel = ctk.CTkLabel(root, width=90, height=50, font=("Arial", 10), text="  Age:                                                              ")
#Enter the Data for Login so you can save it
Users=ctk.CTkEntry(root, width=100, height=20, font=("Arial", 20))
Age=ctk.CTkEntry(root, width=100, height=20, font=("Arial", 20), )
button=ctk.CTkButton(root, width=172, height=50,text="", image=image_send, font=('Arial', 18), command=)
#Places all UI elements
button.place(x=110, y=310)
LoginFrameOuter.place(x=40,y=35)
LoginFrameInner.place(x=60,y=50)
LoginLabel.place(x=60, y=50)
UserLabel.place(x=110,y=230, relx=0, anchor='w')
AgeLabel.place(x=110, y=280, relx=0, anchor='w')
Users.place(x=170, y=218)
Age.place(x=170, y=268)
root.mainloop()