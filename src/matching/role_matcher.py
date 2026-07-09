import pandas as pd


def load_roles():
    """
    Load job roles from CSV.
    Returns a list of dictionaries.
    """

    df = pd.read_csv("data/roles.csv")

    roles = []

    for _, row in df.iterrows():

        roles.append(
            {
                "Role": row["Role"],
                "Skills": [
                    skill.strip()
                    for skill in str(row["Required Skills"]).split(",")
                ]
            }
        )

    return roles


def match_roles(detected_skills, roles):
    """
    Compare detected resume skills with every role
    and calculate the matching score.
    """

    results = []

    detected = {skill.lower() for skill in detected_skills}

    for role in roles:

        role_name = role["Role"]

        required_skills = role["Skills"]

        required = {skill.lower() for skill in required_skills}

        matched = detected.intersection(required)

        missing = required.difference(detected)

        score = round((len(matched) / len(required)) * 100)

        results.append(
            {
                "Role": role_name,
                "Score": score,
                "Matched": sorted(matched),
                "Missing": sorted(missing),
                "Required Skills": required_skills,
            }
        )

    results.sort(
        key=lambda x: x["Score"],
        reverse=True
    )

    return results


if __name__ == "__main__":

    roles = load_roles()

    resume_skills = [
        "Python",
        "SQL",
        "Git",
        "Pandas",
        "NumPy"
    ]

    results = match_roles(resume_skills, roles)

    for role in results:
        print(role)