from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from .load_embeddings import load_embeddings

# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load saved role embeddings
role_embeddings = load_embeddings()


def semantic_role_match(resume_text):
    """
    Returns the best matching role using semantic similarity.
    """

    resume_embedding = model.encode(resume_text)

    best_role = None
    best_score = -1

    for role in role_embeddings:

        score = cosine_similarity(
            [resume_embedding],
            [role["Embedding"]]
        )[0][0]

        if score > best_score:

            best_score = score
            best_role = role["Role"]

    return {
        "Role": best_role,
        "Score": round(float(best_score * 100), 2)
    }