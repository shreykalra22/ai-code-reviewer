import json

from sqlalchemy.orm import Session

from app.config import model
from app.models.review import Review
from app.prompts import CODE_REVIEW_PROMPT


def review_code(
    db: Session,
    language: str,
    code: str
):
    """
    Generate an AI review, save it to the database,
    and return the saved review.
    """

    prompt = CODE_REVIEW_PROMPT.format(
        language=language,
        code=code
    )

    try:
        # Generate AI response
        response = model.generate_content(prompt)

        # Remove markdown wrappers if Gemini returns them
        response_text = response.text.strip()

        if response_text.startswith("```json"):
            response_text = response_text[7:]

        if response_text.endswith("```"):
            response_text = response_text[:-3]

        response_text = response_text.strip()

        # Parse JSON
        data = json.loads(response_text)

        # Create Review object
        new_review = Review(
            language=language,
            code=code,
            review=data["review"],
            score=int(data["score"])
        )

        # Save to database
        db.add(new_review)
        db.commit()
        db.refresh(new_review)

        # Return response
        return {
            "success": True,
            "id": new_review.id,
            "language": new_review.language,
            "review": new_review.review,
            "score": new_review.score,
            "created_at": new_review.created_at.isoformat(),
            "strengths": data.get("strengths", []),
            "weaknesses": data.get("weaknesses", []),
            "suggestions": data.get("suggestions", [])
        }

    except json.JSONDecodeError:

        return {
            "success": False,
            "review": "Gemini returned invalid JSON.",
            "score": 0
        }

    except Exception as e:

        db.rollback()

        return {
            "success": False,
            "review": "Unable to generate AI review.",
            "score": 0,
            "error": str(e)
        }


def get_reviews(
    db: Session,
    skip: int = 0,
    limit: int = 10
):
    """
    Fetch reviews from the database with pagination.
    """

    reviews = (
        db.query(Review)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return reviews


def get_review_by_id(
    db: Session,
    review_id: int
):
    """
    Fetch a single review by its ID.
    """

    review = (
        db.query(Review)
        .filter(Review.id == review_id)
        .first()
    )

    return review