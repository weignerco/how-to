# How-to Create a RAG using OCI GenAI Agent and Streamlit

## Key Services:

* OCI Object Storage
* OCI Generative AI Agent
* Streamlit (for the frontend app)


***Streamlit** is an open-source Python framework that makes it easy to build and share interactive web apps with great aesthetics -- especialy for data science, machine learning, and AI projects. With just a few lines of Python code, you can turn your scripts into live web apps.*

## Pre-requisites:

Versions used in this app demo:
* Python 3.9.6
* Streamlit 1.35.0


## Steps
1. Create an OCI Object Storage bucket and upload your documents (supports PDF and TXT files only)
2. OCI Generative AI Agent

    2.1 Create a Knowledge Base

    2.2 Create an Agent (use RAG for tool)

    2.3 Test the Chat from the Playground

3. Create the Streamlit python app (see `rag-chatbot.py`)
4. Test and run the app (see `deploy-guide.sh`)
