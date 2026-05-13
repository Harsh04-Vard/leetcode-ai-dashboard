from openai import OpenAI
import streamlit as st


# ---------------- GROQ CLIENT ---------------- #

client = OpenAI(
    api_key=st.secrets["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
    timeout=20
)


# ---------------- AI CHATBOT ---------------- #

def ask_ai_mentor(user_question):

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "system",
                    "content": """
You are an expert DSA mentor helping students prepare for coding interviews.

Give:
- concise answers
- practical guidance
- topic recommendations
- interview tips
- coding preparation strategies
"""
                },

                {
                    "role": "user",
                    "content": user_question
                }
            ],

            temperature=0.7,
            max_tokens=400
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Error: {str(e)}"