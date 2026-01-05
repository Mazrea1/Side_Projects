#Use commands in terminal, then run code below:
"""
install ollama
ollama run gemma3
"""
import ollama

response = ollama.chat(
    model='gemma3',
    messages=[
        {
            'role': 'user',
            'content': 'Hello! How are you today?',
        },
    ],
)

print(response['message']['content'])

#Change the string in content to ask different questions or give different prompts to the AI model.