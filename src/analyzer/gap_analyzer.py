def analyze_skill_gap(role_result):
    """
    Analyze missing skills and generate recommendations.
    """

    missing = role_result["Missing"]

    recommendations = []

    for skill in missing:

        recommendations.append({

            "Skill": skill,

            "Priority": "High",

            "Estimated Days": 7

        })

    return recommendations
if __name__ == "__main__":

    sample = {

        "Role":"Machine Learning Intern",

        "Missing":[

            "Machine Learning",

            "NumPy",

            "Scikit-learn"

        ]

    }

    print(analyze_skill_gap(sample))