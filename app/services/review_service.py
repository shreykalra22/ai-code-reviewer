def review_code(language: str, code: str):
    """
    Dummy AI review service.
    Later this will call Gemini.
    """

    return {
        "review": f"Dummy review for {language} code.",
        "score": 8
    }