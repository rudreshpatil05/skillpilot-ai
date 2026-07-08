from src.semantic.embedding_matcher import semantic_role_match

roles = [
    {
        "Role": "Data Scientist",
        "Skills": "Python Machine Learning SQL Pandas"
    },
    {
        "Role": "Frontend Developer",
        "Skills": "HTML CSS JavaScript React"
    },
    {
        "Role": "Backend Developer",
        "Skills": "Python FastAPI Docker SQL"
    }
]

resume = """
Python
Machine Learning
SQL
FastAPI
Git
Pandas
"""

results = semantic_role_match(resume, roles)

for role in results:
    print(role)