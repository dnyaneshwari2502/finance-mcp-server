import streamlit as st
from app import get_finance_news
from client import summarize_news

st.set_page_config(page_title="Finance News Chatbot", page_icon="📈")

st.title("Finance News Chatbot")
st.write("Ask a finance-related question and get an answer based on recent news.")

with st.form("finance_form"):
    question = st.text_input("Enter your question")
    submitted = st.form_submit_button("Ask")

if submitted:
    if question.strip():
        with st.spinner("Fetching news and generating answer..."):
            articles = get_finance_news(question)
            answer = summarize_news(question, articles)

        st.subheader("Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")