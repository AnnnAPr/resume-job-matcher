# import streamlit as st
# from sentence_transformers import SentenceTransformer, util
# import PyPDF2

# st.set_page_config(page_title="Resume Job Matcher", layout="wide")
# st.title("📄 Resume–Job Matcher")
# st.write("Upload your resume (TXT or PDF) and paste a job description to see how well they match.")

# # Load model once
# @st.cache_resource
# def load_model():
#     return SentenceTransformer("all-MiniLM-L6-v2")

# model = load_model()

# # Function to extract text from PDF
# def extract_text_from_pdf(file):
#     pdf_reader = PyPDF2.PdfReader(file)
#     text = ""
#     for page in pdf_reader.pages:
#         page_text = page.extract_text()
#         if page_text:
#             text += page_text
#     return text

# # Resume upload
# uploaded_resume = st.file_uploader("Upload Resume (TXT or PDF)", type=["txt", "pdf"])
# resume_text = None

# if uploaded_resume is not None:
#     if uploaded_resume.type == "application/pdf":
#         resume_text = extract_text_from_pdf(uploaded_resume)
#     else:
#         resume_text = uploaded_resume.read().decode("utf-8")

#     st.subheader("📌 Resume Preview")
#     st.text_area("Resume Content", resume_text, height=200)

# # Job description input
# job_description = st.text_area("Paste Job Description Here")

# if job_description:
#     st.subheader("📌 Job Description Preview")
#     st.write(job_description)

# # Match button
# if st.button("🔍 Match Resume with Job"):
#     if resume_text and job_description:
#         with st.spinner("Calculating similarity..."):
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





# app/app.py
# import time
# import streamlit as st
# from sentence_transformers import SentenceTransformer, util
# import PyPDF2

# st.set_page_config(page_title="Resume Job Matcher", layout="wide")
# st.title("📄 Resume Job matcher")
# st.markdown(
#     "Upload your resume (PDF) or paste it manually, then paste a job description and click **Match**. "
#     "The app computes a similarity score and shows feedback."
# )

# # --- Model loader (cached) ---
# @st.cache_resource
# def load_model():
#     return SentenceTransformer("all-MiniLM-L6-v2")

# model = load_model()

# # --- Helpers ---
# def extract_text_from_pdf(uploaded_file) -> str:
#     # PyPDF2 can take a file-like object (BytesIO)
#     reader = PyPDF2.PdfReader(uploaded_file)
#     text_parts = []
#     for page in reader.pages:
#         p = page.extract_text()
#         if p:
#             text_parts.append(p)
#     return "\n".join(text_parts)

# def normalize_and_truncate(text: str, max_chars=120_000):
#     # Remove weird whitespace and truncate long docs to avoid timeouts
#     cleaned = " ".join(text.split())
#     if len(cleaned) > max_chars:
#         return cleaned[:max_chars] + " ... [truncated]"
#     return cleaned

# # --- Layout: two columns ---
# col1, col2 = st.columns([1, 1])

# with col1:
#     st.subheader("1) Resume")
#     uploaded = st.file_uploader("Upload resume (PDF or TXT)", type=["pdf", "txt"])
#     paste_resume = st.checkbox("Or paste resume text manually", value=False)

#     resume_text = ""
#     if uploaded is not None:
#         if uploaded.type == "application/pdf":
#             resume_text = extract_text_from_pdf(uploaded)
#         else:
#             # txt file
#             resume_text = uploaded.read().decode("utf-8", errors="ignore")
#         resume_text = normalize_and_truncate(resume_text)
#         st.text_area("Resume preview", resume_text, height=220)
#     elif paste_resume:
#         resume_text = st.text_area("Paste resume text", height=220)
#         resume_text = normalize_and_truncate(resume_text or "")
#     else:
#         st.info("Upload a PDF/TXT or check 'Or paste resume text manually' to enter text.")

# with col2:
#     st.subheader("2) Job description")
#     job_description = st.text_area("Paste the job description here", height=420)
#     job_description = normalize_and_truncate(job_description or "")

# st.markdown("---")

# # --- Match button and logic ---
# if st.button("🔍 Match Resume with Job"):
#     if not resume_text or not job_description:
#         st.warning("Please provide both resume text (upload or paste) and a job description.")
#     else:
#         # show progress bar and spinner
#         progress = st.progress(0)
#         with st.spinner("Computing embeddings and similarity..."):
#             # small animation
#             progress.progress(10)
#             time.sleep(0.15)

#             # encode both (tensor)
#             progress.progress(25)
#             embeddings = model.encode([resume_text, job_description], convert_to_tensor=True)
#             progress.progress(60)

#             # cosine similarity (returns -1..1)
#             similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
#             # map -1..1 into 0..100 percent for clearer UX
#             score = round(((similarity + 1) / 2) * 100, 2)
#             progress.progress(100)
#             time.sleep(0.1)

#         # Display results
#         st.metric("Match score", f"{score} %")
#         st.progress(int(min(max(score, 0), 100)))  # progress bar (0..100)

#         # Friendly textual feedback
#         if score >= 80:
#             st.success("🎉 Strong match — your resume aligns very well with this job.")
#         elif 50 <= score < 80:
#             st.info("⚠️ Partial match — some tailoring could improve your fit (skills, keywords, measurable achievements).")
#         else:
#             st.error("❌ Low match — consider rewriting bullets to highlight relevant skills & accomplishments.")

#         # Optional debug / details (collapsed)
#         with st.expander("Details / debug"):
#             st.write(f"Raw cosine similarity: {similarity:.4f}")
#             st.write("Resume length (chars):", len(resume_text))
#             st.write("Job description length (chars):", len(job_description))




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


