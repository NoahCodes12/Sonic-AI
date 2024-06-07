from openai import OpenAI # type: ignore
 
apiKey = "sk-proj-eg1dLsso5B2Q7W6IK1g4T3BlbkFJeqOkZL960QxNUDr8MJA6" # type: ignore
Client = OpenAI(api_key=apiKey)
# handle
def chat_with_gpt(prompt):
    response = Client.chat.completions.create( # type: ignore
        model="gpt-3.5-turbo",
        messages =[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# output
if __name__=="__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
 
        response = chat_with_gpt(user_input)
        print("chatbot: ", response)