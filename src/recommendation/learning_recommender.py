def recommend_learning(missing_skills):

    recommendations = {

        "Python": "Complete Python Advanced + OOP",

        "SQL": "Practice SQL joins, window functions",

        "Pandas": "Complete Pandas Data Analysis",

        "NumPy": "Master NumPy Arrays",

        "Scikit-learn": "Build ML Projects",

        "Machine Learning": "Andrew Ng ML Course",

        "Deep Learning": "PyTorch Fundamentals",

        "Docker": "Docker for Beginners",

        "FastAPI": "Build REST APIs using FastAPI",

        "Git": "Git & GitHub Mastery",

        "Power BI": "Power BI Dashboard Course",

        "Statistics": "Statistics for Data Science"

    }

    learning_path = []

    for skill in missing_skills:

        learning_path.append({
            "Skill": skill,
            "Recommendation": recommendations.get(
                skill,
                "Practice this skill"
            )
        })

    return learning_path