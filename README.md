# AI Chatbot

An AI-powered conversational chatbot developed using Python and a Large Language Model (LLM) API. The application provides a simple chat interface where users can enter questions and receive AI-generated responses.

## Project Overview

The purpose of this project is to demonstrate how a Large Language Model can be integrated into a Python application to build an interactive AI assistant.

The basic workflow is:

```text
User Input
    ↓
Chat Interface
    ↓
Prompt
    ↓
LLM API
    ↓
AI Response
    ↓
Display Response
```

## Features

- Interactive chatbot interface
- Accepts natural-language user queries
- Generates AI-powered responses
- Python-based LLM integration
- Simple modular application structure

## Technologies Used

- Python
- Streamlit
- Large Language Model API
- python-dotenv

## Project Structure

```text
ai-chatbot/
│
├── app.py
├── ai_service.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env.example
```

## Installation

Clone the repository:

```bash
git clone https://github.com/rprasad753-dot/ai-chatbot.git
```

Move into the project directory:

```bash
cd ai-chatbot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project directory and add the API key required by your LLM provider.

Example:

```text
API_KEY=your_api_key_here
```

Do not commit your real `.env` file or API key to GitHub.

## Run the Application

If the interface is built with Streamlit:

```bash
streamlit run app.py
```

Open the local URL shown by Streamlit in your browser.

## How It Works

1. The user enters a message through the chatbot interface.
2. The application receives the user input.
3. The input is passed to the LLM service.
4. The LLM generates a response.
5. The generated response is returned to the application.
6. The response is displayed to the user.

## Learning Outcomes

This project provided practical experience with:

- Large Language Models
- LLM API integration
- Prompt handling
- Python application development
- Streamlit
- Environment-variable management
- Building an end-to-end AI application

## Author

**Rahul Prasad**