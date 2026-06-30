from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.review import ReviewCreate
from app.services.review_service import review_code, get_reviews

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


@router.get("/reviews")
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