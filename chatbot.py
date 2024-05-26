```import os

from groq import Groq

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("Enter your API key here"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": "What is weather today" # add your new question here
        }
    ],
    model="mixtral-8x7b-32768", # you could change the model refer documentation for Groq
)

print(chat_completion.choices[0].message.content)```
