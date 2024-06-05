import customtkinter as ctk
import tkinter as tk
fenster=ctk.CTk()
fenster._set_appearance_mode("system")
fenster.title("Sonic-AI")
fenster.geometry("700x500")
fenster.iconbitmap('Icon.ico')
def execute():
 fenster.quit()
def login():
 print("Nah")
Frame1=ctk.CTkScrollableFrame(fenster, width=200, height=200)
Exit=ctk.CTkButton(fenster, text="Quit", command=execute)
blud= ctk.CTkEntry(fenster, placeholder_text= "Schreib was rein pls", show="Lorem Ipsum")
AiWindow=ctk.CTkLabel(fenster, height=200, width=200, text="", bg_color="Navy")
AiWindow.configure(state="disable")
Frame1.pack()
AiWindow.pack()
blud.pack()
Exit.pack()
fenster.mainloop()
