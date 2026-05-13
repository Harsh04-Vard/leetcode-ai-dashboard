from openai import OpenAI
import streamlit as st


# ---------------- GROQ CLIENT ---------------- #

client = OpenAI(
    api_key=st.secrets["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
    timeout=20
)


# ---------------- AI ROADMAP GENERATOR ---------------- #

def generate_roadmap(data):

    try:

        prompt = f"""
Student Stats:
Easy: {data.get('easySolved', 0)}
Medium: {data.get('mediumSolved', 0)}
Hard: {data.get('hardSolved', 0)}

Generate:
- weakness analysis
- 14 day roadmap
- important topics
- interview advice

Keep concise.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Error: {str(e)}"