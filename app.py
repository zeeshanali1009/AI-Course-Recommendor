import streamlit as st
from modules.resume_loader import extract_text_from_file
from modules.recommender_engine import generate_course_recommendations
from modules.chat_engine import chat_with_mentor

st.set_page_config(page_title="AI Course & Career Mentor", layout="centered")

st.title("🎯 AI Course & Career Mentor")
st.markdown("Upload your resume and get **personalized course paths** powered by **Groq LLM**.")

uploaded_file = st.file_uploader("📄 Upload your Resume (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

career_level = st.selectbox(
    "🎓 Select your current level",
    ["Beginner", "Intermediate", "Advanced"]
)
if uploaded_file:
    file_path = f"temp_resume.{uploaded_file.name.split('.')[-1]}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_text_from_file(file_path)

    st.success("✅ Resume uploaded and processed successfully!")

    if st.button("🚀 Generate Recommendations"):
        with st.spinner("Analyzing your resume and generating personalized courses..."):
            recommendations = generate_course_recommendations(resume_text, career_level)
        st.write("### 📚 Recommended Courses:")
        st.success(recommendations)

        st.markdown("---")
        st.subheader("💬 Chat with AI Mentor")
        user_query = st.text_input("Ask something (e.g., 'Should I learn Python before AI?')")

        if user_query:
            with st.spinner("Mentor is thinking..."):
                mentor_response = chat_with_mentor(user_query, resume_text)
            st.info(mentor_response)
