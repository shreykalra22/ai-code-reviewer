from app.config import model
from app.prompts import CODE_REVIEW_PROMPT


def review_code(language: str, code: str):
    """
    Generate an AI-powered code review using Gemini.
    """

    # Create the prompt by inserting the user's language and code
    prompt = CODE_REVIEW_PROMPT.format(
        language=language,
        code=code
    )

    try:
        # Send the prompt to Gemini
        response = model.generate_content(prompt)

        return {
            "success": True,
            "review": response.text,
            "score": 8  # Placeholder (we'll extract the real score later)
        }

    except Exception as e:
        return {
            "success": False,
            "review": "Unable to generate AI review at the moment.",
            "score": 0,
            "error": str(e)
        }