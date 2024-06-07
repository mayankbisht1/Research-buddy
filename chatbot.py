import os
import fitz  # PyMuPDF
import spacy
from groq import Groq

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Function to summarize text using SpaCy
def summarize_text(text):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    summary = " ".join(sentences[:1000])  # Summarize the whole pdf
    return summary

# Function to read PDF and summarize content
def read_and_summarize_pdf(file_path):
    document = fitz.open(file_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    summary = summarize_text(text)
    return summary

# Path to your PDF file
pdf_path = r"/home/path-to-file/main.pdf" # Add path to your pdf here

# Read and summarize the PDF content
pdf_summary = read_and_summarize_pdf(pdf_path)

# Retrieve the API key from the environment variable
api_key = os.environ.get("Add your API key here")

# Initialize the Groq client with the retrieved API key
client = Groq(
    api_key=api_key
)

# Create a chat completion with the summarized PDF text as context
pdf_summary_chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "explain mechanism of ionic liquids" # ask your question here
        }
    ],
    model="mixtral-8x7b-32768",
)

# Print the response
print("Summary of PDF:", pdf_summary)
print("Response from GROQ API:", pdf_summary_chat_completion.choices[0].message.content)
