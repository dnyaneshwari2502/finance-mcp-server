# Finance MCP Server – AI News Chatbot

This is a personal project built to explore MCP-based tool integration with LLMs and real-time data sources.

This project is a finance-focused AI chatbot that answers user queries using real-time news data, instead of relying only on LLM knowledge.

---

## What it does

- Takes a finance-related question from the user  
- Fetches recent news articles using NewsAPI  
- Sends the retrieved data to a Gemini LLM  
- Returns a summarized, grounded answer  

---

## Tech Stack

- Python  
- Streamlit (UI)  
- Google Gemini API (LLM)  
- NewsAPI (data source)  
- MCP (tool structure)

---

## How it works

User Question  
→ News API fetch  
→ Articles retrieved  
→ Gemini summarization  
→ Final answer  

---

## Features

- Chat-style UI (similar to ChatGPT)  
- Real-time finance news retrieval  
- LLM responses grounded in actual data  
- Deployed web application  

---

## MCP Integration (In Progress)

This project was initially structured using the Model Context Protocol (MCP) to define tools such as finance news retrieval. In the current deployed version, the tool is invoked directly within the application to ensure stability and simplicity for web deployment. I am currently working on extending this into a full MCP-based agent setup, where the LLM can dynamically decide when to call tools through an MCP client-server interaction.

## Author: Dnyaneshwari Rakshe