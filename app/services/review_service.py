import json

from app.config import model
from app.prompts import CODE_REVIEW_PROMPT


def review_code(language: str, code: str):

    prompt = CODE_REVIEW_PROMPT.format(
        language=language,
        code=code
    )

    try:
        response = model.generate_content(prompt)

        data = json.loads(response.text)

        return {
            "success": True,
            "review": data["review"],
            "strengths": data["strengths"],
            "weaknesses": data["weaknesses"],
            "suggestions": data["suggestions"],
            "score": data["score"]
        }

    except json.JSONDecodeError:
        return {
            "success": False,
            "review": "Gemini returned invalid JSON.",
            "score": 0
        }

    except Exception as e:
        return {
            "success": False,
            "review": "Unable to generate AI review.",
            "score": 0,
            "error": str(e)
        }