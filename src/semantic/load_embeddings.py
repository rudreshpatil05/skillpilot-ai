import pickle
import os


def load_embeddings():
    """
    Load precomputed role embeddings from disk.
    """

    file_path = "data/role_embeddings.pkl"

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            "role_embeddings.pkl not found. "
            "Run build_embeddings.py first."
        )

    with open(file_path, "rb") as f:
        embeddings = pickle.load(f)

    return embeddings