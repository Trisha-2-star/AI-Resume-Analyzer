import os
import re
from collections import Counter

# This transparent keyword-matching score is a screening aid, not a real ATS score.
STOPWORDS = {
    "and", "the", "for", "with", "from", "that", "this", "are", "you",
    "your", "will", "our", "have", "has", "into", "using", "who", "all",
    "can", "but", "not", "their", "they", "job", "role", "work", "years",
    "year", "experience", "required", "requirements", "preferred", "skills"
}

def tokenize(text):
    words = re.findall(r"[a-zA-Z][a-zA-Z+#.]{1,}", text.lower())
    return [word.strip(".") for word in words if len(word.strip(".")) > 2]

def extract_keywords(job_description, limit=40):
    tokens = [word for word in tokenize(job_description) if word not in STOPWORDS]
    counts = Counter(tokens)
    return [word for word, _ in counts.most_common(limit)]

def analyze_resume(resume_text, job_description):
    resume_lower = resume_text.lower()
    keywords = extract_keywords(job_description)
    matched = [word for word in keywords if re.search(r"\b" + re.escape(word) + r"\b", resume_lower)]
    missing = [word for word in keywords if word not in matched]
    score = round((len(matched) / len(keywords)) * 100) if keywords else 0

    suggestions = []
    if not re.search(r"\b(python|java|javascript|c\+\+)\b", resume_lower):
        suggestions.append("Add the programming languages you genuinely know.")
    if not re.search(r"\b(project|projects)\b", resume_lower):
        suggestions.append("Include relevant projects and explain your contribution.")
    if not re.search(r"\b(github|portfolio|linkedin)\b", resume_lower):
        suggestions.append("Add relevant professional profile or portfolio links.")
    if missing:
        suggestions.append("Review the missing keywords and add only those supported by your actual skills or experience.")
    if not suggestions:
        suggestions.append("Keep your resume concise and ensure every listed skill can be discussed in an interview.")

    return {
        "score": score,
        "matched": matched,
        "missing": missing,
        "total": len(keywords),
        "suggestions": suggestions,
    }
