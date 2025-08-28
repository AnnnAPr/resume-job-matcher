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









# import streamlit as st

# st.set_page_config(page_title="Resume Job Matcher", layout="wide")

# st.title("📄 Resume–Job Matcher")
# st.write("Upload your resume and paste a job description to get started.")

# # Resume Upload
# uploaded_resume = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"])

# # Job description input
# job_description = st.text_area("Paste Job Description Here")

# # Display uploaded resume
# if uploaded_resume is not None:
#     st.subheader("📌 Resume Preview")
#     if uploaded_resume.type == "text/plain":
#         text = uploaded_resume.read().decode("utf-8")
#         st.text_area("Resume Content", text, height=200)
#     else:
#         st.info("PDF preview coming soon...")

# # Display job description
# if job_description:
#     st.subheader("📌 Job Description Preview")
#     st.write(job_description)






# import streamlit as st
# from sentence_transformers import SentenceTransformer, util

# st.set_page_config(page_title="Resume Job Matcher", layout="wide")

# st.title("📄 Resume–Job Matcher")
# st.write("Upload your resume and paste a job description to see how well they match.")

# # Load model once (lightweight, cached by Streamlit)
# @st.cache_resource
# def load_model():
#     return SentenceTransformer("all-MiniLM-L6-v2")

# model = load_model()

# # Resume Upload
# uploaded_resume = st.file_uploader("Upload Resume (TXT only for now)", type=["txt"])
# job_description = st.text_area("Paste Job Description Here")

# resume_text = None
# if uploaded_resume is not None:
#     resume_text = uploaded_resume.read().decode("utf-8")
#     st.subheader("📌 Resume Preview")
#     st.text_area("Resume Content", resume_text, height=200)

# if job_description:
#     st.subheader("📌 Job Description Preview")
#     st.write(job_description)

# # Match button
# if st.button("🔍 Match Resume with Job"):
#     if resume_text and job_description:
#         with st.spinner("Calculating similarity..."):
#             # Create embeddings
#             embeddings = model.encode([resume_text, job_description], convert_to_tensor=True)
#             similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
#             score = round(similarity * 100, 2)

#         st.success(f"✅ Match Score: **{score}%**")
#         if score > 70:
#             st.write("🎉 Strong match! This resume aligns well with the job description.")
#         elif score > 40:
#             st.write("⚖️ Partial match. Consider tailoring your resume to better fit the job.")
#         else:
#             st.write("❌ Weak match. Resume and job description are not closely aligned.")
#     else:
#         st.warning("Please upload a resume and paste a job description first.")






import streamlit as st
from sentence_transformers import SentenceTransformer, util
import PyPDF2

st.set_page_config(page_title="Resume Job Matcher", layout="wide")
st.title("📄 Resume–Job Matcher")
st.write("Upload your resume (TXT or PDF) and paste a job description to see how well they match.")

# Load model once
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

# Resume upload
uploaded_resume = st.file_uploader("Upload Resume (TXT or PDF)", type=["txt", "pdf"])
resume_text = None

if uploaded_resume is not None:
    if uploaded_resume.type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_resume)
    else:
        resume_text = uploaded_resume.read().decode("utf-8")

    st.subheader("📌 Resume Preview")
    st.text_area("Resume Content", resume_text, height=200)

# Job description input
job_description = st.text_area("Paste Job Description Here")

if job_description:
    st.subheader("📌 Job Description Preview")
    st.write(job_description)

# Match button
if st.button("🔍 Match Resume with Job"):
    if resume_text and job_description:
        with st.spinner("Calculating similarity..."):
            embeddings = model.encode([resume_text, job_description], convert_to_tensor=True)
            similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
            score = round(similarity * 100, 2)

        st.success(f"✅ Match Score: **{score}%**")
        if score > 70:
            st.write("🎉 Strong match! This resume aligns well with the job description.")
        elif score > 40:
            st.write("⚖️ Partial match. Consider tailoring your resume to better fit the job.")
        else:
            st.write("❌ Weak match. Resume and job description are not closely aligned.")
    else:
        st.warning("Please upload a resume and paste a job description first.")
