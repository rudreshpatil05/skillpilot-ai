import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_chatbot(
    question,
    best_role=None,
    detected_skills=None,
    missing_skills=None,
    ats_score=None,
    career=None
):

    prompt = f"""
You are SkillPilot AI.

You are an AI Career Coach.

Use the resume information below while answering.

--------------------------------

Best Role:
{best_role}

Detected Skills:
{detected_skills}

Missing Skills:
{missing_skills}

ATS Score:
{ats_score}

Career Readiness:
{career}

--------------------------------

User Question:

{question}

Rules:

1. Answer professionally.
2. If question is about resume, use resume information.
3. If question is about AI, ML, Python, Data Science, answer normally.
4. Keep answers simple and detailed.
5. Use bullet points whenever possible.
"""

    try:

        chat_completion = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": "You are SkillPilot AI Career Assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.5,
            max_tokens=800

        )

        return chat_completion.choices[0].message.content

    except Exception as e:

        return f"❌ Error:\n\n{str(e)}"