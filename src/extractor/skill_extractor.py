import pandas as pd


def load_skills(csv_path="data/skills.csv"):
    """
    Load skills from skills.csv
    """

    df = pd.read_csv(csv_path)

    return df["Skill"].dropna().tolist()

def extract_skills(text, skills_list):
    """
    Extract skills from resume text.
    """

    detected_skills = []

    text = text.lower()

    for skill in skills_list:

        if skill.lower() in text:

            detected_skills.append(skill)

    return sorted(list(set(detected_skills)))

if __name__ == "__main__":

    skills = load_skills()

    sample_resume = """
    Python
    SQL
    FastAPI
    Docker
    Git
    Machine Learning
    """

    result = extract_skills(sample_resume, skills)

    print(result)