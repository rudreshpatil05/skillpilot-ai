def answer_resume_question(
    question,
    best_role,
    detected_skills,
    missing_skills,
    ats_score,
    career
):
    """
    AI Resume Chatbot
    Answers resume-related questions.
    """

    question = question.lower().strip()

    # -----------------------------
    # Best Role
    # -----------------------------
    if any(word in question for word in [
        "best role",
        "career",
        "job",
        "profession"
    ]):

        return (
            f"✅ Based on your resume, your best career match is "
            f"'{best_role['Role']}' with a match score of "
            f"{best_role['Score']}%."
        )

    # -----------------------------
    # Missing Skills
    # -----------------------------
    elif any(word in question for word in [
        "missing",
        "skills",
        "skill"
    ]):

        if missing_skills:

            return (
                "📚 You should learn these skills first:\n\n• "
                + "\n• ".join(missing_skills)
            )

        return "🎉 Great! No important skills are missing."

    # -----------------------------
    # ATS Score
    # -----------------------------
    elif any(word in question for word in [
        "ats",
        "resume score",
        "applicant tracking system"
    ]):

        return (
            f"⭐ Your ATS Resume Score is {ats_score}/100.\n\n"
            "Improve your projects, achievements, and missing skills "
            "to increase this score."
        )

    # -----------------------------
    # Career Score
    # -----------------------------
    elif any(word in question for word in [
        "career score",
        "career readiness",
        "readiness"
    ]):

        return (
            f"🚀 Career Readiness Score: {career['score']}/100\n"
            f"Level: {career['level']}"
        )

    # -----------------------------
    # Projects
    # -----------------------------
    elif any(word in question for word in [
        "project",
        "projects"
    ]):

        return (
            "💻 Build 3-5 real-world projects, upload them to GitHub, "
            "and deploy them if possible. Strong projects greatly "
            "increase your interview chances."
        )

    # -----------------------------
    # Resume Improvement
    # -----------------------------
    elif any(word in question for word in [
        "resume",
        "improve",
        "improvement"
    ]):

        return (
            "📄 Improve your resume by:\n\n"
            "• Adding projects\n"
            "• Adding certifications\n"
            "• Mentioning achievements with numbers\n"
            "• Including GitHub and LinkedIn\n"
            "• Learning the missing skills"
        )

    # -----------------------------
    # Roadmap
    # -----------------------------
    elif any(word in question for word in [
        "roadmap",
        "learning plan",
        "plan"
    ]):

        return (
            "🛣 Follow the personalized roadmap shown below. "
            "Complete one skill at a time and build a mini project "
            "after each skill."
        )

    # -----------------------------
    # Default
    # -----------------------------
    else:

        return (
            "🤖 I can answer questions about:\n\n"
            "• Best Role\n"
            "• Missing Skills\n"
            "• ATS Score\n"
            "• Career Readiness Score\n"
            "• Resume Improvement\n"
            "• Projects\n"
            "• Learning Roadmap"
        )