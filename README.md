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

7. Queries and their responses. 
```
How do I reset my password? 
"To reset your password, click on 'Forgot Password' at the login screen. You will then receive a reset link via email to change your password"

Where can I generate an API key? 
"You can generate an API key in your Account Settings under Developer Tools. Remember to keep your key secret for security purposes."

What is the daily API limit for free accounts?
"You can generate an API key in your Account Settings under Developer Tools. Make sure to keep your key secret to maintain security"

I cannot log into my account, what should I do?
"If you are unable to log into your account, you can try the following steps based on the issue you are facing: 1. If you are having trouble accessing your account, you can use the 'Recover Account' option. This may require verification via email or 2FA. 2. If your account is locked after 5 failed login attempts, you can wait for 15 minutes before attempting to log in again or reset your password to regain access. 3. If you are experiencing login issues with Single Sign-On, it is recommended to contact your corporate IT administrator for assistance."

My password stopped working suddenly.
"It sounds like your password may have expired. Corporate accounts require password changes every 90 days. Please reset your password using the 'Forgot Password' option. You should receive a reset link via email to create a new password. Let me know if you need any further assistance."
```


