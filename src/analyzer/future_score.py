def calculate_future_score(current_score, missing_skills):
    """
    Predict future score after learning all missing skills.
    """

    future_score = current_score + (len(missing_skills) * 10)

    if future_score > 100:
        future_score = 100

    return future_score


if __name__ == "__main__":
    score = calculate_future_score(
        70,
        ["Docker", "AWS", "PostgreSQL"]
    )

    print(score)

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