import time
import speech_recognition as sr
from openai import OpenAI
import pyttsx3
import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
import subprocess
import json
from colorama import Fore, Style
from LoginGUI import Login_GUI


# Set the API key for OpenAI
apiKey = "sk-proj-gqTSALSOM8gLbLxeZPCsT3BlbkFJCdCkLGw7TXP6OMEhDhyI"
Client = OpenAI(api_key=apiKey)



# JSON-Datei laden und den letzten Eintrag verwenden
def load_last_user_name_from_json(file_path, key):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list) and len(data) > 0:
                last_entry = data[-1]
                if key in last_entry:
                    return last_entry[key]
                else:
                    raise KeyError(f'Schlüssel "{key}" wurde im letzten Eintrag nicht gefunden.')
            else:
                raise ValueError('Die JSON-Daten sind keine Liste oder die Liste ist leer.')
    except FileNotFoundError:
        raise FileNotFoundError(f'Datei "{file_path}" wurde nicht gefunden.')
    except json.JSONDecodeError:
        raise ValueError(f'Datei "{file_path}" ist keine gültige JSON-Datei.')
 
# Benutzername aus JSON laden
json_file_path = 'user_data.json'
key = 'name'
 
try:
    USER_NAME = load_last_user_name_from_json(json_file_path, key)
except (FileNotFoundError, KeyError, ValueError) as e:
    USER_NAME = str(e)
    




# Global variables
current_german_word = None
USER_INPUT = []
current_level = "A1"  # Default level
 
# Get user input and process it
def UserInput():
    UserGet = textbox.get("1.0", 'end-1c')
    print(f"{Style.BRIGHT}{Fore.CYAN}User input retrieved: {Style.NORMAL}{Fore.BLACK}'{UserGet}'")
    # dict scheme to map how to save the user input
    DATATB = {
        f"{USER_NAME}": f"{UserGet}"
    }
 
    for key, value in DATATB.items():
        # scheme to set the example
        scheme = f"{key}: {value}"
        # actual insertions
        output.insert(tk.END, scheme + "\n", "user")
        # clearing the textbox
        textbox.delete("1.0", tk.END)
        # append user data to USER_INPUT
        USER_INPUT.append(scheme)
    response = chat_with_gpt(UserGet)
    output.insert(tk.END, "Dr. Robotnik: " + response + "\n\n", "assistant" )
    print(f"{Style.BRIGHT}{Fore.CYAN}Assistant input retrieved: {Style.NORMAL}{Fore.BLACK}{response}")
 
 
def Log():
    Login_GUI()
 
 
def listen_and_recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        practice_output.insert(tk.END, "Bitte sprechen Sie das deutsche Wort...\n", "assistent")
        root.update_idletasks()
        print(f"Bitte sprechen Sie das deutsche Wort...")
        audio_data = recognizer.listen(source)
        practice_output.insert(tk.END, "Erkennung läuft...\n", "assistent")
        root.update()
        print("Erkennung läuft...")
        root.update()
        try:
            text = recognizer.recognize_google(audio_data, language='de-DE')
            practice_output.insert(tk.END, f"Erkanntes Wort: {text}\n", "user")
            print(f"Erkanntes Wort: {text}")
            return text
        except sr.UnknownValueError:
            error_message = "Die Spracherkennung konnte das Audio nicht verstehen"
            practice_output.insert(tk.END, error_message + "\n\n", "assistent")
            print(error_message)
            return None
        except sr.RequestError as e:
            error_message = f"Fehler bei der Anforderung der Ergebnisse; {e}"
            practice_output.insert(tk.END, error_message + "\n", "assistent")
            print(error_message)
            return None
 
def chat_with_gpt(prompt):
    response = Client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
 
def speak(text):
    print(f"Sprachausgabe: {text}")
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Fehler bei der Sprachausgabe: {e}")
 
def get_random_german_word(sprachniveau):
    prompt = f"Please provide a random German word at language level {sprachniveau} without the English translation"
    return chat_with_gpt(prompt).strip()
 
def check_translation(german_word, user_translation):
    prompt = f"Is the English translation of the German word '{german_word}' '{user_translation}'? If it is incorrect, please provide the correct translation."
    return chat_with_gpt(prompt).strip()
 
def get_sprachniveau():
    sprachniveaus = ["A1", "A2", "B1", "B2", "C1", "C2"]
    print("Bitte geben Sie Ihr gewünschtes Sprachniveau ein (A1, A2, B1, B2, C1, C2):")
    while True:
        sprachniveau = input().strip().upper()
        if sprachniveau in sprachniveaus:
            return sprachniveau
        else:
            print("Ungültiges Sprachniveau. Bitte versuchen Sie es erneut:")
 
def ask_to_advance_level(current_level):
    sprachniveaus = ["A1", "A2", "B1", "B2", "C1", "C2"]
    current_index = sprachniveaus.index(current_level)
    if current_index < len(sprachniveaus) - 1:
        next_level = sprachniveaus[current_index + 1]
        print(f"Möchten Sie zum nächsten Sprachniveau {next_level} wechseln? (ja/nein)")
        speak(f"Möchten Sie zum nächsten Sprachniveau {next_level} wechseln?")
       
        while True:
            response = listen_and_recognize()
            if response and response.lower() in ["ja", "nein"]:
                return response.lower() == "ja", next_level
            else:
                print("Ungültige Antwort. Bitte sagen Sie 'ja' oder 'nein'.")
                speak("Ungültige Antwort. Bitte sagen Sie 'ja' oder 'nein'.")
    return False, current_level
 



    


 
