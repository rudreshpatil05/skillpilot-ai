QUESTION_BANK = {

    "Python Developer": {

        "Easy": [
            "What is Python?",
            "What are Python lists and tuples?",
            "What is the difference between a list and a dictionary?",
            "Explain OOP in Python.",
            "What are Python decorators?"
        ],

        "Medium": [
            "Explain multithreading in Python.",
            "What is the GIL?",
            "Difference between *args and **kwargs.",
            "Explain generators and iterators.",
            "What is FastAPI?"
        ],

        "Hard": [
            "How does Python memory management work?",
            "Explain Python's MRO.",
            "Design a scalable REST API using FastAPI.",
            "Explain asynchronous programming.",
            "How would you optimize a slow Python application?"
        ]
    },

    "Data Scientist": {

        "Easy": [
            "What is Pandas?",
            "What is NumPy?",
            "Difference between supervised and unsupervised learning?",
            "What is feature engineering?",
            "What is data preprocessing?"
        ],

        "Medium": [
            "Explain Random Forest.",
            "Difference between Bagging and Boosting.",
            "What is Cross Validation?",
            "Explain Precision and Recall.",
            "What is ROC-AUC?"
        ],

        "Hard": [
            "Explain XGBoost.",
            "How do you prevent overfitting?",
            "Design an end-to-end ML pipeline.",
            "How would you deploy an ML model?",
            "Explain feature selection techniques."
        ]
    },

    "Machine Learning Intern": {

        "Easy": [
            "What is Machine Learning?",
            "Difference between AI and ML?",
            "What is a dataset?",
            "What is training data?",
            "What is testing data?"
        ],

        "Medium": [
            "Explain Decision Trees.",
            "What is Logistic Regression?",
            "Explain KNN.",
            "Difference between Regression and Classification.",
            "Explain Gradient Descent."
        ],

        "Hard": [
            "How does Random Forest work internally?",
            "Explain Bias-Variance Tradeoff.",
            "What is Hyperparameter Tuning?",
            "Explain Ensemble Learning.",
            "How do you deploy ML models?"
        ]
    },

    "AI Engineer": {

        "Easy": [
            "What is Deep Learning?",
            "What is a Neural Network?",
            "Difference between ML and DL?",
            "What is TensorFlow?",
            "What is PyTorch?"
        ],

        "Medium": [
            "Explain CNN.",
            "Explain RNN.",
            "What is Transfer Learning?",
            "Explain Fine-Tuning.",
            "What are Embeddings?"
        ],

        "Hard": [
            "Explain Transformers.",
            "How do LLMs work?",
            "Explain Attention Mechanism.",
            "How would you fine-tune an LLM?",
            "Design an AI Assistant."
        ]
    }

}

def generate_interview_questions(role):
    """
    Returns interview questions based on the predicted role.
    """

    if role in QUESTION_BANK:
        return QUESTION_BANK[role]

    # Default questions if role is not found
    return {
        "Easy": [
            "Tell me about yourself.",
            "Why do you want this role?"
        ],
        "Medium": [
            "Describe one project you have worked on.",
            "Explain one technical challenge you solved."
        ],
        "Hard": [
            "How would you solve a real-world business problem?",
            "How do you keep your technical skills updated?"
        ]
    }