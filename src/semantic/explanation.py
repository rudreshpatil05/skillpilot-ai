def generate_match_explanation(best_role, detected_skills):
    """
    Generate an explanation for why a role was selected.
    """

    detected = {skill.lower() for skill in detected_skills}

    required = {
        skill.lower()
        for skill in best_role["Required Skills"]
    }

    strengths = sorted(detected.intersection(required))
    missing = sorted(required.difference(detected))

    score = best_role["Score"]

    if score >= 90:
        confidence = "Excellent Match"

    elif score >= 75:
        confidence = "High Match"

    elif score >= 60:
        confidence = "Good Match"

    elif score >= 40:
        confidence = "Average Match"

    else:
        confidence = "Low Match"

    recommendation = ""

    if len(missing) == 0:

        recommendation = (
            "Your resume already matches this role very well."
        )

    else:

        recommendation = (
            "Improve these skills: "
            + ", ".join(missing)
        )

    return {

        "confidence": confidence,

        "strengths": strengths,

        "missing": missing,

        "recommendation": recommendation

    }