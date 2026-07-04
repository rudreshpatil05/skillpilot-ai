def calculate_future_score(best_role):
    """
    Calculates Career Readiness Score.
    """

    score = best_role["Score"]

    if score >= 90:
        level = "Excellent 🚀"

    elif score >= 75:
        level = "Job Ready 💼"

    elif score >= 60:
        level = "Intermediate 📘"

    elif score >= 40:
        level = "Beginner 📚"

    else:
        level = "Needs Improvement ❌"

    return {
        "score": score,
        "level": level
    }


if __name__ == "__main__":

    sample_role = {
        "Role": "Data Analyst",
        "Score": 72
    }

    print(calculate_future_score(sample_role))