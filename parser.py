import spacy
import docx2txt
import re
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    return extract_text(file_path)

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def extract_skills(text):
    skills_db = ["python", "machine learning", "sql", "javascript", "html", "css",
                 "excel", "c++", "java", "data analysis", "deep learning"]
    doc = nlp(text.lower())
    found = set()
    for token in doc:
        if token.text in skills_db:
            found.add(token.text)
    return list(found)

def match_score(resume_skills, jd_skills):
    if not jd_skills: return 0
    resume_skills = set(resume_skills)
    jd_skills = set([s.lower() for s in jd_skills])
    return round((len(resume_skills & jd_skills) / len(jd_skills)) * 100, 2)
