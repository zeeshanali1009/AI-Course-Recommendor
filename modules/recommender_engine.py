from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_course_recommendations(resume_text, career_level):
    prompt = f"""
    The user has uploaded their resume and mentioned they are a {career_level} learner.
    Analyze the resume to detect skills, interests, and experience level.
    Then suggest a personalized AI/ML career roadmap with recommended courses and learning order.
    Make sure recommendations cover relevant domains and technologies.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ Updated model
        messages=[
            {"role": "system", "content": "You are an expert AI course and career mentor."},
            {"role": "user", "content": f"{prompt}\n\nResume:\n{resume_text}"}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content
