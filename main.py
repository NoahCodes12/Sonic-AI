from openai import OpenAI

# Initialize the OpenAI client with the API key
apiKey = "sk-proj-z1nBaNtKFNwSqt6zjgCMT3BlbkFJslEuF5kuV0FaiWW1u5pH"
Client = OpenAI(api_key=apiKey)

def chat_with_gpt(prompt):
    response = Client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

if __name__ == "__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("chatbot: ", response)
