CODE_REVIEW_PROMPT = """
You are an experienced Senior Software Engineer.

Review the following {language} code.

Code:
{code}

Return ONLY valid JSON.

Do not add markdown.
Do not use ```json.
Do not add explanations before or after the JSON.

Return exactly in this format:

{{
    "review": "Overall review of the code",
    "strengths": [
        "Strength 1",
        "Strength 2"
    ],
    "weaknesses": [
        "Weakness 1",
        "Weakness 2"
    ],
    "suggestions": [
        "Suggestion 1",
        "Suggestion 2"
    ],
    "score": 8
}}
"""