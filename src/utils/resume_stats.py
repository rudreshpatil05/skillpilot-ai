def get_resume_statistics(text: str) -> dict:

    if not text:
        return {
            "Characters": 0,
            "Words": 0,
            "Lines": 0,
            "Reading Time": "0 min"
        }

    characters = len(text)

    words = len(text.split())

    lines = len(text.splitlines())

    reading_time = max(1, round(words / 200))

    return {
        "Characters": characters,
        "Words": words,
        "Lines": lines,
        "Reading Time": f"{reading_time} min"
    }