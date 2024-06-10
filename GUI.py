import customtkinter as ctk
from PIL import Image,ImageTk
import tkinter as tk
import json
from colorama import Fore, Style
import AI as ai
import Vokabel as vokabel
import LoginGUI as lg
import subprocess

# import os
# import shutil

# var definition
FILE_NAME = "vlt.json"
USER_INPUT = []
USER_NAME = "NONE"



# Get user input and process it
def UserInput():
    UserGet=textbox.get("1.0",'end-1c')
    print(f"{Style.BRIGHT}{Fore.CYAN}User input retrieved: {Style.NORMAL}{Fore.BLACK}'{UserGet}'")
    # dict scheme to map how to save the user input
    DATATB = {
        f"{USER_NAME}" : f"{UserGet}"
    }

    for key, value in DATATB.items():
        # scheme to set the example
        scheme = f"{key}: {value}"
        # actual insertions
        scroll.insert(tk.END, scheme + "\n")
        # clearing the textbox
        textbox.delete("1.0", tk.END)
        # append user data to USER_INPUT
        USER_INPUT.append(scheme)
    response = ai.chat_with_gpt(UserGet)
    scroll.insert(tk.END, "Assistant: " + response + "\n")
    # ai.speak(response)
    print(f"{Style.BRIGHT}{Fore.CYAN}Assistant input retrieved: {Style.NORMAL}{Fore.BLACK}{response}")

def Login():
    subprocess.run(["python", "LoginGUI.py"])

def Vokabel():
    subprocess.run(["python","Vokabel.py"])



# init window
root = ctk.CTk()
root.geometry('600x440')
root.title('Sonic-AI')
root.iconbitmap('Bild.ico')
image_send= ImageTk.PhotoImage(Image.open('mingcute--send-fill (1).png'))
image_speak=ImageTk.PhotoImage(Image.open('iconoir--microphone-solid (1).png'))

# saving image to variable
dark_image = Image.open("sonic-running-run.png")
# using ctkimage element to add image to
bild = ctk.CTkImage(dark_image=dark_image, size= (80, 80))

# putting the image inside a label
label = ctk.CTkLabel(root, image=bild, text="")
# placing the label
label.place(x=1000, y=30)


# button to handle sending user input
send=ctk.CTkButton(root, width=50, height=50,text="", image=image_send, font=('Arial', 18), command=UserInput)
send.place(x=1155,y=590)

speak = ctk.CTkButton(root, width=50, height=50,text="", image=image_speak, font=('Arial', 18), command=ai.listen_and_recognize) # letting recognize function handle it
speak.place(x=1210,y=590)

# Title
label=ctk.CTkLabel(root, text="Sonic-AI", font=('Arial', 100))
label.pack(padx=20, pady=20)

# text box for user and ai input
textbox=ctk.CTkTextbox(root, width=900, height=50, font=('Arial', 16,), fg_color="white", text_color="black")
textbox.place(x=250, y=590)



blackjack=ctk.CTkButton(root, text="Blackjack", width=150, height=50, font=('Arial', 30))
blackjack.place(x=20, y=315)

def new_chat():
    scroll.delete("1.0", ctk.END)

newchat=ctk.CTkButton(root, text="New Chat", width=150, height=50, font=('Arial', 30), command=new_chat)
newchat.place(x=20, y=380)

# exit function for exit button
def exit():
    root.quit()
# exit button
Exit=ctk.CTkButton(root, text="Quit",font=("Arial", 30), command=exit, width=150, height=50)
Exit.place(x=20, y=40)

# login button
Login=ctk.CTkButton(root, text="Login",font=("Arial", 30), width=150, height=50, command=Login)
Login.place(x=1350, y=40)

# scroll = ctk.CTkScrollableFrame(root, width=980, height=390, fg_color="white")
# scroll.place(x=250, y=188)
scroll = ctk.CTkTextbox(root, width=1010, height=390, fg_color="white", text_color="lime", font=("Helvetica", 20))
scroll.place(x=250, y=188)

#
# function to show choice clicked in dropdown
def combobox_callback(choice):
    print(f"{Style.BRIGHT}{Fore.BLUE}dropdown clicked: {Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}{choice}")

combovalues = ["chat", "practice"]

reference_dict = {

    combovalues[1] : Vokabel

} 

def onChoice(choice):
    if choice in reference_dict:
        reference_dict[choice]()

# dropdown menu
combobox = ctk.CTkComboBox(root,values=combovalues, command=onChoice, width=150, height=50)
combobox.place(x=20, y=188)

english_knowledge = ctk.CTkComboBox(root,values=["Level 1", "Level 2", "Level 3"],command=combobox_callback, width=150, height=50)
english_knowledge.place(x=20, y=250)

root.mainloop()
