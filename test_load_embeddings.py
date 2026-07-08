from src.semantic.load_embeddings import load_embeddings

embeddings = load_embeddings()

print("=" * 50)
print(f"Loaded {len(embeddings)} role embeddings")
print("=" * 50)

print(embeddings[0]["Role"])
print(embeddings[0]["Skills"])
print(type(embeddings[0]["Embedding"]))