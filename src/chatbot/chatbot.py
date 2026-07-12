from google import genai
from google.genai import errors
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def ask_chatbot(
    question,
    best_role=None,
    detected_skills=None,
    missing_skills=None,
    ats_score=None,
    career=None
):
    context = f"""
You are SkillPilot AI.

Resume Information

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

Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=context
        )

        return response.text

    except Exception as e:
        return f"⚠️ AI Assistant is temporarily unavailable.\n\nError: {e}"