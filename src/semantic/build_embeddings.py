import os
import pickle

from sentence_transformers import SentenceTransformer
from src.matching.role_matcher import load_roles

print("Loading model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading roles...")

roles = load_roles()

role_embeddings = []

print("Generating embeddings...")

for role in roles:

    text = role["Role"] + " " + " ".join(role["Skills"])

    embedding = model.encode(text)

    role_embeddings.append(
        {
            "Role": role["Role"],
            "Skills": role["Skills"],
            "Embedding": embedding
        }
    )

os.makedirs("data", exist_ok=True)

with open("data/role_embeddings.pkl", "wb") as f:
    pickle.dump(role_embeddings, f)

print("=" * 50)
print("✅ Role Embeddings Saved")
print(f"Total Roles : {len(role_embeddings)}")
print("=" * 50)