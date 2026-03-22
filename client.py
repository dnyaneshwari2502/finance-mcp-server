import os
from google import genai
from app import get_finance_news

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


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
If no news is available, clearly say that no recent verified news was found.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    question = input("Ask a finance question: ")

    articles = get_finance_news(question)

    answer = summarize_news(question, articles)

    print("\nAnswer:\n")
    print(answer)