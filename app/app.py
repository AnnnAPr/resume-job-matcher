import streamlit as st
from transformers import pipeline

# Title
st.title("📄 Resume Job Matcher")

# Inputs
resume_text = st.text_area("Paste your resume:")
job_text = st.text_area("Paste job description:")

if st.button("Match Resume"):
    if resume_text and job_text:
        # Use a Hugging Face zero-shot classifier
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        
        result = classifier(resume_text, [job_text])
        
        st.subheader("🔍 Match Result")
        st.write(f"Match score: {result['scores'][0]:.2f}")
    else:
        st.warning("Please paste both resume and job description.")
