def analyze_skill_gap(detected_skills, best_role):
    """
    Compare detected skills with required skills
    and return the missing ones.
    """

    required_skills = best_role["Required Skills"]

    detected = {skill.lower() for skill in detected_skills}

    missing_skills = []

    for skill in required_skills:
        if skill.lower() not in detected:
            missing_skills.append(skill)

    return missing_skills