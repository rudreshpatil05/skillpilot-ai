import re


def review_resume(cleaned_text):
    """
    Reviews the resume and returns:
    1. ATS Score
    2. Strengths
    3. Suggestions
    """

    ats_score = 100
    strengths = []
    suggestions = []

    text = cleaned_text.lower()

    # -----------------------------
    # Email Check
    # -----------------------------
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    if re.search(email_pattern, cleaned_text):
        strengths.append("✅ Email address found")
    else:
        ats_score -= 20
        suggestions.append("Add a professional email address.")

    # -----------------------------
    # Phone Number Check
    # -----------------------------
    phone_pattern = r"\+?\d[\d\s\-]{8,}"

    if re.search(phone_pattern, cleaned_text):
        strengths.append("✅ Contact number found")
    else:
        ats_score -= 10
        suggestions.append("Add your contact number.")

    # -----------------------------
    # LinkedIn Check
    # -----------------------------
    if "linkedin" in text:
        strengths.append("✅ LinkedIn profile found")
    else:
        ats_score -= 5
        suggestions.append("Add your LinkedIn profile link.")

    # -----------------------------
    # GitHub Check
    # -----------------------------
    if "github" in text:
        strengths.append("✅ GitHub profile found")
    else:
        ats_score -= 10
        suggestions.append("Add your GitHub profile link.")

    # -----------------------------
    # Summary Check
    # -----------------------------
    if "summary" in text or "objective" in text or "profile" in text:
        strengths.append("✅ Resume summary found")
    else:
        ats_score -= 10
        suggestions.append("Add a professional summary section.")

    # -----------------------------
    # Education Check
    # -----------------------------
    if "education" in text:
        strengths.append("✅ Education section found")
    else:
        ats_score -= 10
        suggestions.append("Add an Education section.")

    # -----------------------------
    # Projects Check
    # -----------------------------
    if "project" in text:
        strengths.append("✅ Projects section found")
    else:
        ats_score -= 20
        suggestions.append("Include at least 2-3 good projects.")

    # -----------------------------
    # Experience Check
    # -----------------------------
    if "experience" in text or "internship" in text:
        strengths.append("✅ Experience section found")
    else:
        ats_score -= 10
        suggestions.append("Add internships or relevant experience.")

    # -----------------------------
    # Skills Check
    # -----------------------------
    if "skills" in text:
        strengths.append("✅ Skills section found")
    else:
        ats_score -= 15
        suggestions.append("Add a dedicated Skills section.")

    # -----------------------------
    # Certifications Check
    # -----------------------------
    if "certificate" in text or "certification" in text:
        strengths.append("✅ Certifications found")
    else:
        suggestions.append("Consider adding relevant certifications.")

    # -----------------------------
    # Resume Length Check
    # -----------------------------
    word_count = len(cleaned_text.split())

    if word_count < 300:
        ats_score -= 20
        suggestions.append(
            f"Resume is too short ({word_count} words). Aim for 400-700 words."
        )

    elif word_count > 900:
        ats_score -= 10
        suggestions.append(
            f"Resume is too long ({word_count} words). Keep it concise."
        )

    else:
        strengths.append("✅ Resume length looks good.")

    # -----------------------------
    # ATS Score Limits
    # -----------------------------
    ats_score = max(0, min(100, ats_score))

    return {
        "ATS Score": ats_score,
        "Strengths": strengths,
        "Suggestions": suggestions
    }


# -----------------------------
# Testing
# -----------------------------
if __name__ == "__main__":

    sample_text = """
    John Doe
    john@gmail.com
    +91 9876543210

    LinkedIn: linkedin.com/in/johndoe
    GitHub: github.com/johndoe

    Summary

    Education

    Skills

    Projects

    Experience

    Certifications
    """

    result = review_resume(sample_text)

    print(result)