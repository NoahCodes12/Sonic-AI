import time
import speech_recognition as sr
from openai import OpenAI
import pyttsx3

# Set the API key for OpenAI
apiKey = "sk-proj-5jLZmHTAYBQMRuFZdkxwT3BlbkFJsMmRcfD4tCgsqweWzcbI"
Client = OpenAI(api_key=apiKey)

def listen_and_recognize():
    """
    Diese Funktion verwendet das Mikrofon, um gesprochenen Text zu erfassen und 
    mit der Google Web Speech API zu erkennen. Der erkannte Text wird zurückgegeben.
    """
    recognizer = sr.Recognizer()  # Initialisiere den Spracherkenner
    with sr.Microphone() as source:  # Verwende das Mikrofon als Audioquelle
        print("Bitte sprechen Sie das deutsche Wort...")
        audio_data = recognizer.listen(source)  # Erfasse Audio-Daten vom Mikrofon
        print("Erkennung läuft...")
        try:
            # Verwende die Google Web Speech API, um den Text zu erkennen
            text = recognizer.recognize_google(audio_data, language='de-DE')
            print(f"Erkanntes Wort: {text}")
            return text
        except sr.UnknownValueError:
            # Fehlerbehandlung, falls die Spracherkennung den Text nicht verstehen konnte
            print("Die Spracherkennung konnte das Audio nicht verstehen")
            return None
        except sr.RequestError as e:
            # Fehlerbehandlung, falls ein Fehler bei der Anforderung der Ergebnisse auftritt
            print(f"Fehler bei der Anforderung der Ergebnisse; {e}")
            return None

def chat_with_gpt(prompt):
    
    #Diese Funktion sendet einen Prompt (Eingabe) an das GPT-3.5-Modell und gibt die Antwort zurück.
    
    response = Client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    # Gibt den Inhalt der ersten Antwort des Modells zurück.
    return response.choices[0].message.content.strip()

def speak(text):
    """
    Diese Funktion verwendet pyttsx3, um den verarbeiteten Text in Sprache umzuwandeln
    und direkt auszugeben.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_random_german_word(sprachniveau):
    
   # Geneiert ein zufälliges deutsches Wort, indem ein Prompt an GPT-3 gesendet wird.
    
    prompt = f"Please provide a random German word at language level {sprachniveau} without the English translation"
    return chat_with_gpt(prompt).strip()

def check_translation(german_word, user_translation):
    
   # Überprüft die vom Benutzer eingegebene Übersetzung des deutschen Wortes.
    
    #es wird ein prompt an chat gpt gesendet um zu kontrollieren, ob die übersetzung richtig ist.
    prompt = f"Is the English translation of the German word '{german_word}' '{user_translation}'? If it is incorrect, please provide the correct translation."
    return chat_with_gpt(prompt).strip()

def get_sprachniveau():
    
   # Fragt den Benutzer nach dem gewünschten Sprachniveau und gibt es zurück.
    
    sprachniveaus = ["A1", "A2", "B1", "B2", "C1", "C2"]
    print("Bitte geben Sie Ihr gewünschtes Sprachniveau ein (A1, A2, B1, B2, C1, C2):")
    while True:
        sprachniveau = input().strip().upper()
        if sprachniveau in sprachniveaus:
            return sprachniveau
        else:
            print("Ungültiges Sprachniveau. Bitte versuchen Sie es erneut:")

def ask_to_advance_level(current_level):
    """
    Fragt den Benutzer, ob er zum nächsten Sprachniveau wechseln möchte.
    """
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

def main():
    """
    Hauptfunktion des Programms:
    1. Frage den Benutzer nach dem Sprachniveau.
    2. Erfasse das gesprochene deutsche Wort.
    3. Verarbeite den erkannten Text.
    4. Überprüfe die Übersetzung mit ChatGPT.
    5. Gib die Antwort von ChatGPT als Audio aus.
    6. Nach fünf korrekten Antworten frage den Benutzer, ob er das Sprachniveau erhöhen möchte.
    """
    sprachniveau = get_sprachniveau()
    correct_streak = 0

    while True:
        # Hole ein zufälliges deutsches Wort von ChatGPT
        german_word = get_random_german_word(sprachniveau)
        
        # Frage den Benutzer nach der Übersetzung
        print(f"Chatbot: Translate '{german_word}' into English")
        speak(f"Bitte übersetzen Sie '{german_word}' ins Englische")

        user_translation = listen_and_recognize()  # Erfasse die gesprochene Übersetzung
        if not user_translation:
            continue  # Wenn keine Übersetzung erkannt wurde, erneut versuchen

        if user_translation.lower() in ["quit", "exit", "bye"]:
            break

        # Überprüfe die Übersetzung
        response = check_translation(german_word, user_translation)
        if "Yes" in response:
            print("Chatbot: Correct!")
            speak("Richtig!")
            correct_streak += 1
        else:
            # Extrahiere die richtige Antwort aus dem Modell
            correct_translation = response.split('correct translation of the German word ')[-1]
            # Extrahiere die eigentliche Übersetzung aus dem vollständigen Satz
            correct_translation = correct_translation.split(' is ')[-1].replace('.', '').strip()
            # Gibt an, wenn Übersetzung falsch und gibt richtiges Wort aus
            print(f"Chatbot: Falsch. Die richtige Übersetzung ist {correct_translation}.")
            speak(f"Falsch. Die richtige Übersetzung ist {correct_translation}.")
            correct_streak = 0
        
        print()

        # Nach fünf richtigen Antworten den Benutzer fragen, ob er das Sprachniveau erhöhen möchte
        if correct_streak >= 2:
            advance, next_level = ask_to_advance_level(sprachniveau)
            if advance:
                sprachniveau = next_level
                correct_streak = 0  # Zurücksetzen der Streak für das neue Niveau
            else:
                correct_streak = 0  # Zurücksetzen der Streak, wenn nicht gewechselt wird

if __name__ == "__main__":
    main()
