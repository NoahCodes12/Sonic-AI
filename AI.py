import os
import speech_recognition as sr
from gtts import gTTS
from openai import OpenAI  # Import für die OpenAI-API
from colorama import Fore, Style
import playsound

# OpenAI API-Schlüssel (stellen Sie sicher, dass dieser Schlüssel sicher ist und nicht öffentlich geteilt wird)
apiKey = "sk-proj-5jLZmHTAYBQMRuFZdkxwT3BlbkFJsMmRcfD4tCgsqweWzcbI"
Client = OpenAI(api_key=apiKey)

def listen_and_recognize():
    # Diese Funktion verwendet das Mikrofon, um gesprochenen Text zu erfassen und mit der Google Web Speech API zu erkennen.
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"{Style.BRIGHT}{Fore.GREEN}Please speak into the microphone..")
        audio_data = recognizer.listen(source)
        print(f"{Fore.RED}{Style.BRIGHT}Processing...")
        try:
            # Verwende die Google Web Speech API, um den Text zu erkennen
            text = recognizer.recognize_google(audio_data, language='de-DE')
            print(f"{Style.BRIGHT}{Fore.CYAN}Recognized input: {text}")
            return text
        except sr.UnknownValueError:
            # Fehlerbehandlung, falls die Spracherkennung den Text nicht verstehen konnte
            print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Speechrecognition was unable to understand the request.")
            return None
        except sr.RequestError as e:
            # Fehlerbehandlung, falls ein Fehler bei der Anforderung der Ergebnisse auftritt
            print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Exception raised: {e}")
            return None
        
def chat_with_gpt(prompt):
    # Diese Funktion sendet den erkannten Text an GPT-3 und erhält eine Antwort.
    response = Client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def speak(text):
    # Diese Funktion verwendet gTTS, um den verarbeiteten Text in Sprache umzuwandeln und als Audiodatei zu speichern und abzuspielen.
    tts = gTTS(text=text, lang='de')  # Verwandle Text in Sprache (Deutsch)
    tts.save("response.mp3")  # Speichere die Sprachausgabe in einer MP3-Datei
    playsound.playsound("response.mp3")  # Spiele die MP3-Datei ab (Windows-Befehl)

if __name__ == "__main__":
    # Hauptteil des Programms:
    # 1. Erfasse den gesprochenen Text.
    # 2. Verarbeite den erkannten Text.
    # 3. Verwandle den verarbeiteten Text in Sprache und spiele ihn ab.
    while True:
        recognized_text = listen_and_recognize()  # Erfasse und erkenne den gesprochenen Text
        if recognized_text:  # Wenn der Text erfolgreich erkannt wurde
            gpt_response = chat_with_gpt(recognized_text)  # Sende den erkannten Text an GPT-3 und erhalte eine Antwort
            print(f"Assistant: {gpt_response}")  # Gib die Antwort von GPT-3 aus
            speak(gpt_response)  # Verwandle die Antwort in Sprache und spiele sie ab
        else:
            print("No valid input recognized, try again?")
