import requests
from app import get_finance_news

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"


def summarize_news(question, articles):

    prompt = f"""
You are a finance assistant.

A user asked this question:
{question}

Here are recent news articles:

{articles}

Summarize the key insights and answer the user's question based only on the news provided.
Keep answers strictly up to 5-6 sentences.
Include sources if relevant.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"]


if __name__ == "__main__":

    question = input("Ask a finance question: ")

    articles = get_finance_news(question)

    answer = summarize_news(question, articles)

    print("\nAnswer:\n")
    print(answer)