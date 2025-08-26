# Resume Job Matcher

A simple AI project that helps match resumes to job descriptions using a free, open-source LLM.

## Features
- Upload a resume (text)
- Paste a job description
- Get a match score + feedback
- Runs free on Hugging Face Spaces

## Tech Stack
- Python
- Streamlit
- Hugging Face Transformers
- Deployed on Hugging Face Spaces (free)

## Setup (Local)
```bash
git clone https://github.com/yourusername/resume-job-matcher.git
cd resume-job-matcher
pip install -r requirements.txt
streamlit run app/app.py

## 🚀 Run Locally  

1. Create a virtual environment
  Windows: python -m venv .venv
  Mac: python3 -m venv .venv

2. Activate the virtual environment
  - Windows: `.venv\Scripts\activate`
  - Mac: source `.venv/bin/activate`

3. Install dependencies
  - Minimal (recommended): `pip install -r requirements.txt`
  - Full freeze (exact versions): `pip install -r requirements-full.txt`

4. Run the app `streamlit run app/app.py`

5. Stop the app: Press CTRL + C in the terminal.

