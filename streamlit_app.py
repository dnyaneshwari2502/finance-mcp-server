import streamlit as st
from app import get_finance_news
from client import summarize_news
import asyncio
from client_mcp import ask_mcp_agent

st.set_page_config(page_title="Finance News Chatbot", page_icon="📈")

st.title("Finance News Chatbot")
st.caption("Ask finance-related questions and get answers based on recent news.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a question")

if question:
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Fetching news and generating answer..."):
            try:
                answer = asyncio.run(ask_mcp_agent(question))
            except Exception:
                # fallback to existing method
                articles = get_finance_news(question)
                answer = summarize_news(question, articles)

        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})