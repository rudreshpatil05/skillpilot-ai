def review_resume(detected_skills, resume_text):
    """
    Analyze the resume and return strengths,
    weaknesses and improvement suggestions.
    """

    score = 100

    strengths = []
    weaknesses = []
    suggestions = []

    # ---------- Skill Count ----------
    if len(detected_skills) >= 8:
        strengths.append("Strong technical skill set")

    else:
        weaknesses.append("Limited technical skills detected")
        suggestions.append("Add more relevant technical skills.")

        score -= 10

    # ---------- Projects ----------
    if "project" in resume_text.lower():

        strengths.append("Projects section detected")

    else:

        weaknesses.append("Projects section missing")

        suggestions.append(
            "Include 2-3 strong projects."
        )

        score -= 10

    # ---------- Education ----------
    if "education" in resume_text.lower():

        strengths.append("Education section present")

    else:

        weaknesses.append("Education section missing")

        suggestions.append(
            "Add your education details."
        )

        score -= 5

    # ---------- GitHub ----------
    if "github" in resume_text.lower():

        strengths.append("GitHub profile included")

    else:

        weaknesses.append("GitHub profile missing")

        suggestions.append(
            "Add your GitHub profile."
        )

        score -= 10

    # ---------- LinkedIn ----------
    if "linkedin" in resume_text.lower():

        strengths.append("LinkedIn profile included")

    else:

        weaknesses.append("LinkedIn profile missing")

        suggestions.append(
            "Add your LinkedIn profile."
        )

        score -= 10

    # ---------- Certifications ----------
    if "certificate" in resume_text.lower() or "certification" in resume_text.lower():

        strengths.append("Certifications detected")

    else:

        suggestions.append(
            "Add certifications to improve credibility."
        )

    score = max(score, 0)

    return {

        "score": score,

        "strengths": strengths,

        "weaknesses": weaknesses,

        "suggestions": suggestions

    }