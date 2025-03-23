import os
import google.generativeai as genai


genai.configure(api_key="AIzaSyAlu3Fzw-4jzNUnjyNb7RB8WPUJ9AhwGW4")  

model = genai.GenerativeModel("gemini-1.5-flash")  

chat_session = model.start_chat(history=[])

print("NaeemGPT: Hello, how can I help you?")
print()

while True:
    user_input = input("You: ").strip()
    print()

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! Have a great day! 😊")
        break 


    response = chat_session.send_message(user_input)
    model_response = response.text

    print(f'Bot: {model_response}')
    print()
