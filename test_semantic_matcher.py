from src.semantic.semantic_matcher import semantic_role_match

resume = """
Python
Machine Learning
Pandas
NumPy
Scikit-learn
Deep Learning
TensorFlow
"""

result = semantic_role_match(resume)

print("=" * 50)
print(result)
print("=" * 50)