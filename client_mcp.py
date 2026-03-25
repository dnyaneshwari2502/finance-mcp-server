import os
import asyncio
import streamlit as st
from dotenv import load_dotenv
from google import genai
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()


def get_gemini_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        return os.getenv("GEMINI_API_KEY")


gemini_client = genai.Client(api_key=get_gemini_key())


def summarize_news(question, articles_text):
    prompt = f"""
You are a finance assistant.

User question:
{question}

Here are recent news articles:
{articles_text}

Answer the user's question using only the news above.
Keep the answer within 5-6 sentences.
If the news is not enough, clearly say that.
"""

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


async def ask_mcp_agent(question: str) -> str:
    server_params = StdioServerParameters(
        command="python",
        args=["app.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                "get_finance_news",
                {"topic": question}
            )

            articles_text = "\n\n".join(item.text for item in result.content)

            if not articles_text.strip():
                return "No recent verified news was found for this question."

            answer = summarize_news(question, articles_text)
            return answer


if __name__ == "__main__":
    question = input("Ask a finance question: ")
    answer = asyncio.run(ask_mcp_agent(question))

    print("\nFinal Answer:\n")
    print(answer)