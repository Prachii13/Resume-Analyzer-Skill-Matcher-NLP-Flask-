from flask import Flask, request, render_template
from parser import extract_text_from_pdf, extract_text_from_docx, extract_skills, match_score
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        file = request.files["resume"]
        jd = request.form["jd"]
        ext = file.filename.split(".")[-1]
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        if ext == "pdf":
            text = extract_text_from_pdf(filepath)
        elif ext == "docx":
            text = extract_text_from_docx(filepath)
        else:
            return "Unsupported file type"

        resume_skills = extract_skills(text)
        jd_skills = extract_skills(jd)
        score = match_score(resume_skills, jd_skills)

        result = {
            "extracted_skills": resume_skills,
            "match_score": score,
            "jd_skills": jd_skills
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
