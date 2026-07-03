import json

from google.genai import errors
from sqlalchemy.orm import Session

from app.config import client, MODEL_NAME
from app.logger import logger
from app.models.review import Review
from app.prompts import CODE_REVIEW_PROMPT


class GeminiUnavailableError(Exception):
    """Raised when the Gemini service is temporarily unavailable."""
    pass


class GeminiInvalidResponseError(Exception):
    """Raised when Gemini returns invalid JSON."""
    pass


class AIReviewError(Exception):
    """Raised when AI review generation fails unexpectedly."""
    pass


def review_code(
    db: Session,
    language: str,
    code: str
):
    """
    Generate an AI review, save it to the database,
    and return the saved review.
    """

    logger.info(
        f"Received review request for language: {language}"
    )

    prompt = CODE_REVIEW_PROMPT.format(
        language=language,
        code=code
    )

    try:
        logger.info("Sending request to Gemini...")

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        logger.info(
            "Gemini generated response successfully."
        )

        response_text = response.text.strip()

        # Remove markdown wrappers if Gemini returns them
        if response_text.startswith("```json"):
            response_text = response_text[7:]

        if response_text.endswith("```"):
            response_text = response_text[:-3]

        response_text = response_text.strip()

        logger.info("Parsing Gemini JSON response.")

        data = json.loads(response_text)

        logger.info("Creating Review object.")

        new_review = Review(
            language=language,
            code=code,
            review=data["review"],
            score=int(data["score"])
        )

        logger.info("Saving review to database.")

        db.add(new_review)
        db.commit()
        db.refresh(new_review)

        logger.info(
            f"Review saved successfully with ID {new_review.id}"
        )

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

    except json.JSONDecodeError as exc:
        db.rollback()

        logger.exception(
            "Gemini returned invalid JSON."
        )

        raise GeminiInvalidResponseError(
            "Gemini returned an invalid response."
        ) from exc

    except errors.ServerError as exc:
        db.rollback()

        logger.exception(
            "Gemini service is temporarily unavailable."
        )

        raise GeminiUnavailableError(
            "AI service is temporarily unavailable. Please try again later."
        ) from exc

    except Exception as exc:
        db.rollback()

        logger.exception(
            "Unexpected error while generating AI review."
        )

        raise AIReviewError(
            "Unable to generate AI review."
        ) from exc


def get_reviews(
    db: Session,
    skip: int = 0,
    limit: int = 10
):
    """
    Fetch reviews from the database with pagination.
    """

    logger.info(
        f"Fetching reviews (skip={skip}, limit={limit})"
    )

    reviews = (
    db.query(Review)
    .order_by(Review.created_at.desc())
    .offset(skip)
    .limit(limit)
    .all()
)

    logger.info(
        f"Fetched {len(reviews)} reviews."
    )

    return reviews


def get_review_by_id(
    db: Session,
    review_id: int
):
    """
    Fetch a single review by its ID.
    """

    logger.info(
        f"Fetching review with ID {review_id}"
    )

    review = (
        db.query(Review)
        .filter(Review.id == review_id)
        .first()
    )

    if review:
        logger.info(
            f"Review {review_id} found."
        )
    else:
        logger.warning(
            f"Review {review_id} not found."
        )

    return review


def delete_review(
    db: Session,
    review_id: int
):
    """
    Delete a review by its ID.
    """

    logger.info(
        f"Attempting to delete review with ID {review_id}"
    )

    review = (
        db.query(Review)
        .filter(Review.id == review_id)
        .first()
    )

    if review is None:
        logger.warning(
            f"Review {review_id} not found."
        )
        return None

    try:
        db.delete(review)
        db.commit()

        logger.info(
            f"Review {review_id} deleted successfully."
        )

        return review

    except Exception:
        db.rollback()

        logger.exception(
            f"Database error while deleting review {review_id}."
        )

        raise


def update_review(
    db: Session,
    review_id: int,
    review_text: str,
    score: int
):
    """
    Update an existing review.
    """

    logger.info(
        f"Updating review with ID {review_id}"
    )

    review = (
        db.query(Review)
        .filter(Review.id == review_id)
        .first()
    )

    if review is None:
        logger.warning(
            f"Review {review_id} not found."
        )
        return None

    try:
        review.review = review_text
        review.score = score

        db.commit()
        db.refresh(review)

        logger.info(
            f"Review {review_id} updated successfully."
        )

        return review

    except Exception:
        db.rollback()

        logger.exception(
            f"Database error while updating review {review_id}."
        )

        raise