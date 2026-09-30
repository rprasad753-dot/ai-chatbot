import os

import streamlit as st
from dotenv import load_dotenv
from google import genai


# ==================================================
# LOAD API KEY
# ==================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found in .env file.")
    st.stop()


# ==================================================
# CREATE GEMINI CLIENT
# ==================================================

client = genai.Client(api_key=api_key)


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="wide"
)


# ==================================================
# SYSTEM PROMPT
# ==================================================

system_prompt = """
You are an AI Study Assistant.

Rules:
1. Explain concepts simply.
2. Give beginner-friendly answers.
3. Use examples when possible.
4. Help with Python, Machine Learning, AI, RAG, and Data Science.
5. Be accurate and do not invent information.
"""


# ==================================================
# SESSION STATE
# ==================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("⚙️ Settings")

    st.write("### 🤖 AI Study Assistant")

    st.write(
        "Ask questions about Python, "
        "AI, Machine Learning, RAG and Data Science."
    )

    st.divider()

    st.write("**Model**")

    st.info("Gemini 2.5 Flash")

    st.divider()

    st.write(
        f"💬 Messages: {len(st.session_state.messages)}"
    )

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = []

        st.rerun()


# ==================================================
# MAIN TITLE
# ==================================================

st.title("🤖 AI Study Assistant")

st.write(
    "Your beginner-friendly AI assistant for "
    "Python, AI, Machine Learning and RAG."
)


# ==================================================
# DISPLAY PREVIOUS MESSAGES
# ==================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# ==================================================
# USER INPUT
# ==================================================

prompt = st.chat_input(
    "Ask me something..."
)


if prompt:

    # ------------------------------------------------
    # DISPLAY USER MESSAGE
    # ------------------------------------------------

    with st.chat_message("user"):

        st.write(prompt)


    # ------------------------------------------------
    # SAVE USER MESSAGE
    # ------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # ------------------------------------------------
    # CREATE HISTORY
    # ------------------------------------------------

    try:

        history = []

        for message in st.session_state.messages[:-1]:

            role = (
                "user"
                if message["role"] == "user"
                else "model"
            )

            history.append(
                {
                    "role": role,
                    "parts": [
                        {
                            "text": message["content"]
                        }
                    ]
                }
            )


        # ------------------------------------------------
        # CREATE CHAT
        # ------------------------------------------------

        chat = client.chats.create(
            model="gemini-3.6-flash",
            history=history
        )


        # ------------------------------------------------
        # SEND MESSAGE
        # ------------------------------------------------

        full_prompt = f"""
{system_prompt}

User Question:
{prompt}
"""


        with st.spinner("🤔 Thinking..."):

            response = chat.send_message(
                full_prompt
            )

            answer = response.text


    except Exception as e:

        answer = f"❌ Error: {e}"


    # ------------------------------------------------
    # DISPLAY AI RESPONSE
    # ------------------------------------------------

    with st.chat_message("assistant"):

        st.write(answer)


    # ------------------------------------------------
    # SAVE AI RESPONSE
    # ------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )