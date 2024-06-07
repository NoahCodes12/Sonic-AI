from openai import OpenAI

 #Set the API key for OpenAI
apiKey = "sk-proj-eg1dLsso5B2Q7W6IK1g4T3BlbkFJeqOkZL960QxNUDr8MJA6"
Client = OpenAI(api_key=apiKey)



#Diese Funktion sendet einen Prompt (Eingabe) an das GPT-3.5-Modell und gibt die Antwort zurück. 
#interagiert mit Modell.
def chat_with_gpt(prompt):
    response = Client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


#Diese Funktion generiert ein zufälliges deutsches Wort ohne die englische Übersetzung. 
#Sie verwendet die chat_with_gpt-Funktion, um den Prompt an das Modell zu senden.
def get_random_german_word():
    prompt = "Please provide a random German word without the English translation."
    return chat_with_gpt(prompt).strip()


#Diese Funktion überprüft, ob die vom Benutzer eingegebene Übersetzung korrekt ist. 
#Sie sendet den Prompt an das Modell und gibt die Antwort zurück.
def check_translation(german_word, user_translation):
    prompt = f"Is the English translation of the German word '{german_word}' '{user_translation}'? If it is incorrect, please provide the correct translation."
    return chat_with_gpt(prompt).strip()



#Schleife zur Wortgenerierung und Übersetzungsprüfung: Die while-Schleife läuft ununterbrochen, 
#bis der Benutzer "quit", "exit" oder "bye" eingibt.

#Zufälliges deutsches Wort: get_random_german_word wird aufgerufen, 
#um ein zufälliges deutsches Wort zu generieren.

#Benutzereingabe: Der Benutzer wird aufgefordert, das Wort ins Englische zu übersetzen.
#Überprüfung: check_translation wird aufgerufen, um die Benutzereingabe zu überprüfen.
#Ergebnisanzeige: Wenn die Übersetzung korrekt ist, wird "Correct!" angezeigt und
#eine neue Vokabel wird generiert. Wenn die Übersetzung falsch ist, wird die korrekte Übersetzung angezeigt und die Schleife beginnt erneut ohne ein neues Wort zu generieren.
def main():
    while True:
        # Hole ein zufälliges deutsches Wort von ChatGPT
        german_word = get_random_german_word()
        
        # Frage den Benutzer nach der Übersetzung
        print(f"You: Translate '{german_word}' into English")
        user_translation = input("Your translation: ").strip()
        
        if user_translation.lower() in ["quit", "exit", "bye"]:
            break

        # Überprüfe die Übersetzung
        response = check_translation(german_word, user_translation)
        #print("das ist die antwort:",response)
        if "Yes" in response:
            print("Chatbot: Correct!")
            #continue  # Generiere eine neue Vokabel
        else:
            correct_translation = response.split('correct translation is ')[-1]
            print(f"Chatbot: Incorrect. {correct_translation}")
            # Starte die Schleife neu, ohne eine neue Vokabel zu generieren
        
        print()

if __name__ == "__main__":
    main()
