# Glex 🤖

Glex is a simple mood-based chatbot built with **Streamlit**, **LangChain**, and **Hugging Face** endpoints.

## Features
- Choose a personality mode before chatting: **Angry**, **Happy**, or **Neutral**
- Powered by `meta-llama/Llama-3.1-8B-Instruct` via Hugging Face Inference Endpoint
- Clean chat interface using Streamlit's `st.chat_message` components
- Maintains full conversation history using LangChain message objects

## Tech Stack
- Python
- Streamlit
- LangChain (`langchain-huggingface`)
- Hugging Face Inference Endpoints

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

Make sure to set your Hugging Face API token in a `.env` file:
```
HUGGINGFACEHUB_API_TOKEN=your_token_here
```
