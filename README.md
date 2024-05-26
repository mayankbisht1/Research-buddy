# Research-buddy
This project is dedicated to all those students with Master's or PhD or Professor to help them with their research interests, daily tasks and much more
Imagine a personalized AI chat box that tells you when to submit your thesis, how you are going to be your PhD supervisor, and when will the next nearest research conference, TA, or RA duty in the upcoming week.
Using the potential of Pathway LLM and long-chain, the potential is immense, and the example shown above is just the tip of the iceberg.
## Steps for installation
Install Pathway , Langchain and other required packages.
```
pip install langchain openai chromadb tiktoken unstructured
```
You can edit constants.py. default to your OpenAI API key and rename constants.py. and put your data in data/data.txt.

## Some prompt examples 
>When is my next TA duty. Also tell me room no and course no. 
```
YOur next TA duty will be on 7th July in room no. 101 with Btech group-4.
```
