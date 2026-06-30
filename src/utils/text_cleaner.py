import re


def clean_resume_text(text : str):
    if not text:
        return ""


    text = text.replace("\n", " ").replace("\t", " ").strip()
    text = re.sub(r"[ ]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    text = re.sub(r"[^\w\s.,:/()@+-]", "", text)
    text = text.strip()
    return text
