import customtkinter as ctk
#import tkinter as tk
import funcs as fs
import CTkMessagebox as ctkm
from PIL import Image as img
from PIL import ImageTk as imgt
import random
    
root = ctk.CTk()
root.geometry('600x440')
root.title('Sonic-AI')
root.iconbitmap('Bild.ico')
# remember to have the slashes be the correct way or else error (pain)
# self.root.iconbitmap('icons8-file-folder-48.png')
label=ctk.CTkLabel(root, text="Sonic-AI", font=('Arial', 36))
label.pack(padx=20, pady=20)

textbox=ctk.CTkTextbox(root, width=1000, height=41, font=('Arial', 16,), fg_color="white", text_color="black")
textbox.place(x=200, y=600)
button=ctk.CTkButton(root, width=100, height=41, text="Senden", font=('Arial', 18))
button.place(x=1200,y=600)
def exit():
    root.quit()
Exit=ctk.CTkButton(root, text="Quit", command=exit)
Exit.pack()

scroll = ctk.CTkScrollableFrame(root, width=980, height=390, fg_color="white")
scroll.place(x=200, y=188)

root.mainloop()




