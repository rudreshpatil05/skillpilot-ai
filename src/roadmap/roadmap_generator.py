from src.roadmap.learning_resources import LEARNING_RESOURCES


def generate_learning_roadmap(missing_skills):

    roadmap = []

    for week, skill in enumerate(missing_skills, start=1):

        details = LEARNING_RESOURCES.get(
            skill,
            {
                "difficulty": "Unknown",
                "days": 7,
                "project": "Mini Project",
                "resources": ["Official Documentation"]
            }
        )

        roadmap.append({
            "Week": week,
            "Skill": skill,
            "Difficulty": details["difficulty"],
            "Days": details["days"],
            "Project": details["project"],
            "Resources": details["resources"]
        })

    return roadmap


# Testing
if __name__ == "__main__":

    missing_skills = [
        "FastAPI",
        "Docker",
        "Machine Learning"
    ]

    roadmap = generate_learning_roadmap(
        missing_skills
    )

    for item in roadmap:
        print(item)