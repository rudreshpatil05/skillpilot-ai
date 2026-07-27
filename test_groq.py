from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv(Path(__file__).resolve().parent / ".env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Say hello."
        }
    ]
)

print(response.choices[0].message.content)