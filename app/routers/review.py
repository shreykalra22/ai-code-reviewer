from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.review import ReviewCreate, ReviewResponse
from app.services.review_service import (
    review_code,
    get_reviews,
    get_review_by_id,
)

router = APIRouter()


@router.post("/review")
def create_review(
    review: ReviewCreate,
    db: Session = Depends(get_db)
):
    return review_code(
        db=db,
        language=review.language,
        code=review.code
    )


@router.get(
    "/reviews",
    response_model=list[ReviewResponse]
)
def read_reviews(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_reviews(
        db=db,
        skip=skip,
        limit=limit
    )


@router.get(
    "/reviews/{review_id}",
    response_model=ReviewResponse
)
def read_review(
    review_id: int,
    db: Session = Depends(get_db)
):
    review = get_review_by_id(
        db=db,
        review_id=review_id
    )

    if review is None:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return review