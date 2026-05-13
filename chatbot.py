from openai import OpenAI
import os


client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    timeout=20
)


def ask_ai_mentor(user_question):

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "system",
                    "content": """
You are an expert DSA mentor helping students prepare for coding interviews.
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