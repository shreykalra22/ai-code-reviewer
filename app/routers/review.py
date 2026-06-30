from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.review import ReviewCreate
from app.services.review_service import review_code

router = APIRouter()


@router.post("/review")
def review(
    review: ReviewCreate,
    db: Session = Depends(get_db)
):
    return review_code(
        db=db,
        language=review.language,
        code=review.code
    )