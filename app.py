import os
import requests
import streamlit as st
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("finance-mcp-server")

NEWS_API_URL = "https://newsapi.org/v2/everything"


def get_news_api_key():
    try:
        return st.secrets["NEWS_API_KEY"]
    except Exception:
        return os.getenv("NEWS_API_KEY")


@mcp.tool()
def get_finance_news(topic: str) -> list:
    """Fetch recent finance-related news articles for a given topic."""

    news_api_key = get_news_api_key()

    if not news_api_key:
        return []

    params = {
        "q": topic,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": news_api_key,
    }

    try:
        response = requests.get(NEWS_API_URL, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()

        articles = data.get("articles", [])
        if not articles:
            return []

        results = []
        for article in articles:
            results.append(
                {
                    "title": article.get("title"),
                    "source": article.get("source", {}).get("name"),
                    "published_at": article.get("publishedAt"),
                    "url": article.get("url"),
                }
            )

        return results

    except requests.RequestException:
        return []


if __name__ == "__main__":
    mcp.run()