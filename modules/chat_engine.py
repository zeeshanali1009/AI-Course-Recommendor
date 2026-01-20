import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_with_mentor(user_query, resume_text):
    prompt = f"""
    You are an AI career mentor. The following is the user's resume content:
    {resume_text}

    The user is asking: "{user_query}"

    Provide a personalized and helpful answer considering their skills and possible learning paths.
    """

    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
