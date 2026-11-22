

import re


def evaluate_resume(resume_text):
    """
    Free rule-based resume evaluator.
    Does not require API credits or internet access.
    """

    if not resume_text or not resume_text.strip():
        return {"error": "No resume text was provided."}

    text = resume_text.lower()

    def contains_keyword(keyword):
        pattern = r"(?<!\w)" + re.escape(keyword.lower()) + r"(?!\w)"
        return bool(re.search(pattern, text))

    # Technical skills
    skill_categories = {
        "Programming Languages": [
            "python", "java", "c", "c++", "javascript"
        ],
        "Web Development": [
            "html", "css", "django", "flask",
            "react", "bootstrap"
        ],
        "Database": [
            "sql", "mysql", "oracle", "mongodb"
        ],
        "Tools": [
            "git", "github", "vscode", "pycharm",
            "jupyter notebook", "excel"
        ],
        "Data and AI": [
            "machine learning", "data science",
            "pandas", "numpy", "opencv",
            "computer vision"
        ]
    }

    found_skills = []

    for category, category_skills in skill_categories.items():
        for skill in category_skills:
            if contains_keyword(skill) and skill not in found_skills:
                found_skills.append(skill)

    # Soft skills
    soft_skill_keywords = [
        "communication",
        "teamwork",
        "leadership",
        "problem solving",
        "problem-solving",
        "adaptability",
        "time management",
        "quick learning",
        "quick learner",
        "team player",
        "customer handling",
        "decision making",
        "creativity",
        "critical thinking",
        "interpersonal skills",
        "collaboration",
        "punctuality"
    ]

    soft_skills = []

    for skill in soft_skill_keywords:
        if contains_keyword(skill) and skill not in soft_skills:
            soft_skills.append(skill)

    # Resume sections
    education_keywords = [
        "bca", "bsc", "b.tech", "bachelor",
        "degree", "education", "college", "university"
    ]

    project_keywords = [
        "project", "developed", "application",
        "system", "implemented"
    ]

    experience_keywords = [
        "internship", "experience", "trainee",
        "work experience", "professional experience"
    ]

    has_education = any(
        contains_keyword(word) for word in education_keywords
    )

    has_project = any(
        contains_keyword(word) for word in project_keywords
    )

    has_experience = any(
        contains_keyword(word) for word in experience_keywords
    )

    # Score calculation
    score = 20
    score += min(len(found_skills) * 3, 30)
    score += 15 if has_education else 0
    score += 15 if has_project else 0
    score += 10 if has_experience else 0
    score += min(len(soft_skills) * 2, 10)

    score = min(score, 100)

    # Missing technical skills
    recommended_skills = [
        "python", "java", "django", "html",
        "css", "javascript", "mysql", "git",
        "machine learning", "react"
    ]

    missing_skills = [
        skill for skill in recommended_skills
        if not contains_keyword(skill)
    ]

    # Suggestions
    suggestions = []

    if not has_project:
        suggestions.append(
            "Add at least one academic or personal project."
        )

    if not has_experience:
        suggestions.append(
            "Add internship, training or practical experience."
        )

    if not has_education:
        suggestions.append(
            "Include your educational qualifications."
        )

    if len(found_skills) < 5:
        suggestions.append(
            "Add more relevant technical skills."
        )

    if not soft_skills:
        suggestions.append(
            "Include relevant soft skills such as communication and teamwork, if applicable."
        )

    suggestions.append(
        "Use measurable achievements wherever possible."
    )

    suggestions.append(
        "Keep your resume clear, professional and well structured."
    )

    # Job role recommendations
    recommended_roles = []

    if "python" in found_skills or "django" in found_skills:
        recommended_roles.append("Python Developer")

    if "html" in found_skills and "css" in found_skills:
        recommended_roles.append("Web Developer")

    if "sql" in found_skills or "mysql" in found_skills:
        recommended_roles.append("Junior SQL Developer")

    if "machine learning" in found_skills or "opencv" in found_skills:
        recommended_roles.append("Junior AI/ML Developer")

    if not recommended_roles:
        recommended_roles.append("Entry-Level IT Trainee")

    # Strengths
    strengths = [
        "Resume text successfully analyzed.",
        f"{len(found_skills)} technical skills identified."
    ]

    if has_education:
        strengths.append("Educational qualifications are included.")

    if has_project:
        strengths.append("Project experience is included.")

    if has_experience:
        strengths.append("Training or experience details are included.")

    if soft_skills:
        strengths.append(
            f"{len(soft_skills)} soft skills identified."
        )

    return {
        "score": score,
        "technical_skills": found_skills,
        "soft_skills": soft_skills,

        "education_feedback": (
            "Education details found in your resume."
            if has_education else
            "Add your education details."
        ),

        "project_feedback": (
            "Project-related content found."
            if has_project else
            "Add details about your projects."
        ),

        "experience_feedback": (
            "Experience or training details found."
            if has_experience else
            "Consider adding practical experience or training."
        ),

        "strengths": strengths,

        "weaknesses": [
            "Evaluation uses keyword matching and cannot fully understand resume context."
        ],

        "missing_skills": missing_skills,
        "suggestions": suggestions,
        "recommended_roles": recommended_roles,

        "evaluation_type": "Free rule-based evaluation (not AI-generated)"
    }
