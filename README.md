# AI Study Assistant

An interactive AI-powered study assistant built with **Python, Streamlit, and Google Gemini** to help users learn and practice topics related to Python, Machine Learning, Artificial Intelligence, RAG, and Data Science.

## Project Overview

AI Study Assistant provides a simple conversational interface where users can ask technical questions and receive AI-generated explanations.

The application uses **Gemini 2.5 Flash** as the Large Language Model (LLM) and Streamlit for the user interface.

## Features

- Interactive chat interface
- AI-powered question answering
- Conversation history during the session
- Gemini 2.5 Flash integration
- Streamlit-based web interface
- Focused on:
  - Python
  - Machine Learning
  - Artificial Intelligence
  - RAG (Retrieval-Augmented Generation)
  - Data Science

## Application Workflow

```text
User Question
      ↓
Streamlit Chat Interface
      ↓
Prompt Processing
      ↓
Gemini 2.5 Flash
      ↓
AI-Generated Response
      ↓
Display Response
```

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google Gen AI SDK (`google-genai`)
- python-dotenv

## Project Structure

```text
ai-chatbot/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env.example
```

The actual `.env` file containing the API key is excluded from GitHub using `.gitignore`.

## Installation

Clone the repository:

```bash
git clone https://github.com/rprasad753-dot/ai-chatbot.git
```

Navigate to the project:

```bash
cd ai-chatbot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project directory:

```text
GEMINI_API_KEY=your_api_key_here
```

Never upload your real API key to GitHub.

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open the local URL displayed by Streamlit, typically:

```text
http://localhost:8501
```

## Requirements

The main dependencies are:

```text
streamlit
google-genai
python-dotenv
```

## What I Learned

Through this project, I gained hands-on experience with:

- Integrating an LLM API with Python
- Working with the Google Gen AI SDK
- Building conversational AI applications
- Managing chat interactions with Streamlit
- Handling API keys securely using environment variables
- Building a simple end-to-end Generative AI application

## Author

**Rahul Prasad**