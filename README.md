# Customer Support Chatbot

Welcome to the Customer Support Chatbot project! - A Simple & Powerful RAG Prototype. This chatbot is designed to assist users with resolving technical issues and inquiries related to your products or services, ensuring a smooth and efficient support experience.

## Overview

The Customer Support Chatbot is built using Python and the FastAPI web framework. It leverages natural language processing (NLP) techniques to understand user queries and generate accurate responses based on the contexts provided. The chatbot integrates with your internal knowledge base and FAQ's to provide relevant solutions and guidance to users..

## Features

- Interactive chat interface for users to interact with the chatbot.
- Alternatively, This application is exposed thru FastAPI endpoint /ask?query=...
- Natural language processing for understanding user queries.
- Stores and manages vector embeddings in AstraDB for scalable, low-latency retrieval.
- Integration with DeepEval evaluation technique to ensure avoiding hallucinations and quality of generated answers.
- Ability to handle various user inquiries related technical issues such as password expiry, account locked etc.,

## Installation

To set up the Customer Support Chatbot locally, follow these steps:

1. Unzip the file and open in VSCode. 

2. Navigate to the project directory:
```
   cd customer-support-chatbot
```

3. Install the required Python packages using uv pip:
```
uv pip install -r requirements.txt
```

4. Set up environment variables:
- Create a .env file in the project directory.
- Configure AstraDB vector store.
- Define the necessary API keys, AstrDB connection details as defined in .env.copy file.
  
5. Ingest data for the first time.
```
python -m itsupportbot.ingest
```

6. Run the FastAPI application:
```
python -m uvicorn fastapi_app:app --reload --host 127.0.0.1 --port 8080
```
