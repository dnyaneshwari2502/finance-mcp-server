# Finance MCP Server – AI News Chatbot

This is a personal project built to explore MCP-based tool integration with LLMs and real-time data sources.

This project is a finance-focused AI chatbot that answers user queries using real-time news data, instead of relying only on LLM knowledge.

---

## What it does

- Takes a finance-related question from the user  
- Fetches recent news articles using NewsAPI  
- Uses an LLM to generate answers grounded in real-time data  
- Returns a concise summary based only on retrieved information  

---

## Tech Stack

- Python  
- Streamlit (UI)  
- Google Gemini API (LLM)  
- NewsAPI (data source)  
- MCP (Model Context Protocol)

---

## How it works

User Question  
→ MCP tool / direct function call  
→ News API fetch  
→ Articles retrieved  
→ Gemini summarization  
→ Final answer  

---

## Features

- Chat-style UI (similar to ChatGPT)  
- Real-time finance news retrieval  
- LLM responses grounded in actual data  
- Fallback mechanism for reliability  
- Deployed web application  

---

## MCP Integration

This project includes a working MCP-based setup where:

- A tool (`get_finance_news`) is defined using MCP  
- A client (`client_mcp.py`) communicates with the MCP server  
- The tool fetches real-time data which is then passed to the LLM  

For deployment stability, the Streamlit app currently uses a hybrid approach:
- It first attempts MCP-based execution  
- Falls back to direct function calls if needed  

This ensures both reliability in production and demonstration of MCP architecture.

---

## Note

This project was built as a personal learning project to explore LLM applications, tool integration, and real-time data grounding.

---

## Author

Dnyaneshwari Rakshe