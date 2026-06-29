from fastapi import APIRouter

from app.schemas.review import ReviewCreate
from app.services import review_service

router = APIRouter()


@router.post("/review")
def review_code(request: ReviewCreate):

    result = review_service.review_code(
        language=request.language,
        code=request.code
    )

    return result