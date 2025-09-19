import streamlit as st
import PyPDF2
from io import BytesIO

# 🎨 Page setup
st.set_page_config(
    page_title="Resume ↔ Job Matcher",
    page_icon="📄",
    layout="centered"
)

# 💡 Helper: Extract text from PDF
def extract_text_from_pdf(uploaded_file):
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    except Exception as e:
        st.error(f"⚠️ Could not read PDF: {e}")
    return text

# 💡 Helper: Simple keyword match
def calculate_match(resume_text, job_text):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_text.lower().split())
    if not resume_words or not job_words:
        return 0
    overlap = resume_words.intersection(job_words)
    return round(len(overlap) / len(job_words) * 100, 2)

# 🎯 UI
st.title("📄 Resume ↔ Job Matcher")
st.caption("Upload your resume and paste a job description to see your match score.")

# 🔹 Sidebar
st.sidebar.header("About")
st.sidebar.info(
    """This app compares your **resume** with a **job description** 
and shows how well they match.

✅ Upload PDF or paste text  
✅ Enter job description  
✅ Get instant % match"""
)

# 🔹 Inputs
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
resume_text = ""

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)

resume_text_area = st.text_area("Or paste your resume text here", height=200)
if resume_text_area.strip():
    resume_text = resume_text_area

job_description = st.text_area("Paste the job description here", height=200)

# 🔹 Button
if st.button("🔍 Match Resume to Job"):
    if not resume_text:
        st.warning("Please upload or paste your resume first.")
    elif not job_description.strip():
        st.warning("Please enter a job description.")
    else:
        score = calculate_match(resume_text, job_description)
        st.success(f"✅ Your resume matches **{score}%** of the job description keywords!")
        st.progress(score / 100)

        if score < 40:
            st.info("💡 Tip: Add more relevant keywords from the job description into your resume.")
        elif score < 70:
            st.info("👍 Good start! Try tailoring your resume more closely to the role.")
        else:
            st.balloons()
            st.success("🚀 Great match! Your resume is highly aligned with this job.")


