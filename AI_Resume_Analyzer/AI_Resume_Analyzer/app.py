import os
import re
from flask import Flask, render_template, request
from dotenv import load_dotenv
from analyzer import analyze_resume

load_dotenv()
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024  # 2 MB upload limit

ALLOWED_EXTENSIONS = {".txt"}

def allowed_file(filename):
    return os.path.splitext(filename.lower())[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        resume_file = request.files.get("resume")
        job_description = request.form.get("job_description", "").strip()

        if not resume_file or not resume_file.filename:
            error = "Please upload your resume as a .txt file."
        elif not allowed_file(resume_file.filename):
            error = "For this starter version, upload a plain-text (.txt) resume."
        elif not job_description:
            error = "Please paste the job description."
        else:
            try:
                resume_text = resume_file.read().decode("utf-8", errors="ignore").strip()
                if not resume_text:
                    error = "The uploaded file appears to be empty."
                else:
                    result = analyze_resume(resume_text, job_description)
            except Exception:
                error = "Something went wrong while analyzing the resume. Please try again."

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
