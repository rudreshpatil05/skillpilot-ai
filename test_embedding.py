from src.semantic.embedding_matcher import get_embedding

text = """
Python
Machine Learning
SQL
FastAPI
Git
"""

embedding = get_embedding(text)

print("=" * 50)
print("Embedding Generated Successfully")
print("=" * 50)
print("Embedding Dimension:", len(embedding))
print("\nFirst 10 Values:\n")
print(embedding[:10])