def speak_command():
    user_translation = listen_and_recognize()
    if user_translation:
        practice_output.insert (tk.END, f"{USER_NAME}: {user_translation}\n", "user")
        response = check_translation(current_german_word, user_translation)
        practice_output.insert(tk.END, "Dr. Robotnik: " + response + "\n\n", "assistent")
        if "Yes" in response:
            speak("Richtig!")
        else:
            correct_translation = response.split('correct translation of the German word ')[-1]
            correct_translation = correct_translation.split(' is ')[-1].replace('.', '').strip()
            root.update_idletasks()
            speak(f"Falsch. Die richtige Übersetzung ist {correct_translation}.")
 
def generate_random_word():
    global current_german_word
    current_german_word = get_random_german_word(current_level)
    practice_output.insert(tk.END, f"Dr. Robotnik: Bitte übersetzen Sie '{current_german_word}' ins Englische.\n")
    root.update_idletasks()
    speak(f"Bitte übersetzen Sie '{current_german_word}' ")
 
def new_chat():
    output.delete("1.0", ctk.END)
    practice_output.delete("1.0", ctk.END)
    root.update_idletasks()
    chat_with_gpt()
 
def new_practice():
    practice_output.delete("1.0", ctk.END)
    generate_random_word()
 
def exit():
    root.quit()
 
def onChoice(choice):
    if choice == "practice":
        practice_output.pack(padx=140, pady=37)
        new_practice()
    else:
        practice_output.pack_forget()


 
 # function to launch blackjack
def launch_Blackjack():
    subprocess.run(["python", "blackjack7.py"])
 
def set_sprachniveau(level):
    global current_level
    levels = {
        "Level 1": "A1",
        "Level 2": "A2",
        "Level 3": "B1",
    }
    current_level = levels.get(level, "A1")
    print(f"Sprachniveau gesetzt auf: {current_level}")
 



 
# Initialize window
root = ctk.CTk()
root.geometry('600x440')
root.title('Sonic-AI')
root.iconbitmap('Bild.ico')
image_send = ImageTk.PhotoImage(Image.open('mingcute--send-fill (1).png'))
image_speak = ImageTk.PhotoImage(Image.open('iconoir--microphone-solid (1).png'))
 
dark_image = Image.open("sonic-running-run.png")
bild = ctk.CTkImage(dark_image=dark_image, size=(80, 80))

dark_image = Image.open("Egger1.png")
bild1 = ctk.CTkImage(dark_image=dark_image, size=(80, 80))
 
label = ctk.CTkLabel(root, image=bild, text="")
label.place(x=480, y=30)

label = ctk.CTkLabel(root, image=bild1, text="")
label.place(x=1000, y=30)
 
send = ctk.CTkButton(root, width=50, height=50, text="", image=image_send, font=('Arial', 18), command=UserInput)
send.place(x=1155, y=590)
 
speak_button = ctk.CTkButton(root, width=50, height=50, text="", image=image_speak, font=('Arial', 18), command=speak_command)
speak_button.place(x=1210, y=590)
 
label = ctk.CTkLabel(root, text="Sonic-AI", font=('Arial', 100))
label.pack(padx=20, pady=20)
 
textbox = ctk.CTkTextbox(root, width=900, height=50, font=('Arial', 16), fg_color="white", text_color="black")
textbox.place(x=250, y=590)
 
newchat = ctk.CTkButton(root, text="New Chat", width=150, height=50, font=('Arial', 30), command=new_chat)
newchat.place(x=20, y=380)
 
Exit = ctk.CTkButton(root, text="Quit", font=("Arial", 30), command=exit, width=150, height=50)
Exit.place(x=20, y=40)
 
Login_button = ctk.CTkButton(root, text="Login", font=("Arial", 30), width=150, height=50, command=Log)
Login_button.place(x=1350, y=40)
 
output = ctk.CTkTextbox(root, width=1010, height=390, fg_color="white", text_color="lime", font=("Helvetica", 20))
output.tag_config("user", foreground="blue")
output.tag_config("assistant", foreground="green")
output.place(x=250, y=188)
 
practice_output = ctk.CTkTextbox(root, width=984, height=390, fg_color="white",bg_color="White", text_color="lime", font=("Helvetica", 20))
practice_output.tag_config("user", foreground="blue")
practice_output.tag_config("assistant", foreground="green")

combovalues = ["chat", "practice"]
 
combobox = ctk.CTkComboBox(root, values=combovalues, command=onChoice, width=150, height=50)
combobox.place(x=20, y=188)

english_knowledge = ctk.CTkComboBox(root, values=["Level 1", "Level 2", "Level 3"], command=set_sprachniveau, width=150, height=50)
english_knowledge.place(x=20, y=250) 

new_word_button = ctk.CTkButton(root, text="New Word", font=("Arial", 30), width=150, height=50, command=generate_random_word)
new_word_button.place(x=20, y=450)

# Additional Buttons
blackjack_button = ctk.CTkButton(root, text="Blackjack", width=150, height=50, font=('Arial', 30), command=launch_Blackjack)
blackjack_button.place(x=20, y=315)
 

 
root.mainloop()