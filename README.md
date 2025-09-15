---
title: Resume Job Matcher
emoji: 📄
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.48.1"
app_file: app/app.py
pinned: false
---

# Resume Job Matcher

A simple AI project that helps match resumes to job descriptions using a free, open-source LLM.

## Features
- Upload resume (**TXT supported**, PDF placeholder for now)  
- Paste job description  
- Preview resume & job description side-by-side  
- **AI-powered similarity scoring** using `sentence-transformers`  
- Match percentage + tailored suggestions (Strong / Partial / Weak) 

## Tech Stack
- Python
- Streamlit
- Hugging Face Transformers
- Deployed on Hugging Face Spaces (free)

## Setup (Local)

- git clone https://github.com/yourusername/resume-job-matcher.git
- cd resume-job-matcher
- pip install -r requirements.txt
- streamlit run app/app.py

## Run Locally  

1. Create a virtual environment
    - Windows: python -m venv .venv
    - Mac: python3 -m venv .venv

2. Activate the virtual environment
    - Windows: `.venv\Scripts\activate`
    - Mac: source `.venv/bin/activate`

3. Install dependencies
    - Minimal (recommended): `pip install -r requirements.txt`
    - Full freeze (exact versions): `pip install -r requirements-full.txt`

4. Run the app `streamlit run app/app.py`

5. Stop the app: Press CTRL + C in the terminal.

