import requests
from bs4 import BeautifulSoup  # BeautifulSoup is a library for parsing HTML and XML documents, extracting data from web pages.
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Read OpenAI API key from environment variables

def summarize_url(url):
    """Fetch and summarize the main content of a URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract main content text
    paragraphs = soup.find_all('p')
    text = ' '.join(p.get_text() for p in paragraphs)

    # Summarize text using OpenAI GPT-4 model
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": "You are an assistant that summarizes text."},
            {"role": "user", "content": f"Summarize the following text:\n{text}"}
        ]
    )

    summary = response['choices'][0]['message']['content']
    return summary

if __name__ == "__main__":
    url = input("Enter a URL to summarize: ")
    try:
        summary = summarize_url(url)
        print("\nSummary:\n", summary)
    except Exception as e:
        print("An error occurred:", e)
