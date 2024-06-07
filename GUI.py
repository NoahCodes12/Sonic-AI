import customtkinter as ctk
from PIL import Image,ImageTk
# import rsvg,cairo 
import tkinter as tk
import json

FILE_NAME = "vlt.json"
USER_INPUT = []
USER_NAME = "Test"

def User_Input():
    UserGet=textbox.get("1.0",'end-1c')
    print(UserGet)
    USER_INPUT.append(UserGet)
    i = 0
    for element in USER_INPUT:
        print(f"{USER_NAME}: {USER_INPUT[i]}")
        with open(FILE_NAME, 'a') as obj:
            data = json.dump(f"{USER_NAME} : {USER_INPUT[i]},", obj)
        # test
        # UserText = ctk.CTkLabel(scroll, width=50, height=50, font=("Arial", 16), text=USER_INPUT)
        # UserText.pack()
    i+=1

root = ctk.CTk()
root.geometry('600x440')
root.title('Sonic-AI')
root.iconbitmap('Bild.ico')
image_send= ImageTk.PhotoImage(Image.open('mingcute--send-fill (1).png'))

# saving image to variable
dark_image = Image.open("sonic-running-run.png")
# using ctkimage element to add image to
bild = ctk.CTkImage(dark_image=dark_image, size= (80, 80))

# putting the image inside a label
label = ctk.CTkLabel(root, image=bild, text="")
# placing the label
label.place(x=1000, y=30)

label=ctk.CTkLabel(root, text="Sonic-AI", font=('Arial', 100))
label.pack(padx=20, pady=20)

textbox=ctk.CTkTextbox(root, width=900, height=50, font=('Arial', 16,), fg_color="white", text_color="black")
textbox.place(x=250, y=600)

button=ctk.CTkButton(root, width=100, height=50,text="", image=image_send, font=('Arial', 18), command=User_Input)
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
