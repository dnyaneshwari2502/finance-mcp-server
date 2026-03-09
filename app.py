import os
import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("finance-mcp-server")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/everything"


@mcp.tool()
def get_finance_news(topic: str) -> str:
    """Fetch recent finance-related news articles for a given topic."""
    
    if not NEWS_API_KEY:
        return "Error: NEWS_API_KEY not found in .env file."

    params = {
        "q": topic,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY,
    }

    try:
        response = requests.get(NEWS_API_URL, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()

        articles = data.get("articles", [])
        if not articles:
            return f"No recent news found for topic: {topic}"

        results = []
        for article in articles:
            title = article.get("title", "No title")
            source = article.get("source", {}).get("name", "Unknown source")
            published_at = article.get("publishedAt", "Unknown date")
            url = article.get("url", "No URL")

            results.append(
                f"Title: {title}\n"
                f"Source: {source}\n"
                f"Published At: {published_at}\n"
                f"URL: {url}"
            )

        return "\n\n".join(results)

    except requests.RequestException as e:
        return f"Error fetching news: {str(e)}"


if __name__ == "__main__":
    mcp.run()