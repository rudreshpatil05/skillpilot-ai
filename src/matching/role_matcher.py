import pandas as pd


def load_roles():
    """
    Load all job roles from the CSV file.
    """
    roles = pd.read_csv("data/roles.csv")
    return roles


def match_roles(detected_skills, roles_df):
    """
    Compare detected resume skills with every role
    and calculate the matching score.
    """

    results = []

    detected = set(skill.lower() for skill in detected_skills)

    for _, row in roles_df.iterrows():

        role = row["Role"]

        required_skills = [
            skill.strip()
            for skill in row["Required Skills"].split(",")
        ]

        required = set(skill.lower() for skill in required_skills)

        matched = detected.intersection(required)

        missing = required.difference(detected)

        score = round((len(matched) / len(required)) * 100)

        results.append({
            "Role": role,
            "Score": score,
            "Matched": sorted(matched),
            "Missing": sorted(missing),
            "Required Skills": required_skills
        })

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