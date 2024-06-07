# Default
import os

from groq import Groq

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("add your key here"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": "tell me about india" #add your question here 
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)
