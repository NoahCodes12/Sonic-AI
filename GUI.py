import customtkinter as ctk
#from PIL import Image
from PIL import Image,ImageTk
# import rsvg,cairo 
import tkinter as tk
#def User_Input():

#def AI_Answer():





root = ctk.CTk()
root.geometry('600x440')
root.title('Sonic-AI')
root.iconbitmap('Bild.ico')
image_send= ImageTk.PhotoImage(Image.open('mingcute--send-fill (1).png'))
# self.root.iconbitmap('icons8-file-folder-48.png')
label=ctk.CTkLabel(root, text="Sonic-AI", font=('Arial', 100))
label.pack(padx=20, pady=20)

textbox=ctk.CTkTextbox(root, width=900, height=50, font=('Arial', 16,), fg_color="white", text_color="black")
textbox.place(x=250, y=600)

button=ctk.CTkButton(root, width=100, height=50,text="", image=image_send, font=('Arial', 18))
button.place(x=1155,y=600)

def exit():
    root.quit()
Exit=ctk.CTkButton(root, text="Quit",font=("Arial", 30), command=exit, width=150, height=50)
Exit.place(x=1200, y=40)

Login=ctk.CTkButton(root, text="Login",font=("Arial", 30), width=150, height=50)
Login.place(x=1350, y=40)

scroll = ctk.CTkScrollableFrame(root, width=980, height=390, fg_color="white")
scroll.place(x=250, y=188)


def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = ctk.CTkComboBox(root,values=["practice", "option2"],command=combobox_callback, width=150, height=50)

combobox.place(x=20, y=188)
root.mainloop()




