# import streamlit as st
# from transformers import pipeline

# # Title
# st.title("📄 Resume Job Matcher")

# # Inputs
# resume_text = st.text_area("Paste your resume:")
# job_text = st.text_area("Paste job description:")

# if st.button("Match Resume"):
#     if resume_text and job_text:
#         # Use a Hugging Face zero-shot classifier
#         classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        
#         result = classifier(resume_text, [job_text])
        
#         st.subheader("🔍 Match Result")
#         st.write(f"Match score: {result['scores'][0]:.2f}")
#     else:
#         st.warning("Please paste both resume and job description.")

import streamlit as st

st.set_page_config(page_title="Resume Job Matcher", layout="wide")

st.title("📄 Resume–Job Matcher")
st.write("Upload your resume and paste a job description to get started.")

# Resume Upload
uploaded_resume = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"])

# Job description input
job_description = st.text_area("Paste Job Description Here")

# Display uploaded resume
if uploaded_resume is not None:
    st.subheader("📌 Resume Preview")
    if uploaded_resume.type == "text/plain":
        text = uploaded_resume.read().decode("utf-8")
        st.text_area("Resume Content", text, height=200)
    else:
        st.info("PDF preview coming soon...")

# Display job description
if job_description:
    st.subheader("📌 Job Description Preview")
    st.write(job_description)
