# AI Resume Analyzer

A beginner-friendly Flask web app that compares a plain-text resume with a job description, shows overlapping and missing keywords, and offers practical review suggestions.

## Features

- Upload a resume as a `.txt` file
- Paste a job description
- See a simple keyword-overlap indicator
- Review matched and missing keywords
- Get basic resume improvement suggestions
- Responsive interface built with HTML and CSS
- No paid API key required

## Tech stack

- Python
- Flask
- HTML5
- CSS3
- Regular expressions and Python collections

## Project structure

```text
AI_Resume_Analyzer/
├── app.py
├── analyzer.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   python app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser.

## How to use

1. Save your resume text in a `.txt` file.
2. Upload it in the app.
3. Paste the job description.
4. Click **Analyze Resume**.
5. Review the matched keywords, missing keywords, and suggestions.

## Important limitations

The displayed score is a simple keyword-overlap indicator based on frequently occurring words extracted from the job description. It is **not** a real ATS score, does not understand context or synonyms, and does not predict whether a recruiter will shortlist a candidate. Always verify suggestions and never add skills you do not have.

This starter version accepts `.txt` resumes only. PDF/DOCX parsing, semantic matching, LLM-based feedback, authentication, and deployment are possible future enhancements.

## Privacy and security

The app has a 2 MB upload limit and does not save uploaded resume text to a database. Avoid uploading sensitive documents when using a public deployment. Before deploying publicly, turn off Flask debug mode and add production-grade configuration and security controls.

## Future improvements

- Add PDF and DOCX text extraction
- Use sentence embeddings for semantic matching
- Add optional LLM-generated feedback with clear consent and secure API-key handling
- Add tests and a production deployment configuration


