# 📋 Resume Analyzer & Skill Matcher

A Flask web app that analyzes uploaded resumes, extracts skills using NLP, and matches them to a job description.

## Features
- Resume parsing from PDF and DOCX
- Skill extraction with spaCy
- JD matching and score calculation
- Simple HTML UI for uploading and viewing results

## How to Use
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
