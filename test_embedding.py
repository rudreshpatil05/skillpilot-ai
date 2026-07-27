from src.semantic.embedding_matcher import get_embedding

text = """
Python
Machine Learning
SQL
Pandas
Scikit-learn
"""

embedding = get_embedding(text)

print(type(embedding))
print(embedding.shape)
print(embedding[:10])