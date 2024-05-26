# Research-buddy
This project is useful to all those students with Bachelor's, Master's or PhD or Professor to help them with their research interests, daily tasks and much more
Imagine a personalized AI chat box that tells you when to submit your thesis, how you will be your PhD supervisor, and when the next nearest research conference, TA, or RA duty will be in the upcoming week.
Using the potential of Pathway LLM and long-chain, the potential is immense, and the example shown above is just the tip of the iceberg.

## Steps for installation
Install Pathway, Langchain, Groq and other required packages.
```
pip install langchain openai chromadb tiktoken unstructured
```
You can edit `constants.py.default` to your OpenAI API key, rename `constants.py.`, and put your data in `data/data.txt`.

##  1.Data Pipeline (For docs uploaded in Google Drive)
To initialize and set up the client, you must give either the URL or the host and port of your document indexing pipeline. The code provided utilizes a publicly accessible demonstration pipeline, which can be accessed using the REST API at `https://demo-document-indexing.pathway.stream.` This demonstration imports documents from Google Drive and Sharepoint and creates an index for efficiently accessing the information.

## 2. Data stored in local drive 
So you want to store data locally no problem! Follow the steps:
### Step 1 : Clone the entire repository  
`git clone <https://github.com/username/repository.git>`

### Step 2: Create a new file .env 
Build a .env file in the project's main directory using the touch command `touch .env`

### Step 3: Using windows 

set `OPENAI_API_TOKEN={OPENAI_API_KEY}`

set `EMBEDDER_LOCATOR=text-embedding-ada-002`

set `EMBEDDING_DIMENSION=1536`

set `MODEL_LOCATOR=gpt-3.5-turbo`

set `MAX_TOKENS=200`

set `TEMPERATURE=0.0`

set `DROPBOX_LOCAL_FOLDER_PATH={REPLACE_WITH_DROPBOX_RELATIVE_PATH}`


## 3. For free API key use GROQ or other (small chatbot)

install groq to same repository
```pip install groq```

create file chatbot.py ``` vim chatbot.py``` or ```nano chatbot.py```
copy the following and edit question 
```import os

from groq import Groq

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": "What is weather today" # add your question here
        }
    ],
    model="mixtral-8x7b-32768", # could change the model refer documentation for Groq
)

print(chat_completion.choices[0].message.content)```


execute 
```python chatbot.py```



## Some prompt examples 
>When is my next TA duty. Also tell me room no and course no. 
```
YOur next TA duty will be on 7th July in room no. 101 with Btech group-4.
```
