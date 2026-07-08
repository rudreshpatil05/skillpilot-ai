from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_role_match(resume_text, roles):
    """
    Compare resume with all role descriptions using embeddings.
    """

    resume_embedding = model.encode(resume_text)

    results = []

    for role in roles:

        role_text = (
            role["Role"] + " " +
            role.get("Skills", "")
        )

        role_embedding = model.encode(role_text)

        score = cosine_similarity(
            [resume_embedding],
            [role_embedding]
        )[0][0]

        results.append({
            "Role": role["Role"],
            "Semantic Score": round(score * 100, 2)
        })

    results.sort(
        key=lambda x: x["Semantic Score"],
        reverse=True
    )

    return results